# parte 3 

import numpy as np
# Importiamo le utilità e le funzioni della parte 2
from esparte1 import salva_su_file, crea_matrice
from esparte2 import calcola_determinante

# OPERAZIONI PARTE 3 

def calcola_inversa(matrice):
    # L'inversa è calcolabile solo se la matrice è quadrata e il suo determinante non è zero
    # Richiamiamo la funzione determinante definita nella Parte 2
    det = calcola_determinante(matrice)
    
    # Se det è una stringa, significa che la funzione ha restituito un messaggio di errore (es. non quadrata)
    if isinstance(det, str):
        return det
        
    # np.isclose è fondamentale: i calcoli decimali (float) possono non essere esattamente 0 
    # a causa dell'approssimazione binaria. Controlliamo se il valore è "quasi zero".
    elif np.isclose(det, 0):
        return "Errore: Matrice singolare (non invertibile) poiché il determinante è 0."
    else:
        # np.linalg.inv esegue l'operazione di inversione della matrice
        inversa = np.linalg.inv(matrice)
        # Registriamo il risultato nel file log.txt
        salva_su_file("Matrice Inversa", inversa)
        return inversa

def applica_funzione_matematica(matrice):
    # NumPy permette di applicare funzioni matematiche a ogni singolo elemento (Vettorizzazione)
    print("\nScegli funzione: 1. Seno, 2. Coseno, 3. Esponenziale")
    scelta_f = input("Scelta: ")
    
    # Inizializziamo variabili per il risultato e il nome dell'operazione
    if scelta_f == "1":
        # Applica il seno (in radianti) a ogni cella
        ris = np.sin(matrice)
        op = "Seno"
    elif scelta_f == "2":
        # Applica il coseno a ogni cella
        ris = np.cos(matrice)
        op = "Coseno"
    elif scelta_f == "3":
        # Calcola e^x per ogni elemento della matrice
        ris = np.exp(matrice)
        op = "Esponenziale"
    else:
        return "Scelta non valida"
    
    # Salvataggio dell'operazione conclusa
    salva_su_file(f"Funzione Universale {op}", ris)
    return ris

def filtra_elementi(matrice):
    # Questa funzione isola solo i dati che soddisfano un criterio logico
    try:
        soglia = float(input("Visualizza elementi maggiori di: "))
        
        # INDICIZZAZIONE BOOLEANA: matrice > soglia crea una maschera di True/False.
        # Applicandola alla matrice, NumPy estrae solo i valori corrispondenti a True.
        # Il risultato è un array 1D (piatto) perché la forma originale potrebbe rompersi.
        elementi_filtrati = matrice[matrice > soglia]
        
        salva_su_file(f"Filtro elementi maggiori di {soglia}", elementi_filtrati)
        return elementi_filtrati
    except ValueError:
        return "Errore: Inserisci un valore numerico valido."
    
# menu parte 3 
    
def menu_parte_3():
    # Gestione dello stato della matrice: inizialmente vuota
    mat = None
    
    while True:
        # Visualizzazione delle nuove funzionalità di analisi e algebra
        print("\n=== MENU AVANZATO (PARTE 3) ===")
        print("1. Crea/Rigenera Matrice")
        print("2. Calcola Matrice Inversa (Algebra Lineare)")
        print("3. Applica Funzione Matematica (sin, cos, exp)")
        print("4. Filtra elementi (maggiori di X)")
        print("0. Esci")
        
        scelta = input("\nScegli un'opzione: ")
        
        if scelta == "1":
            # Generazione della matrice tramite il modulo Parte 1
            mat = crea_matrice()
            if mat is not None:
                print("Matrice corrente:\n", mat)
                
        elif scelta == "2":
            if mat is not None:
                res = calcola_inversa(mat)
                print("Risultato Matrice Inversa:\n", res)
            else:
                print(" Errore: Matrice non definita!")
                
        elif scelta == "3":
            if mat is not None:
                res = applica_funzione_matematica(mat)
                print("Matrice Trasformata:\n", res)
            else:
                print(" Errore: Matrice non definita!")
                
        elif scelta == "4":
            if mat is not None:
                res = filtra_elementi(mat)
                # Stampiamo l'array di elementi che hanno superato il filtro
                print(f"Valori trovati che soddisfano la condizione: {res}")
            else:
                print(" Errore: Matrice non definita!")
                
        elif scelta == "0":
            # Terminazione del modulo avanzato
            print("Chiusura del sistema Parte 3. Dati salvati nel log.")
            break

# Avvio del punto di ingresso principale
if __name__ == "__main__":
    menu_parte_3() 
    
    

