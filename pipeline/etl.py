import pandas as pd
import numpy as np

np.random.seed(42)
n = 500000

categories = ['Electronique', 'Mode', 'Maison', 'Sport', 'Beauté', 'Alimentation']
pays = ['France', 'Allemagne', 'Espagne', 'Italie', 'Belgique']

# Génération des dates avec saisonnalité
dates = pd.date_range(start='2022-01-01', end='2023-12-31', periods=n)

df = pd.DataFrame({
    'transaction_id': range(1, n + 1),
    'date': dates,
    'client_id': np.random.randint(1, 50001, n),
    'categorie': np.random.choice(categories, n, p=[0.20, 0.25, 0.15, 0.15, 0.15, 0.10]),
    'pays': np.random.choice(pays, n, p=[0.45, 0.20, 0.15, 0.10, 0.10]),
    'quantite': np.random.randint(1, 10, n),
    'prix_unitaire': np.random.normal(45, 30, n).clip(5, 300).round(2),
})

df['montant'] = (df['quantite'] * df['prix_unitaire']).round(2)
df['mois'] = df['date'].dt.month
df['jour_semaine'] = df['date'].dt.dayofweek

# Saisonnalité novembre-décembre
mask_nov_dec = df['mois'].isin([11, 12])
df.loc[mask_nov_dec, 'montant'] *= 1.43

# Injection anomalies
df.loc[np.random.choice(df.index, 500), 'montant'] *= 50
df.loc[np.random.choice(df.index, 300), 'quantite'] = 0

print(f"Dataset brut : {df.shape}")
print(f"\nAperçu :\n{df.head()}")

# Détection et suppression anomalies
q99 = df['montant'].quantile(0.99)
df = df[df['montant'] <= q99]
df = df[df['quantite'] > 0]

print(f"\nDataset après nettoyage : {df.shape}")
df.to_csv('pipeline/transactions_clean.csv', index=False)
print("Fichier sauvegardé ✓")
