# sistema gestione inventario 

class Articolo:
    def __init__(self, nome, prezzo, quantita):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

    def __str__(self):
        return f"Prodotto: {self.nome:15} | Prezzo: {self.prezzo:>6}€ | Q.tà: {self.quantita}"

class GestioneInventario:
    def __init__(self):
        # Struttura: { "nome_articolo": oggetto_articolo }
        self.articoli = {
            "casse acustiche": Articolo("Casse acustiche", 100, 10),
            "cuffie": Articolo("Cuffie", 50, 20),
            "microfono": Articolo("Microfono", 80, 15),
            "mixer": Articolo("Mixer", 150, 5),
            "amplificatore": Articolo("Amplificatore", 200, 3)
        }
        
    def stampa_inventario_file(self, nome_file="stato_inventario.txt"):
        # Genera un file di testo con la situazione attuale del magazzino.
        try:
            with open(nome_file, "w") as f:
                f.write("=== REGISTRO MAGAZZINO ===\n")
                f.write(f"{'PRODOTTO':<15} | {'PREZZO':<8} | {'QUANTITA':<10}\n")
                f.write("-" * 40 + "\n")
                
                for art in self.articoli.values():
                    f.write(f"{art.nome:<15} | {art.prezzo:>6}€   | {art.quantita:>8}\n")
                
                f.write("-" * 40 + "\n")
                f.write(f"Ultimo aggiornamento: {len(self.articoli)} articoli totali.\n")
            print(f"Sistema: File '{nome_file}' aggiornato.")
        except Exception as e:
            print(f"Errore nella stampa dell'inventario: {e}")

    def aggiungi_o_aggiorna_articolo(self, nome, prezzo, quantita):
        nome_chiave = nome.lower()
        
        if nome_chiave in self.articoli:  
            # Aggiornamento: sommiamo la nuova quantità a quella vecchia
            self.articoli[nome_chiave].quantita += quantita 
            # Aggiorniamo il prezzo all'ultimo inserito (magari è cambiato il listino)
            self.articoli[nome_chiave].prezzo = prezzo 
            print(f"Inventario: '{nome}' aggiornato (nuova disponibilità: {self.articoli[nome_chiave].quantita}).")
        else:
            # Creazione nuovo articolo
            nuovo = Articolo(nome, prezzo, quantita)
            self.articoli[nome_chiave] = nuovo
            print(f"Inventario: '{nome}' aggiunto al catalogo.")
        
        # Sincronizziamo sempre il file dopo la modifica
        self.stampa_inventario_file()
        
        # Aggiorna automaticamente il file ad ogni modifica
        self.stampa_inventario_file()

    def rimuovi_articolo(self, nome): # Rimuove un articolo dall'inventario. Se l'articolo non esiste, mostra un messaggio di errore.
        nome_chiave = nome.lower()
        if nome_chiave in self.articoli:
            del self.articoli[nome_chiave]
            print(f"Inventario: '{nome}' rimosso.")
            # Aggiorna il file dopo la rimozione
            self.stampa_inventario_file()
        else:
            print(f"Errore: Articolo '{nome}' non trovato.")
            
    def vendi_articolo(self, nome):
        #Riduce la quantità di un articolo di 1 unità. Restituisce l'oggetto Articolo se la vendita ha successo, altrimenti None.
        
        nome_chiave = nome.lower()
        articolo = self.articoli.get(nome_chiave) # Ricerca diretta nel dizionario per efficienza

        if articolo:
            if articolo.quantita > 0:
                articolo.quantita -= 1
                print(f"Vendita: '{articolo.nome}' venduto. Rimasti: {articolo.quantita}")
                # Aggiorniamo il file TXT perché la giacenza è cambiata
                self.stampa_inventario_file()
                return articolo  # Restituiamo l'oggetto per aggiungerlo agli acquisti del cliente
            else:
                print(f"Errore: L'articolo '{articolo.nome}' è esaurito!")
        else:
            print(f"Errore: L'articolo '{nome}' non esiste in inventario.")
        
        return None 

    def visualizza_inventario(self):
        if not self.articoli:
            print("Inventario: Vuoto.")
        else:
            print("\n--- INVENTARIO ---")
            for art in self.articoli.values():
                print(art)

    def cerca_articolo(self, nome):
        return self.articoli.get(nome.lower())
    
   