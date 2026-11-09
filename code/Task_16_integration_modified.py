import numpy as np
from scipy.integrate import simpson

time_s = np.array([0, 5, 10, 15, 20, 25, 30], dtype=float)
speed = np.array([0, 8, 14, 16, 15, 9, 0], dtype=float)   # m/s

print(f"Distance (trapezoid): {np.trapezoid(speed, time_s):.1f} m")
print(f"Distance (Simpson):   {simpson(speed, x=time_s):.1f} m")