import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("The Simple To Do List In Python")
root.geometry("400x450")
root.resizable(False, False)

tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        listbox.delete(0, tk.END)
        tasks.clear()

# UI Elements
title_label = tk.Label(root, text="Simple To-Do List", font=("Arial", 30, "bold"))
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=20, font=("Arial", 12))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=30, height=9, font=("Arial", 12))
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Selected Task", width=20, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", width=20, command=clear_tasks)
clear_button.pack(pady=5)

# Run app
root.mainloop()
