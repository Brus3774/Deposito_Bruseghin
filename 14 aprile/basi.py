print(1 + 5) # somma
print(6 - 5) # differenza
print(3 * 2) # moltiplicazione
print(4 / 2) # divisione
print(3 ** 2) # potenza

# NUMERI
x = 10 # Alcuni esempi di interi in Python
y = - 5 # Alcuni esempi di interi in Python

a = 3.14 # Alcuni esempi di numeri in virgola mobile in Python
b = - 1.0 # Alcuni esempi di numeri in virgola mobile in Python

print(7.345) # bisogna usare il punto per i numeri in virgola mobile

#STRINGHE
nome = 'Alice' # Alcuni esempi di stringhe in Python
msg = "Ciao!" # Alcuni esempi di stringhe in Python

s = "Python"
print(s[0]) # Output: 'P'
print(s[2]) # Output: 't'


saluto = "Ciao"
nome = "Alice"
messaggio = saluto + " " + nome
print(messaggio) # Output: 'Ciao Alice'
carattere = 'A'

saluto = "Ciao"
nome = "Alice"
messaggio = saluto + " " + nome
print(messaggio) # Output: 'Ciao Alice'<

s = "Ciao, mondo!"
print(len(s)) # Output: 12
print(s.upper()) # Output: 'CIAO, MONDO!'
print(s.split(',')) # Output: '[CIAO] , [MONDO!]'
print(s.replace('mondo', 'universo')) # Output: 'Ciao, universo!'

carattere = 'A' # questo è un char

#BOOLEANI
vero = True # Alcuni esempi di valori booleani in Python
falso = False # Alcuni esempi di valori booleani in Python


x = 78
y = 110
print(x == y) # Output: False
print(x != y) # Output: True
print(x > y) # Output: False

x = 5
y = 10
z = 7
print(x < y and y > z) # Output: True
# and restituisce True solo se entrambe le condizioni sono vere
print(x < y or z > y) # Output: True
# or restituisce True se almeno una delle condizioni è vera
print(not(x < y)) # Output: False
# not inverte il valore booleano

#COLLEZIONI: LISTE - [] modificabile e ordinata, mista
numeri = [1, 3, 2, 4, 5]
nomi = ["Alice", "Bob", "Charlie"]
misto = [1, "due", True, 4.5]

numeri = [19, 2, 3, 4, 7]
# Alcuni esempi di liste in Python, LISTA con 4 valori perchè gli indice partono da 0
print(numeri[0]) # Output: 1
print(numeri[2]) # Output: 3

numeri = [3, 1, 4, 2, 5]
print(len(numeri)) # Output: 5 - lunghezza della lista
numeri.append(6)
print(numeri) # Output: [3, 1, 4, 2, 5, 6] - aggiunge un elemento alla fine della lista
numeri.insert(2, 10)
print(numeri) # Output: [3, 1, 10, 4, 2, 5, 6] - inserisce un elemento alla posizione specificata
numeri.remove(4)
print(numeri) # Output: [3, 1, 10, 2, 5, 6] - rimuove la prima occorrenza del valore specificato
numeri.sort()
print(numeri) # Output: [1, 2, 3, 5, 6, 10] - ordina la lista in ordine crescente