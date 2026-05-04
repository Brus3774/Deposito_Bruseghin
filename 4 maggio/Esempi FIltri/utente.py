#esercizio recap

class StudenteAula:
    def __init__(self, nome, corso):
        self.nome = nome
        self.corso = corso

class Aula:
    def __init__(self):
        self.studenti = []

    def ins_mod_studente(self, nome_cercato, corso_nuovo):
        # Definiamo una funzione interna per il filtro
        def controlla_nome(studente):
            return studente.nome.lower() == nome_cercato.lower() # Confrontiamo i nomi in modo case-insensitive per evitare problemi di maiuscole/minuscole

        # Passiamo la funzione 'controlla_nome' a filter per cercare tra gli studenti
        trovati = list(filter(controlla_nome, self.studenti))
        
        if trovati:
            trovati[0].corso = corso_nuovo
            print(f"Aggiornato: {nome_cercato} -> {corso_nuovo}") # Se troviamo uno studente con il nome cercato, aggiorniamo il suo corso e stampiamo un messaggio di conferma. Usiamo 'trovati[0]' perché filter restituisce una lista, anche se contiene un solo elemento.
        else:
            nuovo = StudenteAula(nome_cercato, corso_nuovo) # Creiamo un nuovo oggetto StudenteAula con il nome e il corso forniti
            self.studenti.append(nuovo)
            print(f"Aggiunto: {nome_cercato}")

    def stampa_aula_ordinata(self): # Questa funzione stampa la lista degli studenti presenti nell'aula, ordinati per corso. Se l'aula è vuota, viene visualizzato un messaggio indicante che l'aula è vuota. Altrimenti, vengono raccolti i corsi unici presenti tra gli studenti, ordinati alfabeticamente, e per ogni corso vengono stampati i nomi degli studenti iscritti a quel corso.
        if not self.studenti:
            print("Aula vuota.")
            return

        corsi = []
        for s in self.studenti: # Iteriamo attraverso la lista degli studenti per raccogliere i corsi unici. Se il corso di uno studente non è già presente nella lista 'corsi', lo aggiungiamo. In questo modo otteniamo una lista di corsi senza duplicati.
            if s.corso not in corsi:
                corsi.append(s.corso)
        corsi.sort()

        for c in corsi:
            # Altra funzione interna per filtrare per corso
            def filtra_per_corso(studente):
                return studente.corso == c
            
            studenti_del_corso = list(filter(filtra_per_corso, self.studenti)) # Usiamo filter con la funzione 'filtra_per_corso' per ottenere una lista di studenti che appartengono al corso corrente 'c'. La funzione 'filtra_per_corso' confronta il corso di ogni studente con il corso 'c' e restituisce True se corrispondono, altrimenti False. Il risultato è una lista di studenti iscritti al corso 'c'.
            for s in studenti_del_corso:
                print(f"Corso: {s.corso:10} | Nome: {s.nome}")
                
                