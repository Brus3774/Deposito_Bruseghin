
#esercizio completo


print("=== MENU ===")
print("1 - utilizzo di if")
print("2 - utilizzo di range")
print("3 - utilizzo di for")
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
        for i in range(n, -1, -1):
            print(i)
 
    case "3": # esempio di uso di for
        elementi_numerici = []
        n = int(input("Quanti numeri vuoi inserire? "))
        for i in range(n):
            numero = int(input(f"Inserisci il numero {i + 1}: "))
            elementi_numerici.append(numero)
        for numero in elementi_numerici:
            print(f"{numero}² = {numero ** 2}")