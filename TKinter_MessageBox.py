import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x200")
root.title("Messagebox Demo")

label = tk.Label(root, text="Messagebox Demo", font=("Arial", 14))
label.pack(pady=20)

messagebox.showinfo("showinfo", "Information")
messagebox.showwarning("showwarning", "Warning")
messagebox.showerror("showerror", "Error")
messagebox.askquestion("askquestion", "Are you sure?")
messagebox.askokcancel("askokcancel", "Want to continue?")
messagebox.askyesno("askyesno", "Find the value?")
messagebox.askretrycancel("askretrycancel", "Try again?")

root.mainloop()
