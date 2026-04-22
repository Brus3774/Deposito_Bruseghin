

#Class method


class Animale:
    
    numero_animali = 0 #attributo di classe che conta il numero di animali creati, inizializzato a 0
    
    def __init__(self, nome, specie): #metodo di inizializzazione che prende come parametri il nome e la specie dell'animale e li assegna agli attributi di istanza, inoltre incrementa il contatore del numero di animali creati
        self.nome = nome
        self.specie = specie
        Animale.numero_animali += 1
        
    @classmethod #decoratore che indica che il metodo è di classe, ovvero che può essere chiamato sia dalla classe che dalle istanze della classe
    def quanti_animali(cls) -> int: #metodo di classe che restituisce il numero di animali creati, prende come parametro la classe stessa (cls) e restituisce il valore dell'attributo di classe numero_animali
        return cls.numero_animali
    
    
animale1 = Animale("gatto", "felino") #creo un'istanza della classe Animale, passando come parametri il nome e la specie dell'animale
animale2 = Animale("Lupo", "canide") 
animale3 = Animale("gallina", "uccello") 
animale4 = Animale("balena", "cetaceo") 

risultato = Animale.quanti_animali() #chiamo il metodo di classe senza istanziare la classe, passando come parametro la classe stessa (cls) e assegnando il numero di animali creati alla variabile risultato
print(f"Numero di animali creati: {risultato}") #stampo il numero di animali creati