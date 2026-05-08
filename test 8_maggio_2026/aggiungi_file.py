# Responsabile dell'aggiunta di nuovi prodotti e vendite.

from datetime import date
from dati import Prodotto, Vendita
from crea_file import leggi_prodotti, leggi_vendite, scrivi_prodotti, scrivi_vendite


def _nuovo_id(lista):
    # Genera un nuovo ID incrementale basato sulla lista esistente.
    return str(max((int(x.id) for x in lista), default=0) + 1)


def aggiungi_prodotto(percorso, formato, nome, categoria, prezzo, quantita):
    
    # Aggiunge un nuovo prodotto al file.
    # Restituisce l'oggetto Prodotto creato.
    
    prodotti = leggi_prodotti(percorso, formato)
    nuovo = Prodotto(
        id        = _nuovo_id(prodotti),
        nome      = nome,
        categoria = categoria,
        prezzo    = float(prezzo),
        quantita  = int(quantita),
    )
    prodotti.append(nuovo)
    scrivi_prodotti(percorso, formato, prodotti)
    return nuovo


def aggiungi_vendita(percorso_vendite, percorso_prodotti, formato,
                     id_prodotto, quantita_venduta):
    
    # Registra una nuova vendita e scala la quantità dal magazzino.
    # Restituisce la Vendita creata o None se il prodotto non esiste
    # o le scorte sono insufficienti.
    
    prodotti = leggi_prodotti(percorso_prodotti, formato)
    prodotto = next((p for p in prodotti if p.id == str(id_prodotto)), None)

    if not prodotto:
        return None, "Prodotto non trovato."
    if prodotto.quantita < int(quantita_venduta):
        return None, f"Scorte insufficienti (disponibili: {prodotto.quantita})."

    # Scala magazzino
    prodotto.quantita -= int(quantita_venduta)
    scrivi_prodotti(percorso_prodotti, formato, prodotti)

    # Registra vendita
    vendite = leggi_vendite(percorso_vendite, formato)
    nuova = Vendita(
        id               = _nuovo_id(vendite),
        id_prodotto      = prodotto.id,
        nome_prodotto    = prodotto.nome,
        quantita_venduta = int(quantita_venduta),
        prezzo_unitario  = prodotto.prezzo,
        data             = str(date.today()),
    )
    vendite.append(nuova)
    scrivi_vendite(percorso_vendite, formato, vendite)
    return nuova, None
