import pandas as pd
import numpy as np

np.random.seed(42) 
s = pd.Series(np.random.rand(10))
print("Original Series:")
print(s)

print(f"\nIndexing (element at index 3): {s[3]:.4f}")

filtered_s = s[s > 0.5]
print("\nFiltering (values > 0.5):")
print(filtered_s)

print(f"\nMean: {s.mean():.4f}")
print(f"Median: {s.median():.4f}")
print(f"Min: {s.min():.4f}")
print(f"Max: {s.max():.4f}")