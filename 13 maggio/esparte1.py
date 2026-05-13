# es pa240-241 parte 1 

import numpy as np
import os

#  FUNZIONI 

def salva_su_file(messaggio, dato):
    
    # Assicura che ogni operazione conclusa venga registrata.
    
    nome_file = "log_matrice.txt"
    with open(nome_file, "a") as f:
        f.write(f"--- OPERAZIONE CONCLUSA: {messaggio} ---\n")
        # Se il dato è un numero (come la somma), lo scriviamo direttamente
        # Se è una matrice, NumPy lo formatterà automaticamente come griglia
        f.write(f"Risultato ottenuto:\n{dato}\n")
        f.write("-" * 40 + "\n")
    # Messaggio di feedback per l'utente 
    print(f" Risultato registrato in {nome_file}")

def crea_matrice():
    
    # Permette la creazione dinamica della matrice.
    # Chiediamo righe (r) e colonne (c) all'utente.
    
    try:
        r = int(input("Inserisci numero righe: "))
        c = int(input("Inserisci numero colonne: "))
        # Generiamo numeri casuali (interi) tra 1 e 50. 
        # La forma (shape) è definita dalla tupla (r, c).
        matrice = np.random.randint(1, 51, size=(r, c))
        print("\nMatrice creata con successo!")
        
        # Salviamo l'azione di creazione sul file log
        salva_su_file("Creazione Matrice", matrice)
        return matrice
    except ValueError:
        print("Errore: Inserisci numeri interi validi per le dimensioni!")
        return None

# OPERAZIONI PARTE 1 

def estrai_centrale(matrice):
    
    # Usa lo SLICING per estrarre il cuore della matrice.
    # 1:-1 significa: parti dall'indice 1 (seconda riga/colonna) 
    # fino all'ultimo escluso (quindi scarta l'ultima riga/colonna).
    # Controllo di sicurezza: se la matrice è 2x2 o minore, il "centro" non esiste
    if matrice.shape[0] < 3 or matrice.shape[1] < 3:
        messaggio = "Matrice troppo piccola per estrarre il centro (minimo 3x3)"
        return messaggio
    
    centrale = matrice[1:-1, 1:-1]
    salva_su_file("Estrazione Centrale", centrale)
    return centrale

def trasponi_matrice(matrice):
    
    # La TRASPOSIZIONE inverte le righe con le colonne.
    # In NumPy si può ottenere con l'attributo .T
    
    trasposta = matrice.T
    salva_su_file("Trasposizione", trasposta)
    return trasposta

def calcola_somma(matrice):
    
    #np.sum() calcola la somma algebrica di tutti gli elementi 
    #presenti nella matrice, restituendo un singolo valore scalare.
    
    totale = np.sum(matrice)
    salva_su_file("Somma Totale", totale)
    return totale

# MENU 

def menu():
    # Inizializziamo la variabile 'mat' a None. 
    # Finché l'utente non sceglie l'opzione 1, non avremo dati su cui lavorare.
    mat = None
    
    while True:
        print("\n MENU GESTIONE MATRICE (PARTE 1) ")
        print("1. Crea nuova matrice casuale")
        print("2. Estrai e stampa sotto-matrice centrale")
        print("3. Trasponi e stampa matrice")
        print("4. Calcola e stampa somma totale")
        print("0. Esci")
        
        scelta = input("\nScegli un'opzione: ")
        
        # Gestione delle scelte
        if scelta == "1":
            mat = crea_matrice()
            if mat is not None:
                print(mat)
                
        elif scelta == "2":
            # Verifichiamo sempre che 'mat' esista prima di operare
            if mat is not None:
                ris = estrai_centrale(mat)
                print("Risultato:\n", ris)
            else:
                print(" Errore: Devi prima creare una matrice (Opzione 1)!")
                
        elif scelta == "3":
            if mat is not None:
                ris = trasponi_matrice(mat)
                print("Matrice Trasposta:\n", ris)
            else:
                print("Errore: Nessuna matrice disponibile!")
                
        elif scelta == "4":
            if mat is not None:
                ris = calcola_somma(mat)
                print(f"Somma totale di tutti gli elementi: {ris}")
            else:
                print("Errore: Nessuna matrice disponibile!")
                
        elif scelta == "0":
            print("Uscita in corso... File di log aggiornato.")
            break
            
        else:
            print("Opzione non valida, riprova.")

# Punto di avvio del programma
if __name__ == "__main__":
    menu() 
    
    
