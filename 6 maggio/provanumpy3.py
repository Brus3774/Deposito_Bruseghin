# dtype, shape, arange, reshape

import numpy as np

#dtype
arr = np.array([1, 2, 3], dtype='int32') # crea un array con elementi 1, 2 e 3 e specifica il tipo di dati come int32
print(arr.dtype)  # Output: int32

# shape 
arr = np.array([[1, 2, 3], [4, 5, 6]]) # crea un array bidimensionale (2D) con elementi 1, 2, 3 na prima riga e 4, 5, 6 na seconda riga
print(arr.shape)  # Output: (2, 3) 

#arange 

arr = np.arange(10) # crea un array con valori da 0 a 9 (10 non incluso) utilizzando la funzione arange
print(arr)  # Output: [0 1 2 3 4 5 6 7 8 9]

#reshape 

arr = np.arange(6) # crea un array con valori da 0 a 5 (6 non incluso) utilizzando la funzione arange
reshaped_arr = arr.reshape((2, 3)) # ridimensiona l'array in una matrice 2x3
print(reshaped_arr)

# Output:  [[0 1 2] [3 4 5]] 