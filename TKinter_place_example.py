import tkinter as tk

top = tk.Tk()
top.geometry("400x250")
top.title("User Details")

tk.Label(top, text="Name").place(x=30, y=50)
tk.Label(top, text="Email").place(x=30, y=90)
tk.Label(top, text="Password").place(x=30, y=130)

tk.Entry(top).place(x=100, y=50)
tk.Entry(top).place(x=100, y=90)
tk.Entry(top, show="*").place(x=100, y=130)

top.mainloop()
