
#Chiedi all'utente di inserire un numero. Il programma dovrebbe quindi fare un conto alla rovescia a partire da quel numero fino a zero, stampando ogni numero e chiederti se vuoi ripetere o no.

numero = int(input("Inserisci un numero: "))
for i in range(numero, -1, -1): # range con tre argomenti genera una sequenza di numeri da numero a 0 con passo -1
    print(i)
ripeti = input("Vuoi ripetere? (s/n): ") # chiediamo all'utente se vuole ripetere, convertendo la risposta in minuscolo per facilitare il confronto
if ripeti.lower() == 's':
    numero = int(input("Inserisci un numero: ")) # se l'utente vuole ripetere, chiediamo un nuovo numero e facciamo di nuovo il conto alla rovescia
    for i in range(numero, -1, -1):
        print(i)
