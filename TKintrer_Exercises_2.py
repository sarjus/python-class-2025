'''
Python GUI program using Tkinter that takes the birth date
from the user and displays the age when a button is pressed.
'''
import tkinter as tk
from datetime import date

def calculate_age():
    day = int(entry_day.get())
    month = int(entry_month.get())
    year = int(entry_year.get())

    today = date.today()
    age = today.year - year

    if (today.month, today.day) < (month, day):
        age -= 1

    result_label.config(text="Age = " + str(age) + " years")

# Create main window
window = tk.Tk()
window.title("Age Calculator")
window.geometry("350x250")

# Labels
tk.Label(window, text="Day").grid(row=0, column=0, padx=20, pady=10)
tk.Label(window, text="Month").grid(row=1, column=0, padx=20, pady=10)
tk.Label(window, text="Year").grid(row=2, column=0, padx=20, pady=10)

# Entry fields
entry_day = tk.Entry(window)
entry_day.grid(row=0, column=1)

entry_month = tk.Entry(window)
entry_month.grid(row=1, column=1)

entry_year = tk.Entry(window)
entry_year.grid(row=2, column=1)

# Button
tk.Button(window, text="Calculate Age", command=calculate_age)\
    .grid(row=3, column=1, pady=15)

# Result label
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=1)

# Run the application
window.mainloop()
