# esempio astrazione
from abc import ABC, abstractmethod

class Animale(ABC): # classe astratta
    @abstractmethod
    def muovi(self): # metodo astratto
        pass
    
class Cane(Animale): # classe concreta
    def muovi(self): # implementazione del metodo astratto
        print("corro")
        
class Pesce(Animale): # classe concreta
    def muovi(self): # implementazione del metodo astratto
        print("nuoto")


       