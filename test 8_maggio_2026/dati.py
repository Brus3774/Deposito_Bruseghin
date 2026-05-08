# inserimento dati per creazione file

INTESTAZIONI_PRODOTTI = ["id", "nome", "categoria", "prezzo", "quantita"]
INTESTAZIONI_VENDITE  = ["id", "id_prodotto", "nome_prodotto", "quantita_venduta", "prezzo_unitario", "data"]
# Definizione delle intestazioni (nomi delle colonne) per la futura creazione di file CSV o tabelle.

class Prodotto:
    #Rappresenta un singolo prodotto in magazzino. 

    def __init__(self, id, nome, categoria, prezzo, quantita):
        self.id        = str(id)
        self.nome      = str(nome)
        self.categoria = str(categoria)
        self.prezzo    = float(prezzo)
        self.quantita  = int(quantita)

    def to_dict(self): # Converte l'istanza della classe in un dizionario Python standard.
        return {
            "id":        self.id,
            "nome":      self.nome,
            "categoria": self.categoria,
            "prezzo":    self.prezzo,
            "quantita":  self.quantita,
        }

    def __str__(self):
        return (f"[{self.id}] {self.nome} | Categoria: {self.categoria} | "
                f"Prezzo: €{self.prezzo:.2f} | Quantità: {self.quantita}")


class Vendita:
    # Rappresenta una singola transazione di vendita.

    def __init__(self, id, id_prodotto, nome_prodotto, quantita_venduta, prezzo_unitario, data):
        self.id               = str(id)
        self.id_prodotto      = str(id_prodotto)
        self.nome_prodotto    = str(nome_prodotto)
        self.quantita_venduta = int(quantita_venduta)
        self.prezzo_unitario  = float(prezzo_unitario)
        self.data             = str(data)

    @property
    def totale(self): # Calcola il ricavo della riga.
        return self.quantita_venduta * self.prezzo_unitario

    def to_dict(self): # Trasforma l'oggetto vendita in un dizionario.
        return {
            "id":               self.id,
            "id_prodotto":      self.id_prodotto,
            "nome_prodotto":    self.nome_prodotto,
            "quantita_venduta": self.quantita_venduta,
            "prezzo_unitario":  self.prezzo_unitario,
            "data":             self.data,
        }

    def __str__(self): # # Rappresentazione testuale della vendita comprensiva del totale calcolato
        return (f"[{self.id}] {self.nome_prodotto} | Qtà: {self.quantita_venduta} | "
                f"€{self.prezzo_unitario:.2f} cad. | Totale: €{self.totale:.2f} | Data: {self.data}")
        
        