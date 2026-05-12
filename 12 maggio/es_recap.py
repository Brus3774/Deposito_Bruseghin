# es recap

import numpy as np

arr = np.arange(10, 50) # creazione con arange di un array
print(arr)

print(arr.dtype) # verifica dato array

arr = arr.astype('float64') #cambio del tipo di dato dell'array
print(arr.dtype)

print(arr.shape) # verifica forma array