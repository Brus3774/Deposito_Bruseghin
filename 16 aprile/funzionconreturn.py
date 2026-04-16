 
 #funzioni con return
 
def quadrato(numero):
 return numero * numero
risultato = quadrato(4)
print(risultato) # Output: 16


def saluta(nome:str, messaggio="Ciao"): #definizione della funzione con un parametro opzionale
 print(f"{messaggio} {nome}!") #corpo della funzione, f serve per formattare la stringa
saluta("Mario") # Chiamata alla funzione
saluta("Luigi", messaggio="Buongiorno")


