#esercizio 1 funzione
#Esercizio Base: Indovina il numero
#Descrizione: Scrivi un programma che genera un numero casuale tra 1 e 100 (inclusi). L'utente deve indovinare quale numero è stato generato. Dopo ogni tentativo, il programma dovrebbe ire all'utente se il numero da indovinare è più alto o più basso rispetto al numero inserito. Il gioco termina quando l'utente indovina il numero o decide di uscire.


import random

def genera_numero_casuale(): # Questa funzione genera un numero casuale tra 1 e 100 utilizzando la funzione randint del modulo random.
    return random.randint(1, 100) # Restituisce il numero casuale generato.
numero_da_indovinare = genera_numero_casuale() # Genera un numero casuale da indovinare e lo assegna alla variabile numero_da_indovinare.
tentativi = 0 # Inizializza un contatore di tentativi a 0. Ogni volta che l'utente fa un tentativo, questo contatore verrà incrementato di 1.

def indovina_il_numero(): # Questa funzione contiene la logica del gioco Indovina il numero. Gestisce l'interazione con l'utente, confronta i numeri inseriti con il numero da indovinare e fornisce feedback all'utente.
       
    print("Benvenuto al gioco Indovina il numero!")
    
while True: # Inizia un ciclo infinito che continuerà fino a quando l'utente indovina il numero o decide di uscire.
        tentativi += 1 # Incrementa il contatore dei tentativi di 1 ogni volta che l'utente fa un tentativo.
        numero_utente = int(input("Inserisci un numero tra 1 e 100: ")) # Chiede all'utente di inserire un numero tra 1 e 100 e lo converte in un intero, assegnandolo alla variabile numero_utente.

        if numero_utente == 0: # Se l'utente inserisce 0, il gioco termina e viene stampato un messaggio che mostra il numero da indovinare.
            print("Hai deciso di uscire. Il numero era:", numero_da_indovinare)
            break
        elif numero_utente < numero_da_indovinare: # Se il numero inserito dall'utente è inferiore al numero da indovinare, viene stampato un messaggio che indica che il numero da indovinare è più alto.
            print("Il numero da indovinare è più alto.")
        elif numero_utente > numero_da_indovinare:# Se il numero inserito dall'utente è superiore al numero da indovinare, viene stampato un messaggio che indica che il numero da indovinare è più basso.
            print("Il numero da indovinare è più basso.")
        else:
            print(f"Hai indovinato {numero_da_indovinare} in {tentativi} tentativi!") # Se l'utente indovina il numero, viene stampato un messaggio di congratulazioni che include il numero indovinato e il numero di tentativi impiegati. Il gioco termina con un break.
            break
indovina_il_numero() # Chiamata alla funzione indovina_il_numero per avviare il gioco.


            