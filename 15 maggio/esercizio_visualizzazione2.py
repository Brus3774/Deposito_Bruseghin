#esercizio 2 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'altezza': [165, 180, 155, 190, 172],
    'peso': [60, 85, 50, 95, 70],
    'età': [25, 41, 19, 32, 28]
}
df_originale = pd.DataFrame(data)

# Creiamo una copia per non sovrascrivere i dati originali, utile per il grafico di confronto
df_normalizzato = df_originale.copy()

# 2. Applicazione della normalizzazione Min-Max 
colonne_da_scalare = ['altezza', 'peso']
df_normalizzato[colonne_da_scalare] = (df_originale[colonne_da_scalare] - np.min(df_originale[colonne_da_scalare], axis=0)) / (np.max(df_originale[colonne_da_scalare], axis=0) - np.min(df_originale[colonne_da_scalare], axis=0))

print("Dati Originali:\n", df_originale)
print("\n")
print("Dati Normalizzati (Età invariata):\n", df_normalizzato)
print("\n") 

# GRAFICO MATPLOTLIB
# Creiamo un nuovo DataFrame unendo i dati per il grafico e lo disegnamo in un colpo solo
df_confronto = pd.DataFrame({
    'Altezza Orig': df_originale['altezza'], 'Altezza Norm (x100)': df_normalizzato['altezza'] * 100,
    'Peso Orig': df_originale['peso'], 'Peso Norm (x100)': df_normalizzato['peso'] * 100
})

df_confronto.plot(kind='bar', figsize=(10, 5), color=['skyblue', 'blue', 'lightcoral', 'red'])
plt.title('Confronto Valori Originali vs Normalizzati (Scalati a 100 per l\'asse Y)')
plt.ylabel('Valore / Percentuale del max')
plt.xticks(range(5), [f"Sogg {i+1}" for i in range(5)], rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show() 

# GRAFICO SEABORN
plt.figure(figsize=(6, 5))
sns.scatterplot(data=df_normalizzato, x='altezza', y='peso', s=150, color='purple')

plt.title('Scatterplot Altezza vs Peso Normalizzati')
plt.xlabel('Altezza Normalizzata (0-1)')
plt.ylabel('Peso Normalizzato (0-1)')
plt.grid(True)
plt.show() 