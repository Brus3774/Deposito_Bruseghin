# funzioni generatori e decoratori


# esempio generatore

def fibonacci(n): # funzione generatore che genera i numeri della sequenza di Fibonacci fino a un certo numero n.
    a, b = 0, 1

    while a < n: # finché a è minore di n, la funzione continua a generare numeri della sequenza di Fibonacci.
        yield a # la parola chiave yield viene utilizzata per restituire un valore e sospendere l'esecuzione della funzione, permettendo di riprendere da dove si era interrotta alla successiva chiamata.
    a, b = b, a + b
    
    
# esempio decoratore
def decoratore(funzione):
 def wrapper():
    print("Prima dell'esecuzione della funzione")
    funzione()
    print("Dopo l'esecuzione della funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao!")
saluta()