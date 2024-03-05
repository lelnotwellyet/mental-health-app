import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='group2',
                              host='localhost', database='mood_tracker')
cursor = cnx.cursor()

# Function to add a new mood entry to the database
def add_mood():
    mood = mood_var.get()
    note = note_entry.get().strip()

    # Check if mood is selected
    if mood == "":
        messagebox.showerror("Error", "Please select your mood.")
        return

    # Insert the new mood entry into the database
    try:
        query = "INSERT INTO moods (mood, note) VALUES (%s, %s)"
        cursor.execute(query, (mood, note))
        cnx.commit()
        messagebox.showinfo("Success", "Mood added successfully.")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"An error occurred: {error}")

# Create the main window
window = tk.Tk()
window.title("Mood Tracker")

# Load background image
bg_image = Image.open("pattern.png")
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create a frame to group input labels and entries
input_frame = tk.Frame(window, bg="#f0f0f0")
input_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Set Gothic font
gothic_font = ("Yu Gothic", 12)

# Labels and entries for mood information
mood_label = tk.Label(input_frame, text="Select Your Mood:", bg="#f0f0f0", font=gothic_font)
mood_label.grid(row=0, column=0, padx=20, pady=10)

mood_var = tk.StringVar()
mood_options = ["😄 Happy", "😐 Neutral", "😢 Sad"]
mood_menu = tk.OptionMenu(input_frame, mood_var, *mood_options)
mood_menu.config(bg="white", font=gothic_font)
mood_menu.grid(row=0, column=1, padx=20, pady=10)

note_label = tk.Label(input_frame, text="Optional Note:", bg="#f0f0f0", font=gothic_font)
note_label.grid(row=1, column=0, padx=20, pady=10)

note_entry = tk.Entry(input_frame, bg="white", fg="black", font=gothic_font)
note_entry.grid(row=1, column=1, padx=20, pady=10)

# Create a button to add a new mood entry
add_button = tk.Button(window, text="Add Mood", command=add_mood, bg="green", font=gothic_font)
add_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Run the Tkinter event loop
window.mainloop()

# Close the database connection when the program exits
cursor.close()
cnx.close()
