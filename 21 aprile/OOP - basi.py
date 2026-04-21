# basi OOP


class TANK: #classe
    
    arma_principale = "cannone" #attributo di classe
    arma_secondaria = "mitragliatrice"
    equipaggio = 4
    def __init__(self, nome, nazione): #metodo costruttore, viene chiamato quando creo un oggetto
        self.nome = nome
        self.nazione = nazione
    
    def stampa_info(self): #metodo di istanza, viene chiamato su un oggetto
        print(f"{self.nome} è un tank della {self.nazione} con {self.equipaggio} membri dell'equipaggio e come armamento principale ha un {self.arma_principale} e come armamento secondario una {self.arma_secondaria}")
        
tank1 = TANK("Panzer IV", "Germania") #creazione di un oggetto
tank2 = TANK("T-34", "Russia")
tank3 = TANK("M4 Sherman", "USA")
tank4 = TANK("Churchill", "Inghilterra")
tank5 = TANK("Type 97", "Giappone")
tank6 = TANK("Char B1", "Francia")
tank7 = TANK("Semovente_152", "Italia")  
        
tank1.stampa_info() #chiamata al metodo di istanza
tank2.stampa_info()
    