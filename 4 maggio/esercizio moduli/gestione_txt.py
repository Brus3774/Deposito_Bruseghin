# gestione della stampa su file txt


from abc import ABC, abstractmethod

class ScrittoreBase(ABC): # Classe astratta che definisce un'interfaccia per la scrittura su file
    @abstractmethod
    def salva(self, nome_file, contenuto):
        pass

class GestoreFileTXT(ScrittoreBase):
    def salva(self, nome_file, contenuto):
        #Salva il testo fornito in un file .txt
        try:
            with open(nome_file, "w", encoding="utf-8") as file: # Utilizziamo 'with' per garantire la chiusura del file
                file.write(contenuto)
            print(f"\n[Sistema] Report salvato con successo in: {nome_file}")
        except IOError as e:
            print(f"[Errore] Impossibile scrivere sul file: {e}") 
            