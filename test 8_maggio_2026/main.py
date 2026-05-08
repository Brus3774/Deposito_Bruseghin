# main.py 

import os
import sys

sys.path.insert(0, os.path.dirname(__file__)) # Aggiunge la cartella corrente al percorso di ricerca di Python per importare i moduli locali

# Importazione dei moduli personalizzati 
import crea_file
import aggiungi_file
import modifica_file
import analisi_file
import esporta_file

# Definizione del percorso della cartella dove verranno salvati i file dei dati 
CARTELLA_DATA = os.path.join(os.path.dirname(__file__), "data")


# Interfaccia Utente

def sep(titolo=""): # Crea un separatore grafico per rendere il menu leggibile in console
    print("\n" + "=" * 50)
    if titolo:
        print(f"  {titolo}")
        print("=" * 50)


def input_float(prompt): # Gestisce l'input di numeri decimali, rimpiazzando la virgola con il punto
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("  ✗ Inserisci un numero valido.")


def input_int(prompt): # Forza l'utente a inserire un numero intero, gestendo gli errori di digitazione.
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  ✗ Inserisci un numero intero.")


def input_scelta(opzioni): # Verifica che l'utente scelga solo tra le opzioni valide fornite
    while True:
        s = input("  → Scelta: ").strip()
        if s in opzioni:
            return s
        print(f"  ✗ Opzione non valida. Scegli tra: {', '.join(opzioni)}")


def pausa(): # Interrompe lo scorrimento del testo per permettere all'utente di leggere i risultati
    input("\n  Premi Invio per continuare...")


# Configurazione iniziale 

def scegli_formato(): # Chiede all'utente all'avvio se vuole lavorare con file .csv o .txt
    sep("GESTIONALE MAGAZZINO & VENDITE")
    print("\n  Scegli il formato file:")
    print("  1. CSV  (separatore virgola)")
    print("  2. TXT  (separatore pipe |)")
    while True:
        s = input("\n  → Scelta (1/2): ").strip()
        if s == "1": return "csv"
        if s == "2": return "txt"
        print("  ✗ Scelta non valida.")


# Visualizzazione 

def mostra_prodotti(percorso, formato):
    prodotti = crea_file.leggi_prodotti(percorso, formato)
    if not prodotti:
        print("  Nessun prodotto presente.")
    else:
        for p in prodotti:
            print(f"  {p}")
    return prodotti


def mostra_vendite(percorso, formato):
    vendite = crea_file.leggi_vendite(percorso, formato)
    if not vendite:
        print("  Nessuna vendita registrata.")
    else:
        for v in vendite:
            print(f"  {v}")
    return vendite


# Menu Prodotti 

def menu_prodotti(pp, pv, fmt): # Gestisce tutte le operazioni relative ai prodotti
    while True:
        sep("PRODOTTI")
        print("  1. Visualizza tutti i prodotti")
        print("  2. Aggiungi prodotto")
        print("  3. Modifica prodotto")
        print("  4. Elimina prodotto")
        print("  0. Torna al menu principale")
        sep()
        s = input_scelta(["1", "2", "3", "4", "0"])

        if s == "1":
            sep("ELENCO PRODOTTI")
            mostra_prodotti(pp, fmt)
            pausa()

        elif s == "2":
            sep("AGGIUNGI PRODOTTO")
            nome      = input("  Nome: ").strip()
            categoria = input("  Categoria: ").strip()
            prezzo    = input_float("  Prezzo (€): ")
            quantita  = input_int("  Quantità: ")
            nuovo = aggiungi_file.aggiungi_prodotto(pp, fmt, nome, categoria, prezzo, quantita)
            print(f"\n  ✓ Prodotto aggiunto: {nuovo}")
            pausa()

        elif s == "3":
            sep("MODIFICA PRODOTTO")
            mostra_prodotti(pp, fmt)
            id_p = input("\n  ID prodotto da modificare: ").strip()
            print("  (Lascia vuoto per non modificare il campo)\n")
            nome      = input("  Nuovo nome: ").strip() or None
            categoria = input("  Nuova categoria: ").strip() or None
            pr_str    = input("  Nuovo prezzo: ").strip()
            qt_str    = input("  Nuova quantità: ").strip()
            prezzo    = float(pr_str.replace(",", ".")) if pr_str else None
            quantita  = int(qt_str) if qt_str else None
            ok = modifica_file.modifica_prodotto(pp, fmt, id_p, nome, categoria, prezzo, quantita)
            print("  ✓ Prodotto aggiornato." if ok else "  ✗ ID non trovato.")
            pausa()

        elif s == "4":
            sep("ELIMINA PRODOTTO")
            mostra_prodotti(pp, fmt)
            id_p = input("\n  ID prodotto da eliminare: ").strip()
            prodotti = crea_file.leggi_prodotti(pp, fmt)
            prodotto = next((p for p in prodotti if p.id == id_p), None)
            if not prodotto:
                print("  ✗ Prodotto non trovato.")
            else:
                conf = input(f"\n  Eliminare '{prodotto.nome}'? (s/n): ").strip().lower()
                if conf == "s":
                    modifica_file.elimina_prodotto(pp, fmt, id_p)
                    print("  ✓ Prodotto eliminato.")
                else:
                    print("  Operazione annullata.")
            pausa()

        elif s == "0":
            break


# Menu Vendite 
def menu_vendite(pp, pv, fmt):
    while True:
        sep("VENDITE")
        print("  1. Visualizza tutte le vendite")
        print("  2. Registra nuova vendita")
        print("  3. Elimina vendita")
        print("  0. Torna al menu principale")
        sep()
        s = input_scelta(["1", "2", "3", "0"])

        if s == "1":
            sep("ELENCO VENDITE")
            mostra_vendite(pv, fmt)
            pausa()

        elif s == "2":
            sep("REGISTRA VENDITA")
            prodotti = mostra_prodotti(pp, fmt)
            if not prodotti:
                pausa()
                continue
            id_p = input("\n  ID prodotto: ").strip()
            qtà  = input_int("  Quantità da vendere: ")
            vendita, errore = aggiungi_file.aggiungi_vendita(pv, pp, fmt, id_p, qtà)
            if errore:
                print(f"\n  ✗ {errore}")
            else:
                print(f"\n  ✓ Vendita registrata: {vendita}")
            pausa()

        elif s == "3":
            sep("ELIMINA VENDITA")
            mostra_vendite(pv, fmt)
            id_v = input("\n  ID vendita da eliminare: ").strip()
            vendite = crea_file.leggi_vendite(pv, fmt)
            vendita = next((v for v in vendite if v.id == id_v), None)
            if not vendita:
                print("  ✗ Vendita non trovata.")
            else:
                conf = input(f"\n  Eliminare la vendita [{vendita.id}]? (s/n): ").strip().lower()
                if conf == "s":
                    modifica_file.elimina_vendita(pv, pp, fmt, id_v)
                    print("  ✓ Vendita eliminata. Scorte ripristinate.")
                else:
                    print("  Operazione annullata.")
            pausa()

        elif s == "0":
            break


# Menu Analisi

def menu_analisi(pp, pv, fmt):
    while True:
        sep("ANALISI DATI")
        print("  1. Analisi Prodotti / Magazzino")
        print("  2. Analisi Vendite / Fatturato")
        print("  0. Torna al menu principale")
        sep()
        s = input_scelta(["1", "2", "0"])

        if s == "1":
            sep("ANALISI MAGAZZINO")
            dati = analisi_file.analisi_prodotti(pp, fmt)
            if not dati:
                print("  Nessun dato disponibile.")
            else:
                print(f"  Totale prodotti:    {dati['totale_prodotti']}")
                print(f"  Scorte totali:      {dati['scorte_totali']} unità")
                print(f"  Valore magazzino:   €{dati['valore_magazzino']:.2f}")
                print(f"  Prezzo medio:       €{dati['prezzo_medio']:.2f}")
                print(f"  Prezzo massimo:     €{dati['prezzo_max']:.2f}")
                print(f"  Prezzo minimo:      €{dati['prezzo_min']:.2f}")
                print(f"\n  Prodotti per categoria:")
                for cat, n in dati["prodotti_per_categoria"].items():
                    print(f"    - {cat}: {n}")
                if dati["prodotti_esauriti"]:
                    print(f"\n  ⚠ Prodotti esauriti:")
                    for p in dati["prodotti_esauriti"]:
                        print(f"    - {p.nome}")
            pausa()

        elif s == "2":
            sep("ANALISI VENDITE")
            dati = analisi_file.analisi_vendite(pv, fmt)
            if not dati:
                print("  Nessuna vendita registrata.")
            else:
                print(f"  Totale transazioni: {dati['totale_vendite']}")
                print(f"  Fatturato totale:   €{dati['fatturato_totale']:.2f}")
                print(f"  Fatturato medio:    €{dati['fatturato_medio']:.2f}")
                print(f"  Prodotto top:       {dati['prodotto_top']}")
                print(f"\n  Dettaglio per prodotto:")
                for nome, info in dati["vendite_per_prodotto"].items():
                    print(f"    - {nome}: {info['quantita']} pz | €{info['fatturato']:.2f}")
            pausa()

        elif s == "0":
            break


# Menu Esporta 
def menu_esporta(pp, pv, fmt):
    sep("ESPORTA FILE")
    print(f"  Formato attivo: {fmt.upper()}")
    print()
    print("  Scegli il formato di destinazione:")
    print("  1. CSV")
    print("  2. TXT")
    sep()
    scelta_fmt = input_scelta(["1", "2"])
    fmt_dest = "csv" if scelta_fmt == "1" else "txt"

    if fmt_dest == fmt:
        print(f"\n  (Stai esportando una copia nello stesso formato: {fmt.upper()})")

    sep()
    print("  Cosa vuoi esportare?")
    print("  1. Prodotti")
    print("  2. Vendite")
    print("  3. Entrambi")
    print("  0. Annulla")
    sep()
    s = input_scelta(["1", "2", "3", "0"])

    if s in ["1", "3"]:
        dest = esporta_file.percorso_esportazione(pp, fmt_dest, CARTELLA_DATA)
        ok   = esporta_file.esporta_prodotti(pp, fmt, dest, fmt_dest)
        print(f"  {'✓ Prodotti esportati: ' + dest if ok else '✗ Nessun prodotto da esportare.'}")

    if s in ["2", "3"]:
        dest = esporta_file.percorso_esportazione(pv, fmt_dest, CARTELLA_DATA)
        ok   = esporta_file.esporta_vendite(pv, fmt, dest, fmt_dest)
        print(f"  {'✓ Vendite esportate: ' + dest if ok else '✗ Nessuna vendita da esportare.'}")

    pausa()


# Main 
#Punto di avvio del programma: inizializza le cartelle e avvia il loop principale."""
    
def main():
    os.makedirs(CARTELLA_DATA, exist_ok=True) # Crea la cartella 'data' se non esiste
    fmt = scegli_formato() # Configura il formato di lavoro per questa sessione

    pp = os.path.join(CARTELLA_DATA, f"prodotti.{fmt}") # Costruisce i percorsi ai file prodotti e vendite
    pv = os.path.join(CARTELLA_DATA, f"vendite.{fmt}")

    crea_file.crea_file_prodotti(pp, fmt) # Crea i file (con intestazioni) se è la prima volta che si avvia il programma
    crea_file.crea_file_vendite(pv, fmt)

    while True:
        sep("GESTIONALE MAGAZZINO & VENDITE")
        print("  1. Prodotti")
        print("  2. Vendite")
        print("  3. Analisi Dati")
        print("  4. Esporta File")
        print("  0. Esci")
        sep()
        s = input_scelta(["1", "2", "3", "4", "0"])

        if   s == "1": menu_prodotti(pp, pv, fmt)
        elif s == "2": menu_vendite(pp, pv, fmt)
        elif s == "3": menu_analisi(pp, pv, fmt)
        elif s == "4": menu_esporta(pp, pv, fmt)
        elif s == "0":
            print("\n  Arrivederci!\n")
            break


if __name__ == "__main__":
    main()
