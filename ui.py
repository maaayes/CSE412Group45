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
global conn
conn = dba.create_conn()
global realUser
realUser = None
global userID
global various
various = 0
global photo_locations
photo_locations = []
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
class WelcomeWindow:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("App Landing Page")
        
        self.button = tk.Button(master, text="Log In", command=self.switch_window1)
        self.button.pack(pady=50)
        self.button = tk.Button(master, text="Sign Up", command=self.switch_window2)
        self.button.pack(pady=50)
        conn = dba.create_conn()
        
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
        user_id = self.utext_box.get(1.0, 'end-1c')
        password = self.ptext_box.get(1.0, 'end-1c')

        try:
            conn = dba.create_conn()
            realUser = dba.select_user_by_id_and_password(conn, user_id, password)

            if realUser and realUser[7] == password:
                global userID
                userID = realUser[0]
                  
                pop_photos()
                self.switch_window(user_id)
                
            else:
                print("Invalid Entry. Try Again.")
                messagebox.showerror("Error", "Invalid user ID or password.")
                print(realUser)
                print(realUser[2])
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
        flabel = tk.Label(master, text="First Name:")
        flabel.pack()
        self.ftext_box = tk.Text(master, width=30,height=3)
        self.ftext_box.pack()
        
        llabel = tk.Label(master, text="Last Name:")
        llabel.pack()
        self.ltext_box = tk.Text(master, width=30,height=3)
        self.ltext_box.pack()
        
        self.elabel = tk.Label(master, text="Email:")
        self.elabel.pack()
        self.etext_box = tk.Text(master, width=30,height=3)
        self.etext_box.pack()
        
        self.uidlabel = tk.Label(master, text="User ID:")
        self.uidlabel.pack()
        self.uidtext_box = tk.Text(master, width=30,height=3)
        self.uidtext_box.pack()
        self.passlabel = tk.Label(master, text="Password")
        self.passlabel.pack()
        self.passtext_box = tk.Text(master, width=30,height=3)
        self.passtext_box.pack()
        
        self.htlabel = tk.Label(master, text="Hometown:")
        self.htlabel.pack()
        self.httext_box = tk.Text(master, width=30,height=3)
        self.httext_box.pack()
        
        self.genlabel = tk.Label(master, text="Gender:")
        self.genlabel.pack()
        
        gender_options = ["Male", "Female", "Other"]
        self.selected_gender = tk.StringVar()
        self.selected_gender.set(gender_options[0])
        self.gender_menu = tk.OptionMenu(master, self.selected_gender, *gender_options)
        self.gender_menu.pack()  
        
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
        self.app = HomePage(self.newWindow)
    def get_input(self):
        fname = self.ftext_box.get(1.0, 'end-1c')
        lname = self.ltext_box.get(1.0, 'end-1c')
        email = self.etext_box.get(1.0, 'end-1c')
        user_id = self.uidtext_box.get(1.0, 'end-1c')
        hometown = self.httext_box.get(1.0, 'end-1c')
        gender = self.selected_gender.get()
        dob = self.dob_entry.get_date()
        password = self.passtext_box.get(1.0,'end-1c') # Add a widget to get the user's password, and retrieve it here
        album_num = 0
        try:
            conn = dba.create_conn()
            dba.insert_user(user_id, fname, lname, email, dob, hometown, gender, password, album_num,conn)
            conn = dba.create_conn()
            realUser = dba.select_user_by_id(conn,user_id)
            global userID
            userID = user_id
            pop_photos()
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
        button_bg = "#007BFF"
        button_fg = "#000000"
        button_active_bg = "#0056B3"
        button_active_fg = "#000000"

        button_frame = tk.Frame(master)
        button_frame.pack(side='right', fill='y', padx=10, pady=10)
        
        self.search_button = tk.Button(button_frame, text="Search", command=self.switch_to_search, font=custom_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, relief="solid", bd=1, borderwidth=0)
        self.search_button.pack(pady=10, side='top')
        
        self.upload_button = tk.Button(button_frame, text="Upload Photo", command=self.switch_to_upload, font=custom_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, relief="solid", bd=1, borderwidth=0)
        self.upload_button.pack(pady=10, side='top')
              
        self.album_button = tk.Button(button_frame, text="Create Album", command=self.switch_to_create_album, font=custom_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, relief="solid", bd=1, borderwidth=0)
        self.album_button.pack(pady=10, side='top')
        
        self.profile_button = tk.Button(button_frame, text="Edit Profile", command=self.switch_to_profile, font=custom_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, relief="solid", bd=1, borderwidth=0)
        self.profile_button.pack(pady=10, side='top')
        
        self.profile_button = tk.Button(button_frame, text="Friend Feed", command=self.switch_to_friends, font=custom_font, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, relief="solid", bd=1, borderwidth=0)
        self.profile_button.pack(pady=10, side='top')

        # Scrollable feed in the middle
        feed_frame = ttk.Frame(master)
        feed_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)

        feed_canvas = tk.Canvas(feed_frame, bg='white')
        feed_canvas.pack(side='right', fill='both', expand=True)

        scrollbar = tk.Scrollbar(feed_frame, orient='vertical', command=feed_canvas.yview)
        scrollbar.pack(side='right', fill='y')

        feed_canvas.configure(yscrollcommand=scrollbar.set)
        feed_canvas.bind('<Configure>', lambda e: feed_canvas.configure(scrollregion=feed_canvas.bbox('all')))

        inner_feed_frame = tk.Frame(feed_canvas, bg='white')
        feed_canvas.create_window((0, 0), window=inner_feed_frame, anchor='nw')

        self.add_images(inner_feed_frame)
        
    def add_images(self, inner_feed_frame):
        for photo_info in photo_locations:
            self.display_photo(inner_feed_frame, photo_info)

    def display_photo(self, inner_feed_frame, photo_info):
        photo_id = photo_info['id']
        photo_path = photo_info['path']
        caption = photo_info['caption']
        date = photo_info['date']

        select_photo = dba.select_photo_by_upd(conn, photo_id)  # Uncomment and replace `conn` with the actual database connection

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
            # Uncomment the next line to increment like count in the database
            dba.increment_like_count(conn, photo_id)
            like_button_text.set("Unlike")
         else:
            # Uncomment the next line to decrement like count in the database
            dba.decrement_like_count(conn, photo_id)
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
        self.app = CreateAlbum(self.newWindow)
    def switch_to_search(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master) 
        self.app = Search(self.newWindow)
    def switch_to_friends(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master) 
        self.app = Search(self.newWindow)
        
class MyProfile:
    def __init__(self, master):
        self.master = master
        master.geometry("600x900")
        master.title("Change User Info")
        flabel = tk.Label(master, text="First Name:")
        flabel.pack()
        self.ftext_box = tk.Text(master, width=30,height=3)
        self.ftext_box.pack()
        
        llabel = tk.Label(master, text="Last Name:")
        llabel.pack()
        self.ltext_box = tk.Text(master, width=30,height=3)
        self.ltext_box.pack()
        
        self.elabel = tk.Label(master, text="Email:")
        self.elabel.pack()
        self.etext_box = tk.Text(master, width=30,height=3)
        self.etext_box.pack()
        
      
        self.passlabel = tk.Label(master, text="Password")
        self.passlabel.pack()
        self.passtext_box = tk.Text(master, width=30,height=3)
        self.passtext_box.pack()
        
        self.htlabel = tk.Label(master, text="Hometown:")
        self.htlabel.pack()
        self.httext_box = tk.Text(master, width=30,height=3)
        self.httext_box.pack()
        
        self.genlabel = tk.Label(master, text="Gender:")
        self.genlabel.pack()
        
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
    def get_input(self):
        fname = self.ftext_box.get(1.0, 'end-1c')
        lname = self.ltext_box.get(1.0, 'end-1c')
        email = self.etext_box.get(1.0, 'end-1c')
        hometown = self.httext_box.get(1.0, 'end-1c')
        gender = self.selected_gender.get()
        #dob = self.dob_entry.get_date()
        password = self.passtext_box.get(1.0,'end-1c') # Add a widget to get the user's password, and retrieve it here
      #  album_num = 0
        try:
            conn = dba.create_conn()
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

class UploadPhoto:
    global userID
    def __init__(self, master):
        self.master = master

        self.filename_label = tk.Label(master, text="No file selected", font=("Helvetica", 14))
        self.filename_label.pack(pady=20)

        self.caption_entry_label = tk.Label(master, text="Caption:", font=("Helvetica", 14))
        self.caption_entry_label.pack(pady=10)
        
        self.caption_entry = tk.Entry(master)
        self.caption_entry.pack()

        master.geometry("500x500")
        master.title("Upload Photo")

        self.button = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        self.button.pack(pady=10)

        upload_button = tk.Button(master, text="Select photo", command=self.select_file, bg='#f0f0f0', width=15)
        upload_button.pack(pady=10)

        save_button = tk.Button(master, text="Save", command=self.upload_photo, bg='#f0f0f0', width=15)
        save_button.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)

    def select_file(self):
        filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        filepath = filedialog.askopenfilename(filetypes=filetypes)
        if filepath:
            self.filename_label.config(text=filepath)

    def upload_photo(self):
        filename = self.filename_label.cget("text")
        caption = self.caption_entry.get()
        if filename == "No file selected":
            messagebox.showerror("Error", "No photo selected")
        elif not caption:
            messagebox.showerror("Error", "Caption cannot be empty")
        else:
            unique_id = random.randint(14300,28770)
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            photo_locations.append({'id': unique_id, 'path': filename, 'caption': caption, 'date': current_date})
            dba.insert_photo(conn, unique_id, userID, caption, current_date, filename)  # Uncomment and replace `conn` and `user_id` with the actual database connection and user id
            messagebox.showinfo("Success", f"Photo uploaded\nFilepath: {filename}")
            
class CreateAlbum:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Create Album")
        self.button = tk.Button(master, text="Back", command=self.back)
        self.button.pack(pady=10)
    def back(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = HomePage(self.newWindow) 
from PIL import Image, ImageTk
class Search:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Search")

        self.back_button = tk.Button(master, text="Back", command=self.back)
        self.back_button.pack(pady=10)

        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(master, textvariable=self.search_var)
        self.search_entry.pack(pady=10)

        self.search_categories_label = tk.Label(master, text="Select search categories:")
        self.search_categories_label.pack(pady=10)

        self.search_categories_listbox = tk.Listbox(master, selectmode=tk.MULTIPLE)
        self.search_categories_listbox.pack(pady=10)
        search_categories = ["Tag", "Comment", "UserID", "Date"]
        for category in search_categories:
            self.search_categories_listbox.insert(tk.END, category)

        self.search_button = tk.Button(master, text="Search", command=self.search)
        self.search_button.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)
  
    def search(self):
        search_query = self.search_var.get()
        selected_indices = self.search_categories_listbox.curselection()
        selected_categories = [self.search_categories_listbox.get(i) for i in selected_indices]

        if not selected_categories:
            messagebox.showerror("Error", "Please select at least one search category.")
            return

        for category in selected_categories:
            if category == "Tag":
                photos = dba.search_photos_by_tags(conn, search_query)
                self.display_results("Photos", photos, display_photo=True)

            elif category == "Comment":
                comments = dba.search_comments_by_text(conn, search_query)
                self.display_results("Comments", comments)

            elif category == "UserID":
                user = dba.select_user_by_id(conn, search_query)
                if user:
                    self.display_results("User", [user])
                    photos = dba.select_photos_by_user_id(conn, search_query)
                    self.display_results("User Photos", photos, display_photo=True)
                    comments = dba.select_comments_by_user_id(conn, search_query)
                    self.display_results("User Comments", comments)
                else:
                    messagebox.showerror("Error", "No user found with the specified user ID.")

            elif category == "Date":
                comments = dba.select_comments_by_date(conn, search_query)
                self.display_results("Comments", comments)
                photos = dba.select_photos_by_date(conn, search_query)
                self.display_results("Photos", photos, display_photo=True)

    def display_results(self, title, results, display_photo=False):
        results_popup = tk.Toplevel()
        results_popup.title(title)

        # Create a Listbox to display the results
        results_listbox = tk.Listbox(results_popup, width=50, height=10)
        results_listbox.pack()

        # Add results to the Listbox
        if len(results) > 0:
            for result in results:
                results_listbox.insert(tk.END, result)
                if display_photo:
                    self.display_photo(result[1], results_popup)
        else:
            results_listbox.insert(tk.END, "No results found.")

    def display_photo(self, photo):
        try:
            image = Image.open(photo[1])  # Assuming the file path is at index 1
            image.thumbnail((200, 200))
            tk_image = ImageTk.PhotoImage(image)
            photo_label = tk.Label(self.master, image=tk_image)
            photo_label.image = tk_image
            photo_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading image: {photo}. Error: {e}")
class Find:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Search by username or tags")
        #add a search bar
        
        self.button = tk.Button(master, text="Back to Home", command=self.back)
        self.button.pack(pady=5)
        
    def back(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = Search(self.newWindow) 
        
class TrendingTags:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Trending Tags")
        self.button = tk.Button(master, text="Back to Home", command=self.back)
        self.button.pack(pady=5)
        
    def back(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = MyProfile(self.newWindow) 
    
class FriendFeed:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Friend Feed")
        
        #list friend content
        
        self.button = tk.Button(master, text="Back to Home", command=self.back)
        self.button.pack(pady=5)
        
    def back(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = HomePage(self.newWindow) 
        
class ContributionScore:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Contribution score:")
        self.button = tk.Button(master, text="Back", command=self.back)
        self.button.pack(pady=5)
        
    def back(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = MyProfile(self.newWindow) 

class FriendsList:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Friends")
        
        #insert a list
        
        self.button = tk.Button(master, text="Back", command=self.back)
        self.button.pack(pady=5)
        
    def back(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = MyProfile(self.newWindow) 

root = tk.Tk()
app = WelcomeWindow(root)
root.mainloop()
