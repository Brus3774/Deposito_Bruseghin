# Responsabile dell'esportazione dei dati in un formato diverso da quello attivo.

import csv
import os
from crea_file import leggi_prodotti, leggi_vendite
from dati import INTESTAZIONI_PRODOTTI, INTESTAZIONI_VENDITE


def _separatore(formato):
    return "," if formato == "csv" else "|"


def _scrivi_file(percorso_dest, formato_dest, intestazioni, righe):
    # Scrive un file nel formato indicato.
    with open(percorso_dest, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=intestazioni, delimiter=_separatore(formato_dest))
        writer.writeheader()
        writer.writerows(righe)


def esporta_prodotti(percorso_sorgente, formato_sorgente,
                     percorso_dest, formato_dest):
    
    # Esporta il file prodotti nel formato di destinazione.
    # Restituisce True se l'esportazione è riuscita, False se non ci sono dati.
    
    prodotti = leggi_prodotti(percorso_sorgente, formato_sorgente)
    if not prodotti:
        return False
    _scrivi_file(percorso_dest, formato_dest,
                 INTESTAZIONI_PRODOTTI, [p.to_dict() for p in prodotti])
    return True


def esporta_vendite(percorso_sorgente, formato_sorgente,
                    percorso_dest, formato_dest):
    
    #Esporta il file vendite nel formato di destinazione.
    #Restituisce True se l'esportazione è riuscita, False se non ci sono dati.
    
    vendite = leggi_vendite(percorso_sorgente, formato_sorgente)
    if not vendite:
        return False
    _scrivi_file(percorso_dest, formato_dest,
                 INTESTAZIONI_VENDITE, [v.to_dict() for v in vendite])
    return True


def formato_opposto(formato):
    # Restituisce il formato alternativo (csv ↔ txt).
    return "txt" if formato == "csv" else "csv"


def percorso_esportazione(percorso_originale, formato_dest, cartella_data):
    
    # Costruisce il percorso di destinazione per l'esportazione.
    # Es: data/prodotti.csv → data/prodotti_export.txt
    
    nome_base = os.path.splitext(os.path.basename(percorso_originale))[0]
    return os.path.join(cartella_data, f"{nome_base}_export.{formato_dest}")
