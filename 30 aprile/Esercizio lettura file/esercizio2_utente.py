# genera visita medica con un accettazione postuma, con salvataggio su file e lettura delle visite salvate

import random

class Utente: # classe per rappresentare un utente con nome, cognome, email e un ID cliente generato casualmente
    def __init__(self, nome: str, cognome: str, email: str): #
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.id_cliente = random.randint(1000, 9999)

    def __str__(self):
        return f"Cliente: {self.nome} {self.cognome} ({self.email}) - ID: {self.id_cliente}"
    
class VisitaMedica: # classe per rappresentare una visita medica con un utente, data, ora e medico
    def __init__(self, utente: Utente, data: str, ora: str, medico: str):
        self.utente = utente  # riceve l'oggetto Utente già creato
        self.data = data
        self.ora = ora
        self.medico = medico
        
class Accettazione: # classe per rappresentare l'accettazione di una visita medica, con un riferimento alla visita e uno stato di accettazione
    def __init__(self, visita: VisitaMedica):
        self.visita = visita  # riceve l'oggetto VisitaMedica già creato
        self.accettata = True
        

def salva_visita(visita): # funzione per salvare i dati della visita medica su file
    with open("visite_mediche.txt", "a") as file:
        file.write(f"Visita medica per {visita.utente} - Data: {visita.data} - Ora: {visita.ora} - Medico: {visita.medico}\n")

def salva_accettazione(accettazione): # funzione per salvare i dati dell'accettazione su file
    with open("visite_mediche.txt", "a") as file:
        file.write(f"Accettazione per visita medica di {accettazione.visita.utente} - Data: {accettazione.visita.data} - Ora: {accettazione.visita.ora} - Medico: {accettazione.visita.medico} - Stato: {'Accettata' if accettazione.accettata else 'Rifiutata'}\n")
        
def leggi_registrazioni():
    try:
        with open("visite_mediche.txt", "r") as file:
            contenuto = file.read()
            print("\n--- REGISTRAZIONI SALVATE ---")
            print(contenuto)
    except FileNotFoundError:
        print("Nessuna registrazione trovata.")
        
#menu
def menu(utente): # menu del programma per creare visite mediche e accettazioni
        while True:
            print("\n--- MENU ---")
            print("1 - Registra visita medica")
            print("2 - registra accettazione")
            print("3 - leggi registrazioni")
            print("4 - Esci")

            scelta = input("Scelta: ")

            if scelta == "1":
                data = input("Data visita (es. 10/05/2026): ")
                ora = input("Ora visita (es. 15:30): ")
                medico = input("Nome medico: ")
                
                visita = VisitaMedica(utente, data, ora, medico) # creazione dell'oggetto VisitaMedica con l'utente già creato
               
                salva_visita(visita) # salvataggio della visita su file
                print("Visita medica creata e salvata!")
            
            elif scelta == "2":
                 accettazione = Accettazione(visita) # creazione dell'oggetto Accettazione con la visita appena creata
                 salva_accettazione(accettazione) # salvataggio dell'accettazione su file
                 print("Accettazione registrata!")
                
            elif scelta == "3":
                leggi_registrazioni() # lettura e stampa delle registrazioni salvate
                
            elif scelta == "4":
                print("Arrivederci!")
                break
            else:
                print("Scelta non valida.")
                
# avvio del programmau

print("Inserisci i tuoi dati:") # richiesta dei dati dell'utente per creare un'istanza della classe Utente
nome = input("Nome: ")
cognome = input("Cognome: ")
email = input("Email: ")

utente = Utente(nome, cognome, email)
