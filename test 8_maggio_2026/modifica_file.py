# Responsabile della modifica e dell'eliminazione di prodotti e vendite.

from crea_file import leggi_prodotti, leggi_vendite, scrivi_prodotti, scrivi_vendite


# PRODOTTI 
def modifica_prodotto(percorso, formato, id_prodotto,
                      nome=None, categoria=None, prezzo=None, quantita=None):
    
   # Modifica i campi di un prodotto esistente.
   # Restituisce True se la modifica è avvenuta, False se l'ID non esiste.
    
    prodotti = leggi_prodotti(percorso, formato) # Carica l'intera lista dal file
    prodotto = next((p for p in prodotti if p.id == str(id_prodotto)), None) # 2. Cerca il prodotto specifico. 
    # next() con un generatore è più efficiente di un ciclo for completo per trovare un singolo elemento.

    if not prodotto:
        return False
# Aggiornamento selettivo: modifica l'attributo solo se è stato passato un nuovo valore
    if nome      is not None: prodotto.nome      = nome
    if categoria is not None: prodotto.categoria = categoria
    if prezzo    is not None: prodotto.prezzo    = float(prezzo)
    if quantita  is not None: prodotto.quantita  = int(quantita)

    scrivi_prodotti(percorso, formato, prodotti) # Sovrascrive il file con la lista aggiornata 
    return True


def elimina_prodotto(percorso, formato, id_prodotto):
    
    # Elimina un prodotto per ID.
    # Restituisce il Prodotto eliminato o None se non trovato.
    
    prodotti = leggi_prodotti(percorso, formato)
    prodotto = next((p for p in prodotti if p.id == str(id_prodotto)), None)

    if not prodotto:
        return None

    prodotti.remove(prodotto) # Rimuove l'oggetto trovato dalla lista in memoria
    scrivi_prodotti(percorso, formato, prodotti) # Salva la lista "accorciata" sul file 
    return prodotto


#  VENDITE 

def elimina_vendita(percorso_vendite, percorso_prodotti, formato, id_vendita):
    
    # Elimina una vendita per ID e ripristina la quantità nel magazzino.
    # Restituisce la Vendita eliminata o None se non trovata.
    
    vendite = leggi_vendite(percorso_vendite, formato) # Carica lo storico vendite
    vendita = next((v for v in vendite if v.id == str(id_vendita)), None)

    if not vendita:
        return None

    # Ripristina scorte
    prodotti = leggi_prodotti(percorso_prodotti, formato) # Carica i prodotti per poter aggiornare la giacenza
    prodotto = next((p for p in prodotti if p.id == vendita.id_prodotto), None)
    if prodotto:
        prodotto.quantita += vendita.quantita_venduta # Se il prodotto esiste ancora, aggiunge di nuovo la quantità che era stata venduta
        scrivi_prodotti(percorso_prodotti, formato, prodotti) # Salva subito le scorte aggiornate nel file prodotti

    vendite.remove(vendita) # Rimuove la vendita dalla lista e aggiorna il file vendite 
    scrivi_vendite(percorso_vendite, formato, vendite)
    return vendita 