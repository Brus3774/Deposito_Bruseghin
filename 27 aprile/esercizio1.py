
#esercizio 1

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
    
    def __init__(self, nome, iban): #richiama il costruttore della classe base per inizializzare 'nome'
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

# test sistema pagamento

carta1 = CartaDiCredito("Mario Rossi", "1234-5678-9012-3456") #crea un oggetto di tipo CartaDiCredito con nome e numero carta specificati
paypal1 = PayPal("Luigi Bianchi", "luigi@email.it")
bonifico1 = BonificoBancario("Giuseppe Neri", "IT0012345678901234567890123")

carta1.effettua_pagamento(100) #chiama il metodo 'effettua_pagamento' sull'oggetto 'carta', passando l'importo di 100€.
paypal1.effettua_pagamento(200)
bonifico1.effettua_pagamento(300)

# test gestore pagamenti
gestore1 = GestorePagamenti(carta1) #crea un oggetto di tipo GestorePagamenti, passando come parametro l'oggetto 'carta1' (di tipo CartaDiCredito)
gestore1.paga(150) #chiama il metodo 'paga' sull'oggetto 'gestore1', passando l'importo di 150€. Il metodo 'paga' a sua volta chiama 'effettua_pagamento' sull'oggetto 'carta1' con l'importo specificato.
gestore2 = GestorePagamenti(paypal1)
gestore2.paga(250)  
gestore3 = GestorePagamenti(bonifico1)
gestore3.paga(350)
 



