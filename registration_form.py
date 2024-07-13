import tkinter as tk
from tkinter import messagebox

# Function to be called when the submit button is clicked
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    
    # Simple validation
    if not name or not email or not age:
        messagebox.showwarning("Validation Error", "All fields are required")
        return
    
    try:
        age = int(age)
    except ValueError:
        messagebox.showwarning("Validation Error", "Age must be a number")
        return
    
    # Process the data (for now just print it)
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    
    # Clear the fields after submission
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    
    messagebox.showinfo("Form Submitted", "Registration successful")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place the widgets
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Age").grid(row=2, column=0, padx=10, pady=10)

name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
age_entry = tk.Entry(root)

name_entry.grid(row=0, column=1, padx=10, pady=10)
email_entry.grid(row=1, column=1, padx=10, pady=10)
age_entry.grid(row=2, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
