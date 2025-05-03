import matplotlib.pyplot as plt
import numpy as np

# Voltage and current data (excluding (0,0) to avoid division by zero)
current = np.array([0.01, 0.02, 0.03, 0.04, 0.05])  # in amperes
voltage = np.array([0.45, 0.87, 1.24, 1.65, 2.07])  # in volts

# Calculate resistance and conductance
resistance = voltage / current
conductance = current / voltage

# Plot resistance and conductance
plt.figure(figsize=(8, 5))
plt.plot(current, resistance, label='Résistance (Ω)', marker='o', color='blue')
plt.plot(current, conductance, label='Conductance (S)', marker='x', color='green')

plt.xlabel("Intensité du courant (A)")
plt.ylabel("Valeur")
plt.title("Résistance et conductance en fonction du courant")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
