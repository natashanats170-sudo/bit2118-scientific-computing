from scipy.optimize import root_scalar

cash_flows = [-50000] + [15000]*5

def npv(r):
    return sum(cf / (1 + r)**t for t, cf in enumerate(cash_flows))

def d_npv(r):
    return sum(-t * cf / (1 + r)**(t + 1) for t, cf in enumerate(cash_flows) if t > 0)

newton = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)
print(f"IRR (Newton): {newton.root:.4%}, iterations {newton.iterations}")
print(f"IRR (Secant): {secant.root:.4%}, iterations {secant.iterations}")