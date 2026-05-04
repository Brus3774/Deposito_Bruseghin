# main e manu

# Importiamo la classe Aula dal file utente.py
from utente import Aula

# Importiamo le funzioni dal file gestione_credenziali.py
from Gestione_credenziali import registrazione, login


def main():
    mia_aula = Aula()
    loggato = False

    while True: # Loop principale del programma, che continua finché l'utente non decide di uscire. All'interno del loop, viene gestita la logica per la registrazione, il login e le operazioni sull'aula.
        if not loggato:
            print("\n1. Registrati\n2. Login\n3. Esci")
            scelta = input("Azione: ")
            
            if scelta == "1":
                registrazione()
            elif scelta == "2":
                if login():
                    loggato = True
                    print("Accesso effettuato!")
                else:
                    print("Credenziali non valide.")
            elif scelta == "3":
                break
        else:
            # Menu Operativo (Punto 5 e 6)
            print("\n--- AREA OPERATIVA ---")
            print("1. Inserisci/Modifica Studente")
            print("2. Stampa Aula")
            print("3. Logout")
            op = input("Scelta: ")
            
            if op == "1":
                nome_s = input("Nome studente: ")
                corso_s = input("Corso: ")
                mia_aula.ins_mod_studente(nome_s, corso_s)
            elif op == "2":
                mia_aula.stampa_aula_ordinata()
            elif op == "3":
                loggato = False
                print("Sessione terminata.")

if __name__ == "__main__":
    main() 