# esercizio 1 pag 219
import numpy as np

arr_sl = np.random.randint(10, 51, size=20)
print("Array originale:\n", arr_sl)

primi_10 = arr_sl[0:10] # primi 10 elementi array
ultimi_5 = arr_sl[-5:]  # ultimi 5 elementi array
da_5_a_15 = arr_sl[5:15] # elementi tra gli indici 5  e 15
ogni_terzo = arr_sl[::3] # step ogni 3 elementi array

print("\n2. Primi 10 elementi:", primi_10) # stampe sottoarray
print("3. Ultimi 5 elementi:", ultimi_5)
print("4. Dall'indice 5 al 15 (escluso):", da_5_a_15)
print("5. Ogni terzo elemento:", ogni_terzo)


arr_modificato = arr_sl.copy() # Facciamo una copia per sicurezza
arr_modificato[5:10] = 99 # modifica array tra indici 5 e 10
print("6. Modifica array tra indici 5 e 10:", arr_modificato)

print("\n")

# esercizio 2 pag 220

arr_mr = np.random.randint(1, 101, size = (6, 6)) # creazione matrice 6x6 usando randint
print("Array originale: \n", arr_mr)

sottomatrice_centrale = arr_mr[1:5, 1:5] # prendi dalle righe con indice 1 fino a 4 e dalle colonne con indice 1 fino a 4
inverti_righe = sottomatrice_centrale[::-1, :] # ::-1 inverte l'ordine della prima dimensione (le righe) - : mantiene tutte le colonne nell'ordine originale
estrai_diagonale = np.diag(inverti_righe) # prende una matrice e restituisce un array 1D con gli elementi che si trovano sulla diagonale

matrice_modificata = inverti_righe.copy() # copia di sicurezza
matrice_modificata[matrice_modificata % 3 == 0] = -1 # crea una maschera di valori Booleani (True/False).
# Dove è True (ovvero il resto della divisione per 3 è zero), NumPy assegna il valore -1. 

print("\n2. Sotto-matrice 4x4 centrale:\n", sottomatrice_centrale) # stampe 
print("\n3. Matrice con righe invertite:\n", inverti_righe)
print("\n4. Diagonale principale della invertita:", estrai_diagonale)
print("\n5. Matrice invertita con -1 al posto dei multipli di 3:\n", matrice_modificata) 


