#esercizio RECAP
import random
from unittest import case
     
# Funzioni

def inserisci_numero_positivo(): # Chiede all'utente di inserire un numero positivo. Se l'utente inserisce un numero negativo o zero, il programma dovrebbe continuare a chiedere finché non viene inserito un numero positivo. Una volta inserito un numero positivo, la funzione restituisce quel numero.
                while True:
                    numero = int(input("Inserisci un numero positivo: "))
                    if numero > 0:
                        return numero # Se l'utente inserisce un numero positivo, la funzione restituisce quel numero e termina. Altrimenti, stampa un messaggio di errore e continua a chiedere.
                    else:
                        print("Il numero inserito non è positivo. Riprova.")


def lista_numeri(n): # Chiede all'utente di inserire un numero n e genera una lista di n numeri casuali compresi tra 1 e n, restituendo la lista generata.
    lista = []
    for i in range(n):
        numero = random.randint(1, n) # Genera un numero casuale tra 1 e n usando la funzione random.randint. Aggiunge il numero generato alla lista usando lista.append(numero). Dopo aver generato n numeri, restituisce la lista completa.
        lista.append(numero)
    return lista # Restituisce la lista generata dopo aver aggiunto n numeri casuali.


def somma_pari_da_lista(lista): # Prende la lista dalla funzione precedente, controlla quali numeri nella lista sono pari e calcola la somma di questi numeri, stampando il risultato.
    somma = 0

    for numero in lista: # Itera su ogni numero nella lista e controlla se è pari usando l'operatore modulo (%). Se il numero è pari (cioè se numero % 2 == 0), aggiunge quel numero alla variabile somma. Dopo aver iterato su tutti i numeri nella lista, stampa la somma totale dei numeri pari.
        if numero % 2 == 0:
            somma += numero # Aggiunge il numero alla somma totale se è pari. Alla fine del ciclo, stampa la somma totale dei numeri pari nella lista.

    print("La somma dei numeri pari è:", somma)


def stampa_numeri_dispari_da_lista(lista): # Prende la lista dalla funzione precedente, controlla quali numeri nella lista sono dispari e li stampa.
    print("I numeri dispari nella lista sono:")
    for numero in lista:
        if numero % 2 != 0: # Itera su ogni numero nella lista e controlla se è dispari usando l'operatore modulo (%). Se il numero è dispari (cioè se numero % 2 != 0), stampa quel numero. Alla fine del ciclo, avrai stampato tutti i numeri dispari presenti nella lista.
            print(numero)
              

def determinazione_numero_primo(): # Chiede all'utente di inserire un numero e determina se è primo o no, stampando il risultato.
    numero = int(input("Inserisci un numero: "))
    if numero > 1:
        è_primo = True
        for divisore in range(2, numero):
            if numero % divisore == 0: # Se il numero è divisibile per un qualsiasi numero tra 2 e numero-1, allora non è primo.
                è_primo = False
                break
        if è_primo:
            print(f"Il numero {numero} è primo")
        else:
            print(f"Il numero {numero} non è primo")
    else:
        print(f"Il numero {numero} non è primo")

    
def stampa_numeri_primi_da_lista(lista): # Prende la lista dalla funzione precedente, controlla quali numeri nella lista sono primi e li stampa. Inoltre, salva i numeri primi trovati in una nuova lista e la restituisce alla fine.
    lista = lista_numeri(n)  # prendi la lista dalla funzione precedente
    primi =[]
    print("I numeri primi nella lista sono:")
    for numero in lista:
        if numero > 1:
            è_primo = True
            for divisore in range(2, numero): # Se il numero è divisibile per un qualsiasi numero tra 2 e numero-1, allora non è primo.
                if numero % divisore == 0:
                    è_primo = False
                    break
            if è_primo:
                print(numero)
                primi.append(numero)  # salva il primo nella lista
    return primi  # restituisce la lista dei primi
    
    
def somma_nprimi_lista_è_nprimo(primi): # Prende la lista dei primi trovati nella funzione precedente, calcola la somma di questi primi e determina se la somma è un numero primo o no, stampando il risultato.
    somma = sum(primi) # calcola la somma dei primi nella lista
    print("La somma dei numeri nella lista è:", somma)
    if somma > 1: # un numero è primo solo se è maggiore di 1
        è_primo = True
        for divisore in range(2, somma): # Se la somma è divisibile per un qualsiasi numero tra 2 e somma-1, allora non è primo.
            if somma % divisore == 0:
                è_primo = False
                break
        if è_primo:
            print(f"La somma {somma} è un numero primo") # Se la somma è un numero primo, stampa "La somma {somma} è un numero primo". Altrimenti, stampa "La somma {somma} non è un numero primo".
        else:
            print(f"La somma {somma} non è un numero primo") # Se la somma è un numero primo, stampa "La somma {somma} è un numero primo". Altrimenti, stampa "La somma {somma} non è un numero primo".
    else:
        print(f"La somma {somma} non è un numero primo")
          
        
while True:
    print("=== MENU ===") # Stampa un menu con 7 opzioni: 1 - esercizio 1, 2 - esercizio 2, 3 - esercizio 3, 4 - esercizio 4, 5 - esercizio 5, 6 - esercizio 6, 7 - esercizio 7. Chiedi all'utente di inserire la sua scelta e poi esegui l'esercizio corrispondente a quella scelta. Se la scelta è "0", esci dal programma. Se la scelta non è valida, stampa "Scelta non valida".
    print("1 - esercizio 1")
    print("2 - esercizio 2")
    print("3 - esercizio 3")
    print("4 - esercizio 4")
    print("5 - esercizio 5")
    print("6 - esercizio 6")
    print("7 - esercizio 7")
    print("0 - Esci")

    scelta = input("Inserisci la tua scelta: ")

    match scelta:
        case "1":
            risultato = inserisci_numero_positivo() # Chiede all'utente di inserire un numero positivo. Se l'utente inserisce un numero negativo o zero, il programma dovrebbe continuare a chiedere finché non viene inserito un numero positivo. Una volta inserito un numero positivo, la funzione restituisce quel numero.
            print(f"Numero inserito: {risultato}")

        case "2":
            n = int(input("Inserisci un numero: ")) # Chiede all'utente di inserire un numero n e genera una lista di n numeri casuali compresi tra 1 e n, restituendo la lista generata.
            lista = lista_numeri(n)
            print(f"Lista generata: {lista}")

        case "3":
            n = int(input("Inserisci un numero: ")) # Chiede all'utente di inserire un numero n e genera una lista di n numeri casuali compresi tra 1 e n, restituendo la lista generata. Poi, prende la lista generata e calcola la somma dei numeri pari presenti nella lista, stampando il risultato.
            lista = lista_numeri(n)
            somma_pari_da_lista(lista)

        case "4":
            n = int(input("Inserisci un numero: ")) #  Chiede all'utente di inserire un numero n e genera una lista di n numeri casuali compresi tra 1 e n, restituendo la lista generata. Poi, prende la lista generata e stampa i numeri dispari presenti nella lista.
            lista = lista_numeri(n)
            stampa_numeri_dispari_da_lista(lista)

        case "5":
            determinazione_numero_primo() # Chiede all'utente di inserire un numero e determina se è primo o no, stampando il risultato.

        case "6":
            n = int(input("Inserisci un numero: ")) # Chiede all'utente di inserire un numero n e genera una lista di n numeri casuali compresi tra 1 e n, restituendo la lista generata. Poi, prende la lista generata e stampa i numeri primi presenti nella lista. Inoltre, salva i numeri primi trovati in una nuova lista e la restituisce alla fine.
            lista = lista_numeri(n)
            stampa_numeri_primi_da_lista(lista)

        case "7":
            n = int(input("Inserisci un numero: ")) # Chiede all'utente di inserire un numero n e genera una lista di n numeri casuali compresi tra 1 e n, restituendo la lista generata. Poi, prende la lista generata e stampa i numeri primi presenti nella lista. Inoltre, salva i numeri primi trovati in una nuova lista e la restituisce alla fine. Infine, prende la lista dei primi trovati, calcola la somma di questi primi e determina se la somma è un numero primo o no, stampando il risultato.
            lista = lista_numeri(n)
            primi = stampa_numeri_primi_da_lista(lista)
            somma_nprimi_lista_è_nprimo(primi)
         
        case "0": # Se l'utente sceglie 0, esce dal programma. # Se la scelta non è valida, stampa "Scelta non valida".
            print("Uscita dal programma. Arrivederci!")                  
                       
        