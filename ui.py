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
conn = dba.createConn()
global realUser
realUser = None
global userID
global various
various = 0
global photoLocations
photoLocations = []
#Little helper that is used to retrive locally stored photos
def popPhotos():
    conn = dba.createConn()
    try:
        global userID
        results = dba.getAllPhotosForAlbum(conn,userID) #userID is used as UAD for home photos
        for i in results:
            photoLocations.append({'id': i[0], 'path': i[4], 'caption': i[2], 'date': i[3]})
            print(i)
    except Exception as error:
        print(error)
#Begin Class Declerations
class WelcomeWindow:
    def _Init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("App Landing Page")
        #Basic Button Setup
        self.button = tk.Button(master, text="Log In", command=self.switchWindow1)
        self.button.pack(pady=50)
        self.button = tk.Button(master, text="Sign Up", command=self.switchWindow2)
        self.button.pack(pady=50)
        
    def switchWindow1(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master)
        self.app = LoginScreen(self.newWindow)
    def switchWindow2(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master)
        self.app = SignUpScreen(self.newWindow)
        
class LoginScreen:
    def _Init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Log In Existing User")
        
        self.ulabel = tk.Label(master, text="User ID:")
        self.ulabel.pack()
        self.utextBox = tk.Text(master, width=50,height = 3)
        self.utextBox.pack()
        
        self.plabel = tk.Label(master, text="Password:")
        self.plabel.pack()
        self.ptextBox = tk.Text(master, width=50, height=3)
        self.ptextBox.pack()
        
        self.button = tk.Button(master, text="Log In", command=self.getInput)
        self.button.pack(pady=50)
    def getInput(self):
        #We use end-1c because this trims the \n character that we were getting here.
        userId = self.utextBox.get(1.0, 'end-1c')
        password = self.ptextBox.get(1.0, 'end-1c')

        try:
            #establish connection
            conn = dba.createConn()
            #populate a realuser
            realUser = dba.selectUserByIdAndPassword(conn, userId, password)
            #Now we check if there is a present user and there password matches
            if realUser and realUser[7] == password:
                global userID
                userID = realUser[0] #Set userID as person is now logged in
                  
                popPhotos() #init the photo method so we can load there feed when they login
                self.switchWindow(userId)
                
            else:
                print("Invalid Entry. Try Again.")
                messagebox.showerror("Error", "Invalid user ID or password.") #tell user they messed up
                print(realUser) #debug info
                print(realUser[2]) #debug info
        except Exception as error:
            print("Error:", error)
   
    def switchWindow(self, userId):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)

    
class SignUpScreen:
    def _Init__(self, master):
        self.master = master
        master.geometry("600x900")
        master.title("New User Sign Up")
        #Bunch of boring labels, they setup the register screen, flabel is first name
        flabel = tk.Label(master, text="First Name:")
        flabel.pack()
        self.ftextBox = tk.Text(master, width=30,height=3)
        self.ftextBox.pack()
        #last name label
        llabel = tk.Label(master, text="Last Name:")
        llabel.pack()
        self.ltextBox = tk.Text(master, width=30,height=3)
        self.ltextBox.pack()
        #email label
        self.elabel = tk.Label(master, text="Email:")
        self.elabel.pack()
        self.etextBox = tk.Text(master, width=30,height=3)
        self.etextBox.pack()
        #user ID label
        self.uidlabel = tk.Label(master, text="User ID:")
        self.uidlabel.pack()
        self.uidtextBox = tk.Text(master, width=30,height=3)
        self.uidtextBox.pack()
        #password label 
        self.passlabel = tk.Label(master, text="Password")
        self.passlabel.pack()
        self.passtextBox = tk.Text(master, width=30,height=3)
        self.passtextBox.pack()
        #hometown label
        self.htlabel = tk.Label(master, text="Hometown:")
        self.htlabel.pack()
        self.httextBox = tk.Text(master, width=30,height=3)
        self.httextBox.pack()
        #gender label
        self.genlabel = tk.Label(master, text="Gender:")
        self.genlabel.pack()
        #various options are stored here, other is used to simplfy things
        genderOptions = ["Male", "Female", "Other"]
        self.selectedGender = tk.StringVar()
        self.selectedGender.set(genderOptions[0])
        self.genderMenu = tk.OptionMenu(master, self.selectedGender, *genderOptions)
        self.genderMenu.pack()  
        #Setup dob here
        self.doblabel = tk.Label(master, text="Date of Birth:")
        self.doblabel.pack()
        self.dobEntry = DateEntry(master, width=15, background='darkblue',foreground='white', borderwidth=2)
        self.dobEntry.pack(padx=10, pady=10)
        
        self.button = tk.Button(master, text="Create Your Account", command=self.getInput)
        self.button.pack(pady=5)
        
        self.button = tk.Button(master, text="Back to Home", command=self.back)
        self.button.pack(pady=5)
    #  print(httextBox)
     
    def back(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = WelcomeWindow(self.newWindow) 
        
    def switchWindow(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master) 
        self.app = HomePage(self.newWindow)\
    #Real driver function here
    def getInput(self):
        #Retrives all the labels text values after they have been entered
        fname = self.ftextBox.get(1.0, 'end-1c')
        lname = self.ltextBox.get(1.0, 'end-1c')
        email = self.etextBox.get(1.0, 'end-1c')
        userId = self.uidtextBox.get(1.0, 'end-1c')
        hometown = self.httextBox.get(1.0, 'end-1c')
        gender = self.selectedGender.get()
        dob = self.dobEntry.getDate()
        password = self.passtextBox.get(1.0,'end-1c') # Add a widget to get the user's password, and retrieve it here
        albumNum = 0 # most users start with 0 albums, hopefully.
        try:
            #Setup connection
            conn = dba.createConn()
            dba.insertUser(userId, fname, lname, email, dob, hometown, gender, password, albumNum,conn) #make database call
            conn = dba.createConn()
            realUser = dba.selectUserById(conn,userId)
            global userID
            userID = userId #set user as they are loggedin
            popPhotos() #fill feed anyways even though it should be empty
        except():
            print("Invalid Entry Try Again")
        
        self.switchWindow()
    
class HomePage:
    def _Init__(self, master):
        self.master = master
        master.geometry("800x500")
        master.title("User xHome Page")
        self.photoLocations = []
        self.createUiElements(master)
        self.configureFeed()
        
    #Wrap Ui Eles in Func
    def createUiElements(self, master):
        customFont = ("Helvetica", 12, "bold") #nice font

        buttonFrame = self.createButtonFrame(master, customFont)
        #feedFrame is going to contain our instagram feed
        feedFrame, feedCanvas = self.createFeedFrame(master)
        feedFrame.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        #scrollBar helper func
        scrollbar = self.createScrollbar(feedFrame, feedCanvas)
        scrollbar.pack(side='right', fill='y')

        innerFeedFrame = self.createInnerFeedFrame(feedCanvas)
        self.addRandomImages(innerFeedFrame)

        # Pack the buttonFrame after all other elements are created and packed
        buttonFrame.pack(side='right', fill='y', padx=10, pady=10)

    #On click change
    def updateScrollRegion(event):
        feedCanvas.configure(scrollregion=feedCanvas.bbox("all")) 
        innerFeedFrame.bind("<Configure>", updateScrollRegion) #bind is a cool function we binde configure so that on updateScrollRegion we change the innerframe contents
        return innerFeedFrame
    #Sets up Button Frame
    def createButtonFrame(self, master, customFont):
        buttonBg = "#007BFF" #light grey
        buttonFg = "#000000" #black
        buttonActiveBg = "#0056B3" #light grey
        buttonActiveFg = "#000000" #black

        buttonFrame = tk.Frame(master)
        #Store buttons in tuple list with name and function so we can iterate through them
        buttons = [
            ("Search", self.switchToSearch), 
            ("Upload Photo", self.switchToUpload),
            ("Friends", self.switchToFriends),
            ("Albums", self.switchToAlbums),
            ("Edit Profile", self.switchToProfile),
            ("Trending Tags", self.switchToTrending)
        ]

        for text, command in buttons:
            button = tk.Button(buttonFrame, text=text, command=command, font=customFont, bg=buttonBg, fg=buttonFg, activebackground=buttonActiveBg, activeforeground=buttonActiveFg, relief="solid", bd=1, borderwidth=0)
            button.pack(pady=10, side='top')

        return buttonFrame
    #helper funciton sets up feed
    def createFeedFrame(self, master):
        feedFrame = ttk.Frame(master) #ttk is special library from tinkter with fun sub methods for building ui
        feedCanvas = tk.Canvas(feedFrame, bg='white')
        feedCanvas.pack(side='left', fill='both', expand=True)
        return feedFrame, feedCanvas
    #Create ScrolLBar
    def createScrollbar(self, feedFrame, feedCanvas):
        scrollbar = tk.Scrollbar(feedFrame, orient='vertical', command=feedCanvas.yview) #basic scrollbar setup orient vertical instead of horizontal
        feedCanvas.configure(yscrollcommand=scrollbar.set)
        feedCanvas.bind('<Configure>', lambda e: feedCanvas.configure(scrollregion=feedCanvas.bbox('all'))) #lambda means this is gonna run through all bbox in feedcanvas
        return scrollbar
    #within our feed we have an inner method that will hold the photos
    def createInnerFeedFrame(self, feedCanvas):
        innerFeedFrame = tk.Frame(feedCanvas, bg='white')
        feedCanvas.createWindow((0, 0), window=innerFeedFrame, anchor='nw')
        return innerFeedFrame
    #setup feed here by getting all the photos and randomly shufflying them
    def configureFeed(self):
        self.photoLocations = dba.getAllPhotos(conn) #this is a cool call gets all photo info
        random.shuffle(self.photoLocations)
    #load photos from dba
    def addRandomImages(self, innerFeedFrame):
        self.photoLocations = dba.getAllPhotos(conn) #get all photo info
        for photoInfo in self.photoLocations:
            print(photoInfo)
            self.displayPhoto(innerFeedFrame, photoInfo) #iterate photos and siplay them
    def displayPhoto(self, innerFeedFrame, photoInfo):
        print(photoInfo)
        photoId = photoInfo['upd']
        photoPath = photoInfo['filepath']
        caption = photoInfo['caption']
        date = photoInfo['data']
        #print(photoPath)
        selectPhoto = dba.selectPhotoByUpd(conn, photoId)  #call photo upload feature

        imageLabel = tk.Label(innerFeedFrame, bg='white', borderwidth=2, relief="groove")
        imageLabel.image = self.loadImageFromPath(photoPath)
        imageLabel.config(image=imageLabel.image)
        imageLabel.pack(pady=10,anchor='center')
       
        
        likeButtonText = tk.StringVar()
        likeButtonText.set("Like")
        likeButton = tk.Button(innerFeedFrame, textvariable=likeButtonText, command=lambda: self.likePhoto(photoId, likeButtonText))
        likeButton.pack()
        # Add comment button and comment section
        commentButton = tk.Button(innerFeedFrame, text="Comments", command=lambda: self.showCommentsPopup(photoId))
        commentButton.pack()

        # Add tags button and tag section
        tagButton = tk.Button(innerFeedFrame, text="Tags", command=lambda: self.showTagsPopup(photoId))
        tagButton.pack()

        captionLabel = tk.Label(innerFeedFrame, text=caption, font=("Helvetica", 10, "bold"), bg='white', wraplength=200, justify='center')
        captionLabel.pack()

        dateLabel = tk.Label(innerFeedFrame, text=date, font=("Helvetica", 8), bg='white')
        dateLabel.pack()

    # Like photo method
    def likePhoto(self, photoId,likeButtonText):
         if likeButtonText.get() == "Like":
            
            dba.incrementLikeCount(conn, photoId)
            likeButtonText.set("Unlike")
         else:
          
            dba.decrementLikeCount(conn, photoId)
            likeButtonText.set("Like")

        
    # Show comments popup
    def showCommentsPopup(self, photoId):
        
        comments = dba.selectCommentsByUpd(conn,photoId)
        commentsPopup = tk.Toplevel()
        commentsPopup.title("Comments")

    # Create a Listbox to display the comments
        commentsListbox = tk.Listbox(commentsPopup, width=50, height=10)
        commentsListbox.pack()

    # Display existing comments
        if(len(comments) > 1):
            for comment in comments:
        # Add each comment to the Listbox
                commentsListbox.insert(tk.END, comment)

    # Add new comment entry and submit button
        newCommentEntry = tk.Entry(commentsPopup)
        newCommentEntry.pack()

        submitCommentButton = tk.Button(commentsPopup, text="Submit Comment", command=lambda: self.submitComment(photoId, newCommentEntry.get()))
        submitCommentButton.pack()

    # Submit comment method
    def submitComment(self, photoId, commentText):
        x = random.randint(0,500000)
        dba.insertComment(conn,x,commentText,userID,photoId,datetime.datetime.now().strftime("%Y-%m-%d"))
        if hasattr(self, 'commentsPopup') and self.commentsPopup:
            self.commentsPopup.destroy()
        self.showCommentsPopup(photoId)
    def showTagsPopup(self, photoId):
        if hasattr(self, 'tagsPopup') and self.tagsPopup:
            self.tagsPopup.destroy()
        tagsPopup = tk.Toplevel()
        tagsPopup.title("Tags")
    
        tagsListbox = tk.Listbox(tagsPopup, width=50, height=10)
        tagsListbox.pack()

        tags = dba.selectTagsByUpd(conn, photoId)
        for tag in tags:
            tagsListbox.insert(tk.END, tag)

        newTagEntry = tk.Entry(tagsPopup)
        newTagEntry.pack()

        submitTagButton = tk.Button(tagsPopup, text="Submit Tag", command=lambda: self.submitTag(photoId, newTagEntry.get()))
        submitTagButton.pack()

    # Submit tag method
    def submitTag(self, photoId, tagText):
        dba.insertTag(conn,tagText,photoId)
        self.showTagsPopup(photoId)
        
    def loadImageFromPath(self, filepath):
        from PIL import Image, ImageTk

        img = Image.open(filepath)
        self.master.update()
        img = img.resize((int(self.master.winfoWidth() / 4), int(self.master.winfoHeight() / 4)), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    def switchToTrending(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = TrendingTags(self.newWindow)
    def switchToFriends(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master) 
        self.app = Friends(self.newWindow)
    def switchToProfile(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master) 
        self.app = MyProfile(self.newWindow) 
    def switchToUpload(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master) 
        self.app = UploadPhoto(self.newWindow)
    def switchToCreateAlbum(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master) 
        self.app =  AlbumsPage(self.newWindow)
    def switchToSearch(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master) 
        self.app = Search(self.newWindow)
    def switchToAlbums(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = AlbumsPage(self.newWindow)


class AlbumsPage:
    global userID

    def _Init__(self, master):
        self.master = master
        master.geometry("800x500")
        master.title("Albums")
        #Set up Album Label
        self.titleLabel = tk.Label(master, text="Albums", font=("Helvetica", 16))
        self.titleLabel.pack(pady=10)
        #Frame Albums
        self.albumsFrame = tk.Frame(master)
        self.albumsFrame.pack(pady=10)

        self.loadAlbums()
        #Redirect to Create Album
        createButton = tk.Button(master, text="Create Album", command=self.createAlbum, bg='#f0f0f0', width=15)
        createButton.pack(pady=10)

        backButton = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        backButton.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)

    def loadAlbums(self):
        albums = dba.selectAlbumsByUid(conn, userID) #Call dba all albums by UID

        for album in albums:
            albumButton = tk.Button(self.albumsFrame, text=album[1], command=lambda a=album[0]: self.viewAlbum(a)) #Dispolay album info
            albumButton.pack(side=tk.LEFT, padx=10) #Center to left

    def viewAlbum(self, uad):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = ViewAlbum(self.newWindow, uad)

    def createAlbum(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = CreateAlbum(self.newWindow)
class CreateAlbum:
    global userID

    def _Init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Create Album")
        #Setup Album Name Labels
        self.albumNameLabel = tk.Label(master, text="Album Name:", font=("Helvetica", 14))
        self.albumNameLabel.pack(pady=10)
        #Get Album Entry
        self.albumNameEntry = tk.Entry(master)
        self.albumNameEntry.pack()
        #Submit Create Info
        createButton = tk.Button(master, text="Create", command=self.createAlbum, bg='#f0f0f0', width=15)
        createButton.pack(pady=10)

        backButton = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        backButton.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)

    def createAlbum(self):
        albumName = self.albumNameEntry.get()
        if not albumName:
            messagebox.showerror("Error", "Album name cannot be empty") #Need valid Album
        else:
            uad = random.randint(1,15000) #Set random unique album

            # Get the current date
            doc = datetime.datetime.now()

            # Insert the album into the database
            dba.insertAlbum(conn, uad, albumName, userID, doc)
            messagebox.showinfo("Success", "Album created successfully")

            # Redirect to the newly created album view
            self.master.withdraw()
            self.newWindow = tk.Toplevel(self.master)
            self.app = ViewAlbum(self.newWindow, uad)
# Modified ViewAlbum class
class ViewAlbum:
    def _Init__(self, master, uad):
        #Set up Album Info
        self.master = master
        self.uad = uad
        master.geometry("800x600")
        master.title("View Album")

        # Fetch album name and display it
        album = dba.selectAlbumByUad(conn, uad)
        if album:
            self.albumName = album[1] #Get Album in Column 1
        else:
            self.albumName = "Untitled Album"
        #Setup Album Labels
        self.albumNameLabel = tk.Label(master, text=self.albumName, font=("Helvetica", 18))
        self.albumNameLabel.pack(pady=10)

        #Setup Title Labels
        self.titleLabel = tk.Label(master, text="Album Photos", font=("Helvetica", 16))
        self.titleLabel.pack(pady=10)
        #Setup Photo Frames
        self.photosFrame = tk.Frame(master)
        self.photosFrame.pack(pady=10)
        #Loop Photos
        self.loadPhotos()
        #Setup Add Photo
        addPhotoButton = tk.Button(master, text="Add Photo", command=self.addPhoto, bg='#f0f0f0', width=15)
        addPhotoButton.pack(pady=10)

        backButton = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        backButton.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = AlbumsPage(self.newWindow)

    def loadPhotos(self):
        photos = dba.selectPhotosByUad(conn, self.uad) #Get photos within the unique album identifier

        for photo in photos:
            img = Image.open(photo[4])   #Get photo at filepath
            img = img.resize((100, 100), Image.ANTIALIAS) #Create Image
            img = ImageTk.PhotoImage(img)

            photoLabel = tk.Label(self.photosFrame, image=img) #Setup Photo Labels
            photoLabel.image = img
            photoLabel.pack(side=tk.LEFT, padx=10)
    #Adding Photo
    def addPhoto(self):
        filepath = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*"))) #Get all photo types
        if filepath:
            self.selectedFilepath = filepath   #Setup filepath
            self.captionWindow = tk.Toplevel(self.master)
            self.captionWindow.title("Enter Caption")#Setup seperate caption captuer
            self.captionLabel = tk.Label(self.captionWindow, text="Enter a caption for this photo:", font=("Helvetica", 14)) #Capture caption
            self.captionLabel.pack(pady=10)
            self.captionEntry = tk.Entry(self.captionWindow)
            self.captionEntry.pack()
            self.submitCaptionButton = tk.Button(self.captionWindow, text="Submit", command=self.submitCaption, bg='#f0f0f0', width=15)
            self.submitCaptionButton.pack(pady=10) #Send Caption Back
        else:
            messagebox.showinfo("Info", "No file was selected.")

    def submitCaption(self):
        caption = self.captionEntry.get()
        filepath = self.selectedFilepath

        with open(filepath, "rb") as file:
            data = file.read()

        dba.insertPhoto(conn, random.randint(1100,23000), self.uad, caption, data, filepath) #Pass photo with caption in

        # Close the caption window
        self.captionWindow.destroy()

        # Reload photos in the album
        for widget in self.photosFrame.winfoChildren():
            widget.destroy()

        self.loadPhotos()
class FriendFeed:
    global userID
    def _Init__(self, master):
        self.master = master
        master.geometry("800x500")
        master.title("Friend Feed")

        self.titleLabel = tk.Label(master, text="Friend Feed", font=("Helvetica", 16))
        self.titleLabel.pack(pady=10)

        self.scrollbar = tk.Scrollbar(master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.feedListbox = tk.Listbox(master, yscrollcommand=self.scrollbar.set, width=80, height=20)
        self.feedListbox.pack(pady=10)

        self.scrollbar.config(command=self.feedListbox.yview)

        self.loadFriendFeed()

        backButton = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        backButton.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)

    def loadFriendFeed(self):
        # Fetch recent photo uploads from friends
        recentUploads = dba.getFriendFeed(conn, userID)

        for upload in recentUploads:
            friendName = upload[0]
            photoName = upload[1]
            uploadTime = upload[2]

            self.feedListbox.insert(tk.END, f"{friendName} uploaded '{photoName}' on {uploadTime}")
class MyProfile:
    def _Init__(self, master):
        self.master = master
        master.geometry("600x900")
        master.title("Change User Info")
        #Setup First Name Label
        flabel = tk.Label(master, text="First Name:")
        flabel.pack()
        self.ftextBox = tk.Text(master, width=30,height=3)
        self.ftextBox.pack()
        #Setup Last Name Label
        llabel = tk.Label(master, text="Last Name:")
        llabel.pack()
        self.ltextBox = tk.Text(master, width=30,height=3)
        self.ltextBox.pack()
        #Setup Email Label
        self.elabel = tk.Label(master, text="Email:")
        self.elabel.pack()
        self.etextBox = tk.Text(master, width=30,height=3)
        self.etextBox.pack()
        #Setup Password Label
      
        self.passlabel = tk.Label(master, text="Password")
        self.passlabel.pack()
        self.passtextBox = tk.Text(master, width=30,height=3)
        self.passtextBox.pack()
        #Set HomeTown Label
        self.htlabel = tk.Label(master, text="Hometown:")
        self.htlabel.pack()
        self.httextBox = tk.Text(master, width=30,height=3)
        self.httextBox.pack()
        #Set Gender Options
        self.genlabel = tk.Label(master, text="Gender:")
        self.genlabel.pack()
        #Setup Gender Options
        genderOptions = ["Male", "Female", "Other"]
        self.selectedGender = tk.StringVar()
        self.selectedGender.set(genderOptions[0])
        self.genderMenu = tk.OptionMenu(master, self.selectedGender, *genderOptions)
        self.genderMenu.pack()  
        
       # self.doblabel = tk.Label(master, text="Date of Birth:")
        #self.doblabel.pack()
        #self.dobEntry = DateEntry(master, width=15, background='darkblue',foreground='white', borderwidth=2)
        #self.dobEntry.pack(padx=10, pady=10)
        
        self.button = tk.Button(master, text="Update Changes", command=self.getInput)
        self.button.pack(pady=5)
        
        self.button = tk.Button(master, text="Back to Home", command=self.back)
        self.button.pack(pady=5)
    #  print(httextBox)
     
    def back(self):
        self.master.withdraw()  
        self.newWindow = tk.Toplevel(self.master)  
        self.app = WelcomeWindow(self.newWindow) 
        
    def switchWindow(self):
        self.master.withdraw() 
        self.newWindow = tk.Toplevel(self.master) 
        self.app = HomePage(self.newWindow)
    #Main Driver Function
    def getInput(self):
        #Get TextBox INputs
        fname = self.ftextBox.get(1.0, 'end-1c')
        lname = self.ltextBox.get(1.0, 'end-1c')
        email = self.etextBox.get(1.0, 'end-1c')
        hometown = self.httextBox.get(1.0, 'end-1c')
        gender = self.selectedGender.get()
        #dob = self.dobEntry.getDate()
        password = self.passtextBox.get(1.0,'end-1c') 
      #  albumNum = 0
        try:
            conn = dba.createConn() #Various If Statements Loop Through DBA Update Calls
            if(fname != ""):
                dba.updateUserFname(conn,userID,fname)
            if(lname != ""):
                dba.updateUserLname(conn,userID,lname)
            if(email != ""):
                dba.updateUserEmail(conn,userID,email)
            if(hometown != ""):
                dba.updateUserHometown(conn,userID,hometown)
            if(gender != ""):
                dba.updateUserGender(conn,userID,gender)
            if(password!= ""):
                dba.updateUserPassword(conn,userID,password)
                
        except():
            print("Invalid Entry Try Again")
        
        self.switchWindow()
class Friends:
    def _Init__(self, master):
        self.master = master
        master.geometry("800x1200")
        master.title("Friends")
        #Setup Friend Search
        searchLabel = tk.Label(master, text="Search Friends by User ID:", font=("Helvetica", 14))
        searchLabel.pack(pady=10)

        self.searchEntry = tk.Entry(master)
        self.searchEntry.pack()

        searchButton = tk.Button(master, text="Search", command=self.searchUsers, bg='#f0f0f0', width=15)
        searchButton.pack(pady=10)

        self.searchResultsListbox = tk.Listbox(master, width=50, height=5)
        self.searchResultsListbox.pack(pady=10)
        #Setup Friend Box
        self.friendsListbox = tk.Listbox(master, width=50, height=15)
        self.friendsListbox.pack(pady=10)
        #Call update list on every recall
        self.updateFriendsList()
        #Setup add friend button
        addFriendButton = tk.Button(master, text="Add Friend", command=self.addFriend, bg='#f0f0f0', width=15)
        addFriendButton.pack(side='left', padx=10)
        #setup remove friend button
        removeFriendButton = tk.Button(master, text="Remove Friend", command=self.removeFriend, bg='#f0f0f0', width=15)
        removeFriendButton.pack(side='right', padx=10)
        #back button
        backButton = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        backButton.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)
    #Setup simple search
    def searchUsers(self):
        searchQuery = self.searchEntry.get()
        if searchQuery:
            try:
                userId = int(searchQuery) #Get typesafe user id
                searchResults = dba.selectUserById(conn, userId) #call dba connection
                if searchResults:
                    self.updateSearchResultsList(searchResults) #append to listbox
                else:
                    self.searchResultsListbox.delete(0, tk.END) #return nothing
                    messagebox.showerror("Error", "No user found with this User ID")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid User ID")
    def updateSearchResultsList(self, user):
        self.searchResultsListbox.delete(0, tk.END)
        self.searchResultsListbox.insert(tk.END, f"{user[1]} {user[2]} ({user[3]})") #add user info

    def updateFriendsList(self, friends=None):
        self.friendsListbox.delete(0, tk.END)
        if friends is None:
            friends = dba.selectFriendsByUserId(conn, userID) #call freinds by user id dba call

        for friend in friends:
            self.friendsListbox.insert(tk.END, f"{friend[1]}") #add friend id to friends list

    def addFriend(self):
        selectedIndex = self.searchResultsListbox.curselection() #get the currently selected query
        if selectedIndex:
            friendEmail = self.searchResultsListbox.get(selectedIndex).split('(')[-1].split(')')[0] #parse for there email
            friend = dba.selectUserByEmail(conn, friendEmail) #store email
            if friend:
                friend = friend[0] #get friend id which is stroed in column 0 in users
                dba.insertFriend(conn, userID, friend[0], datetime.datetime.now())
                messagebox.showinfo("Success", f"Added {friend[1]} {friend[2]} as a friend") #sucsess
                self.updateFriendsList()
            else:
                messagebox.showerror("Error", "Unable to find the selected user")

    def removeFriend(self):
        selectedIndex = self.friendsListbox.curselection() #get current query
        if selectedIndex:
            friendId = self.friendsListbox.get(selectedIndex).split('(')[-1].split(')')[0] #parse for friend id
            friend = dba.selectUserById(conn,friendId) #now pass friend id back
            if friend:
                dba.deleteFriend(conn, userID, friend[0]) #if valid friend now we delete them
                messagebox.showinfo("Success", f"Removed {friend[1]} {friend[2]} as a friend") #sucsess
                self.updateFriendsList() #refresh
            else:
                messagebox.showerror("Error", "Unable to find the selected user")
                   
class UploadPhoto:
    global userID #Ensure we are searching the right user
    def _Init__(self, master):
        self.master = master
        #Set up FileName Label
        self.filenameLabel = tk.Label(master, text="No file selected", font=("Helvetica", 14))
        self.filenameLabel.pack(pady=20)
        #Setup Caption Label
        self.captionEntryLabel = tk.Label(master, text="Caption:", font=("Helvetica", 14))
        self.captionEntryLabel.pack(pady=10)
        #Get Caption as Entry
        self.captionEntry = tk.Entry(master)
        self.captionEntry.pack()

        master.geometry("500x500")
        master.title("Upload Photo")
        #Back Button
        self.button = tk.Button(master, text="Back", command=self.back, bg='#f0f0f0', width=15)
        self.button.pack(pady=10)
        #Upload Button
        self.uploadButton = tk.Button(master, text="Select photo", command=self.selectFile, bg='#f0f0f0', width=15)
        self.uploadButton.pack(pady=10)
        #Save Button
        self.saveButton = tk.Button(master, text="Save", command=self.uploadPhoto, bg='#f0f0f0', width=15)
        self.saveButton.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)
    #Accept jpeg and png and as catch all we can acccept whatever uploads but it mihgt not be valid
    def selectFile(self):
        filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        filepath = filedialog.askopenfilename(filetypes=filetypes)
        if filepath:
            self.filenameLabel.config(text=filepath) #Setup filename from filepath from os
    
    def uploadPhoto(self):
        filename = self.filenameLabel.cget("text")
        caption = self.captionEntry.get()
        if filename == "No file selected":
            messagebox.showerror("Error", "No photo selected")
        elif not caption:
            messagebox.showerror("Error", "Caption cannot be empty")
        else:
            uniqueId = random.randint(14300,28770) #Randomly generate uuid
            currentDate = datetime.datetime.now().strftime("%Y-%m-%d") #Get current date
            photoLocations.append({'id': uniqueId, 'path': filename, 'caption': caption, 'date': currentDate}) #Add photo to photo locations array
            dba.insertPhoto(conn, uniqueId, userID, caption, currentDate, filename)  #Insert Symlink in Databse
            messagebox.showinfo("Success", f"Photo uploaded\nFilepath: {filename}")
            

from PIL import Image, ImageTk
class Search:
    def _Init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.title("Search")
        #Setup Buttons
        self.backButton = tk.Button(master, text="Back", command=self.back)
        self.backButton.pack(pady=10)
         #Set up Search Input
        self.search_var = tk.StringVar()
        self.searchEntry = tk.Entry(master, textvariable=self.search_var)
        self.searchEntry.pack(pady=10)
        #Setup Display Input
        self.searchCategoriesLabel = tk.Label(master, text="Select search categories:")
        self.searchCategoriesLabel.pack(pady=10)

        self.searchCategoriesListbox = tk.Listbox(master, selectmode=tk.MULTIPLE)
        self.searchCategoriesListbox.pack(pady=10)
        searchCategories = ["Tag", "Comment", "UserID", "Date"]
        for category in searchCategories: 
            self.searchCategoriesListbox.insert(tk.END, category) #Display all categories 

        self.searchButton = tk.Button(master, text="Search", command=self.search)
        self.searchButton.pack(pady=10)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)
     #Searh Function
    def search(self):
        searchQuery = self.search_var.get()
        selectedIndices = self.searchCategoriesListbox.curselection()
        selectedCategories = [self.searchCategoriesListbox.get(i) for i in selectedIndices] #Collect all selected driver categories

        if not selectedCategories:
            messagebox.showerror("Error", "Please select at least one search category.")
            return

        for category in selectedCategories:
            if category == "Tag": #Tag Category
                photos = dba.searchPhotosByTags(conn, searchQuery) #Search for photos with this tag
                self.displayResults("Photos", photos, displayPhoto=True) # Display The Photo with This Tag

            elif category == "Comment":
                comments = dba.searchCommentsByText(conn, searchQuery) #Get all comments related with this text
                self.displayResults("Comments", comments) #Display comments

            elif category == "UserID":
                user = dba.selectUserById(conn, searchQuery) #Get user info
                if user:
                    self.displayResults("User", [user])
                    photos = dba.selectPhotosByUserId(conn, searchQuery) #Display User Photos
                    self.displayResults("User Photos", photos, displayPhoto=True)
                    comments = dba.selectCommentsByUserId(conn, searchQuery) #Display User Comments
                    self.displayResults("User Comments", comments) 
                else:
                    messagebox.showerror("Error", "No user found with the specified user ID.")

            elif category == "Date":
                comments = dba.selectCommentsByDate(conn, searchQuery) #Get comments by date
                self.displayResults("Comments", comments)
                photos = dba.selectPhotosByDate(conn, searchQuery) #Get Photos by Date
                self.displayResults("Photos", photos, displayPhoto=True)

    def displayResults(self, title, results, displayPhoto=False):
        resultsWindow = tk.Toplevel()
        resultsWindow.title(title)
        #Check to make sure Results is valid
        if results is not None and len(results) > 0:
            for result in results:
                if displayPhoto: #Get photo information to pass back
                    photoId = result['id']
                    photoPath = result['path']
                    caption = result['caption']
                    date = result['date']

                    self.displayPhoto(resultsWindow, photoId, photoPath, caption, date)
                else:
                    resultLabel = tk.Label(resultsWindow, text=str(result), wraplength=400)
                    resultLabel.pack()
        else:
            noResultsLabel = tk.Label(resultsWindow, text="No results found.")
            noResultsLabel.pack()
            
    def displayPhoto(self, photo):
        try:
            #Try opening an image
            image = Image.open(photo[4])  #file path is at index 4
            image.thumbnail((200, 200))
            tkImage = ImageTk.PhotoImage(image)
            #Create Photo Labels
            photoLabel = tk.Label(self.master, image=tkImage)
            photoLabel.image = tkImage
            photoLabel.pack(pady=10)
        except Exception as e:
            print(f"Error loading image: {photo}. Error: {e}")
class TrendingTags:
    def _Init__(self,master):
        self.master = master
        master.geometry("500x500")
        master.title("Trending Tags")

        self.backButton = tk.Button(master, text="Back", command=self.back)

        tags = dba.getTopTags(searchQuery) #Get comments by date
        self.displayResults("Top Tags", tags)

    def back(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = HomePage(self.newWindow)
root = tk.Tk()
app = WelcomeWindow(root)
root.mainloop()
