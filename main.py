import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit 

# Experimental data 
naoh_added = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 8.25, 8.5, 8.75, 9, 9.25, 9.5, 9.75, 10, 
                      10.25, 10.5, 10.75, 11, 11.25, 11.5, 11.75, 12, 12.25, 12.5, 12.75, 13, 14, 15]) 

ph_hcl = np.array([1.35, 1.37, 1.41, 1.47, 1.54, 1.63, 1.74, 1.86, 2, 2.12, 2.17, 2.22, 2.27, 
                  2.41, 2.54, 2.71, 2.82, 3.14, 5.05, 7.02, 8.61, 9.83, 10.05, 10.29, 10.48, 
                  10.64, 10.74, 10.83, 10.90, 11.07, 11.17]) #from 0-15 mL

naoh_added_full = np.array([0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 8.25, 8.50, 8.75, 9.00, 
    9.25, 9.50, 9.75, 10.00, 10.25, 10.50, 10.75, 11.00, 11.25, 11.50, 11.75, 12.00, 
    12.25, 12.50, 12.75, 13.00, 14.00, 15.00, 16.00, 17.00, 18.00, 19.00, 20.00, 
    21.00, 22.00, 23.00, 24.00, 25.00, 26.00, 27.00, 28.00, 29.00, 30.00, 31.00, 
    32.00, 33.00, 34.00, 35.00, 36.00, 37.00, 38.00, 39.00, 40.00, 41.00, 42.00, 
    43.00, 44.00, 45.00, 46.00, 47.00, 48.00, 49.00, 50.00])

ph_hcl_full = np.array([1.35, 1.37, 1.41, 1.47, 1.54, 1.63, 1.74, 1.86, 2.00, 2.12, 2.17, 2.22, 2.27, 
    2.41, 2.54, 2.71, 2.82, 3.14, 5.05, 7.02, 8.61, 9.83, 10.05, 10.29, 10.48, 10.64, 
    10.74, 10.83, 10.90, 11.07, 11.17, 11.23, 11.30, 11.32, 11.35, 11.37, 11.40, 
    11.41, 11.43, 11.44, 11.45, 11.47, 11.48, 11.49, 11.50, 11.51, 11.52, 11.53, 
    11.54, 11.55, 11.55, 11.56, 11.57, 11.58, 11.58, 11.59, 11.60, 11.61, 11.63, 
    11.64, 11.64, 11.64, 11.65, 11.65, 11.65, 11.66])

# Define sigmoid function 
def sigmoid(x, L, x0, k, b): 
   return L / (1 + np.exp(-k * (x - x0))) + b 

# Initial guesses for parameters 
L_initial = max(ph_hcl) - min(ph_hcl) 
print(L_initial)
x0_initial = 10.5  # approximate midpoint 
k_initial = 1 
b_initial = min(ph_hcl) 

p0 = [L_initial, x0_initial, k_initial, b_initial] #initial guess

# Fit the sigmoid curve 
params, _ = curve_fit(sigmoid, naoh_added, ph_hcl, p0=p0) 
params_full, _ = curve_fit(sigmoid, naoh_added_full, ph_hcl_full, p0=p0) #change to 0-15 data
print(params)
print(params_full)
# Generate fitted data 
naoh_fit = np.linspace(0, 15, 300) #change back to 15
ph_fit = sigmoid(naoh_fit, *params) #change back to *params

# Plot experimental and fitted data 
plt.figure(figsize=(8, 6)) 
plt.scatter(naoh_added, ph_hcl, color='blue', label='Données expérimentales', marker="x") #change to not full data
plt.plot(naoh_fit, ph_fit, color='red', label='Courbe sigmoïde approximative') 
plt.xlabel('NaOH ajouté (mL)') 
plt.ylabel('pH de la solution') 
plt.title('pH de la solution en fonction de la quantité de NaOH ajouté (mL) \navec la courbe sigmoïde approximative (0-15mL)') 
plt.legend() 
plt.grid(True) 
plt.show() 