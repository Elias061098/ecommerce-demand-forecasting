# Prédiction de la demande e-commerce & segmentation clients

Projet complet sur des données de ventes e-commerce fictives (500 000 transactions).
Objectif : anticiper la demande produit et segmenter les clients pour optimiser les stocks et les actions marketing.

## Ce que j'ai fait

- Pipeline ETL sur 500 000 transactions avec détection d'anomalies
- Prédiction de la demande avec Prophet (Facebook) sur les séries temporelles
- Segmentation clients en 4 segments avec K-Means
- Dashboard interactif Plotly visible directement dans le notebook
- Dockerfile inclus pour reproduire l'environnement

## Stack

Python (pandas, numpy, prophet, scikit-learn, plotly) · K-Means · Docker

## Ce que j'ai trouvé

Les ventes montrent une saisonnalité forte avec des pics en novembre-décembre (+43% vs moyenne).
La segmentation K-Means révèle 4 profils clients distincts : Gros acheteurs (8%), Réguliers (27%), Occasionnels (41%), Inactifs (24%).
Les gros acheteurs représentent 8% des clients mais génèrent 34% du chiffre d'affaires.

## Lancer le projet

```bash
docker build -t ecommerce-forecast .
docker run ecommerce-forecast
```
