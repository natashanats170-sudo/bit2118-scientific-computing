import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([
    [ 3., -1.,  0.,  0.],
    [-1.,  3., -1.,  0.],
    [ 0., -1.,  3., -1.],
    [ 0.,  0., -1.,  3.]
])

loads = [
    np.array([10., 0., 0., 5.]),
    np.array([20., 0., 0., 10.]),
    np.array([0., 15., 15., 0.])
]

lu, piv = lu_factor(A)          # factor once
for b in loads:
    x = lu_solve((lu, piv), b)
    print("Load", b, "-> displacement", np.round(x, 4))