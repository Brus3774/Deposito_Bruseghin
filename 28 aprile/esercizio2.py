# sistema astratto di trasporto merci

from abc import ABC, abstractmethod

class VeicoloTrasporto(ABC): # classe astratta
    def __init__(self, targa: str, peso_massimo: int, carico_attuale: int = 0): 
        self._targa = targa
        self._peso_massimo = peso_massimo
        self._carico_attuale = carico_attuale
    
    @property # getter per targa, peso_massimo e carico_attuale
    def targa(self):
        return self._targa
    
    @property
    def peso_massimo(self):
        return self._peso_massimo
    
    @property
    def carico_attuale(self):
        return self._carico_attuale
    
    @abstractmethod # metodo astratto per calcolare il costo di manutenzione, da implementare nelle classi concrete
    def costo_manutenzione(self):
        pass
    
    def carica_peso(self, peso): # metodo per caricare peso, con controllo sul peso massimo
        if self._carico_attuale + peso > self._peso_massimo: 
            print(f"Errore: il carico totale supererebbe il peso massimo di {self._peso_massimo} kg.")
        else:
            self._carico_attuale += peso
            print(f"Carico di {peso} kg aggiunto. Carico attuale: {self._carico_attuale} kg.") 
    
    def scarica (self, peso): # metodo per scaricare peso, con controllo sul carico attuale
        if self._carico_attuale - peso < 0:
            print(f"Errore: il carico da scaricare supererebbe il carico attuale di {self._carico_attuale} kg.")
        else:
            self._carico_attuale -= peso
            print(f"Carico di {peso} kg rimosso. Carico attuale: {self._carico_attuale} kg.")
   
class Camion(VeicoloTrasporto): # classe concreta
        def __init__(self, targa, numero_assi: int):
           super().__init__(targa, peso_massimo = 30000)
           self.numero_assi = numero_assi
           
        def costo_manutenzione(self): # implementazione del metodo astratto, con costo che dipende dal numero di assi e dal peso massimo
            costo_base = 1000
            costo_per_asse = 200
            costo_per_kg = 1
            costo_totale = costo_base + (costo_per_asse * self.numero_assi) + (costo_per_kg * self.peso_massimo)
            return costo_totale  

class Furgone(VeicoloTrasporto):
        def __init__(self, targa, alimentazione: str):
            super().__init__(targa, peso_massimo = 5000)
            self.alimentazione = alimentazione
        
        def costo_manutenzione(self): # implementazione del metodo astratto, con costo che dipende dal tipo di alimentazione e dal peso massimo
            costo_base = 500
            costo_per_kg = 1
            costo_totale = costo_base + (costo_per_kg * self.peso_massimo)
            if self.alimentazione == "elettrica":
                costo_totale *= 0.8 # sconto del 20% per veicoli elettrici
            elif self.alimentazione == "benzina":
                costo_totale *= 1.1 # aumento del 10% per veicoli a benzina
            elif self.alimentazione == "diesel":
                costo_totale *= 1.2 # aumento del 20% per veicoli diesel
            return costo_totale
        
class Motocarro(VeicoloTrasporto):
        def __init__(self, targa, anni_servizio: int):
            super().__init__(targa, peso_massimo = 1000)
            self.anni_servizio = anni_servizio
            
        def costo_manutenzione(self): # implementazione del metodo astratto, con costo che dipende dagli anni di servizio e dal peso massimo
                costo_base = 300
                costo_per_anno = 50
                costo_per_kg = 1
                costo_totale = costo_base + (costo_per_anno * self.anni_servizio) + (costo_per_kg * self.peso_massimo)
                return costo_totale
            
class GestoreFlotta: # classe che gestisce una flotta di veicoli, con metodi per aggiungere, rimuovere, calcolare il costo totale di manutenzione e stampare i dati dei veicoli
    def __init__(self, veicoli: list):
        self._veicoli = veicoli
        
    def aggiungi_veicolo(self, veicolo): # metodo per aggiungere un veicolo alla flotta
        self._veicoli.append(veicolo)
    
    def rimuovi_veicolo(self, targa): # metodo per rimuovere un veicolo dalla flotta, identificato dalla targa
        self._veicoli = [veicolo for veicolo in self._veicoli if veicolo.targa != targa]
    
    def calcola_costo_manutenzione(self): # metodo per calcolare il costo totale di manutenzione della flotta, sommando i costi di manutenzione di tutti i veicoli
        return sum(v.costo_manutenzione() for v in self._veicoli)
    
    def stampa_veicoli(self): # metodo per stampare i dati di tutti i veicoli della flotta, sfruttando il polimorfismo per chiamare il metodo costo_manutenzione() che si comporterà diversamente a seconda del tipo di veicolo
        for veicolo in self._veicoli:
            print(f"Veicolo: {veicolo.targa} | Carico Attuale: {veicolo.carico_attuale} kg | Peso Massimo: {veicolo.peso_massimo} kg"
                  f" | Costo Manutenzione: {veicolo.costo_manutenzione()}€")  
         
 # Menu utente
def menu(): # funzione che gestisce il menu utente per interagire con il sistema di gestione della flotta
    gestore = GestoreFlotta([])
    
    while True: # ciclo infinito per mostrare il menu finché l'utente non sceglie di uscire
        print("--- MENU GESTIONE FLOTTA ---")
        print("1. Aggiungi veicolo")
        print("2. Rimuovi veicolo")
        print("3. Calcola costo manutenzione totale")
        print("4. Stampa elenco veicoli")
        print("5. Esci")
        
        scelta = input("\nScegli un'opzione: ") # input dell'utente per scegliere un'opzione del menu
        
        match scelta:
            case "1":
                tipo = input("Tipo di veicolo (camion/furgone/motocarro): ").lower() # input dell'utente per scegliere il tipo di veicolo da aggiungere, con conversione a minuscolo per facilitare il confronto
                targa = input("Inserisci la targa: ") # Necessaria per il nuovo costruttore
                
                match tipo: # confronto del tipo di veicolo scelto dall'utente, con creazione dell'istanza del veicolo corrispondente
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
                
                gestore.aggiungi_veicolo(veicolo) # aggiunta del veicolo alla flotta tramite il metodo del gestore
                print(f"Veicolo {targa} aggiunto alla flotta.")
            
            case "2": # rimozione di un veicolo dalla flotta, identificato dalla targa inserita dall'utente
                targa = input("Inserisci la targa del veicolo da rimuovere: ")
                gestore.rimuovi_veicolo(targa)
                print(f"Procedura di rimozione completata per: {targa}")
            
            case "3": # calcolo del costo totale di manutenzione della flotta, con stampa del risultato formattato
                costo = gestore.calcola_costo_manutenzione()
                print(f"\n> Costo totale manutenzione flotta: {costo:.2f}€")
            
            case "4": # stampa dei dati di tutti i veicoli della flotta, sfruttando il metodo del gestore che utilizza il polimorfismo per chiamare il metodo costo_manutenzione() di ogni veicolo
                gestore.stampa_veicoli()
            
            case "5": # uscita dal programma, con messaggio di chiusura
                print("Chiusura del sistema. Arrivederci!")
                break
            
            case _:
                print("Opzione non valida. Riprova.")

 



 

