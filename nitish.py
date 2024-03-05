import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class FeedbackForm:
    def __init__(self, master):
        master.title('Feedback')
        master.resizable(False, False)
        master.configure(background='#e1d8b9')

        # Connect to the MySQL database
        self.cnx = mysql.connector.connect(user='root', password='group2',
                                            host='localhost', database='feedback_database')
        self.cursor = self.cnx.cursor()

        # Create the feedback table if it doesn't exist
        self.create_feedback_table()

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9', font=('Arial', 11))
        self.style.configure('header.TLabel', font=('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text="Thanks for Exploring!", style='header.TLabel').grid(row=0, column=1)
        ttk.Label(self.frame_header, text="We're glad you chose to explore!\nPlease tell us how it was!",
                  justify='center').grid(row=1, column=1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text='Name:').grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Email:').grid(row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Comments:').grid(row=2, column=0, padx=5, sticky='sw')

        self.entry_name = ttk.Entry(self.frame_content, width=24)
        self.entry_email = ttk.Entry(self.frame_content, width=24)
        self.text_comments = tk.Text(self.frame_content, width=50, height=10, font=('Arial', 10))

        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)

        ttk.Button(self.frame_content, text='Submit', command=self.submit).grid(row=4, column=0, padx=5, sticky='e')
        ttk.Button(self.frame_content, text='Clear', command=self.clear).grid(row=4, column=1, padx=5, sticky='w')

    def create_feedback_table(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS feedback (
                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                    name VARCHAR(255) NOT NULL,
                                    email VARCHAR(255) NOT NULL,
                                    comments TEXT NOT NULL
                                )''')
            self.cnx.commit()
        except mysql.connector.Error as error:
            print(f"Error creating feedback table: {error}")

    def submit(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        comments = self.text_comments.get(1.0, 'end').strip()

        if not name or not email or not comments:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            query = "INSERT INTO feedback (name, email, comments) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (name, email, comments))
            self.cnx.commit()
            messagebox.showinfo("Success", "Feedback submitted successfully.")
            self.clear()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"An error occurred: {error}")

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')

    def __del__(self):
        self.cursor.close()
        self.cnx.close()


def main():
    root = tk.Tk()
    feedback_form = FeedbackForm(root)
    root.mainloop()


if __name__ == "__main__":
    main()
