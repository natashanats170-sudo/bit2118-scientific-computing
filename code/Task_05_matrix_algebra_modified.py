import numpy as np

# Rectangle path (x, y)
waypoints = np.array([[0, 0], [2, 0], [2, 1], [0, 1]], dtype=float)

angle = np.deg2rad(30)
tx, ty = 3.0, 2.0

# Homogeneous matrix: rotation by 30 degrees plus translation
H = np.array([
    [np.cos(angle), -np.sin(angle), tx],
    [np.sin(angle),  np.cos(angle), ty],
    [0, 0, 1]
])

homog = np.hstack([waypoints, np.ones((len(waypoints), 1))])
moved = homog @ H.T

print("Transformed waypoints:\n", moved[:, :2])