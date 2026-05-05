# la matrice è una lista di liste, dove ogni lista interna rappresenta una riga della matrice

matrice = [[1, 2, 3],
           [4, 5, 6], 
           [7, 8, 9], 
           [10]] # matrice 4x3 (4 righe e 3 colonne) 
print(matrice[0][0])  # Stampa 1
print(matrice[1][2])  # Stampa 6

for riga in matrice:
    for elemento in riga:
        print(elemento, end=' ')  # Stampa l'elemento seguito da uno spazio invece di una nuova riga
    print()  # Stampa una nuova riga dopo ogni riga della matrice  