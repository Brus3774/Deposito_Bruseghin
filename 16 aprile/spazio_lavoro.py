

def inserisci_numero_positivo():
                while True:
                    numero = int(input("Inserisci un numero positivo: "))
                    if numero > 0:
                        return numero
                    else:
                        print("Il numero inserito non è positivo. Riprova.")

risultato = inserisci_numero_positivo()
print(f"Numero inserito: {risultato}")



import random

def crea_lista_numeri(n):
    lista = []
    for i in range(n):
        numero = random.randint(1, n)
        lista.append(numero)
    return lista

n = int(input("Inserisci un numero: "))
risultato = crea_lista_numeri(n)
print(f"Lista generata: {risultato}")



def somma_pari_da_lista():
    lista = crea_lista_numeri(n)  # prendi la lista dalla funzione precedente
    somma = 0

    for numero in lista:
        if numero % 2 == 0:
            somma += numero

    print("La somma dei numeri pari è:", somma)


# esecuzione
somma_pari_da_lista()


def stampa_numeri_dispari_da_lista():
    lista = crea_lista_numeri(n)  # prendi la lista dalla funzione precedente
    print("I numeri dispari nella lista sono:")
    for numero in lista:
        if numero % 2 != 0:
            print(numero)
            
stampa_numeri_dispari_da_lista()   