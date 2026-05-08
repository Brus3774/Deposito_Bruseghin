# Responsabile del calcolo delle statistiche su prodotti e vendite.

from crea_file import leggi_prodotti, leggi_vendite


def analisi_prodotti(percorso, formato):
    
    # Calcola le statistiche del magazzino.
    # Restituisce un dizionario con i dati o None se non ci sono prodotti.
    
    prodotti = leggi_prodotti(percorso, formato)
    if not prodotti:
        return None

# List Comprehension per estrarre liste numeriche su cui fare calcoli statistici
    prezzi   = [p.prezzo    for p in prodotti]
    quantita = [p.quantita  for p in prodotti]

# Calcolo della distribuzione dei prodotti per categoria tramite un dizionario
    categorie = {}
    for p in prodotti:
        categorie[p.categoria] = categorie.get(p.categoria, 0) + 1

# Restituisce un report completo sotto forma di dizionario
    return {
        "totale_prodotti":        len(prodotti),
        "scorte_totali":          sum(quantita),
        "valore_magazzino":       sum(p.prezzo * p.quantita for p in prodotti),
        "prezzo_medio":           sum(prezzi) / len(prezzi),
        "prezzo_max":             max(prezzi),
        "prezzo_min":             min(prezzi),
        "prodotti_per_categoria": categorie,
        "prodotti_esauriti":      [p for p in prodotti if p.quantita == 0],
    }


def analisi_vendite(percorso, formato):
    
    # Calcola le statistiche delle vendite.
    # Restituisce un dizionario con i dati o None se non ci sono vendite.
    
    vendite = leggi_vendite(percorso, formato) # # Carica i dati trasformandoli in una lista di oggetti 'Vendita'
    if not vendite:
        return None

    fatturato_totale = sum(v.totale for v in vendite) # Calcola il giro d'affari complessivo usando la proprietà 'totale' della classe Vendita

    per_prodotto = {} # Raggruppamento dati per prodotto (per capire cosa si vende di più)
    for v in vendite:
        if v.nome_prodotto not in per_prodotto: 
            
            # Inizializza un sotto-dizionario per ogni nuovo prodotto incontrato
            per_prodotto[v.nome_prodotto] = {"quantita": 0, "fatturato": 0.0}
            
            # Accumula i valori della transazione corrente
        per_prodotto[v.nome_prodotto]["quantita"]  += v.quantita_venduta
        per_prodotto[v.nome_prodotto]["fatturato"] += v.totale

# Trova il nome del prodotto che ha generato più fatturato
    # key=lambda k: definisce il criterio di confronto (il valore del fatturato nel dizionario)
    prodotto_top = max(per_prodotto, key=lambda k: per_prodotto[k]["fatturato"])

    return {
        "totale_vendite":      len(vendite),
        "fatturato_totale":    fatturato_totale,
        "fatturato_medio":     fatturato_totale / len(vendite),
        "prodotto_top":        prodotto_top,
        "vendite_per_prodotto": per_prodotto,
    }
