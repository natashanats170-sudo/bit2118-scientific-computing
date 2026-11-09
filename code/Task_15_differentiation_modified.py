import numpy as np

time = np.arange(0, 6, dtype=float)
velocity = np.array([0, 3.2, 6.1, 9.5, 12.0, 14.1])   # m/s

# np.gradient uses central differences inside and one-sided at the ends
acceleration = np.gradient(velocity, time)

for t, a in zip(time, acceleration):
    print(f"t = {t:.0f} s, acceleration = {a:.2f} m/s^2")