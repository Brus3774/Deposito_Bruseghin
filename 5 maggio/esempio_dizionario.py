# dizionario

studente = { # creo un dizionario con le informazioni di uno studente
    "nome": "davide", # chiave: nome, valore: davide
    "cognome": "frattesi",
    "eta": 25
        
}

studente["eta"] = 27 # modifico il valore di eta
studente["citta"] = "roma" # aggiungo una nuova chiave: citta con il valore roma

print(studente["nome"])
print(studente["cognome"])  
print(studente["eta"])
print(studente["citta"])
print(studente.keys()) # stampa tutte le chiavi del dizionario
print(studente.values()) # stampa tutti i valori del dizionario 