# Recap Numpy

import numpy as np
arr = np.array([1, 2, 3, 4, 5]) # array monodimennsionale


arr2d = np.array([[1, 2, 3], [4, 5, 6]]) # array bidimensionali

print(arr)
print(arr2d)

# recap 2

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Utilizzo di alcuni metodi

print("Forma dell'array:", arr.shape)  # Output: (5,)

print("Dimensioni dell'array:", arr.ndim)  # Output: 1

print("Tipo di dati:", arr.dtype)  # Output: int64 (varia a seconda della piattaforma)

print("Numero di elementi:", arr.size)  # Output: 5

print("Somma degli elementi:", arr.sum())  # Output: 15

print("Media degli elementi:", arr.mean())  # Output: 3.0

print("Valore massimo:", arr.max())  # Output: 5

print("Indice del valore massimo:", arr.argmax())  # Output: 4

# slicing e indexing

print("\n")

arr_2d = np.array([[1, 2, 3, 4],

                   [5, 6, 7, 8],

                   [9, 10, 11, 12]])

# Slicing sulle righe

print(arr_2d[1:3])  # Output: [[ 5  6  7  8]

                   #          [ 9 10 11 12]]

# Slicing sulle colonne

print(arr_2d[:, 1:3])  # Output: [[ 2  3]

                       #          [ 6  7]

                       #          [10 11]]

# Slicing misto

print(arr_2d[1:3, 1:3])  # Output: [[ 6  7]

                        #          [10 11]]
                        
print("\n")
                        
arr4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])                        
                        
# Slicing con passo

print(arr4[1:8:2])  # Output: [1 3 5 7]

# Omettere start e stop

print(arr4[:5])  # Output: [0 1 2 3 4]

print(arr4[5:])  # Output: [5 6 7 8 9]

# Utilizzare indici negativi

print(arr4[-5:])  # Output: [5 6 7 8 9]

print(arr4[:-5])  # Output: [0 1 2 3 4]

# fancy indexing

print("\n")

arrFI = np.array([10, 20, 30, 40, 50])

# Utilizzo di un array di indici

indices = np.array([1, 3])

print(arrFI[indices])  # Output: [20 40]

# Utilizzo di una lista di indici

indices = [0, 2, 4]

print(arrFI[indices])  # Output: [10 30 50]