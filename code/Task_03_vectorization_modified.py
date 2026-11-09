import numpy as np

rng = np.random.default_rng(1)
bandwidth_mbps = rng.uniform(10, 100, 1000)   # 1000 speed tests

mb_per_s = bandwidth_mbps / 8                 # 8 bits = 1 byte
rms = np.sqrt(np.mean(mb_per_s ** 2))

print("First three values (MB/s):", mb_per_s[:3])
print(f"RMS speed: {rms:.2f} MB/s")