

        # === DATABASE IN MEMORIA ===
utenti = []       # lista vuota: conterrà tuple (id, nome, password)
prossimo_id = 1   # primo ID da assegnare; si incrementa dopo ogni registrazione

def registra_utente(nome, password):
    global prossimo_id   # senza "global" Python creerebbe una variabile locale
                         # e non modificherebbe quella esterna

    if not nome or not password:   # stringa vuota "" è falsa in Python
        print("Errore: nome e password non possono essere vuoti.")
        return   # esce subito dalla funzione, non esegue il resto

    if any(u[1] == nome for u in utenti):
        # any() scorre le tuple una per una
        # u[1] è il nome (indice 1 della tupla)
        # si ferma e restituisce True appena trova una corrispondenza
        # se la lista è vuota restituisce False direttamente
        print("Errore: nome già in uso. Scegli un altro nome.")
        return

    utenti.append((prossimo_id, nome, password))   # aggiunge la tupla in fondo alla lista
    print(f"Account creato con successo! Il tuo ID è: {prossimo_id}")
    prossimo_id += 1   # incrementa DOPO aver usato il valore corrente

def login_utente(nome, password):
    for u in utenti:                           # scorre ogni tupla della lista
        if u[1] == nome and u[2] == password:  # u[1]=nome, u[2]=password
            return u                           # restituisce la tupla intera se trovata
    return None                                # se il for finisce senza trovare nulla

def esegui_operazione(scelta):
    try:
        a = float(input("Primo numero:  "))    # float accetta sia interi che decimali
        b = float(input("Secondo numero: "))
    except ValueError:
        # scatta se l'utente scrive qualcosa che non è convertibile in numero
        # es. "ciao", "tre", stringa vuota
        print("Errore: inserisci valori numerici validi.")
        return None   # None segnala al chiamante che l'operazione non è riuscita

    if scelta == "1":
        return ("+", a, b, a + b)    # restituisce una tupla con simbolo, operandi, risultato
    elif scelta == "2":
        return ("-", a, b, a - b)
    elif scelta == "3":
        return ("*", a, b, a * b)
    elif scelta == "4":
        if b == 0:
            print("Errore: divisione per zero non consentita.")
            return None              # caso speciale: b==0 renderebbe il calcolo impossibile
        return ("/", a, b, a / b)
    elif scelta == "5":
        return ("**", a, b, a ** b)  # operatore potenza di Python

def stampa_risultati(storico):
    if not storico:           # lista vuota è falsa: evita di stampare un'intestazione inutile
        print("Nessuna operazione eseguita.")
        return

    print("\n=== STORICO OPERAZIONI ===")
    for i, op in enumerate(storico, 1):
        # enumerate restituisce coppie (indice, elemento)
        # il secondo argomento "1" fa partire il conteggio da 1 invece che da 0
        # op è la tupla (simbolo, a, b, risultato)
        # op[0]=simbolo  op[1]=a  op[2]=b  op[3]=risultato
        print(f"{i}. {op[1]} {op[0]} {op[2]} = {op[3]}")

def mostra_menu_accesso():
    print("\n=== MENU PRINCIPALE ===")
    print("1 - Registrati")
    print("2 - Accedi")
    print("0 - Esci")
    return input("Inserisci la tua scelta: ").strip()
    # strip() rimuove spazi accidentali: " 1 " diventa "1"
    # il valore viene restituito direttamente al chiamante

def mostra_menu_calcolatrice(nome_utente, operazioni_rimaste):
    print(f"\n=== CALCOLATRICE ({nome_utente}) ===")
    print(f"Operazioni rimanenti: {operazioni_rimaste}")
    # mostra quante operazioni restano prima del logout forzato
    print("1 - Addizione       (+)")
    print("2 - Sottrazione     (-)")
    print("3 - Moltiplicazione (*)")
    print("4 - Divisione       (/)")
    print("5 - Potenza         (**)")
    print("6 - Stampa storico")
    print("0 - Logout")
    return input("Inserisci la tua scelta: ").strip()

#---------- LOOP PRINCIPALE ----------
while True:   # gira all'infinito: si interrompe solo con break
    scelta = mostra_menu_accesso()

    if scelta == "1":
        nome = input("Nome utente: ").strip()
        password = input("Password: ")         # no strip() sulla password: gli spazi
        registra_utente(nome, password)        # potrebbero essere intenzionali

    elif scelta == "2":
        nome = input("Nome utente: ").strip()
        password = input("Password: ")
        utente_loggato = login_utente(nome, password)  # None oppure tupla

        if utente_loggato is None:
            print("Credenziali errate. Accesso negato.")
        else:
            print(f"\nBenvenuto, {utente_loggato[1]}! (ID: {utente_loggato[0]})")

            # --- LOOP CALCOLATRICE ---
            storico = []        # lista vuota: si azzera ad ogni nuovo login
            MAX_OPERAZIONI = 4  # costante: limite operazioni per sessione
            contatore = 0       # tiene traccia delle operazioni valide eseguite

            while contatore < MAX_OPERAZIONI:
                rimanenti = MAX_OPERAZIONI - contatore   # calcolato ad ogni iterazione
                scelta_calc = mostra_menu_calcolatrice(utente_loggato[1], rimanenti)

                if scelta_calc in ("1", "2", "3", "4", "5"):
                    risultato = esegui_operazione(scelta_calc)

                    if risultato is not None:   # None = errore di input, non conta
                        storico.append(risultato)
                        contatore += 1          # incrementa solo se l'operazione è valida
                        print(f"Risultato: {risultato[1]} {risultato[0]} {risultato[2]} = {risultato[3]}")

                        mostra = input("Vuoi vedere lo storico? (s/n): ").strip().lower()
                        # lower() normalizza: "S" e "s" vengono trattati allo stesso modo
                        if mostra == "s":
                            stampa_risultati(storico)

                elif scelta_calc == "6":
                    stampa_risultati(storico)   # consultabile in qualsiasi momento

                elif scelta_calc == "0":
                    print(f"Logout effettuato. Arrivederci, {utente_loggato[1]}!")
                    break   # esce dal while interno, torna al menu principale

                else:
                    print("Scelta non valida. Riprova.")

            else:
                # il blocco else di un while scatta SOLO se il loop termina
                # per condizione falsa (contatore == MAX_OPERAZIONI)
                # NON scatta se il loop è uscito con break (logout manuale)
                print(f"\nHai esaurito le {MAX_OPERAZIONI} operazioni disponibili.") # avvisa l'utente che ha raggiunto il limite
                stampa_risultati(storico)
                print("Verrai reindirizzato al menu principale per rientrare.")

    elif scelta == "0":
        print("Uscita dal programma.")
        break   # esce dal while esterno, termina il programma

    else:
        print("Scelta non valida. Riprova.")