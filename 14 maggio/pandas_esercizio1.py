# esercizio 1 pp 252

import pandas as pd
import numpy as np

# PREPARAZIONE DEL DATASET

# Liste di base per la generazione casuale
nomi = ["Alice", "Bob", "Charlie", "Diana", "Erik", "Fiona", "Giorgio", "Helga", "Ivan", "Jenny"]
citta = ["Roma", "Milano", "Napoli", "Torino", "Palermo"]

# Numero di righe desiderate
n_righe = 20

# Generazione dati casuali
data = {
    "Nome": [np.random.choice(nomi) for _ in range(n_righe)],
    "Età": [np.random.randint(10, 85) for _ in range(n_righe)],
    "Città": [np.random.choice(citta) for _ in range(n_righe)],
    "Salario": [np.random.randint(20000, 50000) for _ in range(n_righe)]
}

# DATAFRAME

df_lavoratori = pd.DataFrame(data)

#inseriamo eventuali valori duplicati

df_lavoratori = pd.concat([df_lavoratori, df_lavoratori.iloc[:2]], ignore_index=True)

# Inseriamo dei valori mancanti (NaN) in Età e Salario
df_lavoratori.loc[2, "Età"] = np.nan
df_lavoratori.loc[5, "Salario"] = np.nan 

# visualizzazione dataframe

print("Prime 5 righe")
print(df_lavoratori.head())

print("\nUltime 5 righe")
print(df_lavoratori.tail())

print("\nTipo di dato per colonna")
print(df_lavoratori.dtypes)

# Selezioniamo solo le colonne numeriche per evitare errori con le stringhe
print("\n Statistiche Descrittive")
print(f"Media:\n{df_lavoratori[['Età', 'Salario']].mean()}")
print(f"\nMediana:\n{df_lavoratori[['Età', 'Salario']].median()}")
print(f"\nDeviazione Standard:\n{df_lavoratori[['Età', 'Salario']].std()}")

#GESTIONE DUPLICATI
# Identifichiamo il numero di righe duplicate prima della rimozione
n_duplicati = df_lavoratori.duplicated().sum()
print(f"\nNumero di duplicati identificati: {n_duplicati}")

# Rimuoviamo i duplicati mantenendo solo la prima occorrenza (keep='first')
# inplace=False è il default, quindi riassegniamo la variabile
df_lavoratori = df_lavoratori.drop_duplicates()
print("Duplicati rimossi correttamente.")


# GESTIONE VALORI MANCANTI
# Calcoliamo le mediane di colonna 
mediana_eta = df_lavoratori["Età"].median()
mediana_salario = df_lavoratori["Salario"].median()

# fillna sostituisce i valori nulli con il valore specificato
df_lavoratori["Età"] = df_lavoratori["Età"].fillna(mediana_eta)
df_lavoratori["Salario"] = df_lavoratori["Salario"].fillna(mediana_salario)
print("\nValori mancanti gestiti con la mediana.")

print("\n")

# funzione per definire nuova colonna
def assegna_categoria(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"

# Applichiamo la funzione alla colonna Età per creare la nuova colonna
df_lavoratori["Categoria Età"] = df_lavoratori["Età"].apply(assegna_categoria)

print(df_lavoratori)
