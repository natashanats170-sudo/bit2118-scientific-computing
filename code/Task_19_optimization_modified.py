import numpy as np
from scipy.optimize import minimize

# x = bags of fertilizer 1 (30 per bag, 10 kg N, 5 kg P)
# y = bags of fertilizer 2 (40 per bag,  5 kg N, 12.5 kg P)
# Field needs at least 12 kg N and 10 kg P
def cost(z):
    return 30*z[0] + 40*z[1]

constraints = [
    {"type": "ineq", "fun": lambda z: 10*z[0] + 5*z[1] - 12},
    {"type": "ineq", "fun": lambda z: 5*z[0] + 12.5*z[1] - 10}
]

sol = minimize(cost, x0=[2, 2], method="SLSQP",
               bounds=[(0, None), (0, None)], constraints=constraints)
print("Success:", sol.success)
print("Bags of F1, F2:", np.round(sol.x, 3), " cost:", round(sol.fun, 2))

# Whole bags only
best = None
for a in range(0, 10):
    for b in range(0, 10):
        if 10*a + 5*b >= 12 and 5*a + 12.5*b >= 10:
            c = 30*a + 40*b
            if best is None or c < best[0]:
                best = (c, a, b)
print("Best whole-bag option (cost, F1, F2):", best)