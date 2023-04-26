#Various Boring Imports
import tkinter as tk
import random
import tkcalendar
from tkcalendar import DateEntry
from tkinter import *
import uuid
import datetime
import database as dba
from tkinter import filedialog, messagebox
from tkinter import ttk
#Declare some Global Variables, We will use these Quite A Bit.
global conn
conn = dba.create_conn()
global realUser
realUser = None
global contribution_score
global userID
global various
various = 0
global photo_locations
photo_locations = []
#Little helper that is used to retrive locally stored photos
def pop_photos():
    conn = dba.create_conn()
    try:
        global userID
        results = dba.get_all_photos_for_album(conn,userID) #userID is used as UAD for home photos
        for i in results:
            photo_locations.append({'id': i[0], 'path': i[4], 'caption': i[2], 'date': i[3]})
            print(i)
    except Exception as error:
        print(error)
#Begin Class Declerations
class WelcomeWindow:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("App Landing Page")
        #Basic Button Setup
        self.button = tk.Button(master, text="Log In", command=self.switch_window1)
        self.button.pack(pady=50)
        self.button = tk.Button(master, text="Sign Up", command=self.switch_window2)
        self.button.pack(pady=50)
        
    def switch_window1(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master)
        self.app = LoginScreen(self.newWindow)
    def switch_window2(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master)
        self.app = SignUpScreen(self.newWindow)
        
class LoginScreen:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Log In Existing User")
        
        self.ulabel = tk.Label(master, text="User ID:")
        self.ulabel.pack()
        self.utext_box = tk.Text(master, width=50,height = 3)
        self.utext_box.pack()
        
        self.plabel = tk.Label(master, text="Password:")
        self.plabel.pack()
        self.ptext_box = tk.Text(master, width=50, height=3)
        self.ptext_box.pack()
        
        self.button = tk.Button(master, text="Log In", command=self.get_input)
        self.button.pack(pady=50)
    def get_input(self):
        #We use end-1c because this trims the \n character that we were getting here.
        user_id = self.utext_box.get(1.0, 'end-1c')
        password = self.ptext_box.get(1.0, 'end-1c')

        try:
            #establish connection
            conn = dba.create_conn()
            #populate a realuser
            realUser = dba.select_user_by_id_and_password(conn, user_id, password)
            #Now we check if there is a present user and there password matches
            if realUser and realUser[7] == password:
                global userID
                userID = realUser[0] #Set userID as person is now logged in
                  
                pop_photos() #init the photo method so we can load there feed when they login
                self.switch_window(user_id)
                
            else:
                print("Invalid Entry. Try Again.")
                messagebox.showerror("Error", "Invalid user ID or password.") #tell user they messed up
                print(realUser) #debug info
                print(realUser[2]) #debug info
        except Exception as error:
            print("Error:", error)
   
    def switch_window(self, user_id):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)

    
class SignUpScreen:
    def __init__(self, master):
        self.master = master
        master.geometry("600x900")
        master.title("New User Sign Up")
        #Bunch of boring labels, they setup the register screen, flabel is first name
        flabel = tk.Label(master, text="First Name:")
        flabel.pack()
        self.ftext_box = tk.Text(master, width=30,height=3)
        self.ftext_box.pack()
        #last name label
        llabel = tk.Label(master, text="Last Name:")
        llabel.pack()
        self.ltext_box = tk.Text(master, width=30,height=3)
        self.ltext_box.pack()
        #email label
        self.elabel = tk.Label(master, text="Email:")
        self.elabel.pack()
        self.etext_box = tk.Text(master, width=30,height=3)
        self.etext_box.pack()
        #user ID label
        self.uidlabel = tk.Label(master, text="User ID:")
        self.uidlabel.pack()
        self.uidtext_box = tk.Text(master, width=30,height=3)
        self.uidtext_box.pack()
        #password label 
        self.passlabel = tk.Label(master, text="Password")
        self.passlabel.pack()
        self.passtext_box = tk.Text(master, width=30,height=3)
        self.passtext_box.pack()
        #hometown label
        self.htlabel = tk.Label(master, text="Hometown:")
        self.htlabel.pack()
        self.httext_box = tk.Text(master, width=30,height=3)
        self.httext_box.pack()
        #gender label
        self.genlabel = tk.Label(master, text="Gender:")
        self.genlabel.pack()
        #various options are stored here, other is used to simplfy things
        gender_options = ["Male", "Female", "Other"]
        self.selected_gender = tk.StringVar()
        self.selected_gender.set(gender_options[0])
        self.gender_menu = tk.OptionMenu(master, self.selected_gender, *gender_options)
        self.gender_menu.pack()  
        #Setup dob here
        self.doblabel = tk.Label(master, text="Date of Birth:")
        self.doblabel.pack()
        self.dob_entry = DateEntry(master, width=15, background='darkblue',foreground='white', borderwidth=2)
        self.dob_entry.pack(padx=10, pady=10)
        
        self.button = tk.Button(master, text="Create Your Account", command=self.get_input)
        self.button.pack(pady=5)
        
        self.button = tk.Button(master, text="Back to Home", command=self.back)
        self.button.pack(pady=5)
    #  print(httext_box)
     
    def back(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = WelcomeWindow(self.newWindow) 
        
    def switch_window(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master) 
        self.app = HomePage(self.newWindow)\
    #Real driver function here
    def get_input(self):
        #Retrives all the labels text values after they have been entered
        fname = self.ftext_box.get(1.0, 'end-1c')
        lname = self.ltext_box.get(1.0, 'end-1c')
        email = self.etext_box.get(1.0, 'end-1c')
        user_id = self.uidtext_box.get(1.0, 'end-1c')
        hometown = self.httext_box.get(1.0, 'end-1c')
        gender = self.selected_gender.get()
        dob = self.dob_entry.get_date()
        password = self.passtext_box.get(1.0,'end-1c') # Add a widget to get the user's password, and retrieve it here
        album_num = 0 # most users start with 0 albums, hopefully.
        try:
            #Setup connection
            conn = dba.create_conn()
            dba.insert_user(user_id, fname, lname, email, dob, hometown, gender, password, album_num,conn) #make database call
            conn = dba.create_conn()
            realUser = dba.select_user_by_id(conn,user_id)
            global userID
            userID = user_id #set user as they are loggedin
            pop_photos() #fill feed anyways even though it should be empty
        except():
            print("Invalid Entry Try Again")
        
        self.switch_window()
    
class HomePage:
    def __init__(self, master):
        self.master = master
        master.geometry("800x500")
        master.title("User Home Page")
        
        # Custom font
        custom_font = ("Helvetica", 12, "bold")

        # Styling for buttons
        button_bg = "#007BFF" #light grey
        button_fg = "#000000" #black
        button_active_bg = "#0056B3" #grey
        button_active_fg = "#000000" #black

        button_frame = tk.Frame(master)
        button_frame.pack(side='right', fill='y', padx=10, pady=10)
        #Setup Buttons Here
        self.search_button = tk.Button(button_frame, text="Search", command=self.switch_to_search, font=custom_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, relief="solid", bd=1, borderwidth=0)
        self.search_button.pack(pady=10, side='top')
        
        self.upload_button = tk.Button(button_frame, text="Upload Photo", command=self.switch_to_upload, font=custom_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, relief="solid", bd=1, borderwidth=0)
        self.upload_button.pack(pady=10, side='top')

        self.friends_button = tk.Button(button_frame, text="Friends", command=self.switch_to_friends, font=custom_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, relief="solid", bd=1, borderwidth=0)
        self.friends_button.pack(pady=10, side='top')

        self.album_button = tk.Button(button_frame, text="Albums", command=self.switch_to_albums, font=custom_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, relief="solid", bd=1, borderwidth=0)
        self.album_button.pack(pady=10, side='top')
        
        self.profile_button = tk.Button(button_frame, text="Edit Profile", command=self.switch_to_profile, font=custom_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, relief="solid", bd=1, borderwidth=0)
        self.profile_button.pack(pady=10, side='top')
        
        self.profile_button = tk.Button(button_frame, text="Recommended Friends", command=self.switch_to_rec, font=custom_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, relief="solid", bd=1, borderwidth=0)
        self.profile_button.pack(pady=10, side='top')
        
        self.profile_button = tk.Button(button_frame, text="Contribution Score", command=self.switch_to_cs, font=custom_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, relief="solid", bd=1, borderwidth=0)
        self.profile_button.pack(pady=10, side='top')
        
        # Scrollable feed in the middle
        feed_frame = ttk.Frame(master) #special tinkter tink
        feed_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        feed_canvas = tk.Canvas(feed_frame, bg='white')
        feed_canvas.pack(side='left', fill='both', expand=True)

        scrollbar = tk.Scrollbar(feed_frame, orient='vertical', command=feed_canvas.yview)
        scrollbar.pack(side='left', fill='y')

        feed_canvas.configure(yscrollcommand=scrollbar.set)
        feed_canvas.bind('<Configure>', lambda e: feed_canvas.configure(scrollregion=feed_canvas.bbox('all')))

        inner_feed_frame = tk.Frame(feed_canvas, bg='white')
        feed_canvas.create_window((0, 0), window=inner_feed_frame, anchor='nw')

        self.add_images(inner_feed_frame)
        
    def add_images(self, inner_feed_frame):
        for photo_info in photo_locations:
            self.display_photo(inner_feed_frame, photo_info) #loop through all photos and call display photo function

    def display_photo(self, inner_feed_frame, photo_info):
        photo_id = photo_info['id']
        photo_path = photo_info['path']
        caption = photo_info['caption']
        date = photo_info['date']

        select_photo = dba.select_photo_by_upd(conn, photo_id)  #call photo upload feature

        image_label = tk.Label(inner_feed_frame, bg='white', borderwidth=2, relief="groove")
        image_label.image = self.load_image_from_path(photo_path)
        image_label.config(image=image_label.image)
        image_label.pack(pady=10,anchor='center')
       
        
        like_button_text = tk.StringVar()
        like_button_text.set("Like")
        like_button = tk.Button(inner_feed_frame, textvariable=like_button_text, command=lambda: self.like_photo(photo_id, like_button_text))
        like_button.pack()
        # Add comment button and comment section
        comment_button = tk.Button(inner_feed_frame, text="Comments", command=lambda: self.show_comments_popup(photo_id))
        comment_button.pack()

        # Add tags button and tag section
        tag_button = tk.Button(inner_feed_frame, text="Tags", command=lambda: self.show_tags_popup(photo_id))
        tag_button.pack()

        caption_label = tk.Label(inner_feed_frame, text=caption, font=("Helvetica", 10, "bold"), bg='white', wraplength=200, justify='center')
        caption_label.pack()

        date_label = tk.Label(inner_feed_frame, text=date, font=("Helvetica", 8), bg='white')
        date_label.pack()

    # Like photo method
    def like_photo(self, photo_id,like_button_text):
         if like_button_text.get() == "Like":
            
            dba.increment_like_count(conn, photo_id)
            dba.inc_contribution_score(conn, user_id, contribution_score)
            like_button_text.set("Unlike")
         else:
          
            dba.decrement_like_count(conn, photo_id)
            dba.dec_contribution_score(conn, user_id, contribution_score)
            like_button_text.set("Like")

        
    # Show comments popup
    def show_comments_popup(self, photo_id):
        
        comments = dba.select_comments_by_upd(conn,photo_id)
        comments_popup = tk.Toplevel()
        comments_popup.title("Comments")

    # Create a Listbox to display the comments
        comments_listbox = tk.Listbox(comments_popup, width=50, height=10)
        comments_listbox.pack()

    # Display existing comments
        if(len(comments) > 1):
            for comment in comments:
        # Add each comment to the Listbox
                comments_listbox.insert(tk.END, comment)

    # Add new comment entry and submit button
        new_comment_entry = tk.Entry(comments_popup)
        new_comment_entry.pack()

        submit_comment_button = tk.Button(comments_popup, text="Submit Comment", command=lambda: self.submit_comment(photo_id, new_comment_entry.get()))
        submit_comment_button.pack()

    # Submit comment method
    def submit_comment(self, photo_id, comment_text):
        x = random.randint(0,500000)
        dba.insert_comment(conn,x,comment_text,userID,photo_id,datetime.datetime.now().strftime("%Y-%m-%d"))
        dba.inc_contribution_score(conn, user_id, contribution_score)
        if hasattr(self, 'comments_popup') and self.comments_popup:
            self.comments_popup.destroy()
        self.show_comments_popup(photo_id)
    def show_tags_popup(self, photo_id):
        if hasattr(self, 'tags_popup') and self.tags_popup:
            self.tags_popup.destroy()
        tags_popup = tk.Toplevel()
        tags_popup.title("Tags")
    
        tags_listbox = tk.Listbox(tags_popup, width=50, height=10)
        tags_listbox.pack()

        tags = dba.select_tags_by_upd(conn, photo_id)
        for tag in tags:
            tags_listbox.insert(tk.END, tag)

        new_tag_entry = tk.Entry(tags_popup)
        new_tag_entry.pack()

        submit_tag_button = tk.Button(tags_popup, text="Submit Tag", command=lambda: self.submit_tag(photo_id, new_tag_entry.get()))
        submit_tag_button.pack()

    # Submit tag method
    def submit_tag(self, photo_id, tag_text):
        dba.insert_tag(conn,tag_text,photo_id)
        self.show_tags_popup(photo_id)
        
    def load_image_from_path(self, filepath):
        from PIL import Image, ImageTk

        img = Image.open(filepath)
        self.master.update()
        img = img.resize((int(self.master.winfo_width() / 4), int(self.master.winfo_height() / 4)), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    
    def switch_to_friends(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master) 
        self.app = Friends(self.newWindow)
    def switch_to_profile(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master) 
        self.app = MyProfile(self.newWindow) 
    def switch_to_upload(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master) 
        self.app = UploadPhoto(self.newWindow)
    def switch_to_create_album(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master) 
        self.app =  AlbumsPage(self.newWindow)
    def switch_to_search(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master) 
        self.app = Search(self.newWindow)
    def switch_to_albums(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = AlbumsPage(self.newWindow)
    def switch_to_rec(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = RecomendedFriends(self.newWindow)
    def switch_to_cs(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = ContributionScore(self.newWindow)


class AlbumsPage:
    global userID

    def __init__(self, master):
        self.master = master
        master.geometry("800x500")
        master.title("Albums")
        #Set up Album Label
        self.title_label = tk.Label(master, text="Albums", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        #Frame Albums
        self.albums_frame = tk.Frame(master)
        self.albums_frame.pack(pady=10)

        self.load_albums()
        #Redirect to Create Album
        create_button = tk.Button(master, text="Create Album", command=self.create_album, bg='#f0f0f0', width=15)
        create_button.pack(pady=10)

        back_button = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        back_button.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)

    def load_albums(self):
        albums = dba.select_albums_by_uid(conn, userID) #Call dba all albums by UID

        for album in albums:
            album_button = tk.Button(self.albums_frame, text=album[1], command=lambda a=album[0]: self.view_album(a)) #Dispolay album info
            album_button.pack(side=tk.LEFT, padx=10) #Center to left

    def view_album(self, uad):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = ViewAlbum(self.newWindow, uad)

    def create_album(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = CreateAlbum(self.newWindow)
class CreateAlbum:
    global userID

    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Create Album")
        #Setup Album Name Labels
        self.album_name_label = tk.Label(master, text="Album Name:", font=("Helvetica", 14))
        self.album_name_label.pack(pady=10)
        #Get Album Entry
        self.album_name_entry = tk.Entry(master)
        self.album_name_entry.pack()
        #Submit Create Info
        create_button = tk.Button(master, text="Create", command=self.create_album, bg='#f0f0f0', width=15)
        create_button.pack(pady=10)

        back_button = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        back_button.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)

    def create_album(self):
        album_name = self.album_name_entry.get()
        if not album_name:
            messagebox.showerror("Error", "Album name cannot be empty") #Need valid Album
        else:
            uad = random.randint(1,15000) #Set random unique album

            # Get the current date
            doc = datetime.datetime.now()

            # Insert the album into the database
            dba.insert_album(conn, uad, album_name, userID, doc)
            messagebox.showinfo("Success", "Album created successfully")

            # Redirect to the newly created album view
            self.master.withdraw()
            self.newWindow = tk.Toplevel(self.master)
            self.app = ViewAlbum(self.newWindow, uad)
# Modified ViewAlbum class
class ViewAlbum:
    def __init__(self, master, uad):
        #Set up Album Info
        self.master = master
        self.uad = uad
        master.geometry("800x600")
        master.title("View Album")

        # Fetch album name and display it
        album = dba.select_album_by_uad(conn, uad)
        if album:
            self.album_name = album[1] #Get Album in Column 1
        else:
            self.album_name = "Untitled Album"
        #Setup Album Labels
        self.album_name_label = tk.Label(master, text=self.album_name, font=("Helvetica", 18))
        self.album_name_label.pack(pady=10)

        #Setup Title Labels
        self.title_label = tk.Label(master, text="Album Photos", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        #Setup Photo Frames
        self.photos_frame = tk.Frame(master)
        self.photos_frame.pack(pady=10)
        #Loop Photos
        self.load_photos()
        #Setup Add Photo
        add_photo_button = tk.Button(master, text="Add Photo", command=self.add_photo, bg='#f0f0f0', width=15)
        add_photo_button.pack(pady=10)

        back_button = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        back_button.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = AlbumsPage(self.newWindow)

    def load_photos(self):
        photos = dba.select_photos_by_uad(conn, self.uad) #Get photos within the unique album identifier

        for photo in photos:
            img = Image.open(photo[4])   #Get photo at filepath
            img = img.resize((100, 100), Image.ANTIALIAS) #Create Image
            img = ImageTk.PhotoImage(img)

            photo_label = tk.Label(self.photos_frame, image=img) #Setup Photo Labels
            photo_label.image = img
            photo_label.pack(side=tk.LEFT, padx=10)
    #Adding Photo
    def add_photo(self):
        filepath = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*"))) #Get all photo types
        if filepath:
            self.selected_filepath = filepath   #Setup filepath
            self.caption_window = tk.Toplevel(self.master)
            self.caption_window.title("Enter Caption")#Setup seperate caption captuer
            self.caption_label = tk.Label(self.caption_window, text="Enter a caption for this photo:", font=("Helvetica", 14)) #Capture caption
            self.caption_label.pack(pady=10)
            self.caption_entry = tk.Entry(self.caption_window)
            self.caption_entry.pack()
            self.submit_caption_button = tk.Button(self.caption_window, text="Submit", command=self.submit_caption, bg='#f0f0f0', width=15)
            self.submit_caption_button.pack(pady=10) #Send Caption Back
        else:
            messagebox.showinfo("Info", "No file was selected.")

    def submit_caption(self):
        caption = self.caption_entry.get()
        filepath = self.selected_filepath

        with open(filepath, "rb") as file:
            data = file.read()

        dba.insert_photo(conn, random.randint(1100,23000), self.uad, caption, data, filepath) #Pass photo with caption in

        # Close the caption window
        self.caption_window.destroy()

        # Reload photos in the album
        for widget in self.photos_frame.winfo_children():
            widget.destroy()

        self.load_photos()
class FriendFeed:
    global userID
    def __init__(self, master):
        self.master = master
        master.geometry("800x500")
        master.title("Friend Feed")

        self.title_label = tk.Label(master, text="Friend Feed", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.scrollbar = tk.Scrollbar(master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.feed_listbox = tk.Listbox(master, yscrollcommand=self.scrollbar.set, width=80, height=20)
        self.feed_listbox.pack(pady=10)

        self.scrollbar.config(command=self.feed_listbox.yview)

        self.load_friend_feed()

        back_button = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        back_button.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)

    def load_friend_feed(self):
        # Fetch recent photo uploads from friends
        recent_uploads = dba.get_friend_feed(conn, userID)

        for upload in recent_uploads:
            friend_name = upload[0]
            photo_name = upload[1]
            upload_time = upload[2]

            self.feed_listbox.insert(tk.END, f"{friend_name} uploaded '{photo_name}' on {upload_time}")
class MyProfile:
    def __init__(self, master):
        self.master = master
        master.geometry("600x900")
        master.title("Change User Info")
        #Setup First Name Label
        flabel = tk.Label(master, text="First Name:")
        flabel.pack()
        self.ftext_box = tk.Text(master, width=30,height=3)
        self.ftext_box.pack()
        #Setup Last Name Label
        llabel = tk.Label(master, text="Last Name:")
        llabel.pack()
        self.ltext_box = tk.Text(master, width=30,height=3)
        self.ltext_box.pack()
        #Setup Email Label
        self.elabel = tk.Label(master, text="Email:")
        self.elabel.pack()
        self.etext_box = tk.Text(master, width=30,height=3)
        self.etext_box.pack()
        #Setup Password Label
      
        self.passlabel = tk.Label(master, text="Password")
        self.passlabel.pack()
        self.passtext_box = tk.Text(master, width=30,height=3)
        self.passtext_box.pack()
        #Set HomeTown Label
        self.htlabel = tk.Label(master, text="Hometown:")
        self.htlabel.pack()
        self.httext_box = tk.Text(master, width=30,height=3)
        self.httext_box.pack()
        #Set Gender Options
        self.genlabel = tk.Label(master, text="Gender:")
        self.genlabel.pack()
        #Setup Gender Options
        gender_options = ["Male", "Female", "Other"]
        self.selected_gender = tk.StringVar()
        self.selected_gender.set(gender_options[0])
        self.gender_menu = tk.OptionMenu(master, self.selected_gender, *gender_options)
        self.gender_menu.pack()  
        
       # self.doblabel = tk.Label(master, text="Date of Birth:")
        #self.doblabel.pack()
        #self.dob_entry = DateEntry(master, width=15, background='darkblue',foreground='white', borderwidth=2)
        #self.dob_entry.pack(padx=10, pady=10)
        
        self.button = tk.Button(master, text="Update Changes", command=self.get_input)
        self.button.pack(pady=5)
        
        self.button = tk.Button(master, text="Back to Home", command=self.back)
        self.button.pack(pady=5)
    #  print(httext_box)
     
    def back(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = WelcomeWindow(self.newWindow) 
        
    def switch_window(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master) 
        self.app = HomePage(self.newWindow)
    #Main Driver Function
    def get_input(self):
        #Get TextBox INputs
        fname = self.ftext_box.get(1.0, 'end-1c')
        lname = self.ltext_box.get(1.0, 'end-1c')
        email = self.etext_box.get(1.0, 'end-1c')
        hometown = self.httext_box.get(1.0, 'end-1c')
        gender = self.selected_gender.get()
        #dob = self.dob_entry.get_date()
        password = self.passtext_box.get(1.0,'end-1c') 
      #  album_num = 0
        try:
            conn = dba.create_conn() #Various If Statements Loop Through DBA Update Calls
            if(fname != ""):
                dba.update_user_fname(conn,userID,fname)
            if(lname != ""):
                dba.update_user_lname(conn,userID,lname)
            if(email != ""):
                dba.update_user_email(conn,userID,email)
            if(hometown != ""):
                dba.update_user_hometown(conn,userID,hometown)
            if(gender != ""):
                dba.update_user_gender(conn,userID,gender)
            if(password!= ""):
                dba.update_user_password(conn,userID,password)
                
        except():
            print("Invalid Entry Try Again")
        
        self.switch_window()
class Friends:
    def __init__(self, master):
        self.master = master
        master.geometry("800x1200")
        master.title("Friends")
        #Setup Friend Search
        search_label = tk.Label(master, text="Search Friends by User ID:", font=("Helvetica", 14))
        search_label.pack(pady=10)

        self.search_entry = tk.Entry(master)
        self.search_entry.pack()

        search_button = tk.Button(master, text="Search", command=self.search_users, bg='#f0f0f0', width=15)
        search_button.pack(pady=10)

        self.search_results_listbox = tk.Listbox(master, width=50, height=5)
        self.search_results_listbox.pack(pady=10)
        #Setup Friend Box
        self.friends_listbox = tk.Listbox(master, width=50, height=15)
        self.friends_listbox.pack(pady=10)
        #Call update list on every recall
        self.update_friends_list()
        #Setup add friend button
        add_friend_button = tk.Button(master, text="Add Friend", command=self.add_friend, bg='#f0f0f0', width=15)
        add_friend_button.pack(side='left', padx=10)
        #setup remove friend button
        remove_friend_button = tk.Button(master, text="Remove Friend", command=self.remove_friend, bg='#f0f0f0', width=15)
        remove_friend_button.pack(side='right', padx=10)
        #back button
        back_button = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        back_button.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)
    #Setup simple search
    def search_users(self):
        search_query = self.search_entry.get()
        if search_query:
            try:
                user_id = int(search_query) #Get typesafe user id
                search_results = dba.select_user_by_id(conn, user_id) #call dba connection
                if search_results:
                    self.update_search_results_list(search_results) #append to listbox
                else:
                    self.search_results_listbox.delete(0, tk.END) #return nothing
                    messagebox.showerror("Error", "No user found with this User ID")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid User ID")
    def update_search_results_list(self, user):
        self.search_results_listbox.delete(0, tk.END)
        self.search_results_listbox.insert(tk.END, f"{user[1]} {user[2]} ({user[3]})") #add user info

    def update_friends_list(self, friends=None):
        self.friends_listbox.delete(0, tk.END)
        if friends is None:
            friends = dba.select_friends_by_user_id(conn, userID) #call freinds by user id dba call

        for friend in friends:
            self.friends_listbox.insert(tk.END, f"{friend[1]}") #add friend id to friends list

    def add_friend(self):
        selected_index = self.search_results_listbox.curselection() #get the currently selected query
        if selected_index:
            friend_email = self.search_results_listbox.get(selected_index).split('(')[-1].split(')')[0] #parse for there email
            friend = dba.select_user_by_email(conn, friend_email) #store email
            if friend:
                friend = friend[0] #get friend id which is stroed in column 0 in users
                dba.insert_friend(conn, userID, friend[0], datetime.datetime.now())
                messagebox.showinfo("Success", f"Added {friend[1]} {friend[2]} as a friend") #sucsess
                self.update_friends_list()
            else:
                messagebox.showerror("Error", "Unable to find the selected user")

    def remove_friend(self):
        selected_index = self.friends_listbox.curselection() #get current query
        if selected_index:
            friend_id = self.friends_listbox.get(selected_index).split('(')[-1].split(')')[0] #parse for friend id
            friend = dba.select_user_by_id(conn,friend_id) #now pass friend id back
            if friend:
                dba.delete_friend(conn, userID, friend[0]) #if valid friend now we delete them
                messagebox.showinfo("Success", f"Removed {friend[1]} {friend[2]} as a friend") #sucsess
                self.update_friends_list() #refresh
            else:
                messagebox.showerror("Error", "Unable to find the selected user")
                   
class UploadPhoto:
    global userID #Ensure we are searching the right user
    def __init__(self, master):
        self.master = master
        #Set up FileName Label
        self.filename_label = tk.Label(master, text="No file selected", font=("Helvetica", 14))
        self.filename_label.pack(pady=20)
        #Setup Caption Label
        self.caption_entry_label = tk.Label(master, text="Caption:", font=("Helvetica", 14))
        self.caption_entry_label.pack(pady=10)
        #Get Caption as Entry
        self.caption_entry = tk.Entry(master)
        self.caption_entry.pack()

        master.geometry("500x500")
        master.title("Upload Photo")
        #Back Button
        self.button = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        self.button.pack(pady=10)
        #Upload Button
        self.upload_button = tk.Button(master, text="Select photo", command=self.select_file, bg='#f0f0f0', width=15)
        self.upload_button.pack(pady=10)
        #Save Button
        self.save_button = tk.Button(master, text="Save", command=self.upload_photo, bg='#f0f0f0', width=15)
        self.save_button.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)
    #Accept jpeg and png and as catch all we can acccept whatever uploads but it mihgt not be valid
    def select_file(self):
        filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        filepath = filedialog.askopenfilename(filetypes=filetypes)
        if filepath:
            self.filename_label.config(text=filepath) #Setup filename from filepath from os
    
    def upload_photo(self):
        filename = self.filename_label.cget("text")
        caption = self.caption_entry.get()
        if filename == "No file selected":
            messagebox.showerror("Error", "No photo selected")
        elif not caption:
            messagebox.showerror("Error", "Caption cannot be empty")
        else:
            unique_id = random.randint(14300,28770) #Randomly generate uuid
            current_date = datetime.datetime.now().strftime("%Y-%m-%d") #Get current date
            photo_locations.append({'id': unique_id, 'path': filename, 'caption': caption, 'date': current_date}) #Add photo to photo locations array
            dba.insert_photo(conn, unique_id, userID, caption, current_date, filename)  #Insert Symlink in Databse
            messagebox.showinfo("Success", f"Photo uploaded\nFilepath: {filename}")
class TrendingTags:
    def __init__(self):
        self.master = master
        master.geometry("500x500")
        master.title("Trending Tags")

        self.back_button = tk.Button(master, text="Back", command=self.back)

        tags = dba.get_top_tags(search_query) #Get comments by date
        self.display_results("Top Tags", tags)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)
    
    
class RecomendedFriends():
    def __init__(self):
        self.master = master
        master.geometry("500x500")
        master.title("Users You May Know")
        
        self.button = tk.Button(master, text="Back", command=self.back)
        self.button.pack(pady=5)
        
        users = dba.recommend_friends(conn, user_id)
        self.display_results("Recommended Friends", users)
        
    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)

from PIL import Image, ImageTk

class ContributionScore:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Contribution Score")
        
        contribution_score=dba.show_contribution_score(conn, user_id, contribution_score)
        self.display_results("Contribution Score:", contriibution_score)
        self.button = tk.Button(master, text="Back", command=self.back)
        self.button.pack(pady=5)
        
    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)
        
        
        
class Search:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Search")
        #Setup Buttons
        self.back_button = tk.Button(master, text="Back", command=self.back)
        self.back_button.pack(pady=10)
         #Set up Search Input
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(master, textvariable=self.search_var)
        self.search_entry.pack(pady=10)
        #Setup Display Input
        self.search_categories_label = tk.Label(master, text="Select search categories:")
        self.search_categories_label.pack(pady=10)

        self.search_categories_listbox = tk.Listbox(master, selectmode=tk.MULTIPLE)
        self.search_categories_listbox.pack(pady=10)
        search_categories = ["Tag", "Comment", "UserID", "Date"]
        for category in search_categories: 
            self.search_categories_listbox.insert(tk.END, category) #Display all categories 

        self.search_button = tk.Button(master, text="Search", command=self.search)
        self.search_button.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)
     #Searh Function
    def search(self):
        search_query = self.search_var.get()
        selected_indices = self.search_categories_listbox.curselection()
        selected_categories = [self.search_categories_listbox.get(i) for i in selected_indices] #Collect all selected driver categories

        if not selected_categories:
            messagebox.showerror("Error", "Please select at least one search category.")
            return

        for category in selected_categories:
            if category == "Tag": #Tag Category
                photos = dba.search_photos_by_tags(conn, search_query) #Search for photos with this tag
                self.display_results("Photos", photos, display_photo=True) # Display The Photo with This Tag

            elif category == "Comment":
                comments = dba.search_comments_by_text(conn, search_query) #Get all comments related with this text
                self.display_results("Comments", comments) #Display comments

            elif category == "UserID":
                user = dba.select_user_by_id(conn, search_query) #Get user info
                if user:
                    self.display_results("User", [user])
                    photos = dba.select_photos_by_user_id(conn, search_query) #Display User Photos
                    self.display_results("User Photos", photos, display_photo=True)
                    comments = dba.select_comments_by_user_id(conn, search_query) #Display User Comments
                    self.display_results("User Comments", comments) 
                else:
                    messagebox.showerror("Error", "No user found with the specified user ID.")

            elif category == "Date":
                comments = dba.select_comments_by_date(conn, search_query) #Get comments by date
                self.display_results("Comments", comments)
                photos = dba.select_photos_by_date(conn, search_query) #Get Photos by Date
                self.display_results("Photos", photos, display_photo=True)

    def display_results(self, title, results, display_photo=False):
        results_window = tk.Toplevel()
        results_window.title(title)
        #Check to make sure Results is valid
        if results is not None and len(results) > 0:
            for result in results:
                if display_photo: #Get photo information to pass back
                    photo_id = result['id']
                    photo_path = result['path']
                    caption = result['caption']
                    date = result['date']

                    self.display_photo(results_window, photo_id, photo_path, caption, date)
                else:
                    result_label = tk.Label(results_window, text=str(result), wraplength=400)
                    result_label.pack()
        else:
            no_results_label = tk.Label(results_window, text="No results found.")
            no_results_label.pack()
            
    def display_photo(self, photo):
        try:
            #Try opening an image
            image = Image.open(photo[4])  #file path is at index 4
            image.thumbnail((200, 200))
            tk_image = ImageTk.PhotoImage(image)
            #Create Photo Labels
            photo_label = tk.Label(self.master, image=tk_image)
            photo_label.image = tk_image
            photo_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading image: {photo}. Error: {e}")
    

root = tk.Tk()
app = WelcomeWindow(root)
root.mainloop()