# esercizio 1 incapsulamento

class ContoBancario:
    def __init__(self, titolare, saldo_iniziale):
        self.__titolare = titolare
        self.__saldo = saldo_iniziale

    # --- GETTER E SETTER PER IL TITOLARE ---
    @property
    def titolare(self):
        return self.__titolare

    @titolare.setter
    def titolare(self, valore):
        #Setter: controlla che il valore sia una stringa e non sia vuota.
        # isinstance(valore, str) controlla che il tipo sia una stringa
        # .strip() rimuove gli spazi bianchi (es. "  ") per evitare nomi 'invisibili'
        if isinstance(valore, str) and valore.strip():
            self.__Titolare = valore
        else:
            print("Errore: Il titolare deve essere un nome valido!")

    # --- GETTER PER IL SALDO ---
    @property
    def saldo(self):
        return self.__saldo

    # --- METODI PUBBLICI ---

    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di {importo}€ eseguito. Nuovo saldo: {self.__saldo}€")
        else:
            print("Errore: L'importo del deposito deve essere positivo.")

    def preleva(self, importo):
        if importo <= 0:
            print("Errore: L'importo del prelievo deve essere positivo.")
        elif importo > self.__saldo:
            print(f"Errore: Fondi insufficienti. Saldo disponibile: {self.__saldo}€")
        else:
            self.__saldo -= importo
            print(f"Prelievo di {importo}€ eseguito. Saldo rimanente: {self.__saldo}€")

    def visualizza_saldo(self):
        # Non serve passare 'importo' qui, vogliamo solo vedere lo stato attuale
        print(f"Il saldo attuale di {self.__titolare} è: {self.__saldo}€")
        
Cb1 = ContoBancario("Davide Bruseghin", 3000)
Cb1.deposita(600)
Cb1.preleva(800)
Cb1.preleva(-100)
Cb1.preleva (3100)
Cb1.visualizza_saldo()
Cb1.titolare = ""



