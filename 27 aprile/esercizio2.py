#esercizio 2 p.159 -- metodo modifica prenotazione?? deve essere ripetibile, controllo privati/protetti.

class Posto:
    
    def __init__(self, numero: int, fila: str, occupato: bool = False): # il posto è libero di default
        self._numero = numero
        self._fila = fila
        self._occupato = occupato

    def prenota(self): # se il posto è libero, lo prenoto e ritorno True, altrimenti ritorno False
        if not self._occupato:
            self._occupato = True
            return True
        return False
    
    def libera(self): # se il posto è occupato, lo libero e ritorno True, altrimenti ritorno False
        if self._occupato:
            self._occupato = False
            return True
        return False 
   
    @property # getter per numero, fila e occupato, rendendo questi attributi di sola lettura dall'esterno della classe
    def numero(self):
        return self._numero

    @property 
    def fila(self):
        return self._fila

    @property
    def occupato(self):
        return self._occupato

class PostoVip(Posto):
    def __init__(self, numero: int, fila: str, occupato: bool = False, servizi_extra = None): # il posto è libero di default, servizi_extra è opzionale
        super().__init__(numero, fila, occupato)
        if servizi_extra is None:
            self.servizi_extra = ["catering", "accesso lounge", "assistenza personalizzata"] # lista di servizi extra inclusi nel posto VIP
        else:
            self.servizi_extra = servizi_extra  
        
    def prenota(self): # sovrascrivo il metodo prenota per includere i servizi extra
        print (f"Posto VIP {self._numero} della fila {self._fila} prenotato con successo. Servizi extra inclusi: {', '.join(self.servizi_extra)}") 

class PostoStandard(Posto):
    def __init__(self, numero: int, fila: str, costo, occupato: bool = False): # il posto è libero di default, costo è obbligatorio
        super().__init__(numero, fila, occupato)
        self.costo = costo
    
    def prenota(self): # sovrascrivo il metodo prenota per includere il costo del posto standard
        print (f"Posto Standard {self._numero} della fila {self._fila} prenotato con successo. Costo: {self.costo}€")


class Teatro:
    def __init__(self, lista_posti_iniziale=None):
        # self._posti è la lista che conterrà TUTTI gli oggetti (Vip e Standard)
        if lista_posti_iniziale is None:
            self._posti = []
        else:
            self._posti = lista_posti_iniziale
        
    def aggiungi_posto(self, posto): 
        # Aggiunge un oggetto (PostoVip o PostoStandard) alla lista
        self._posti.append(posto)
        
    def prenota_posto(self, numero, fila): 
        # Cerchiamo il posto nella lista
        for posto in self._posti:
            # Usiamo le property .numero e .fila (non i nomi privati con _)
            if posto.numero == numero and posto.fila == fila:
                # Eseguiamo il metodo prenota() dell'oggetto trovato
                if posto.prenota():
                    print(f"Prenotazione confermata per il posto {numero} fila {fila}.")
                else:
                    print(f"Attenzione: il posto {numero} fila {fila} risulta già occupato.")
                return # Usciamo dal metodo una volta trovato il posto
        
        print(f"Errore: il posto {numero} fila {fila} non esiste in questo teatro.")
        
    def stampa_posti_occupati(self): 
        print("\n--- ELENCO POSTI OCCUPATI ---")
        trovati = False
        for posto in self._posti:
            if posto.occupato: # Usiamo la property .occupato
                print(f"Posto {posto.numero} della fila {posto.fila}")
                trovati = True
        
        if not trovati:
            print("Nessun posto risulta attualmente occupato.")
        print("-----------------------------\n")

                
    # test sistema prenotazione
posto1 = PostoStandard(1, "A", 50)
posto2 = PostoVip(2, "A")
posto3 = PostoStandard(3, "B", 30)
teatro = Teatro([posto1, posto2, posto3])
teatro.prenota_posto(1, "A") # prenota il posto 1 della fila A
teatro.prenota_posto(2, "A") # prenota il posto 2 della fila A
teatro.prenota_posto(3, "B") # prenota il posto 3 della fila B
teatro.aggiungi_posto(PostoStandard(4, "B", 30)) # aggiunge un nuovo posto standard alla fila B
teatro.prenota_posto(1, "A") # tenta di prenotare nuovamente il posto 1 della fila A, che è già occupato
teatro.stampa_posti_occupati() # stampa tutti i posti occupati del teatro

    
    