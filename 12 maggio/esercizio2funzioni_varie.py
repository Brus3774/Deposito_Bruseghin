# es 2 p.227

import numpy as np
import os

def esegui_processo():
    while True:
        # 1. Creazione array
        arr_lin = np.linspace(0, 10, 50)
        arr_cs = np.random.random(50) # random.random è simile a rand

        # 2. Somma elemento per elemento (Vettorizzazione)
        arr_risultante = arr_lin + arr_cs

        # 3. Calcolo somme
        somma_totale = arr_risultante.sum()
        somma_maggiori_5 = arr_risultante[arr_risultante > 5].sum()

        # 4. Stampe
        print("\n--- RISULTATI ---")
        print(f"Somma totale: {somma_totale:.2f}")
        print(f"Somma elementi > 5: {somma_maggiori_5:.2f}")

        # 5. Gestione File TXT
        nome_file = "risultati_numpy.txt"
        modalita = 'w' # Default: sovrascrivi
        
        if os.path.exists(nome_file):
            scelta = input(f"\nIl file '{nome_file}' esiste già. Vuoi sovrascriverlo? (s/n): ").lower()
            if scelta != 's':
                modalita = 'a' # Append: aggiungi in fondo senza cancellare

        with open(nome_file, modalita) as f:
            f.write(f"\n--- Sessione ---\n")
            f.write(f"Somma totale: {somma_totale}\n")
            f.write(f"Somma > 5: {somma_maggiori_5}\n")
            f.write(f"Array risultante:\n{arr_risultante}\n")
        
        print(f"Dati salvati in {nome_file} (modalità: {'Sovrascrittura' if modalita=='w' else 'Aggiunta'})")

        # 6. Ripetibilità
        ancora = input("\nVuoi ripetere il processo? (s/n): ").lower()
        if ancora != 's':
            print("Chiusura programma.")
            break

if __name__ == "__main__":
    esegui_processo() 