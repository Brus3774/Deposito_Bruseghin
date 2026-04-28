# esercizio 1 B

from abc import ABC, abstractmethod

class Impiegato(ABC): # classe astratta
    def __init__(self, nome, cognome, stipendio_base): # costruttore
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base
    
    @abstractmethod
    def calcola_stipendio(self): # metodo astratto
        pass
 
    
class ImpiegatoFisso(Impiegato): # classe concreta
    def __init__ (self, nome, cognome, stipendio_base): 
        super().__init__(nome, cognome, stipendio_base)
       
    def calcola_stipendio(self): # implementazione del metodo astratto
        return self.stipendio_base
        
class ImpiegatoAProvvigione(Impiegato): # classe concreta
    def __init__ (self, nome, cognome, stipendio_base, provvigione):
      super().__init__(nome, cognome, stipendio_base)
      self.provvigione = provvigione

    def calcola_stipendio(self): # implementazione del metodo astratto
        return self.stipendio_base + self.provvigione
    
def stampa_dati_impiegati(lista_impiegati): # funzione che sfrutta il polimorfismo per stampare i dati di una lista di impiegati
    for impiegato in lista_impiegati: # polimorfismo: chiama calcola_stipendio() che si comporterà diversamente a seconda del tipo di impiegato
        stipendio = impiegato.calcola_stipendio()
        print(f"Impiegato: {impiegato.nome} {impiegato.cognome} | Stipendio Totale: {stipendio}€")
        
impiegati_azienda = [
    ImpiegatoFisso("Mario", "Minotti", 2000),
    ImpiegatoAProvvigione("Silvio", "Bianchi", 1300, 500),
    ImpiegatoAProvvigione("Anna", "Caffarena", 1300, 300)
]
stampa_dati_impiegati(impiegati_azienda)