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

Sans segmentation, on divise les clients en gros/petits dépensiers — une seule dimension.
Le K-Means révèle que la fréquence d'achat est plus discriminante que le montant par transaction.

Les Gros acheteurs et les Occasionnels ont quasiment le même panier moyen (310€ vs 297€)
mais une fréquence 4x supérieure (24 achats vs 5). Sans clustering, ces clients
seraient invisibles dans une analyse classique.

Résultat : l'entreprise peut concentrer son budget marketing sur les vrais
moteurs de CA plutôt que sur les gros paniers ponctuels — une différence
de stratégie qui peut représenter plusieurs millions d'euros sur une vraie base client.

Segments identifiés sur 50 000 clients :
- Gros acheteurs (12%) — 24 achats/an → programme fidélité premium
- Réguliers (37,5%) — coeur de cible → offres personnalisées
- Occasionnels (38,2%) → campagnes de relance
- Inactifs (12,3%) → win-back ou abandon

## Lancer le projet

```bash
docker build -t ecommerce-forecast .
docker run ecommerce-forecast
```
