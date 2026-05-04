
#main con 3 parti: inserimento dati, analisi dati e gestione txt, da decidere se il giorno è da inserire nel lain o fare un modulo a parte
from datetime import datetime 
from Inserimento_dati import InserimentoDati
from analisi_dati import AnalizzatoreVendite
from gestione_txt import GestoreFileTXT

def mostra_menu():
    print("\n--- GESTIONE VENDITE ---")
    print("1. Inserisci nuovi dati e genera report")
    print("2. Visualizza info programma")
    print("3. Esci")
    return input("Scegli un'opzione: ")

def main():
    salvatore = GestoreFileTXT()
    # Variabile per tenere traccia se abbiamo dei dati pronti
    ultimo_report = None 

    while True:
        scelta = mostra_menu()

        match scelta:
            case "1":
                nome = input("Nome venditore: ")
                cognome = input("Cognome venditore: ")
                
                # Fase di input
                utente = InserimentoDati(nome, cognome)
                dati = utente.ottieni_e_converti()
                
                # Fase di analisi
                analizzatore = AnalizzatoreVendite(dati)
                ultimo_report = analizzatore.genera_report()
                
                # Fase di salvataggio
                timestamp = datetime.now().strftime("%Y%m%d_%H%M")
                nome_file = f"report_{nome}_{cognome}_{timestamp}.txt"
                salvatore.salva(nome_file, ultimo_report)

            case "2":
                print("\nSoftware di Analisi Vendite v1.0")
                print("Gestisce l'inserimento validato, il calcolo della media")
                print("e l'individuazione dei giorni sopra soglia.")

            case "3":
                print("Uscita in corso... Arrivederci!")
                break

            case _: # Caso di default (input errato)
                print("Opzione non valida. Per favore, scegli 1, 2 o 3.")

if __name__ == "__main__":
    main() 
