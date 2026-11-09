from scipy.optimize import root_scalar

def profit(q):
    return 30*q - 0.01*q**2 - 2000     # margin 30, rising cost, fixed cost 2000

low  = root_scalar(profit, bracket=[0, 500],    method="bisect", xtol=1e-8)
high = root_scalar(profit, bracket=[500, 3500], method="bisect", xtol=1e-8)
print("First break-even:", round(low.root, 3), "units, steps:", low.iterations)
print("Second break-even:", round(high.root, 2), "units")

# Fixed-point form: q = (2000 + 0.01 q^2) / 30
q = 100.0
for step in range(1, 500):
    q_new = (2000 + 0.01*q*q) / 30
    if abs(q_new - q) < 1e-8:
        break
    q = q_new
print("Fixed-point answer:", round(q_new, 3), "after", step, "iterations")