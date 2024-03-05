import tkinter as tk
from tkcalendar import Calendar
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class DoctorAppointmentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Doctor Appointment Scheduler")
        self.geometry("600x400")

        self.label = tk.Label(self, text="Schedule an Appointment", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.patient_label = tk.Label(self, text="Patient Name:")
        self.patient_label.pack()

        self.patient_entry = tk.Entry(self)
        self.patient_entry.pack()

        self.date_label = tk.Label(self, text="Select Date:")
        self.date_label.pack()

        self.calendar = Calendar(self, selectmode='day', date_pattern='yyyy-mm-dd')
        self.calendar.pack()

        self.time_label = tk.Label(self, text="Select Time:")
        self.time_label.pack()

        self.time_combo = ttk.Combobox(self, values=["9:00 AM", "10:00 AM", "11:00 AM", "1:00 PM", "2:00 PM"])
        self.time_combo.pack()

        self.submit_button = tk.Button(self, text="Schedule Appointment", command=self.schedule_appointment)
        self.submit_button.pack(pady=10)

        # Call method to create database and table
        self.create_database_and_table()

    def create_database_and_table(self):
        try:
            # Connect to MySQL and create database and table if not exists
            cnx = mysql.connector.connect(user='root', password='your_password',
                                           host='localhost')
            cursor = cnx.cursor()

            cursor.execute('''CREATE DATABASE IF NOT EXISTS doctor_appointments''')
            cursor.execute('''USE doctor_appointments''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                    patient_name VARCHAR(255) NOT NULL,
                                    appointment_date DATE NOT NULL,
                                    appointment_time VARCHAR(20) NOT NULL
                                )''')
            cnx.commit()
        except mysql.connector.Error as error:
            print(f"Error creating database and table: {error}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'cnx' in locals():
                cnx.close()

    def schedule_appointment(self):
        patient_name = self.patient_entry.get()
        selected_date = self.calendar.get_date()
        selected_time = self.time_combo.get()

        # Here you can add logic to check for conflicts, save the appointment, etc.
        messagebox.showinfo("Appointment Scheduled", f"Appointment scheduled for {patient_name} on {selected_date} at {selected_time}")

if __name__ == "__main__":
    app = DoctorAppointmentApp()
    app.mainloop()
