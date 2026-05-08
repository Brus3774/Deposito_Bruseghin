# Responsabile della creazione dei file e della lettura dei dati da disco.

import csv
import os  # Importa le classi per trasformare dati grezzi in oggetti e le liste dei nomi delle colonne
from dati import Prodotto, Vendita, INTESTAZIONI_PRODOTTI, INTESTAZIONI_VENDITE


def _separatore(formato):
    return "," if formato == "csv" else "|"


def crea_file_prodotti(percorso, formato):
    #  Verifica se il file esiste già per evitare di sovrascriverlo e perdere dati
    if os.path.exists(percorso):
        return
    with open(percorso, "w", encoding="utf-8", newline="") as f: # Apre il file in modalità scrittura
        writer = csv.DictWriter(f, fieldnames=INTESTAZIONI_PRODOTTI, delimiter=_separatore(formato)) # DictWriter permette di scrivere righe partendo da dizionari Python 
        writer.writeheader() # # Scrive la prima riga del file
    print(f"  ✓ File creato: {percorso}")


def crea_file_vendite(percorso, formato):
    # Crea il file vendite vuoto con intestazioni se non esiste.
    if os.path.exists(percorso):
        return
    with open(percorso, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=INTESTAZIONI_VENDITE, delimiter=_separatore(formato))
        writer.writeheader()
    print(f"  ✓ File creato: {percorso}")


def leggi_prodotti(percorso, formato):
    #Legge il file prodotti e restituisce una lista di oggetti Prodotto.
    if not os.path.exists(percorso): # Se il file non esiste, ritorna una lista vuota per non bloccare il programma
        return []
    prodotti = []
    with open(percorso, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=_separatore(formato)) # DictReader legge ogni riga come un dizionario
        for riga in reader:
            prodotti.append(Prodotto(**riga))
    return prodotti


def leggi_vendite(percorso, formato):
    # Legge il file vendite e restituisce una lista di oggetti Vendita.
    if not os.path.exists(percorso):
        return []
    vendite = []
    with open(percorso, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=_separatore(formato))
        for riga in reader:
            vendite.append(Vendita(**riga))
    return vendite


def scrivi_prodotti(percorso, formato, prodotti):
    # Sovrascrive il file prodotti con la lista aggiornata.
    with open(percorso, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=INTESTAZIONI_PRODOTTI, delimiter=_separatore(formato))
        writer.writeheader()
        writer.writerows([p.to_dict() for p in prodotti]) # Trasforma ogni oggetto Prodotto in un dizionario (tramite to_dict) prima di scriverlo


def scrivi_vendite(percorso, formato, vendite):
    # Sovrascrive il file vendite con la lista aggiornata.
    with open(percorso, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=INTESTAZIONI_VENDITE, delimiter=_separatore(formato))
        writer.writeheader()
        writer.writerows([v.to_dict() for v in vendite]) ## Converte la lista di oggetti Vendita in una lista di dizionari scrivibili su CSV
