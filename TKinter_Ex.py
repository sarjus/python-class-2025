# Import tkinter module
import tkinter as tk
from tkinter import messagebox


# Function to calculate area
def calculate_area():
    # Get values from entry boxes
    length = float(entry_length.get())
    width = float(entry_width.get())

    # Calculate area
    area = length * width
    # Display result
    label_result.config(text=f"Area of Rectangle: {area}")


# Create main window
rectangle = tk.Tk()
rectangle.title("Rectangle Area Calculator")
rectangle.geometry("350x200")

# Length Label and Entry
tk.Label(rectangle, text="Enter Length:").grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(rectangle)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Width Label and Entry
tk.Label(rectangle, text="Enter Width:").grid(row=1, column=0, padx=10, pady=10)
entry_width = tk.Entry(rectangle)
entry_width.grid(row=1, column=1, padx=10, pady=10)

# Calculate Button
tk.Button(rectangle, text="Calculate Area", command=calculate_area).grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
label_result = tk.Label(rectangle, text="Area of Rectangle: ")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
rectangle.mainloop()
