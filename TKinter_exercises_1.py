'''
Design a Python GUI program that takes user input for
the length and width of a rectangle, and when a button
is pressed, calculates and displays the area of the rectangle.
'''
import tkinter as tk

def calculate_area():
    length = float(entry_length.get())
    width = float(entry_width.get())
    area = length * width
    result_label.config(text="Area of Rectangle = " + str(area))

# Create main window
window = tk.Tk()
window.title("Rectangle Area Calculator")
window.geometry("350x220")

# Labels
tk.Label(window, text="Length").grid(row=0, column=0, padx=20, pady=10)
tk.Label(window, text="Width").grid(row=1, column=0, padx=20, pady=10)

# Entry fields
entry_length = tk.Entry(window)
entry_length.grid(row=0, column=1)

entry_width = tk.Entry(window)
entry_width.grid(row=1, column=1)

# Button
tk.Button(window, text="Calculate Area", command=calculate_area).grid(row=2, column=1, pady=15)

# Result label
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=1)

# Run the application
window.mainloop()
