import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données
file_path = "experimentations_5G.csv"  
data = pd.read_csv(file_path, sep=";", encoding="cp1252", usecols=["Région", "Usage - Mobilité connectée", 
                                                                  "Usage - Internet des objets", 
                                                                  "Usage - Ville intelligente", 
                                                                  "Usage - Réalité virtuelle", 
                                                                  "Usage - Télémédecine", 
                                                                  "Usage - Industrie du futur", 
                                                                  "Usage - Technique ou R&D", 
                                                                  "Usage - Autre"])
data = data.fillna(0)

# Calcul des totaux par région et des pourcentages
region_totals = data.groupby("Région").sum()
region_pourcentages = region_totals.div(region_totals.sum(axis=1), axis=0) * 100

# Créer des positions numériques pour les régions
x_positions = np.arange(len(region_pourcentages))

# Couleurs pour les usages
colors = plt.cm.tab20(np.linspace(0, 1, len(region_pourcentages.columns)))

# Créer le graphique empilé
fig, ax = plt.subplots(figsize=(14, 8))
bottoms = np.zeros(len(region_pourcentages))  # Initialisation pour empiler les barres

for i, usage in enumerate(region_pourcentages.columns):
    ax.bar(
        x_positions,  # Utiliser les positions numériques
        region_pourcentages[usage], 
        bottom=bottoms, 
        color=colors[i], 
        label=usage
    )
    bottoms += region_pourcentages[usage]

# Ajouter des titres et des labels
ax.set_title('Répartition des usages par région (en %)', fontsize=16)
ax.set_ylabel('Pourcentage (%)', fontsize=12)
ax.set_xlabel('Régions', fontsize=12)
ax.set_xticks(x_positions)
ax.set_xticklabels(region_pourcentages.index, rotation=45, ha='right', fontsize=10)

# Ajouter la légende titre et affichage
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Usages', fontsize=9)
plt.tight_layout()
plt.show()
