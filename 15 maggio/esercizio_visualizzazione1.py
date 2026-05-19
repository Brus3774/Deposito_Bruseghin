import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Genera i dati
np.random.seed(42)
# np.random.uniform(10, 35, 30) genera 30 numeri decimali casuali distribuiti 
# in modo uniforme (tutti hanno la stessa probabilità di uscire) in un range tra 10 e 35. 
df = pd.DataFrame({'temperature': np.random.uniform(10, 35, 30)})

# Calcola le statistiche
print("Max:   ", df['temperature'].max())
print("Min:   ", df['temperature'].min())
print("Media: ", df['temperature'].mean())
print("Mediana:", df['temperature'].median())
print("\n")

# MATPLOTLIB: Line Plot con linea della media

plt.figure(figsize=(10, 4)) # stabilisce le dimensioni della finestra
plt.plot(df.index, df['temperature'], marker='o', color='b', label='Temperatura')
# Aggiunge la linea orizzontale della media
plt.axhline(df['temperature'].mean(), color='r', linestyle='--', linewidth=2, label=f"Media ({df['temperature'].mean():.2f})")

plt.title('Andamento delle Temperature')
plt.xlabel('Indice dei giorni / campioni')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

# SEABORN: Histplot con KDE (Distribuzione)
plt.figure(figsize=(10, 4))
sns.histplot(data=df, x='temperature', kde=True, color='purple', bins=10)

plt.title('Distribuzione delle Temperature')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Frequenza')
plt.show()