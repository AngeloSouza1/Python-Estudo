import tkinter as tk
from tkinter import ttk

def add_employee():
    name = entry_name.get()
    email = entry_email.get()
    
    # Add code here to store the employee data somewhere (e.g., database, file, list, etc.)
    # For now, we're just displaying the data in the table
    
    tree.insert("", tk.END, values=(name, email))
    
    # Clear the entry fields after adding an employee
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Main window configuration
root = tk.Tk()
root.title("Employee Registration")

# Create a table using the Treeview widget
tree = ttk.Treeview(root, columns=("Name", "Email"))
tree.heading("Name", text="Name")
tree.heading("Email", text="Email")
tree.pack()

# Create entry fields for name and position
label_name = tk.Label(root, text="Name:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

# Button to add an employee
button_add = tk.Button(root, text="Add", command=add_employee)
button_add.pack()

# Start the program's execution
root.mainloop()