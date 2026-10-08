import numpy as np

np.random.seed(42)
distances = np.random.uniform(1.0, 15.0, 25)
fees = 20 + 5 * distances
mask = fees > 60

print("\n=== DELIVERY FEE ANALYSIS ===")
for d, f in zip(distances[mask], fees[mask]):
    print(f"Distance: {d:6.2f} km | Fee: Rs {f:7.2f}")
print(f"\nMinimum: Rs {np.min(fees):.2f}")
print(f"Maximum: Rs {np.max(fees):.2f}")
print(f"Mean: Rs {np.mean(fees):.2f}")
print(f"Std deviation: Rs {np.std(fees):.2f}")
