import tkinter as tk
import random
import tkcalendar
from tkcalendar import DateEntry
from tkinter import *
import uuid
import datetime
import database as dba
from tkinter import filedialog, messagebox
global conn
conn = dba.create_conn()
global realUser
realUser = None
global userID
userID = -1
global photo_locations
photo_locations = []
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
        feed_frame = tk.Frame(master, bg='white')
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
            photo_id = photo_info['id']
            photo_path = photo_info['path']
            caption = photo_info['caption']
            date = photo_info['date']
            
            # select_photo = select_photo_by_upd(conn, photo_id)  # Uncomment and replace `conn` with the actual database connection
            
            image_label = tk.Label(inner_feed_frame, bg='white')
            image_label.image = self.load_image_from_path(photo_path)
            image_label.config(image=image_label.image)
            image_label.pack(pady=10)

            caption_label = tk.Label(inner_feed_frame, text=caption, font=("Helvetica", 10, "bold"), bg='white', wraplength=200, justify='center')
            caption_label.pack()

            date_label = tk.Label(inner_feed_frame, text=date, font=("Helvetica", 8), bg='white')
            date_label.pack()
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
        master.geometry("500x500")
        master.title("Edit Profile")
        
        self.button = tk.Button(master, text="See Friends", command=self.see_friends)
        self.button.pack(pady=10)
        
        self.button = tk.Button(master, text="Delete Photo or Album", command=self.back)
        self.button.pack(pady=10)
        
        self.button = tk.Button(master, text="See Contribution Score", command=self.see_cs)
        self.button.pack(pady=10)
        
        self.button = tk.Button(master, text="Back", command=self.back)
        self.button.pack(pady=10)
        
    def see_friends(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = FriendsList(self.newWindow) 
        
    def see_cs(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = HomePage(self.newWindow)
        
    def back(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = HomePage(self.newWindow)
       
class UploadPhoto:
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
            unique_id = random.randint(14300,2877777)
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            photo_locations.append({'id': unique_id, 'path': filename, 'caption': caption, 'date': current_date})
            dba.insert_photo(conn, unique_id, userID, caption, current_date)  # Uncomment and replace `conn` and `user_id` with the actual database connection and user id
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

class Search:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Search")
        
        self.button = tk.Button(master, text="Back", command=self.back)
        self.button.pack(pady=10)
        
        self.button = tk.Button(master, text="Add or Find Friends", command=self.goto_find)
        self.button.pack(pady=10)
        
        self.button = tk.Button(master, text="See Trending Tags", command=self.goto_find)
        self.button.pack(pady=10)
        
    def back(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)
    def goto_find(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master)
        self.app = Find(self.newWindow)
    def goto_trending(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master)
        self.app = TrendingTags(self.newWindow)
        
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
