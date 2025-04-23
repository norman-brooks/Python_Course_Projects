import sqlite3
import tkinter as tk
from tkinter import messagebox

# Set up the database
def create_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT,
                        last_name TEXT,
                        phone_number TEXT,
                        email TEXT,
                        current_course TEXT)''')
    conn.commit()
    conn.close()

def insert_student(first_name, last_name, phone_number, email, current_course):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO students (first_name, last_name, phone_number, email, current_course)
                      VALUES (?, ?, ?, ?, ?)''', (first_name, last_name, phone_number, email, current_course))
    conn.commit()
    conn.close()

def fetch_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

# Set up the main window
def submit_student():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    phone_number = entry_phone_number.get()
    email = entry_email.get()
    current_course = entry_current_course.get()

    if not first_name or not last_name or not phone_number or not email or not current_course:
        messagebox.showwarning("Input Error", "All fields must be filled out.")
        return
    
    insert_student(first_name, last_name, phone_number, email, current_course)
    refresh_student_list()

    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_phone_number.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_current_course.delete(0, tk.END)

def refresh_student_list():
    for widget in frame_list.winfo_children():
        widget.destroy()

    students = fetch_students()

    for student in students:
        student_str = f"{student[1]} {student[2]} | {student[3]} | {student[4]} | {student[5]}"
        label = tk.Label(frame_list, text=student_str, anchor="w")
        label.grid(sticky="w")
        
        delete_button = tk.Button(frame_list, text="Delete", command=lambda student_id=student[0]: delete_student_and_refresh(student_id))
        delete_button.grid(row=frame_list.grid_size()[1]-1, column=1)

def delete_student_and_refresh(student_id):
    delete_student(student_id)
    refresh_student_list()

# Set up the GUI layout
root = tk.Tk()
root.title("Student Tracking")

# Title Label
label_title = tk.Label(root, text="Student Tracking", font=("Arial", 16))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# Form to input student data
label_first_name = tk.Label(root, text="First Name:")
label_first_name.grid(row=1, column=0, sticky="e", padx=5)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=1, column=1)

label_last_name = tk.Label(root, text="Last Name:")
label_last_name.grid(row=2, column=0, sticky="e", padx=5)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=2, column=1)

label_phone_number = tk.Label(root, text="Phone Number:")
label_phone_number.grid(row=3, column=0, sticky="e", padx=5)
entry_phone_number = tk.Entry(root)
entry_phone_number.grid(row=3, column=1)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=4, column=0, sticky="e", padx=5)
entry_email = tk.Entry(root)
entry_email.grid(row=4, column=1)

label_current_course = tk.Label(root, text="Current Course:")
label_current_course.grid(row=5, column=0, sticky="e", padx=5)
entry_current_course = tk.Entry(root)
entry_current_course.grid(row=5, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_student)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Section to display list of students
frame_list = tk.Frame(root)
frame_list.grid(row=7, column=0, columnspan=2, pady=10)

# Create database and initialize the list
create_db()
refresh_student_list()

root.mainloop()
