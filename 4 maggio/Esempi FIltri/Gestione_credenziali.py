# gestione creenziali: registrazione e login


def registrazione(): # Questa funzione permette all'utente di registrarsi inserendo un username e una password. I dati vengono salvati su un file di testo chiamato "credenziali.txt". Se il file non esiste, viene creato automaticamente. Ogni volta che un nuovo utente si registra, le sue credenziali vengono aggiunte alla fine del file, separate da una virgola e seguite da una nuova riga.
    print("\n--- REGISTRAZIONE ---")
    nome = input("Username: ")
    pwd = input("Password: ")
    
    # Scrittura su file in modalità append (a) per aggiungere nuove credenziali senza sovrascrivere quelle esistenti
    file = open("credenziali.txt", "a")
    file.write(f"{nome},{pwd}\n")
    file.close()
    print("Utente registrato con successo.")

def login():
    print("\n--- LOGIN ---")
    u_in = input("Username: ")
    p_in = input("Password: ")
    
    try:
        file = open("credenziali.txt", "r")
        # Leggiamo tutte le righe
        righe = file.readlines()
        file.close()
        
        # Cerchiamo l'utente tra le righe
        for riga in righe:
            nome, pwd = riga.strip().split(",") # Separiamo il nome e la password usando la virgola come delimitatore
            if nome == u_in and pwd == p_in:
                return True
    except FileNotFoundError:
        print("Errore: Nessun database utenti trovato. Registrati.")
    
    return False

