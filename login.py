from tkinter import *
from PIL import ImageTk

# Function to handle the login process and insert user details into the database
def login():
    username = usernameEntry.get().strip()
    password = passwordEntry.get().strip()

    # Placeholder for database connection and insertion logic

# Function to handle username entry focus event
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

# Function to handle password entry focus event
def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

# Function to hide the password
def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

# Function to show the password
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

root = Tk()
root.geometry('990x660+50+50')
root.resizable(False, False)
root.title('Login Page')

bgImage = ImageTk.PhotoImage(file='background.jpg')
bgLabel = Label(root, image=bgImage)
bgLabel.pack()

heading = Label(root, text='User Login', font=('Forte', 23, 'bold'), bg='white', fg='firebrick1')
heading.place(x=590, y=100)  # Adjusted position of the heading

usernameEntry = Entry(root, width=25, font=('Forte', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=550, y=220)  # Adjusted position of username field
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(root, width=250, height=2, bg='firebrick1')
frame1.place(x=550, y=242)  # Adjusted position of the line below username field

passwordEntry = Entry(root, width=25, font=('Forte', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=550, y=270)  # Adjusted position of password field
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

frame2 = Frame(root, width=250, height=2, bg='firebrick1')
frame2.place(x=550, y=292)  # Adjusted position of the line below password field

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(root, image=openeye, bd=0, bg='white', cursor='hand2', command=hide)
eyeButton.place(x=770, y=270)  # Adjusted position of the eye button

forgotButton = Button(root, text='Forgot password?', bd=0, bg='white', cursor='hand2',
                      font=('forte', 9, 'bold'), fg='firebrick1')
forgotButton.place(x=570, y=320)  # Adjusted position of the forgot password button

loginButton = Button(root, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',
                     activebackground='white', activeforeground='firebrick1', cursor='hand2', bd=0, width=19,
                     command=login)
loginButton.place(x=550, y=370)  # Adjusted position of the login button

root.mainloop()
