
#es 1b: aggiunta classe Gestione utenti

import random

class MetodoPagamento: #classe astratta
    def  __init__ (self, nome):
        self.nome = nome
    
    def effettua_pagamento(self, importo): #metodo astratto, da sovrascrivere nelle sottoclassi
        pass

class CartaDiCredito(MetodoPagamento): #sottoclasse che eredita da MetodoPagamento
    
    def __init__(self, nome, numero_carta): 
        super().__init__(nome) #richiama il costruttore della classe base per inizializzare 'nome'
        self.numero_carta = numero_carta
    
    def effettua_pagamento(self, importo): #sovrascrive il metodo astratto per implementare il pagamento con carta di credito
        print(f"Pagamento di {importo}€ effettuato con Carta di Credito n. {self.numero_carta} intestata a {self.nome}.")
    
class PayPal(MetodoPagamento):
    
    def __init__(self, nome, indirizzo_email):
        super().__init__(nome)
        self.indirizzo_email = indirizzo_email
    
    def effettua_pagamento(self, importo): #sovrascrive il metodo astratto per implementare il pagamento con PayPal
        print(f"Pagamento di {importo}€ effettuato con PayPal all'indirizzo {self.indirizzo_email} intestato a {self.nome}.")
    
    
class BonificoBancario(MetodoPagamento):
    
    def __init__(self, nome, iban):
        super().__init__(nome)
        self.iban = iban
    
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con Bonifico Bancario iban {self.iban} intestato a {self.nome}.")
        
    
class GestorePagamenti:
    def __init__(self, metodo_scelto):
        # Riceve un oggetto (istanza) di una delle sottoclassi di MetodoPagamento
        self.metodo_scelto = metodo_scelto

    def paga(self, importo):
        print(f"Inizio transazione per {importo}€...") # Duck Typing: Chiamiamo il metodo senza chiederci di che tipo sia l'oggetto
        self.metodo_scelto.effettua_pagamento(importo)
        print("Transazione conclusa con successo.\n") 

class GestioneUtenti:
    def __init__(self):
        # Usiamo un dizionario per memorizzare: nome -> {metodo, budget}
        self.utenti = {}

    def registra_utente(self, nome_utente, metodo_pagamento):
        # Generiamo un budget random per ogni utente al momento della registrazione (tra 50 e 300€)
        budget_iniziale = random.randint(50, 300)
        self.utenti[nome_utente] = { #nome_utente è la chiave, il valore è un dizionario con 'metodo' e 'budget'
            "metodo": metodo_pagamento,
            "budget": budget_iniziale
        }
        print(f"Utente '{nome_utente}' registrato. Budget disponibile: {budget_iniziale}€.")

    def acquisto_utente(self, nome_utente, importo): #metodo per effettuare un acquisto, controlla se l'utente ha abbastanza budget e poi chiama il metodo di pagamento
        if nome_utente not in self.utenti:
            print(f"Errore: L'utente '{nome_utente}' non esiste.")
            return

        dati = self.utenti[nome_utente] #dati è un dizionario con 'metodo' e 'budget' per l'utente specificato
        
        # Controllo del budget prima di procedere
        if dati["budget"] >= importo:
            # Sottraiamo l'importo
            dati["budget"] -= importo
            # POLIMORFISMO: il 'metodo' sa già se è PayPal, Carta o Bonifico
            dati["metodo"].effettua_pagamento(importo)
            print(f"Budget residuo per {nome_utente}: {dati['budget']}€\n")
        else:
            print(f"Spiacente {nome_utente}, budget insufficiente! (Hai {dati['budget']}€, richiesti {importo}€)\n")

# test del sistema di pagamento e gestione utente

sistema = GestioneUtenti()

# Creiamo le istanze dei metodi di pagamento
p1 = PayPal("Mario Rossi", "mario@email.it")
p2 = CartaDiCredito("Luigi Verdi", "5555-4444-3333-2222")

# Registriamo gli utenti nel sistema
sistema.registra_utente("Mario88", p1)
sistema.registra_utente("Luigi_Pro", p2)

# Simuliamo degli acquisti
print("\n--- AVVIO SESSIONE ACQUISTI ---")
sistema.acquisto_utente("Mario88", 40)
sistema.acquisto_utente("Luigi_Pro", 250)


        
        
        
