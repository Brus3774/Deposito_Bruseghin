# Chiedi all'utente di inserire un numero. Il programma dovrebbe controllare se il numero inserito è primo / pari o no. Se è primo, lo salva e stampa "Il numero è primo". Altrimenti, stampa "Il numero non è primo". si ferma il tutto quando ha 5 numeri primi


# Lista che raccoglie i numeri primi trovati, si ferma quando raggiunge 5 elementi
primi_trovati = []

# Ciclo principale: continua a chiedere numeri finché la lista non ha 5 primi
while len(primi_trovati) < 5:

    # Chiede all'utente di inserire un numero
    numero = int(input("Inserisci un numero: "))

    # Esclude subito 0 e 1 che per definizione non sono primi
    if numero > 1:

        # Assume che il numero sia primo finché non trova un divisore
        è_primo = True

        # Testa tutti i divisori da 2 fino a numero-1
        for divisore in range(2, numero):
            # Se trova un divisore esatto, il numero non è primo
            if numero % divisore == 0:
                è_primo = False
                break  # inutile continuare a cercare altri divisori

        # Se il numero è primo lo salva nella lista e lo comunica
        if è_primo:
            primi_trovati.append(numero)
            print(f"Il numero {numero} è primo — primi trovati finora: {primi_trovati}")

        # Altrimenti comunica che non è primo
        else:
            print(f"Il numero {numero} non è primo")

    # Se l'utente inserisce 0 o 1 avvisa direttamente
    else:
        print(f"Il numero {numero} non è primo")

# Stampa il riepilogo finale quando la lista ha raggiunto 5 elementi
print(f"\nRaggiunto il limite! I 5 numeri primi inseriti sono: {primi_trovati}")
  
    
  
 