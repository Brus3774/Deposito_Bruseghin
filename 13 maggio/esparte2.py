# parte 2

import numpy as np
from esparte1 import salva_su_file, crea_matrice

#  OPERAZIONI PARTE 2 

def moltiplicazione_element_wise(matrice1):
    # Questa funzione esegue la moltiplicazione di Hadamard (elemento per elemento)
    print("\nCreazione della seconda matrice per la moltiplicazione:")
    
    # Recuperiamo le dimensioni (righe, colonne) della matrice esistente per crearne una identica
    r, c = matrice1.shape
    
    # Generiamo una matrice B con le stesse dimensioni di A per permettere l'operazione
    matrice2 = np.random.randint(1, 11, size=(r, c)) 
    
    # In NumPy, l'operatore * moltiplica le celle corrispondenti (es. A[0,0] * B[0,0])
    risultato = matrice1 * matrice2
    
    # Salviamo sia la matrice generata casualmente sia il risultato finale del calcolo
    salva_su_file("Seconda Matrice Generata", matrice2)
    salva_su_file("Moltiplicazione Element-wise", risultato)
    
    print("Seconda Matrice:\n", matrice2)
    return risultato

def calcola_media(matrice):
    # Calcola il valore medio di tutti i numeri presenti nella matrice
    media = np.mean(matrice)
    
    # Registriamo il valore della media nel file log.txt
    salva_su_file("Media degli elementi", media)
    return media

def calcola_determinante(matrice):
    # Il determinante è un valore cruciale in algebra lineare, calcolabile solo per matrici quadrate
    r, c = matrice.shape
    
    # Verifichiamo la condizione di "quadratura" (righe uguali alle colonne)
    if r == c:
        # np.linalg è il sottomodulo di NumPy dedicato all'algebra lineare
        det = np.linalg.det(matrice)
        
        # Salviamo il risultato numerico ottenuto
        salva_su_file("Determinante", det)
        return det
    else:
        # Se la matrice è rettangolare, l'operazione non è definita matematicamente
        return "Errore: Il determinante richiede una matrice quadrata."  

# menu parte 2 
def menu_parte_2():
    # Inizializziamo la variabile che conterrà la nostra matrice di lavoro
    mat = None
    
    while True:
        # Mostriamo le nuove opzioni disponibili in questa versione del software
        print("\nMENU GESTIONE MATRICE (PARTE 2)") 
        print("1. Crea nuova matrice")
        print("2. Moltiplicazione Element-wise (con nuova matrice)")
        print("3. Calcola Media degli elementi")
        print("4. Calcola Determinante (solo matrici quadrate)")
        print("0. Esci")
        
        scelta = input("\nScegli un'opzione: ")
        
        if scelta == "1":
            # Richiamiamo la funzione di creazione definita nella Parte 1
            mat = crea_matrice()
            print(mat)
            
        elif scelta == "2":
            # Controllo di sicurezza: verifichiamo che la matrice principale esista
            if mat is not None:
                res = moltiplicazione_element_wise(mat)
                print("Risultato Moltiplicazione:\n", res)
            else:
                print("Errore: Devi prima generare la Matrice 1!")
                
        elif scelta == "3":
            if mat is not None:
                res = calcola_media(mat)
                # Formattiamo l'output a video con 2 decimali per pulizia visiva
                print(f"Media degli elementi: {res:.2f}")
            else:
                print(" Nessuna matrice disponibile!")
                
        elif scelta == "4":
            if mat is not None:
                res = calcola_determinante(mat)
                print(f"Risultato Determinante: {res}")
            else:
                print(" Nessuna matrice disponibile!")
                
        elif scelta == "0":
            # Interrompiamo il ciclo per chiudere l'applicazione
            print("Uscita dalla Parte 2...")
            break

# Questo blocco assicura che il menu parta solo se il file viene eseguito direttamente
if __name__ == "__main__":
    menu_parte_2() 