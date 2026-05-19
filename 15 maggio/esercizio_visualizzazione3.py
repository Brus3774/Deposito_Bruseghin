# esercizio 3 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# GENERAZIONE DATI 
np.random.seed(42)
date_range = pd.date_range(start='2025-01-01', periods=365, freq='D')

# Creiamo un trend lineare che cresce, più del rumore casuale
trend = np.linspace(100, 500, 365) 
rumore = np.random.normal(0, 30, 365)
visitatori = (trend + rumore).astype(int)

# DataFrame con le date come indice 
df = pd.DataFrame({'visitatori': visitatori}, index=date_range)

# CALCOLO STATISTICHE MENSILI (Media e Deviazione Standard)

# Raggruppiamo per mese usando il Resample ('ME' o 'M')
stats_mensili = df['visitatori'].resample('ME').agg(['mean', 'std'])
print("Statistiche Mensili (Primi 5 mesi):\n", stats_mensili.head())
print("\n")

# Calcoliamo anche la media mobile a 7 giorni per il grafico
df['media_mobile_7d'] = df['visitatori'].rolling(window=7).mean()

# MATPLOTLIB: Giornaliero vs Media Mobile

plt.figure(figsize=(12, 5))

# Disegniamo i dati giornalieri (linea sottile e chiara)
plt.plot(df.index, df['visitatori'], color='lightblue', alpha=0.7, label='Giornaliero')
# Disegniamo la media mobile (linea più spessa e marcata)
plt.plot(df.index, df['media_mobile_7d'], color='navy', linewidth=2, label='Media Mobile 7gg')

plt.title('Visitatori Giornalieri e Media Mobile a 7 Giorni')
plt.xlabel('Data')
plt.ylabel('Numero di Visitatori')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# SEABORN: Lineplot della Media Mensile

plt.figure(figsize=(10, 4))

# Passiamo direttamente la nostra tabella delle statistiche mensili
sns.lineplot(data=stats_mensili, x=stats_mensili.index, y='mean', marker='o', color='crimson', linewidth=2.5)

plt.title('Andamento della Media Mensile dei Visitatori')
plt.xlabel('Mese')
plt.ylabel('Media Visitatori')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()