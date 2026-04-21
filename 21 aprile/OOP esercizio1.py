

#esercizio 1
class Punto: #creo una classe punto che rappresenta un punto in un piano cartesiano
  
    def __init__(self, x, y): #metodo costruttore che inizializza le coordinate x e y del punto
        self.x = x 
        self.y = y
        
    def muovi(self, dx, dy): #metodo che muove il punto di dx unità in x e dy unità in y
        self.x += dx
        self.y += dy
        print(f"Il punto si è mosso a ({self.x}, {self.y})")        
    
    def distanza_da_origine(self): #metodo che calcola la distanza del punto dall'origine (0,0) usando il teorema di Pitagora
        return (self.x ** 2 + self.y ** 2) ** 0.5
       
    def stampa_info(self): #metodo che stampa le coordinate del punto e la sua distanza dall'origine
        print(f"Il punto è in ({self.x}, {self.y}) e la sua distanza dall'origine è {self.distanza_da_origine():.2f}")  
        
punto1 = Punto(3, 4) #creazione di un oggetto punto1 con coordinate (3,4)
punto2 = Punto(6, 8) #creazione di un oggetto punto2 con coordinate (6,8)
punto3 = Punto(0, 0) #creazione di un oggetto punto3 con coordinate (0,0)
punto1.muovi(2, 3)  # Muovi x di 2 e y di 3
punto2.muovi(-1, -2) # Muovi x di -1 e y di -2
punto3.muovi(5, 12) # Muovi x di 5 e y di 12

punto1.stampa_info() #stampa le informazioni del punto1
punto2.stampa_info() #stampa le informazioni del punto2
punto3.stampa_info() #stampa le informazioni del punto3
    



