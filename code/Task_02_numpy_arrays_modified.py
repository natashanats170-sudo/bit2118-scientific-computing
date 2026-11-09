import numpy as np

# Assumed hourly greenhouse temperatures (deg C), invented data
temps = np.array([
    16.0, 15.5, 15.0, 14.8, 15.2, 17.0,
    19.5, 22.0, 24.5, 26.0, 27.5, 28.2,
    28.8, 28.5, 27.9, 26.5, 25.0, 23.0,
    21.0, 19.5, 18.5, 17.5, 16.8, 16.2
])

print(f"Mean: {temps.mean():.2f} C, Min: {temps.min():.2f} C, Max: {temps.max():.2f} C")
print("Hours above 25 C:", (temps > 25).sum())
print("Hottest hour (0-23):", np.argmax(temps))