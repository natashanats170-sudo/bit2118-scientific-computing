import os
import numpy as np
import matplotlib.pyplot as plt

n = 7
A = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
b = np.zeros(n)
b[0], b[-1] = 80.0, 30.0        # end temperatures

def jacobi(A, b, tol=1e-8, max_iter=5000):
    D = np.diag(A); R = A - np.diagflat(D)
    x = np.zeros_like(b); errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        err = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(err)
        if err < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=5000):
    x = np.zeros_like(b); errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        err = np.linalg.norm(x - old, ord=np.inf)
        errors.append(err)
        if err < tol:
            return x, errors
    return x, errors

xj, ej = jacobi(A, b)
xg, eg = gauss_seidel(A, b)
print("Gauss-Seidel temperatures:", np.round(xg, 2))
print("Direct solution:         ", np.round(np.linalg.solve(A, b), 2))
print("Iterations: Jacobi =", len(ej), " Gauss-Seidel =", len(eg))

plt.semilogy(ej, label="Jacobi")
plt.semilogy(eg, label="Gauss-Seidel")
plt.xlabel("Iteration"); plt.ylabel("Maximum change")
plt.title("Convergence for a 7-point rod")
plt.legend(); plt.grid(True)
os.makedirs("images", exist_ok=True)
plt.savefig("images/Task_08_modified_convergence.png", dpi=150)
plt.show()