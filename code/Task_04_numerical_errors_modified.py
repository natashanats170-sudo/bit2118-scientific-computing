import numpy as np

# Add 0.1 one million times; the true total is 100000
total = 0.0
for _ in range(1_000_000):
    total += 0.1
print("Repeated addition:", total, " error:", abs(total - 100000))
print("np.sum:", np.sum(np.full(1_000_000, 0.1)))

# float32 loses even more accuracy
balance = np.float32(0.0)
for _ in range(100_000):
    balance += np.float32(0.01)
print("float32 total (true value 1000):", balance)