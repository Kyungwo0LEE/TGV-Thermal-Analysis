import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd


# 1. Data
h = np.array([
    1.00e-4, 9.50e-5, 9.00e-5, 8.50e-5, 8.00e-5,
    7.50e-5, 7.00e-5, 6.50e-5, 6.00e-5, 5.50e-5,
    5.00e-5, 4.50e-5, 4.00e-5, 3.50e-5, 3.00e-5,
    2.50e-5, 2.00e-5, 1.50e-5
])

Tmax = np.array([
    29.724, 29.741, 29.743, 29.741, 29.726,
    29.743, 29.757, 29.750, 29.700, 29.757,
    29.757, 29.759, 29.761, 29.761, 29.759,
    29.762, 29.762, 29.763
])



# 2. Normalize h 
h_norm = h / h.max()

def model(hn, Tinf, A, B):
    return Tinf - A * np.exp(-B * hn)

initial_guess = [29.763, 0.05, 5.0]

params, _ = curve_fit(
    model, h_norm, Tmax,
    p0=initial_guess,
    maxfev=10000
)

Tinf, A, B = params



# 3. Smooth curve
h_fit = np.linspace(h.min(), h.max(), 500)
h_fit_norm = h_fit / h.max()
T_fit = model(h_fit_norm, Tinf, A, B)


# Reference converged temperature
Tinf_ref = 29.763


# 4. Plot
plt.figure(figsize=(7.2, 5.2))
plt.scatter(h, Tmax, color='black', s=40, label='Data', zorder=3)
plt.plot(h_fit, T_fit, color='red', linewidth=2.5, label='Regression function')

plt.axhline(
    Tinf_ref,
    color='red',
    linestyle='--',
    linewidth=1.8,
    label=r'$T_\infty = 29.763^\circ C$'
)

plt.xscale('log')
plt.xlabel('element size (m)', fontsize=12)
plt.ylabel('Maximum temperature of model (°C)', fontsize=12)
plt.title('Nonlinear regression', fontsize=13)

plt.grid(True, which='both', linestyle='--', alpha=0.4)
plt.legend(frameon=True, fontsize=10)
plt.tight_layout()



# 5. Figure
plt.savefig(
    "mesh_convergence.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# 6. Save data to CSV

# (1) Data + fitted curve
df_data = pd.DataFrame({
    "element_size_m": h,
    "Tmax_data_C": Tmax,
    "Tmax_fitted_C": model(h_norm, Tinf, A, B)
})

df_data.to_csv(
    "mesh_convergence_data.csv",
    index=False
)

# (2) Regression parameters
df_params = pd.DataFrame({
    "parameter": ["Tinf_fitted", "A", "B", "Tinf_reference"],
    "value": [Tinf, A, B, Tinf_ref]
})

df_params.to_csv(
    "mesh_convergence_params.csv",
    index=False
)

print("Files saved:")
print("- mesh_convergence.png")
print("- mesh_convergence_data.csv")
print("- mesh_convergence_params.csv")
