import numpy as np

# Nodes A..E; links A-B, A-C, B-C, C-D, D-E
A = np.array([
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0]
], dtype=float)

values, vectors = np.linalg.eig(A)
i = np.argmax(values.real)
v = np.abs(vectors[:, i].real)
scores = v / v.sum()

print("Dominant eigenvalue:", round(values[i].real, 4))
for name, s in zip("ABCDE", scores):
    print(name, round(s, 4))