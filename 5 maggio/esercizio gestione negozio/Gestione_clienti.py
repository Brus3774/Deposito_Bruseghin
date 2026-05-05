# sistema gestione clienti 

from Gestione_inventario import Articolo

# sistema gestione clienti 

from Gestione_inventario import Articolo

class Cliente:
    def __init__(self, nome, cognome, email):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.acquisti = []  # Lista degli oggetti Articolo acquistati

    def genera_ricevuta(self):
        #Genera un file TXT individuale con lo storico acquisti del cliente.
        
        nome_file = f"ricevuta_{self.cognome.lower()}_{self.nome.lower()}.txt"
        try:
            with open(nome_file, "w") as f:
                f.write(f"=== RICEVUTA PERSONALE ===\n")
                f.write(f"CLIENTE: {self.nome.upper()} {self.cognome.upper()}\n")
                f.write(f"EMAIL:   {self.email}\n")
                f.write("-" * 35 + "\n")
                
                if not self.acquisti:
                    f.write("Nessun acquisto registrato.\n")
                else:
                    totale = 0
                    for art in self.acquisti:
                        f.write(f"- {art.nome:15} | Prezzo: {art.prezzo}€\n")
                        totale += art.prezzo
                    f.write("-" * 35 + "\n")
                    f.write(f"TOTALE COMPLESSIVO: {totale}€\n")
                
                f.write("\nGrazie per aver scelto il nostro negozio!")
            print(f"Sistema: Ricevuta individuale aggiornata in '{nome_file}'.")
        except Exception as e:
            print(f"Errore nella generazione della ricevuta: {e}")

    def __str__(self):
        return f"{self.nome.capitalize()} {self.cognome.capitalize()} ({self.email})"

class GestioneClienti:
    def __init__(self):
        self.clienti = {} # { email: oggetto_cliente }

    def aggiungi_cliente(self, nome, cognome, email):
        if email.lower() in self.clienti:
            print(f"Errore: Il cliente con email {email} è già registrato.")
        else:
            nuovo = Cliente(nome, cognome, email)
            self.clienti[email.lower()] = nuovo 
            print(f"Sistema: Cliente {nome} registrato con successo.")

    def seleziona_cliente(self, email):
        return self.clienti.get(email.lower()) 

    def visualizza_tutti(self):
        if not self.clienti:
            print("Sistema: Nessun cliente in archivio.")
        else:
            print("\n--- ELENCO CLIENTI REGISTRATI ---")
            for c in self.clienti.values():
                print(c)

    def stampa_report_txt(self, nome_file="report_clienti.txt"):
        # Genera il report globale di tutti i clienti 
        try:
            with open(nome_file, "w") as f:
                f.write("=== REPORT VENDITE PER CLIENTE ===\n\n")
                for c in self.clienti.values():
                    f.write(f"CLIENTE: {c.nome.upper()} {c.cognome.upper()} ({c.email})\n")
                    f.write("DETTAGLIO ACQUISTI:\n")
                    if not c.acquisti:
                        f.write("  - Nessun acquisto effettuato.\n")
                    else:
                        totale = 0
                        for art in c.acquisti:
                            f.write(f"  * {art.nome:15} | Prezzo: {art.prezzo}€\n")
                            totale += art.prezzo
                        f.write(f"  TOTALE SPESA: {totale}€\n")
                    f.write("-" * 40 + "\n")
            print(f"Sistema: Report globale salvato in '{nome_file}'.")
        except Exception as e:
            print(f"Errore nella stampa del report: {e}") 




        


        
    