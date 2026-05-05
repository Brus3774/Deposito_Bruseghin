# main

from Gestione_clienti import GestioneClienti
from Gestione_inventario import GestioneInventario
from Amministrazione import Amministrazione


from Gestione_clienti import GestioneClienti
from Gestione_inventario import GestioneInventario
from Amministrazione import Amministrazione

def main(): # Punto di ingresso del programma, gestisce il menu principale e le interazioni con l'utente.
    g_clienti = GestioneClienti()
    g_inventario = GestioneInventario()
    admin_panel = Amministrazione(g_clienti, g_inventario)

    while True:
        print("\n  SISTEMA NEGOZIO - MENU PRINCIPALE ")
        print("1. Area Cliente")
        print("2. Area Amministrazione")
        print("3. Esci")
        
        scelta = input("Seleziona area: ")

        if scelta == "1":
            menu_cliente(g_clienti, g_inventario)
        elif scelta == "2":
            # Usiamo .strip() per eliminare spazi accidentali battuti sulla tastiera
            user = input("Username: ").strip()
            pwd = input("Password: ").strip()
            
            if admin_panel.login(user, pwd):
                # Se il login è True, passiamo al menu admin
                menu_admin(admin_panel, g_inventario)
            else:
                # Opzionale: un messaggio di errore se fallisce
                print("Sistema: Credenziali non valide per l'area amministrativa.") 
        elif scelta == "3":
            print("Chiusura sistema...")
            break

def menu_cliente(gc, gi):
    while True:
        print("\n--- MENU CLIENTE ---")
        print("1. Registrazione")
        print("2. Acquisto")
        print("3. Indietro")
        scelta = input("Scelta: ")

        if scelta == "1":
            n = input("Nome: ")
            c = input("Cognome: ")
            e = input("Email: ")
            gc.aggiungi_cliente(n, c, e)
        
        elif scelta == "2":
            email = input("Email per procedere: ")
            cliente = gc.seleziona_cliente(email)
            if cliente:
                gi.visualizza_inventario()
                nome_art = input("Nome articolo da comprare: ")
                # Usiamo il metodo dedicato che abbiamo creato nell'inventario
                articolo_venduto = gi.vendi_articolo(nome_art)
                if articolo_venduto:
                 cliente.acquisti.append(articolo_venduto)
                 cliente.genera_ricevuta() # <-- Questa riga crea/aggiorna il file del cliente
                 print(f"Acquisto di {nome_art} effettuato!")
        
        elif scelta == "3":
            break

def menu_admin(ap, gi):
    while True:
        print("\n--- MENU AMMINISTRAZIONE ---")
        print("1. Aggiungi/Aggiorna Articolo")
        print("2. Rimuovi Articolo")
        print("3. Report Vendite (Video)")
        print("4. Stampa Mega Report (.txt)")
        print("5. Indietro")
        scelta = input("Scelta: ")

        if scelta == "1":
            try:
                n = input("Nome Articolo: ")
                p = float(input("Prezzo: "))
                q = int(input("Quantità da aggiungere: "))
                gi.aggiungi_o_aggiorna_articolo(n, p, q)
            except ValueError:
                print("Errore: Inserire valori numerici per prezzo e quantità.")
        
        elif scelta == "2":
            n = input("Nome Articolo da rimuovere: ")
            gi.rimuovi_articolo(n)
            
        elif scelta == "3":
            ap.visualizza_rapporto_vendite()
            
        elif scelta == "4":
            
            ap.stampa_report()
            
        elif scelta == "5":
            break

if __name__ == "__main__":
    main()