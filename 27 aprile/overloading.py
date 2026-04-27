#esempio di overloding

class Calcolatrice:
    # Simuliamo l'overloading usando parametri con valore di default (None)
    def somma(self, a, b, c = None):
        if c is not None:
            # Caso con 3 numeri
            return a + b + c
        else:
            # Caso con 2 numeri
            return a + b

# --- TEST ---
calc = Calcolatrice()

# Chiamata "Versione 1" (2 parametri)
print(f"Somma di due numeri: {calc.somma(10, 5)}") 

# Chiamata "Versione 2" (3 parametri)
print(f"Somma di tre numeri: {calc.somma(10, 5, 20)}")