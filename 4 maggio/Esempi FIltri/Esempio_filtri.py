def is_even(x): # Questa funzione restituisce True se x è un numero pari, altrimenti restituisce False
    return x % 2 == 0 # L'operatore % restituisce il resto della divisione di x per 2. Se il resto è 0, significa che x è divisibile per 2 e quindi è un numero pari.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers)) # La funzione filter applica la funzione is_even a ogni elemento della lista numbers e restituisce un iteratore con solo gli elementi per cui is_even restituisce True. La funzione list converte l'iteratore in una lista.
print(even_numbers)
