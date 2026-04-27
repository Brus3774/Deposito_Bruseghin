#esempio di polimorfismo

# --- CLASSE ORIGINE ---
class Veicolo:
    def __init__(self, marca):
        self.marca = marca

    def muovi(self):
        # Questo metodo verrà sovrascritto dalle sottoclassi
        pass

# --- SOTTOCLASSE 1 ---
class Auto(Veicolo):
    def muovi(self):
        return f"L'auto {self.marca} accelera premendo il pedale del gas"

# --- SOTTOCLASSE 2 ---
class Bicicletta(Veicolo):
    def muovi(self):
        return f"La bicicletta {self.marca} si muove pedalando"

# --- DIMOSTRAZIONE DEL POLIMORFISMO ---

# Creiamo una lista che contiene oggetti di tipo diverso (ma con origine comune)
parcheggio = [
    Auto("Ferrari"),
    Bicicletta("Bianchi"),
    Auto("Fiat")
]

print("Azione nel parcheggio:")
print("-" * 30)

for veicolo in parcheggio:
    # POLIMORFISMO: Chiamiamo lo stesso metodo 'muovi()' su oggetti diversi.
    # Python capisce da solo quale versione del metodo eseguire a seconda del tipo.
    print(veicolo.muovi())