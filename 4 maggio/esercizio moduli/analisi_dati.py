# analisi dei dati 

from abc import ABC, abstractmethod
from datetime import datetime

#  Definiamo il "contratto" per tutti gli analizzatori futuri
class AnalizzatoreBase(ABC):
    
    @abstractmethod
    def calcola_media(self):
        #Ogni analizzatore deve poter calcolare una media
        pass

    @abstractmethod
    def genera_report(self):
        #Ogni analizzatore deve poter stampare un report
        pass

# IMPLEMENTAZIONE: La tua classe specifica per le vendite
class AnalizzatoreVendite(AnalizzatoreBase):
    def __init__(self, lista_importi):
        # rendiamo la lista privata
        self.__importi = lista_importi if lista_importi else []

    def calcola_totale(self): # Metodo per calcolare il totale delle vendite
        return sum(self.__importi)

    def calcola_media(self): # Metodo per calcolare la media delle vendite
        if not self.__importi:
            return 0
        return sum(self.__importi) / len(self.__importi)

    def ottieni_giorni_sopra_media(self): # Metodo per ottenere i giorni con vendite sopra la media
        # Restituisce una lista di tuple (Giorno, Valore)
        media = self.calcola_media()
        return [
            (i + 1, val) 
            for i, val in enumerate(self.__importi) 
            if val > media
        ]
        
    def genera_report(self): 
        # 1. Recuperiamo la data e l'ora attuale
        adesso = datetime.now()
        data_stringa = adesso.strftime("%d/%m/%Y %H:%M")

        # 2. Iniziamo a costruire la stringa del report con l'intestazione e la data
        report = "\nREPORT ANALITICO\n"
        report += f"Data di generazione: {data_stringa}\n" 

        if not self.__importi:
            msg_errore = "Messaggio: Non sono presenti dati di vendita per l'elaborazione."
            print(msg_errore)
            return msg_errore

        totale = self.calcola_totale()
        media = self.calcola_media()
        sopra_media = self.ottieni_giorni_sopra_media()

        # 3. Aggiungiamo i dati economici
        report += f"Totale Vendite: {totale:.2f}€\n"
        report += f"Media Periodo:  {media:.2f}€\n"
        
        if not sopra_media:
            report += "Nessun giorno ha superato la media.\n"
        else:
            report += "Giorni con vendite sopra la media:\n"
            for giorno, valore in sopra_media:
                report += f"  > Giorno {giorno}: {valore:.2f}€\n"
        
        # 4. Stampiamo  e restituiamo la stringa completa
        print(report)
        return report
        
