

#ereditarietà multipla

class Prodotto: #creo una classe Prodotto che rappresenta un prodotto generico
    
    def __init__(self, nome, costo_produzione, prezzo_vendita): #metodo di inizializzazione che prende come parametri il nome e il prezzo del prodotto e li assegna agli attributi di istanza
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def descrizione(self): #metodo che restituisce la descrizione del prodotto, in questo caso restituisce una stringa generica "prodotto generico"
        return "prodotto generico"
    
    def calcola_profitto(self): #metodo che calcola il profitto del prodotto, sottraendo il costo di produzione dal prezzo di vendita e restituendo il risultato
        return self.prezzo_vendita - self.costo_produzione
    
class Prodotto_Elettronico(Prodotto): #creo una classe ProdottoElettronico che eredita dalla classe Prodotto, ovvero che ha tutti gli attributi e i metodi della classe Prodotto, ma può anche avere attributi e metodi specifici per i prodotti elettronici
    
    def descrizione(self): #sovrascrivo il metodo descrizione della classe Prodotto, in questo caso restituisce una stringa specifica "prodotto elettronico"
        return "prodotto elettronico"
    
    def garanzia(self): #metodo specifico per i prodotti elettronici che restituisce una stringa "il prodotto ha una garanzia di 2 anni"
        return "il prodotto ha una garanzia di 2 anni"
    
    def certificazione_ce(self): #metodo specifico per i prodotti elettronici che restituisce una stringa "il prodotto è certificato CE"
        return "il prodotto è certificato CE"
    
    def descrizione(self):
        # Restituiamo una stringa completa di tutto
        return f"Elettronico - Garanzia: 2 anni - Certificato: CE"

class Prodotto_Abbigliamento(Prodotto): #creo una classe ProdottoAbbigliamento che eredita dalla classe Prodotto, ovvero che ha tutti gli attributi e i metodi della classe Prodotto, ma può anche avere attributi e metodi specifici per i prodotti di abbigliamento
    
    def descrizione(self): #sovrascrivo il metodo descrizione della classe Prodotto, in questo caso restituisce una stringa specifica "prodotto di abbigliamento"
        return "prodotto di abbigliamento"
    
    def materiale(self): #metodo specifico per i prodotti di abbigliamento che restituisce una stringa "il prodotto è fatto di cotone"
        return "il prodotto è fatto di cotone"
    
    def taglia(self): #metodo specifico per i prodotti di abbigliamento che restituisce una stringa "il prodotto è disponibile nelle taglie S, M, L, XL"
        return "il prodotto è disponibile nelle taglie S, M, L, XL" 
    
    def descrizione(self):
        # Restituiamo una stringa completa di tutto
        return f"Abbigliamento - Materiale: cotone - Taglia: S, M, L, XL"


class Fabbrica: #creo una classe Fabbrica che rappresenta una fabbrica che produce prodotti, questa classe non eredita da nessuna classe, ma può essere utilizzata per creare istanze di prodotti
    
    inventario = [] #attributo di classe che rappresenta l'inventario della fabbrica, inizializzato come una lista vuota
    def __init__(self, nome): #metodo di inizializzazione che prende come parametro il nome della fabbrica e lo assegna all'attributo di istanza
        self.nome = nome
        self.inventario = []
    def aggiungi_prodotto(self, prodotto): #metodo che aggiunge un prodotto all'inventario della fabbrica, prende come parametro un'istanza di prodotto e la aggiunge alla lista inventario
        self.inventario.append(prodotto)
    
    def vendi_prodotto(self, prodotto): #metodo che vende un prodotto, prende come parametro un'istanza di prodotto e la rimuove dalla lista inventario, inoltre stampa una stringa "prodotto venduto: " seguita dal nome del prodotto
        self.inventario.remove(prodotto)
        profitto_operazione = prodotto.calcola_profitto()
        print(f"Prodotto venduto: {prodotto.nome}")
        print(f"Profitto generato da questa vendita: {profitto_operazione}€")
        print("-" * 30) # Una linea per separare le vendite
        print(f"Dettagli: {prodotto.descrizione()}")

    
    def resi_prodotto(self, prodotto): #metodo che gestisce i resi dei prodotti, prende come parametro un'istanza di prodotto e la aggiunge nuovamente alla lista inventario, inoltre stampa una stringa "prodotto restituito: " seguita dal nome del prodotto
        self.inventario.append(prodotto)
        print(f"prodotto restituito: {prodotto.nome}")

fabbrica1 = Fabbrica("Samsung") #creo un'istanza della classe Fabbrica, passando come parametro il nome della fabbrica
prodotto1 = Prodotto_Elettronico("Smartphone", 200, 500) #creo un'istanza della classe ProdottoElettronico, passando come parametri il nome, il costo di produzione e il prezzo di vendita del prodotto
prodotto2 = Prodotto_Abbigliamento("Maglietta", 10, 30) #creo un'istanza della classe ProdottoAbbigliamento, passando come parametri il nome, il costo di produzione e il prezzo di vendita del prodotto
fabbrica1.aggiungi_prodotto(prodotto1) #aggiungo il prodotto1 all'inventario della fabbrica1, chiamando il metodo aggiungi_prodotto e passando come parametro l'istanza di prodotto1
fabbrica1.aggiungi_prodotto(prodotto2) #aggiungo il prodotto2 all'inventario della fabbrica1, chiamando il metodo aggiungi_prodotto e passando come parametro l'istanza di prodotto2
fabbrica1.vendi_prodotto(prodotto1) #vendo il prodotto1, chiamando il metodo vendi_prodotto e passando come parametro l'istanza di prodotto1
fabbrica1.resi_prodotto(prodotto1) #gestisco il reso del prodotto1, chiamando il metodo resi_prodotto e passando come parametro l'istanza di prodotto1 
fabbrica1.vendi_prodotto(prodotto2) #vendo il prodotto2, chiamando il metodo vendi_prodotto e passando come parametro l'istanza di prodotto2


                                 
        
    
        
 
    
    
        