# esercizio 2 p. 253
import pandas as pd
import numpy as np

# creazione dati

prodotti = ["Laptop", "Schermo", "Cuffie", "Mouse", "Tastiera", "Stampante", "Speaker", "Hard Disk", "Ram", "Ventola"]
citta = ["Pescara", "Venezia", "Salerno", "Cuneo", "Siracusa"]


# Numero di righe desiderate
n_righe = 40

# Generazione dati casuali
data = {
    "Prodotti": [np.random.choice(prodotti) for _ in range(n_righe)],
    "Quantità": [np.random.randint(10, 85) for _ in range(n_righe)],
    "Prezzo Unitario": [round(np.random.uniform(15, 1500), 2) for _ in range(n_righe)],
    "Città": [np.random.choice(citta) for _ in range(n_righe)]
    
}

df_vendite = pd.DataFrame(data)


# AGGIUNGERE COLONNA "TOTALE VENDITE"

df_vendite["Totale Vendite"] = df_vendite["Quantità"] * df_vendite["Prezzo Unitario"]

# RAGGRUPPAMENTO PER PRODOTTO
# Calcoliamo la somma del Totale Vendite per ogni tipo di prodotto
vendite_per_prodotto = df_vendite.groupby("Prodotti")["Totale Vendite"].sum()
print("\nTotale vendite per prodotto:\n", vendite_per_prodotto)

#  PRODOTTO PIÙ VENDUTO
# Raggruppo e sommo
somma_quantita = df_vendite.groupby("Prodotti")["Quantità"].sum()

# Ordino dal più grande al più piccolo e prendo il primo nome
prodotto_top = somma_quantita.sort_values(ascending=False).index[0]

print(f"Il prodotto più venduto è: {prodotto_top}") 

# CITTÀ CON MAGGIOR VOLUME DI VENDITE
citta_top_vendite = df_vendite.groupby("Città")["Totale Vendite"].sum().idxmax()
print(f"La città con il maggior volume d'affari è: {citta_top_vendite}")

#  FILTRAGGIO VENDITE SUPERIORI A 1000 EURO
# Creiamo un nuovo DataFrame con il filtro
df_high_value = df_vendite[df_vendite["Totale Vendite"] > 1000].copy()

# ORDINAMENTO DECRESCENTE ---
df_vendite = df_vendite.sort_values(by="Totale Vendite", ascending=False)

# Conta quante volte compare ogni città (numero di transazioni)
conteggio_citta = df_vendite["Città"].value_counts()
print("\nNumero di vendite effettuate per città:\n", conteggio_citta)
