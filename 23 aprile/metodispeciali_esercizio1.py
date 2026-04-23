# metodi speciali


class Unitamilitare:
    def __init__(self, nome: str, numero_soldati: int): # metodo  __init__ è il costruttore della classe, viene chiamato quando creiamo un'istanza della classe
        self.nome = nome
        self.numero_soldati = numero_soldati
        
    def muovi(self, destinazione): # metodo che rappresenta il movimento dell'unità verso una destinazione
        print(f"{self.nome} si sta muovendo verso {destinazione}")
        
    def attacca(self, bersaglio): # metodo che rappresenta l'attacco dell'unità verso un bersaglio
        print(f"{self.nome} sta attaccando {bersaglio}")
        
    def ritirata(self): # metodo che rappresenta la ritirata dell'unità
        print(f"{self.nome} si sta ritirando")
        
    def __str__(self):
        return f"Unità coinvolta: [{self.nome}] - Forza: {self.numero_soldati} soldati" # metodo __str__ viene chiamato quando stampiamo un'istanza della classe, restituisce una stringa che rappresenta l'istanza
    
    def __len__(self):     
        #Restituisce il numero di soldati usando len(unita) 
        return self.numero_soldati
    
    def __eq__(self, altro):
        # Permette di usare unita1 == unita2
        if isinstance(altro, Unitamilitare):
            return self.nome == altro.nome and self.numero_soldati == altro.numero_soldati
        return False
        

class Fanteria(Unitamilitare): # classe che rappresenta l'unità di fanteria, che ha un metodo speciale per costruire trincee
    def __init__(self, nome: str, numero_soldati: int):
        # super().__init__ richiama il costruttore della classe madre
        # così non dobbiamo riscrivere self.nome = nome ecc.
        super().__init__(nome, numero_soldati)
    
    def costruisci_trincea(self):
        print(f"{self.nome} sta costruendo una trincea")    

class Artiglieria(Unitamilitare): # classe che rappresenta l'unità di artiglieria, che ha un metodo speciale per calibrare i cannoni
    def __init__(self, nome:str, numero_soldati: int):
        super().__init__(nome, numero_soldati)
    
    def calibra_cannoni(self):
        print(f"{self.nome} sta calibrando le batterie")

class Cavalleria(Unitamilitare): # classe che rappresenta l'unità di cavalleria, che ha un metodo speciale per esplorare il terreno
    def __init__(self, nome: str, numero_soldati: int):
        super().__init__(nome, numero_soldati)
    
    def esplora_terreno(self):
        print(f"{self.nome} sta esplorando il terreno")

class Supportologistico(Unitamilitare): # classe che rappresenta l'unità di supporto logistico, che ha un metodo speciale per rifornire le truppe
    def __init__(self, nome: str, numero_soldati: int):
        super().__init__(nome, numero_soldati)
        
    def rifornisci_unità(self):
        print(f"{self.nome} sta rifornendo le truppe")

class Ricognizione(Unitamilitare): # classe che rappresenta l'unità di ricognizione, che ha un metodo speciale per raccogliere informazioni sul nemico
    def __init__(self, nome: str, numero_soldati: int):
        super().__init__(nome, numero_soldati)
        
    def raccogli_informazioni(self):
        print(f"{self.nome} sta raccogliendo informazioni sul nemico")

class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, Supportologistico, Ricognizione): # classe che eredita da tutte le altre classi, quindi ha tutti i metodi di tutte le classi
    def __init__(self, nome: str, numero_soldati: int):
        # Inizializziamo la classe madre comune tramite super()
        super().__init__(nome, numero_soldati)
        # Il dizionario richiesto per gestire le altre unità
        self.registro_unita = {}      
        
    def __len__(self):
        return len(self.registro_unita)
    

    def registra_unita(self, unita):
        self.registro_unita[unita.nome] = unita
        print(f"Unità {unita.nome} registrata nel sistema.")

    def mostra_unita(self):
        print("\n--- Unità nel Registro ---")
        for nome in self.registro_unita:
            print(f"- {nome}")

    def dettagli_unita(self, nome):
        if nome in self.registro_unita:
            print(f"Dettagli: {self.registro_unita[nome]}")
        else:
            print("Unità non trovata.")
            
# Creiamo il Centro di Controllo (che è esso stesso un'unità speciale)
hq = ControlloMilitare("Quartier Generale", 100)

# Creiamo alcune unità e le registriamo nel sistema
fan1 = Fanteria("1ª Divisione Fanteria Cuneo", 10000)
art1 = Artiglieria("1ª Divisione Artiglieria Vulcano",  1200)
cav1 = Cavalleria("3ª Divisione Cavalleria Ariete", 3300)                
Sup1 = Supportologistico("4ª Battaglione Supporto Logistico Perugia", 1500)
ric1 = Ricognizione("5ª Battaglione Ricognizione - Cagliari", 100)
fan2 = Fanteria("4ª Divisione Fanteria Roma", 12000)
art2 = Artiglieria("2ª Divisione Artiglieria Etna", 1300)
cav2 = Cavalleria("6ª Divisione Cavalleria Centauro", 3500)


hq.registra_unita(fan1)
hq.registra_unita(art1)
hq.registra_unita(cav1)
hq.registra_unita(Sup1)
hq.registra_unita(ric1)

hq.mostra_unita()
hq.dettagli_unita("1ª Divisione Fanteria Cuneo")   
hq.dettagli_unita("1ª Divisione Artiglieria Vulcano")
hq.dettagli_unita("4ª Divisione Fanteria Roma")

fan1.muovi(destinazione= "confine")
art1.attacca(bersaglio = "snodo logistico")
cav1.ritirata()

fan1.costruisci_trincea()

print(f"Soldati nella fanteria: {len(fan1)}") # Richiama __len__ di Unitamilitare
print(f"Unità totali nel registro HQ: {len(hq)}") # Richiama __len__ di ControlloMilitare
print(f"L'unità uno è diversa dall'unità due? {fan1 == fan2}") 

