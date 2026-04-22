

#static method - si può anche aggiungere importo per farlo funzionare in modo più flessibile

class Convertitore: #creo una classe che contiene dei metodi statici, ovvero dei metodi che non hanno bisogno di essere istanziati per essere utilizzati
    
    @staticmethod #decoratore che indica che il metodo è statico, ovvero che non ha bisogno di essere istanziato per essere utilizzato
    def euro_in_dollari(euro): #metodo statico che converte euro in dollari, prende come parametro il numero di euro da convertire e restituisce il numero di dollari corrispondente
        return euro * 1.08
    
    @staticmethod
    def km_in_miglia(km): #metodo statico che converte km in miglia, prende come parametro il numero di km da convertire e restituisce il numero di miglia corrispondente
        return km * 0.621371
    
    
print(f"100 euro equivalgono a {Convertitore.euro_in_dollari(100)} dollari") #chiamo il metodo statico senza istanziare la classe, passando come parametro il numero di euro da convertire

print(f"100 km equivalgono a {Convertitore.km_in_miglia(100)} miglia") #chiamo il metodo statico senza istanziare la classe, passando come parametro il numero di km da convertire

