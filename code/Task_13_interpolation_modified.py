import os
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

hours = np.array([0, 3, 6, 9, 12, 15, 18], dtype=float)
rain_mm = np.array([0, 2.0, 5.5, 9.0, 10.5, 11.0, 11.2])   # cumulative rainfall

linear = interp1d(hours, rain_mm)
cubic = CubicSpline(hours, rain_mm)

print("Rain by hour 10 - linear:", round(float(linear(10)), 2), "mm, cubic:", round(float(cubic(10)), 2), "mm")

t = np.linspace(0, 18, 200)
plt.scatter(hours, rain_mm, label="Gauge readings")
plt.plot(t, linear(t), label="Linear")
plt.plot(t, cubic(t), label="Cubic spline")
plt.xlabel("Hour"); plt.ylabel("Cumulative rain (mm)")
plt.legend(); plt.grid(True)
os.makedirs("images", exist_ok=True)
plt.savefig("images/Task_13_modified_rainfall.png", dpi=150)
plt.show()