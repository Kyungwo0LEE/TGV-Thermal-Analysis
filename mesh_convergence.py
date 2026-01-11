import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Mesh sweep data

h = np.array([
    1.0e-4, 9.0e-5, 8.0e-5, 7.0e-5, 6.0e-5,
    5.0e-5, 4.0e-5, 3.0e-5, 2.0e-5, 1.5e-5
])

Tmax = np.array([
    29.724, 29.743, 29.726, 29.757, 29.700,
    29.757, 29.761, 29.759, 29.762, 29.763
])

df = pd.DataFrame({
    "Mesh size (h)": h,
    "Max Temperature (degC)": Tmax
})

print(df)



relative_change = np.abs(np.diff(Tmax)) / Tmax[1:]

for i in range(len(relative_change)):
    print(f"h = {h[i]:.1e} → {h[i+1]:.1e}, "
          f"Relative change = {relative_change[i]*100:.3f} %")




import matplotlib.pyplot as plt

# Tmax vs mesh size
plt.figure()
plt.plot(h, Tmax, marker='o')
plt.gca().invert_xaxis()
plt.xlabel("Mesh size (h)")
plt.ylabel("Max temperature (degC)")
plt.title("Mesh Convergence Study")
plt.grid(True)
plt.savefig("mesh_convergence_Tmax.png",dpi=300,bbox_inches="tight")
plt.show()

# Relative change plot
plt.figure()
plt.plot(h[1:], relative_change * 100, marker='s')
plt.gca().invert_xaxis()
plt.xlabel("Mesh size (h)")
plt.ylabel("Relative change (%)")
plt.title("Relative Change Between Mesh Refinements")
plt.grid(True)
plt.savefig("mesh_convergence_reltative_change.png",dpi=300,bbox_inches="tight")
plt.show()
