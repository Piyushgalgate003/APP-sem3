import numpy as np

arr = np.arange(1, 11)
print(f"Original Array: {arr}")

slice_arr = arr[2:7]
print(f"Sliced Array: {slice_arr}")

print(f"Sum: {arr.sum()}")
print(f"Mean: {arr.mean()}")
print(f"Max: {arr.max()}")
print(f"Min: {arr.min()}")

broadcast_arr = arr * 10
print(f"Broadcasting (multiply by 10): {broadcast_arr}")