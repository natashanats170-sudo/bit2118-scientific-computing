import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def sir(t, y, beta, gamma):
    S, I, R = y
    return [-beta*S*I, beta*S*I - gamma*I, gamma*I]

for beta in (0.4, 0.2):
    sol = solve_ivp(sir, (0, 100), [0.99, 0.01, 0.0], args=(beta, 0.1),
                    t_eval=np.linspace(0, 100, 1001), rtol=1e-8)
    I = sol.y[1]
    print(f"beta = {beta}: peak infected {I.max():.1%} on day {sol.t[I.argmax()]:.1f}, "
          f"final recovered {sol.y[2, -1]:.1%}")
    plt.plot(sol.t, I, label=f"Infected, beta = {beta}")

plt.xlabel("Day"); plt.ylabel("Fraction of population")
plt.title("SIR epidemic model")
plt.legend(); plt.grid(True)
os.makedirs("images", exist_ok=True)
plt.savefig("images/Task_18_modified_sir.png", dpi=150)
plt.show()