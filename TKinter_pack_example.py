import tkinter as tk

window = tk.Tk()
window.title("pack() Example")
redbutton = tk.Button(window, text="Red", fg="red")
redbutton.pack(side=tk.LEFT)

greenbutton = tk.Button(window, text="Green", fg="green")
greenbutton.pack(side=tk.RIGHT)

bluebutton = tk.Button(window, text="Blue", fg="blue")
bluebutton.pack(side=tk.TOP)

blackbutton = tk.Button(window, text="Black", fg="black")
blackbutton.pack(side=tk.BOTTOM)

window.mainloop()
