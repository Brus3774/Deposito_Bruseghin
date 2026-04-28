# esercizio 1

from abc import ABC, abstractmethod

class Impiegato(ABC): # classe astratta
    def __init__(self, nome, cognome, stipendio_base): # costruttore
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base
    
    @abstractmethod
    def calcola_stipendio(self): # metodo astratto
        pass
    
    def mostra_dati(self):
        # Sfrutta il polimorfismo: chiama calcola_stipendio() 
        # che si comporterà diversamente a seconda del tipo di impiegato
        stipendio = self.calcola_stipendio()
        print(f"Impiegato: {self.nome} {self.cognome} | Stipendio Totale: {stipendio}€") 
    
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
    
# test
impiegato1 = ImpiegatoFisso("Mario", "Minotti", 2000)
impiegato2 = ImpiegatoAProvvigione("Silvio", "Bianchi", 1300, 500)
impiegato3 = ImpiegatoAProvvigione("Anna", "Caffarena", 1300, 300)
impiegato1.mostra_dati() 
impiegato2.mostra_dati() 
impiegato3.mostra_dati()  