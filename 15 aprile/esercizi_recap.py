
#esercizio completo


print("=== MENU ===") # Stampa un menu con 4 opzioni: 1 - utilizzo di if, 2 - utilizzo di range, 3 - utilizzo di for, 4 - utilizzo di if, for e while insieme. Chiedi all'utente di inserire la sua scelta e poi esegui l'esercizio corrispondente a quella scelta. Se la scelta non è valida, stampa "Scelta non valida".
print("1 - utilizzo di if")
print("2 - utilizzo di range")
print("3 - utilizzo di for")
print("4 - utilizzo di if,for e while insieme")
scelta = input("Inserisci la tua scelta: ")

match scelta: 
    case "1": #esempio di uso di if
     numero = int(input("Inserisci un numero: "))
     if numero % 2 == 0:
        print("Il numero è pari")
     else:
        print("Il numero è dispari")
        
    case "2": # esempio di uso di range
     while True:
        n = int(input("Inserisci un numero intero positivo: "))   
        for i in range(n, -1, -1): # Stampa i numeri da n a 0 in ordine decrescente usando un ciclo for e la funzione range.
            print(i)
 
    case "3": # esempio di uso di for
        elementi_numerici = []
        n = int(input("Quanti numeri vuoi inserire? "))
        for i in range(n):
            numero = int(input(f"Inserisci il numero {i + 1}: ")) # Chiede all'utente di inserire n numeri e li salva in una lista chiamata elementi_numerici. Poi, usa un ciclo for per stampare il quadrato di ogni numero nella lista.
            elementi_numerici.append(numero) # Aggiunge il numero inserito alla lista elementi_numerici.
        for numero in elementi_numerici: # Itera su ogni numero nella lista elementi_numerici e stampa il suo quadrato.
            print(f"{numero}² = {numero ** 2}") # Stampa il numero e il suo quadrato in formato "numero² = quadrato".
     
    case "4": # esempio di uso di if, for e while insieme
        lista_numeri_interi = []
        n = int(input("Quanti numeri vuoi inserire? "))
        for i in range(n):
            numero = int(input(f"Inserisci il numero {i + 1}: "))
            lista_numeri_interi.append(numero)

        if not lista_numeri_interi:
            print("La lista è vuota: ")
            
        else:
            # Usa for per trovare il numero massimo
            massimo = lista_numeri_interi[0]
            for numero in lista_numeri_interi:
                if numero > massimo:
                    massimo = numero

            # Usa while per contare gli elementi
            contatore = 0
            indice = 0
            while indice < len(lista_numeri_interi):
                contatore += 1
                indice += 1

            print(f"Numero massimo: {massimo}")
            print(f"Elementi nella lista: {contatore}")

    case _:
        print("Scelta non valida")