 # Esercizio di lettura e scrittura su file con classi e funzioni in Python
 
import random

class Utente: # classe per rappresentare un utente con nome, cognome, email e un ID cliente generato casualmente
    def __init__(self, nome: str, cognome: str, email: str): #
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.id_cliente = random.randint(1000, 9999)

    def __str__(self):
        return f"Cliente: {self.nome} {self.cognome} ({self.email}) - ID: {self.id_cliente}"

def crea_ricevuta_acquisto(utente): # funzione per creare una ricevuta di acquisto e salvarla su file
    print("\n--- RICEVUTA DI ACQUISTO ---")
    prodotto = input("Nome prodotto: ")
    prezzo = float(input("Prezzo (€): "))
# formattazione della stringa della ricevuta con i dati dell'utente, prodotto e prezzo
    ricevuta = f"RICEVUTA DI ACQUISTO\n{utente}\nProdotto: {prodotto}\nTotale: € {prezzo:.2f}\n\n"
# uso with open per gestire i file in modo sicuro e automatico, con modalità "a" per aggiungere al file senza sovrascrivere
    with open("ricevute.txt", "a") as file:
        file.write(ricevuta)

    print("Ricevuta salvata!")


def crea_ricevuta_ordine(utente): # funzione per creare una ricevuta di ordine e salvarla su file
    print("\n--- RICEVUTA DI ORDINE ---")
    prodotto = input("Nome prodotto: ")
    prezzo = float(input("Prezzo (€): "))
    consegna = input("Data consegna (es. 10/05/2026): ")

    ricevuta = f"RICEVUTA DI ORDINE\n{utente}\nProdotto: {prodotto}\nTotale: € {prezzo:.2f}\nConsegna: {consegna}\n\n"

    with open("ricevute.txt", "a") as file:
        file.write(ricevuta)

    print("Ricevuta salvata!")
    
    
def leggi_ricevute(): # funzione per leggere e stampare tutte le ricevute salvate
    try:
        with open("ricevute.txt", "r") as file:
            contenuto = file.read()
            print("\n" + contenuto)
    except FileNotFoundError:
        print("Nessuna ricevuta trovata.")

# menu del programma
def menu(utente):
    while True:
        print("\n--- MENU ---")
        print("1 - Crea ricevuta di acquisto")
        print("2 - Crea ricevuta di ordine")
        print("3 - Leggi ricevute")
        print("4 - Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            crea_ricevuta_acquisto(utente)
        elif scelta == "2":
            crea_ricevuta_ordine(utente)
        elif scelta == "3":
            leggi_ricevute()
        elif scelta == "4":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida.")
            
# avvio del programma

print("Inserisci i tuoi dati:") # richiesta dei dati dell'utente per creare un'istanza della classe Utente
nome = input("Nome: ")
cognome = input("Cognome: ")
email = input("Email: ")

utente = Utente(nome, cognome, email)
menu(utente)
 