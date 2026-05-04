# inserimento dati utente

from abc import ABC, abstractmethod
from datetime import datetime

class GestoreDati(ABC): # Classe astratta che definisce un'interfaccia per la gestione dei dati
    @abstractmethod
    def ottieni_e_converti(self):
        pass

class InserimentoDati(GestoreDati): # Classe concreta che implementa il metodo astratto
    def __init__(self, nome, cognome):
        # Attributi privati (Encapsulation)
        self.__nome = nome
        self.__cognome = cognome
        self.lista_importi = []
        self.__data_creazione = datetime.now()

    # Getter per accedere al nome in sola lettura
    @property
    def nome_completo(self):
        return f"{self.__nome} {self.__cognome}"

    def ottieni_e_converti(self):
        print(f"\n--- Sessione di: {self.nome_completo} ---")
        
        while True: # Loop per garantire l'inserimento corretto dei dati
            try:
                input_utente = input("Inserisci almeno 6 importi (separati da spazio): ")
                
                # Conversione con gestione virgole
                nuova_lista = [float(i.replace(',', '.')) for i in input_utente.split()]
                
                # Doppio controllo sulla lunghezza della lista
                if len(nuova_lista) < 6:
                    print(f"Errore: Ne servono almeno 6 (ne hai inseriti {len(nuova_lista)}).")
                    continue
                
                # Controllo extra: numeri positivi
                if any(n < 0 for n in nuova_lista):
                    print("Errore: Gli importi di vendita non possono essere negativi.")
                    continue

                self.lista_importi = nuova_lista
                return self.lista_importi

            except ValueError:
                print("Errore: Inserimento non valido. Usa solo numeri.")

    def info_sessione(self): # Metodo per mostrare info sulla sessione
        return f"Dati inseriti da {self.__nome} il {self.__data_creazione.strftime('%d/%m/%Y')}"
    
    