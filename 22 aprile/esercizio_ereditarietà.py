# esercizio ereditarietà

class Animale: #creo una classe Animale che rappresenta un animale generico
    
    def __init__(self, nome, età): #metodo di inizializzazione che prende come parametri il nome e la specie dell'animale e li assegna agli attributi di istanza
        self.nome = nome
        self.età = età
        
    def verso(self): #metodo che restituisce il verso dell'animale, in questo caso restituisce una stringa generica "verso dell'animale"
        return "verso generico dell'animale"

class Cammello(Animale): #creo una classe Cammello che eredita dalla classe Animale, ovvero che ha tutti gli attributi e i metodi della classe Animale, ma può anche avere attributi e metodi specifici per i cammelli
    
    def verso(self): #sovrascrivo il metodo verso della classe Animale, in questo caso restituisce una stringa specifica "muggito del cammello"
        return "muggito del cammello"
    
    def scorta_acqua(self): #metodo specifico per i cammelli che restituisce una stringa "il cammello ha una scorta d'acqua di 40 litri"
        return "il cammello ha una scorta d'acqua di 40 litri"
    
class Balena(Animale): #creo una classe Balena che eredita dalla classe Animale, ovvero che ha tutti gli attributi e i metodi della classe Animale, ma può anche avere attributi e metodi specifici per le balene
    
    def verso(self): #sovrascrivo il metodo verso della classe Animale, in questo caso restituisce una stringa specifica "canto della balena"
        return "canto della balena"
    
    def nuota(self): #metodo specifico per le balene che restituisce una stringa "la balena nuota nell'oceano"
        return "la balena nuota nell'oceano"
    
class Pipistrello(Animale): #creo una classe Pipistrello che eredita dalla classe Animale, ovvero che ha tutti gli attributi e i metodi della classe Animale, ma può anche avere attributi e metodi specifici per i pipistrelli
    
    def verso(self): #sovrascrivo il metodo verso della classe Animale, in questo caso restituisce una stringa specifica "ululato del pipistrello"
        return "stridio del pipistrello"
    
    def ecolocalizzazione(self): #metodo specifico per i pipistrelli che restituisce una stringa "il pipistrello utilizza l'ecolocalizzazione"
        return "il pipistrello utilizza l'ecolocalizzazione"
    
cammello1 = Cammello("Camillo", 5) #creo un'istanza della classe Cammello, passando come parametri il nome e l'età del cammello
balena1 = Balena("Elena", 10) #creo un'istanza della classe Balena, passando come parametri il nome e l'età della balena
pipistrello1 = Pipistrello("Pippo", 2) #creo un'istanza della classe Pipistrello, passando come parametri il nome e l'età del pipistrello
cammello2 = Cammello("Pietro", 3)
balena2 = Balena("Giulia", 8)
pipistrello2 = Pipistrello("Pippo", 4)

print(f"il cammello si chiama {cammello1.nome} e ha {cammello1.età} anni")#stampo il nome del cammello1, che è un attributo ereditato dalla classe Animale
print(f"la balena si chiama {balena1.nome} e ha {balena1.età} anni") #stampo il nome e l'età della balena1,che è un attributo ereditato dalla classe Animale
print(f"il pipistrello si chiama {pipistrello1.nome} e ha {pipistrello1.età} anni") #stampo il nome e l'età del pipistrello1, che è un attributo ereditato dalla classe Animale
print(cammello2.scorta_acqua()) #stampo la scorta d'acqua del cammello2, che è un metodo specifico della classe Cammello
print(balena2.nuota()) #stampo la nuotata della balena2, che è un metodo specifico della classe Balena
print(pipistrello2.ecolocalizzazione()) #stampo l'ecolocalizzazione del pipistrello2, che è un metodo specifico della classe Pipistrello    

