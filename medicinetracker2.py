import mysql.connector
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='group2',
                              host='localhost', database='medicine_tracker')
cursor = cnx.cursor()

# Function to validate positive integer input
def validate_positive_input(action, value_if_allowed):
    if action == '1':  # insert
        if value_if_allowed.isdigit():
            return True
        else:
            return False
    return True

# Function to add a new medicine to the database
def add_medicine():
    medicine_name = medicine_name_entry.get().strip()
    dosage = dosage_entry.get().strip()
    frequency = frequency_entry.get().strip()
    start_date = start_date_entry.get().strip()
    end_date = end_date_entry.get().strip()

    # Check if all fields are filled
    if not medicine_name or not dosage or not frequency or not start_date or not end_date:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Validate dosage and frequency as positive integers
    if not validate_positive_input('1', dosage) or not validate_positive_input('1', frequency):
        messagebox.showerror("Error", "Dosage and frequency must be positive integers.")
        return

    # Insert the new medicine into the database
    try:
        query = "INSERT INTO medicines (medicine_name, dosage, frequency, start_date, end_date) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (medicine_name, dosage, frequency, start_date, end_date))
        cnx.commit()
        messagebox.showinfo("Success", "Medicine added successfully.")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"An error occurred: {error}")

# Create the main window
window = tk.Tk()
window.title("Medicine Tracker")

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

# Labels and entries for medicine information
labels = ["Medicine Name:", "Dosage (units):", "Frequency (times/day):", "Start Date (YYYY-MM-DD):", "End Date (YYYY-MM-DD):"]
for i, label_text in enumerate(labels):
    label = tk.Label(input_frame, text=label_text, bg="#f0f0f0", font=gothic_font)
    label.grid(row=i, column=0, padx=20, pady=20)

entries = []
for i in range(len(labels)):
    entry = tk.Entry(input_frame, bg="white", fg="black", font=gothic_font)  # Change text color to black
    entry.grid(row=i, column=1, padx=20, pady=20)
    entries.append(entry)

medicine_name_entry, dosage_entry, frequency_entry, start_date_entry, end_date_entry = entries

# Heading "Medicine Tracker"
heading_label = tk.Label(window, text="Medicine Tracker", bg="#f0f0f0", font=("Century Gothic", 24, "bold"))
heading_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Create a button to add a new medicine
add_button = tk.Button(window, text="Add Medicine", command=add_medicine, bg="green", font=gothic_font)
add_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Run the Tkinter event loop
window.mainloop()

# Close the database connection when the program exits
cursor.close()
cnx.close()
