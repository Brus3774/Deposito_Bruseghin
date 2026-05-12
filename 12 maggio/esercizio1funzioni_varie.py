# es 1 p.226

import numpy as np

# 1. Array di 12 numeri equidistanti tra 0 e 1
# Parametri: inizio=0, fine=1, quanti numeri=12
arr_lin = np.linspace(0, 1, 12)

# 2. Cambia forma a 3x4
matrice_A = arr_lin.reshape(3, 4)

# 3. Matrice 3x4 di numeri casuali tra 0 e 1
# np.random.rand crea direttamente una matrice della forma passata con valori [0, 1)
matrice_B = np.random.rand(3, 4)

# 4. Calcolo delle somme
somma_A = np.sum(matrice_A) # o matrice_A.sum()
somma_B = np.sum(matrice_B)

# Stampe
print("Matrice Linspace (3x4):\n", matrice_A)
print("\nMatrice Casuale (3x4):\n", matrice_B)
print(f"\nSomma elementi Matrice A: {somma_A:.2f}")
print(f"Somma elementi Matrice B: {somma_B:.2f}")
