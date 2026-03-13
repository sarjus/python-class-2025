'''
Generates values from 0 to 2𝜋
Plots sin(x) with a solid line.
Plots cos(x) with a dashed line.
Adds axis labels, custom ticks, legend, title, and grid for clarity.
'''
import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2π
x = np.linspace(0, 2*np.pi, 100)

# Define the functions
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure()

# Plot sin(x) with a solid line
plt.plot(x, y_sin, linestyle='-', label='y = sin(x)')

# Plot cos(x) with a dashed line
plt.plot(x, y_cos, linestyle='--', label='y = cos(x)')

# Customize ticks
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           ['0', 'π/2', 'π', '3π/2', '2π'])

# Labels for axes
plt.xlabel('x')
plt.ylabel('y')

# Title
plt.title('Plot of sin(x) and cos(x) from 0 to 2π')

# Legend
plt.legend()

# Grid (optional but improves readability)
plt.grid(True)

# Display the plot
plt.show()