
#esercizio avanzato

def stampa_sequenza_fibonacci(n):
    a = 0
    b = 1

    # Stampa i primi due numeri della sequenza
    print(a)
    print(b)

    while True:
        c = a + b
        # Si ferma quando il prossimo numero supera n
        if c > n:
            break
        print(c)
        a = b
        b = c

numero_utente = int(input("Inserisci un numero: "))
stampa_sequenza_fibonacci(numero_utente)
