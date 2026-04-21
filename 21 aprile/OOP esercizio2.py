

#esercizio 2

class Libro:
    
    def __init__(self, titolo, autore, pagine): #metodo costruttore che inizializza il titolo, l'autore e il numero di pagine del libro
        self.titolo = titolo #attributo di istanza che rappresenta il titolo del libro
        self.autore = autore
        self.pagine = pagine
        
    def stampa_info(self): #metodo che stampa le informazioni del libro
        print(f"Il libro '{self.titolo}' è stato scritto da {self.autore} e ha {self.pagine} pagine.")
        
libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1178) #creazione di un oggetto libro1 con titolo, autore e numero di pagine
libro2 = Libro("Harry Potter e la Pietra Filosofale", "J.K Rowling", 223) #creazione di un oggetto libro2 con titolo, autore e numero di pagine
libro3 = Libro("Il Codice Da Vinci", "Dan Brown", 689) #creazione di un oggetto libro3 con titolo, autore e numero di pagine

libro1.stampa_info() #stampa le informazioni del libro1
libro2.stampa_info() #stampa le informazioni del libro2
libro3.stampa_info() #stampa le informazioni del libro3


