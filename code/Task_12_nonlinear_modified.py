from scipy.optimize import root

# Tower 1 at (0,0) range 5 km; tower 2 at (6,0) range 4 km
def towers(z):
    x, y = z
    return [x**2 + y**2 - 25,
            (x - 6)**2 + y**2 - 16]

for guess in ([3.0, 3.0], [3.0, -3.0]):
    sol = root(towers, guess)
    print("Guess:", guess, "-> point:", sol.x, "residuals:", towers(sol.x), "converged:", sol.success)