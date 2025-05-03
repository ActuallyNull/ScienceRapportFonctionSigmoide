import matplotlib.pyplot as plt
import numpy as np

"""
current_rayan = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05]
voltage_rayan = [0.00, 0.45, 0.87, 1.24, 1.65, 2.07]
current_radu = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05]
voltage_radu = [0.00, 0.028, 0.50, 0.74, 0.93, 1.01]
"""

current_rayan = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25]
voltage_rayan = [0.00, 1.06, 2.16, 3.12, 4.05, 5.19]
current_radu = [0.00, 0.10, 0.20, 0.30, 0.40]
voltage_radu = [0.00, 1.12, 2.11, 3.08, 4.05]

# Find the closest and farthest points for Rayan's data
closest_rayan = (current_rayan[0], voltage_rayan[0])
farthest_rayan = (current_rayan[-1], voltage_rayan[-1])

# Find the closest and farthest points for Radu's data
closest_radu = (current_radu[0], voltage_radu[0])
farthest_radu = (current_radu[-1], voltage_radu[-1])

# Plot the scatter plots
plt.scatter(current_rayan, voltage_rayan, color='blue', label="Données de résistor #2")
plt.scatter(current_radu, voltage_radu, color='red', label="Données de résistor #1")

# Draw lines between the closest and farthest points for Rayan's data
plt.plot(
    [closest_rayan[0], farthest_rayan[0]],
    [closest_rayan[1], farthest_rayan[1]],
    color='cyan',
    label="Droite ajustée selon pour résistor #2"
)

# Draw lines between the closest and farthest points for Radu's data
plt.plot(
    [closest_radu[0], farthest_radu[0]],
    [closest_radu[1], farthest_radu[1]],
    color='orange',
    label="Droite ajustée selon pour résistor #1"
)

# Add coordinate labels for Rayan's data points (skip (0,0))
for x, y in zip(current_rayan, voltage_rayan):
    if x == 0 and y == 0:
        continue
    dx = 0.001 if x == 0 else 0
    dy = 0.05 if y == 0 else 0
    plt.text(x + dx, y + dy, f"({x:.2f}A; {y:.2f}V)", fontsize=8, color='darkblue', ha='center')

# Add coordinate labels for Radu's data points (skip (0,0))
for x, y in zip(current_radu, voltage_radu):
    if x == 0 and y == 0:
        continue
    dx = -0.001 if x == 0 else 0
    dy = 0.05 if y == 0 else 0
    plt.text(x + dx, y + dy, f"({x:.2f}A; {y:.2f}V)", fontsize=8, color='darkred', ha='center')

# Calculate dynamic axis limits
max_current = max(max(current_rayan), max(current_radu))
max_voltage = max(max(voltage_rayan), max(voltage_radu))

# Set axis limits with a small margin above the max, but 0 as the lower limit
plt.xlim(0, max_current + 0.005)
plt.ylim(0, max_voltage + 0.1)

# Add labels, legend, and title
plt.xlabel('Intensité du courant de la source (I) en ampères')
plt.ylabel('Tension du résistor (U) en volts')
plt.title(
    "La tension du résistor (U, V) en fonction de l'intensité du courant de la source (I, A)",
    fontsize=10
)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.savefig("betterone.png")
plt.show()