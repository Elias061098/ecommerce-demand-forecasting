import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
n_clients = 50000

# Simulation des features clients RFM
clients = pd.DataFrame({
    'client_id': range(1, n_clients + 1),
    'recence_jours': np.random.exponential(scale=60, size=n_clients).clip(1, 365).astype(int),
    'frequence': np.random.exponential(scale=8, size=n_clients).clip(1, 100).astype(int),
    'montant_total': np.random.exponential(scale=300, size=n_clients).clip(10, 5000).round(2),
    'nb_categories': np.random.randint(1, 7, n_clients),
    'taux_retour': np.random.beta(2, 10, n_clients).round(3),
})

# Normalisation
scaler = StandardScaler()
X = scaler.fit_transform(clients.drop('client_id', axis=1))

# K-Means
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
clients['segment'] = kmeans.fit_predict(X)

# Labellisation des segments
mapping = {
    clients.groupby('segment')['montant_total'].mean().idxmax(): 'Gros acheteurs',
    clients.groupby('segment')['frequence'].mean().idxmax(): 'Réguliers',
    clients.groupby('segment')['recence_jours'].mean().idxmax(): 'Inactifs',
}
mapping = {k: v for k, v in mapping.items()}
clients['segment_label'] = clients['segment'].map(mapping).fillna('Occasionnels')

# Stats par segment
stats = clients.groupby('segment_label').agg(
    nb_clients=('client_id', 'count'),
    montant_moyen=('montant_total', 'mean'),
    frequence_moyenne=('frequence', 'mean'),
    recence_moyenne=('recence_jours', 'mean')
).round(1)

print("=== Segments clients ===")
print(stats)
print(f"\nRépartition :")
print((clients['segment_label'].value_counts() / len(clients) * 100).round(1))
