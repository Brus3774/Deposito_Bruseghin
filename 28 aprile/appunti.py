def menu():
    gestore = GestoreFlotta([])
    
    while True:
        print("\n--- MENU GESTIONE FLOTTA ---")
        print("1. Aggiungi veicolo")
        print("2. Rimuovi veicolo")
        print("3. Calcola costo manutenzione totale")
        print("4. Stampa elenco veicoli")
        print("5. Esci")
        
        scelta = input("\nScegli un'opzione: ")
        
        match scelta:
            case "1":
                tipo = input("Tipo di veicolo (camion/furgone/motocarro): ").lower()
                targa = input("Inserisci la targa: ") # Necessaria per il nuovo costruttore
                
                match tipo:
                    case "camion":
                        assi = int(input("Numero di assi: "))
                        veicolo = Camion(targa, assi)
                    case "furgone":
                        alim = input("Alimentazione (benzina/diesel/elettrica): ").lower()
                        veicolo = Furgone(targa, alim)
                    case "motocarro":
                        anni = int(input("Anni di servizio: "))
                        veicolo = Motocarro(targa, anni)
                    case _:
                        print("Tipo di veicolo non riconosciuto.")
                        continue
                
                gestore.aggiungi_veicolo(veicolo)
                print(f"Veicolo {targa} aggiunto alla flotta.")
            
            case "2":
                targa = input("Inserisci la targa del veicolo da rimuovere: ")
                gestore.rimuovi_veicolo(targa)
                print(f"Procedura di rimozione completata per: {targa}")
            
            case "3":
                costo = gestore.calcola_costo_manutenzione()
                print(f"\n> Costo totale manutenzione flotta: {costo:.2f}€")
            
            case "4":
                gestore.stampa_veicoli()
            
            case "5":
                print("Chiusura del sistema. Arrivederci!")
                break
            
            case _:
                print("Opzione non valida. Riprova.")

# Per avviare il programma
if __name__ == "__main__":
    menu()       
         