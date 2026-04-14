#ESERCIZIO 1
numero = int(input("Inserisci un numero: ")) # inserimento imput numerico
if numero > 10:
    print("maggiore di 10") #se il numero maggiore di 10, stampa "maggiore di 10"
    if numero > 100:
        print("centinaia") # se il numero è maggiore di 100, stampa "centinaia"
        if numero == 1000:
            print("migliaia") # se il numero è uguale a 1000, stampa "migliaia"

#ESERCIZIO 1 bis
parola = input("Inserisci una parola: ")
if len(parola) > 10:
    print(" Very Long") # se la parola ha più di 10 caratteri, stampa " Very Long"
elif len(parola) < 4:
    print("Short") # se la parola ha meno di 4 caratteri, stampa "Short"
elif len(parola) > 8:
    print("Long") # se la parola ha più di 8 caratteri, stampa "Long"
else:
    print("Medium") # se la parola ha tra 4 e 8 caratteri, stampa "Medium"

#ESERCIZIO 2
# Lista che funge da "database" in memoria, pre-popolata con 5 paesi
elementi = ["Germania", "Francia", "Spagna", "Inghilterra", "Italia"]

# Mostriamo il menu all'utente
print("=== MENU ===")
print("1 - Aggiungi")
print("2 - Rimuovi")
print("3 - Elimina tutto")

# Leggiamo la scelta dell'utente (input restituisce sempre una stringa)
scelta = input("Inserisci la tua scelta: ")

# Controlliamo se l'utente ha scelto "1" → Aggiungi
if scelta == "1":
    # Chiediamo quale paese aggiungere e lo inseriamo in fondo alla lista
    nuovo = input("Paese da aggiungere: ")
    elementi.append(nuovo)
    print(f"'{nuovo}' aggiunto!")

# Se non era "1", controlliamo "2" → Rimuovi paese specifico
elif scelta == "2":
    da_rimuovere = input("Paese da rimuovere: ")
    # Verifichiamo che il paese esista prima di tentare la rimozione
    if da_rimuovere in elementi:
        elementi.remove(da_rimuovere)  # rimuove la prima occorrenza trovata
        print(f"'{da_rimuovere}' rimosso!")
    else:
        print("Paese non trovato.")

# Se non era né "1" né "2", controlliamo "3" → Svuota tutta la lista
elif scelta == "3":
    elementi.clear()  # elimina tutti i paesi in una sola operazione
    print("Lista svuotata.")

# Nessuna delle condizioni sopra era vera → input non riconosciuto
else:
    print("Scelta non valida.")

#esercizio 3





    



