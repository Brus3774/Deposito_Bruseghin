# Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.
 #  extra stampa in csv txt
import numpy as np

arr = np.arange(10, 50)
print (arr) 
print(arr.dtype) # stampa il tipo

arr = np.array(arr, dtype='float64') # cambio del tipo da int a float 
print(arr.dtype)
print(arr.shape) 

with open("risultato_array.csv", "w") as file: # stampa in file csv
    for numero in arr:
        # Scriviamo il numero seguito da una virgola (o punto e virgola)
        file.write(str(numero) + ",")  
