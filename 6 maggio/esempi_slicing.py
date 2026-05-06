# esempi slicing

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing di base

print(arr[2:7])  # Output: [2 3 4 5 6]

# Slicing con passo

print(arr[1:8:2])  # Output: [1 3 5 7]

# Omettere start e stop

print(arr[:5])  # Output: [0 1 2 3 4]

print(arr[5:])  # Output: [5 6 7 8 9]

# Utilizzare indici negativi

print(arr[-5:])  # Output: [5 6 7 8 9]

print(arr[:-5])  # Output: [0 1 2 3 4]