import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

def button_function():
    print("Login button clicked!")

app = customtkinter.CTk()  # creating custom tkinter window
app.geometry("900x740")
app.title('Login')
def button_function():
    app.destroy()            # destroy current window and creating new one
    w = customtkinter.CTk()
    w.geometry("1280x720")
    w.title('Welcome')
    l1=customtkinter.CTkLabel(master=w, text="Home Page",font=('Century Gothic',60))
    l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
    w.mainloop()

img1=ImageTk.PhotoImage(Image.open("pattern.png"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20),anchor=tkinter.CENTER)
l2.place(x=50, y=45)
entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)
entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)
l3=customtkinter.CTkLabel(master=frame, text="Forget password?",font=('Century Gothic',12))
l3.place(x=155,y=195)
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)

img3=customtkinter.CTkImage(Image.open("124010.png").resize((20,20)))
button2= customtkinter.CTkButton(master=frame, image=img3, text="mat daba", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button2.place(x=50, y=290)

app.mainloop()












app.mainloop()












app.mainloop()