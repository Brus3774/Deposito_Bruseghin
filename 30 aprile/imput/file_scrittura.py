# Apertura di un file in modalità scrittura e scrittura di alcune righe

file = open("prova1.txt", "w") # apertura del file in modalità scrittura
file.write("Ciao, questo è un file di prova.\n") # scrittura di una riga nel file
file.write("Questa è la seconda riga del file.\n") # scrittura di un'altra riga nel file
file.close() # chiusura del file

