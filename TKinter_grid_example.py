import tkinter as tk

window = tk.Tk()
window.title("grid() Example")

tk.Label(window, text="Username").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(window).grid(row=0, column=1)

tk.Label(window, text="Password").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(window, show="*").grid(row=1, column=1)

tk.Button(window, text="Login").grid(row=2, column=1, pady=10)

window.mainloop()
