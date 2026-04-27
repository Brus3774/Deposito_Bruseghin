# esercizio 2

class Persona:
    def __init__(self, nome: str, eta: int):
        self.nome = nome
        self.eta = eta
    
    # --- GETTER E SETTER PER NOME ---
    @property
    def nome(self): 
        return self.__nome #rendiamo l'attributo nome un attributo privato
    
    @nome.setter
    def nome(self, valore):
        if isinstance(valore, str) and valore.strip(): # deve sempre esserci una stringa che rappresenti il nome
            self.__nome = valore
        else:
            print("Errore: Il nome deve essere una stringa non vuota.")

    # --- GETTER E SETTER PER ETA ---
    @property
    def eta(self):
        return self.__eta # rendiamo l'eta un attributo privato
    
    @eta.setter
    def eta(self, valore):
        if isinstance(valore, int) and valore >= 0: # il valore dell'eta deve essere positivo
            self.__eta = valore
        else:
            print("Errore: L'età deve essere un numero intero positivo.")

    # --- METODO DI PRESENTAZIONE ---
    def presentazione(self):
        # Usiamo le property (self.nome) invece degli attributi privati (__nome)
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")
               
    
class Studente(Persona):
    def __init__(self, nome: str, eta: int, voti: list):
        super().__init__ (nome, eta) # richiamo attributi classe madre
        self.voti = voti
    
    def calcola_media(self):
        #Restituisce la media dei voti. Se la lista è vuota, restituisce 0.
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)
    
    def presentazione(self):
        #Override del metodo di Persona per includere la media.
        media = self.calcola_media()
        print(f"Ciao, mi chiamo {self.nome}, ho {self.eta} anni e la mia media voti è {media:.2f}.")
    

class Professore(Persona):
    def __init__(self, nome: str, eta: int, materia: str):
        super().__init__ (nome, eta) #richiamo attributi classe madre
        self.materia = materia
        
    def presentazione(self): #override della presentazione per includere la materia
        print(f"Buongiorno, sono il Professor {self.nome}, ho {self.eta} anni e insegno {self.materia}.")
        
# Creazione degli oggetti
studente1 = Studente("Luca", 20, [28, 30, 27])
professore1 = Professore("Rossi", 45, "Informatica")
studente2 = Studente("Marco", 21, [27, 25, 26])
professore2 = Professore("Giovanni", 56, "Storia")

# Creiamo una lista di persone 
persone = [studente1, professore1, studente2, professore2]

for p in persone:
    p.presentazione()
        
studente1.eta = -50
studente1.nome = ""
studente1.presentazione()
