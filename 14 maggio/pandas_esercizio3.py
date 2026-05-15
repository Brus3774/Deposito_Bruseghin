# esercizio pp 275 - 277

import pandas as pd
import numpy as np

# DATAFRAME Iscritti
nomi = ["Marco", "Sofia", "Luca", "Elena", "Giuseppe", "Chiara", "Alessandro", "Valentina", "Matteo", "Sara"]
citta_iscritti = ["Roma", "Milano", "Napoli"]
abbonamenti = ["Base", "Premium", "Family"]

data_iscritti = {
    "Nome": [np.random.choice(nomi) for _ in range(10)],
    "Età": [np.random.randint(18, 70) for _ in range(10)],
    "Citta": [np.random.choice(citta_iscritti) for _ in range(10)],
    "Tipo_Abbonamento": [np.random.choice(abbonamenti) for _ in range(10)]
}

df_iscritti = pd.DataFrame(data_iscritti)

# Vincoli Iscritti: Duplicato e Valore Mancante
# Duplichiamo la prima riga
df_iscritti = pd.concat([df_iscritti, df_iscritti.iloc[[0]]], ignore_index=True)
# Inseriamo un valore mancante nell'Età
df_iscritti.at[2, "Età"] = np.nan


# DATAFRAME Presenze
corsi = ["Yoga", "Crossfit", "Nuoto", "Pilates"]
date_presenze = ["2024-05-01", "2024-05-02", "2024-05-03"]
citta_centri = ["Roma", "Milano", "Napoli"]

n_righe = 15 # condizione di taglia per il dataframe 

data_presenze = {
    "Data": [np.random.choice(date_presenze) for _ in range(15)],
    "Corso": [np.random.choice(corsi) for _ in range(15)],
    "Citta": [np.random.choice(citta_centri) for _ in range(15)],
    "Partecipanti": [np.random.randint(5, 30) for _ in range(15)]
}

df_presenze = pd.DataFrame(data_presenze)
# Convertiamo la colonna Data in formato datetime per poter fare analisi temporali
df_presenze["Data"] = pd.to_datetime(df_presenze["Data"])


#  DATAFRAME Costi abbonamento
# Questa è una tabella di riferimento
data_costi = {
    "Tipo_Abbonamento": ["Base", "Premium", "Family"],
    "Costo_Mensile": [40.0, 70.0, 100.0]
}

df_costi = pd.DataFrame(data_costi)
 
# verifica dataframe con stampe
print("--- Iscritti ---")
print(df_iscritti) 
print("\n--- Presenze ---")
print(df_presenze) 
print("\n--- Listino Costi ---")
print(df_costi) 

print("\n")

# Analisi iniziale
print("--- Iscritti ---")
print(df_iscritti) 
print("\n")

df_older = df_iscritti[df_iscritti['Età'] > 25] # filtraggio iscritti per età
print(df_older)
print("\n")

# sono attivi tutti quelli che non hanno l'abbonamento Base
df_iscritti["Attivo"] = df_iscritti["Tipo_Abbonamento"] != "Base"
print(df_iscritti)
print("\n")

# Pulizia dati
# Rimuoviamo i duplicati
df_iscritti = df_iscritti.drop_duplicates()

#  Gestione valori mancanti nell'Età (sostituzione con media)
media_eta = df_iscritti["Età"].mean()
df_iscritti["Età"] = df_iscritti["Età"].fillna(media_eta)

print("Dati puliti:") 
print(df_iscritti)
print("\n") 

# Trasformazione dati
def fascia_età(eta):
    if eta < 18:
        return "Junior"
    elif 18 <= eta <= 44: 
        return "Adulto"
    else:
        return "Senior"

# Applichiamo la funzione alla colonna Età per creare la nuova colonna
df_iscritti["Categoria Età"] = df_iscritti["Età"].apply(fascia_età)

# Aggregazione dati 

# Ordinamento per Città (A-Z) e Partecipanti (dal più grande al più piccolo)
df_presenze_sorted = df_presenze.sort_values(by=["Citta", "Partecipanti"], ascending=[True, False])

# Groupby per Corso: Somma totale partecipanti
totale_per_corso = df_presenze.groupby("Corso")["Partecipanti"].sum()

# Groupby per Città: Media partecipanti
media_per_citta = df_presenze.groupby("Citta")["Partecipanti"].mean()

# Pivot Table
# Crea una griglia dove vedi subito come vanno i corsi nelle varie città
tabella_pivot = df_presenze.pivot_table(
    index="Corso", 
    columns="Citta", 
    values="Partecipanti", 
    aggfunc="mean"
)

print("\n--- Analisi Presenze ---")
print("Totale partecipanti per corso:\n", totale_per_corso)
print("\nMedia partecipanti per città:\n", media_per_citta)
print("\nTabella Pivot (Media Partecipanti per Corso/Città):\n", tabella_pivot)
print("\n") 

# Multindex

dati_sede = {
    'Sede': ['Nord', 'Nord', 'Centro', 'Centro', 'Sud', 'Sud'], # nuovo dizionario con dati suggeriti
    'Anno': [2024, 2025, 2024, 2025, 2024, 2025],
    'Iscritti': [150, 180, 120, 130, 90, 110]
}
df_sedi = pd.DataFrame(dati_sede).set_index(['Sede', 'Anno'])

# Accesso con loc
iscritti_nord = df_sedi.loc['Nord']
valore_specifico = df_sedi.loc[('Centro', 2025), 'Iscritti']

# Merge e costi

# Uniamo gli iscritti ai costi basandoci sul tipo di abbonamento
df_iscritti_completo = pd.merge(df_iscritti, df_costi, on='Tipo_Abbonamento')

# Calcolo annuale
df_iscritti_completo['Costo_Annuale'] = df_iscritti_completo['Costo_Mensile'] * 12
print("DataFrame Iscritti completo") 
print(df_iscritti_completo)


# Salvataggio csv

# index=False evita di creare una colonna extra con i numeri di riga (0, 1, 2...)
df_iscritti.to_csv('iscritti_puliti.csv', index=False)
df_iscritti_completo.to_csv('iscritti_con_costi.csv', index=False)

# Per la pivot ha senso tenere l'index perché contiene i nomi dei corsi
tabella_pivot.to_csv('report_presenze_pivot.csv', index=True) 