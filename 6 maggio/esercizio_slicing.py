# esercizio 1 
# stampare su file txt e/o csv 

import numpy as np

arr = np.random.randint(10, 51, size=20) # creiamo l'array usando random e radint
print("1. Array originale:\n", arr)

primi_10 = arr[0:10] # primi 10 elementi array
ultimi_5 = arr[-5:]  # ultimi 5 elementi array
da_5_a_15 = arr[5:15] # elementi tra gli indici 5  e 15
ogni_terzo = arr[::3] # step ogni 3 elementi array

print("\n2. Primi 10 elementi:", primi_10) # stampe sottoarray
print("3. Ultimi 5 elementi:", ultimi_5)
print("4. Dall'indice 5 al 15 (escluso):", da_5_a_15)
print("5. Ogni terzo elemento:", ogni_terzo)


arr_modificato = arr.copy() # Facciamo una copia per sicurezza
arr_modificato[5:10] = 99 # modifica array tra indici 5 e 10

# SALVATAGGIO IN TXT 
with open("esercizio_slicing.txt", "w") as f:
    f.write(" ESERCIZIO NUMPY SLICING \n\n")
    f.write(f"Array Originale: {arr}\n")
    f.write(f"Primi 10 elementi: {primi_10}\n")
    f.write(f"Ultimi 5 elementi: {ultimi_5}\n")
    f.write(f"Indici 5-15: {da_5_a_15}\n")
    f.write(f"Ogni terzo elemento: {ogni_terzo}\n")
    f.write(f"Array Modificato (5-10 = 99): {arr_modificato}\n")

# SALVATAGGIO IN CSV

with open("esercizio_slicing.csv", "w") as f:
    f.write("Descrizione,Valori\n") # Intestazione
    f.write(f"Originale,\"{','.join(map(str, arr))}\"\n")
    f.write(f"Primi 10,\"{','.join(map(str, primi_10))}\"\n")
    f.write(f"Ultimi 5,\"{','.join(map(str, ultimi_5))}\"\n")
    f.write(f"Indici 5-15,\"{','.join(map(str, da_5_a_15))}\"\n")
    f.write(f"Ogni terzo,\"{','.join(map(str, ogni_terzo))}\"\n")
    f.write(f"Modificato,\"{','.join(map(str, arr_modificato))}\"\n")

print("Sistema: Report salvato in 'esercizio_slicing.txt' e 'esercizio_slicing.csv'.") 