import numpy as np

R1, R2, R3 = 10.0, 20.0, 30.0
V1, V2 = 12.0, 6.0

# Mesh current equations
A = np.array([
    [R1 + R2, -R2],
    [-R2, R2 + R3]
])
b = np.array([V1, -V2])

i = np.linalg.solve(A, b)
print("I1 =", round(i[0], 4), "A, I2 =", round(i[1], 4), "A")
print("Residual norm:", np.linalg.norm(b - A @ i))

# Change: V2 = 12 V
i2 = np.linalg.solve(A, np.array([V1, -12.0]))
print("With V2 = 12 V:", i2)