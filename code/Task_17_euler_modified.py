import os
import numpy as np
import matplotlib.pyplot as plt

k, C0, end = 0.173, 10.0, 24.0     # per hour, mg/L, hours

def euler(h):
    t = np.arange(0, end + h/2, h)
    C = np.zeros(len(t))
    C[0] = C0
    for i in range(len(t) - 1):
        C[i + 1] = C[i] - h * k * C[i]
    return t, C

exact_end = C0 * np.exp(-k * end)
for h in (1.0, 2.0, 4.0, 12.0):
    t, C = euler(h)
    print(f"h = {h:4.1f} h: C(24) = {C[-1]:.4f}  (exact {exact_end:.4f})")

t, C = euler(1.0)
plt.plot(t, C, marker="o", label="Euler h = 1")
plt.plot(t, C0*np.exp(-k*t), label="Exact")
plt.xlabel("Time (h)"); plt.ylabel("Concentration (mg/L)")
plt.legend(); plt.grid(True)
os.makedirs("images", exist_ok=True)
plt.savefig("images/Task_17_modified_drug.png", dpi=150)
plt.show()