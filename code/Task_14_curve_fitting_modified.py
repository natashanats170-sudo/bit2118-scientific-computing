import os
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

hours = np.array([0, 1, 2, 3, 4, 5, 6, 8], dtype=float)
battery = np.array([100, 91, 83, 76, 69, 63, 58, 48], dtype=float)

def decay(t, a, k):
    return a * np.exp(-k * t)

(a, k), _ = curve_fit(decay, hours, battery, p0=[100, 0.1])
rmse = np.sqrt(np.mean((battery - decay(hours, a, k))**2))

print(f"a = {a:.2f}, k = {k:.4f} per hour, RMSE = {rmse:.2f} %")
print(f"Battery at 12 h: {decay(12, a, k):.1f} %")
print(f"Half-life: {np.log(2)/k:.2f} h")
print(f"Time to reach 20%: {np.log(20/a)/(-k):.1f} h")

t = np.linspace(0, 20, 200)
plt.scatter(hours, battery, label="Measured")
plt.plot(t, decay(t, a, k), label="Fitted")
plt.xlabel("Hours"); plt.ylabel("Battery (%)")
plt.legend(); plt.grid(True)
os.makedirs("images", exist_ok=True)
plt.savefig("images/Task_14_modified_battery.png", dpi=150)
plt.show()