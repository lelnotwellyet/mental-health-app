import tkinter as tk
from PIL import ImageTk, Image
import os

class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x740")
        self.title("Home Page")

        self.bg_image = Image.open("pattern.png")
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.pack(fill="both", expand=True)

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            "Login Page",
            "Doctor Appointment Scheduler",
            "Mood Tracker",
            "Medicine Tracker",
            "Feedback Form"
        ]
        button_commands = [
            self.open_login_page,
            self.open_doctor_appointment,
            self.open_mood_tracker,
            self.open_medicine_tracker,
            self.open_feedback_form
        ]

        for i, text in enumerate(button_texts):
            button = tk.Button(self, text=text, font=("Helvetica", 16), command=button_commands[i])
            button.place(relx=0.5, rely=0.2 + i * 0.1, anchor="center")

    def open_login_page(self):
        os.system("python login.py")

    def open_doctor_appointment(self):
        os.system("python rupali.py")

    def open_mood_tracker(self):
        os.system("python rhemat.py")

    def open_medicine_tracker(self):
        os.system("python medicinetracker2.py")

    def open_feedback_form(self):
        os.system("python nitish.py")

if __name__ == "__main__":
    app = HomePage()
    app.mainloop()

