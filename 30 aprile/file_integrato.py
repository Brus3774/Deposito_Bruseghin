# uso with open per gestire i file in modo sicuro e automatico

with open("prova1.txt", "r") as file: # apertura del file in modalità lettura
    contenuto = file.read() # lettura del contenuto del file
    print(contenuto) # stampa del contenuto del file
    