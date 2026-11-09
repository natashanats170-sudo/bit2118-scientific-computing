import os
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
N = 200_000

# Task durations in weeks: triangular(min, most likely, max)
design = rng.triangular(4, 6, 10, N)
build  = rng.triangular(3, 5, 9, N)
test   = rng.triangular(5, 8, 14, N)
total  = design + build + test

print(f"Mean duration: {total.mean():.2f} weeks")
print(f"P(more than 20 weeks): {(total > 20).mean():.1%}")
print(f"P(more than 18 weeks): {(total > 18).mean():.1%}")
print(f"P(more than 22 weeks): {(total > 22).mean():.1%}")
print(f"90th percentile: {np.percentile(total, 90):.1f} weeks")

plt.hist(total, bins=60)
plt.axvline(20, linestyle="--", label="20-week deadline")
plt.xlabel("Total duration (weeks)"); plt.ylabel("Number of runs")
plt.legend()
os.makedirs("images", exist_ok=True)
plt.savefig("images/Task_20_modified_histogram.png", dpi=150)
plt.show()