
def saluta(nome):# definisce una funzione che prende un argomento "nome"

    print("Ciao,", nome)


PI = 3.14159


class Cerchio: # definisce una classe chiamata "Cerchio"

    def __init__(self, raggio):

        self.raggio = raggio


    def area(self): # definisce un metodo che calcola l'area del cerchio

        return PI * self.raggio**2
     