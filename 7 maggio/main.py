

from models import *
from crud import crea_capo, modifica_capo, elimina_capo
from generatore import genera_dati, vendite, _genera_capi_casuali, _genera_componenti_casuali
from analytics import analizza_tutti, analizza_per_tipo, analizza_per_tipo_e_personalizzazione
from export import esporta_csv

# liste di capi e componenti
lista_capi       = []  
lista_componenti = [] 

def menu_analisi():
     # Sottomenu dedicato alle analisi, richiamato dal menu principale. 
    print("\n--- ANALISI ---")
    print("1. Analizza tutti i capi")
    print("2. Analizza solo per tipo di capo")
    print("3. Analizza per tipo e personalizzazione")
    print("0. Torna indietro")

    scelta = input("\nScelta: ").strip()

    if scelta == "1":
        analizza_tutti(lista_capi)
    elif scelta == "2":
        analizza_per_tipo(lista_capi)
    elif scelta == "3":
        analizza_per_tipo_e_personalizzazione(lista_capi)
    elif scelta == "0":
        return
    else:
        print("Scelta non valida.")

def menu():
    """Funzione principale: gestisce il loop del menu."""

    # genera le vendite iniziali a partire dalle liste già popolate
    genera_dati(lista_capi, lista_componenti)
    print("Dati iniziali generati automaticamente.")

    while True:
        print("\n===== SARTORIA ELEGANTE =====")
        print("1. Crea capo")
        print("2. Modifica capo")
        print("3. Elimina capo")
        print("4. Genera nuovi dati")
        print("5. Analisi")
        print("6. Esporta CSV")
        print("0. Esci")

        scelta = input("\nScelta: ").strip()

        if scelta == "1":
            crea_capo(lista_capi, lista_componenti)
        elif scelta == "2":
            modifica_capo(lista_capi, lista_componenti)
        elif scelta == "3":
            elimina_capo(lista_capi, lista_componenti)
        elif scelta == "4":
            genera_dati(lista_capi, lista_componenti)
        elif scelta == "5":
            menu_analisi()
        elif scelta == "6":
            esporta_csv(lista_capi, lista_componenti, vendite)
        elif scelta == "0":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    menu()