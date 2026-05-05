# sistema amministrazione

class Amministrazione:
    def __init__(self, gestione_clienti, gestione_inventario):
        # Riceve le istanze degli altri moduli per accedere ai loro dati
        self.gc = gestione_clienti
        self.gi = gestione_inventario
        # Amministratori preinseriti: { "username": "password" }
        self.admin_credenziali = {
            "AntonioBarbero": "HistoriaVitae",
            "BeppeSpalletti": "FutbolCLub"
        }

    def login(self, username, password):
        # Verifica se le credenziali admin sono corrette.
        if self.admin_credenziali.get(username) == password:
            print(f"Amministrazione: Benvenuto {username}.")
            return True
        print("Amministrazione: Accesso negato.")
        return False

    def calcola_guadagni_totali(self):
        # Calcola la somma di tutti gli acquisti di tutti i clienti.
        totale = 0
        for cliente in self.gc.clienti.values():
            for art in cliente.acquisti:
                totale += art.prezzo
        return totale

    def visualizza_rapporto_vendite(self):
        #Mostra a video il riepilogo vendite.
        print("\n- RAPPORTO VENDITE -")
        for c in self.gc.clienti.values():
            if c.acquisti:
                print(f"Cliente: {c.nome} {c.cognome} | Acquisti: {len(c.acquisti)}")
        print(f"GUADAGNO TOTALE: {self.calcola_guadagni_totali()}€")

    def stampa_report(self, nome_file="report_amministrazione.txt"): # Genera un report completo con stato inventario e vendite per cliente.
       
        try:
            with open(nome_file, "w") as f:
                
                f.write("       REPORT GLOBALE AMMINISTRAZIONE     \n")
                
                # 1. Stato Inventario
                f.write("- STATO CORRENTE INVENTARIO -\n")
                if not self.gi.articoli:
                    f.write("Magazzino vuoto.\n")
                else:
                    for art in self.gi.articoli.values():
                        f.write(f"ID: {art.nome:15} | Q.tà: {art.quantita:<5} | Prezzo: {art.prezzo}€\n")
                
                f.write("\n" + "="*40 + "\n\n")

                # 2. Dettaglio Vendite per Cliente
                f.write("- DETTAGLIO VENDITE -\n")
                for c in self.gc.clienti.values():
                    if c.acquisti:
                        f.write(f"CLIENTE: {c.nome} {c.cognome} ({c.email})\n")
                        for a in c.acquisti:
                            f.write(f"  > {a.nome}: {a.prezzo}€\n")
                        f.write("-" * 20 + "\n")

                # 3. Guadagni Totali
                f.write(f"\n>>> GUADAGNI TOTALI AZIENDALI: {self.calcola_guadagni_totali()}€ <<<\n")
                f.write("\nFine Report.")
            
            print(f"Amministrazione: Report salvato in '{nome_file}'.")
        except Exception as e:
            print(f"Errore nella stampa del report admin: {e}")