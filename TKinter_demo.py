import tkinter as tk

from TKinter_exercises_1 import entry_length, entry_width

window = tk.Tk()
window.title("Demo")
window.geometry("500x500")

tk.Label(window, text="Length").grid(column=0, row=0,pady=10)
tk.Label(window, text="Width").grid(column=1, row=0,pady=10)

entry_length = tk.Entry(window).grid(row=0, col=1)
entry_width = tk.Entry(window).grid(row=1, col=1)
