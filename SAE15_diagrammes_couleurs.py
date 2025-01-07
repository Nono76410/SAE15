import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "experimentations_5G.csv"  
data = pd.read_csv(file_path, sep=";", encoding="cp1252", usecols=["Région", "Techno - Massive MIMO", "Techno - Beamforming/beamtracking", "Techno - Duplexage temporel (mode TDD)", "Usage - Mobilité connectée", "Usage - Internet des objets", "Usage - Ville intelligente"])
data = data.fillna(0)

region_totals = data.groupby("Région").sum()
region_pourcentages = region_totals.div(region_totals.sum(axis=1), axis=0) * 100

# Couleurs pour les usages
colors = plt.cm.tab20(np.linspace(0, 1, len(region_pourcentages.columns)))

# Créer le graphique empilé
fig, ax = plt.subplots(figsize=(14, 8))
bottoms = np.zeros(len(region_pourcentages))  # Initialisation pour empiler les barres

for i, usage in enumerate(region_pourcentages.columns):
    ax.bar(
        region_pourcentages.index, 
        region_pourcentages[usage], 
        bottom=bottoms, 
        color=colors[i], 
        label=usage
    )
    bottoms += region_pourcentages[usage]

# Ajouter des labels et une légende
ax.set_title('Répartition des usages par région (en %)', fontsize=16)
ax.set_ylabel('Pourcentage (%)', fontsize=12)
ax.set_xlabel('Régions', fontsize=12)
ax.set_xticks(range(len(region_pourcentages.index)))
ax.set_xticklabels(region_pourcentages.index, rotation=45, ha='right', fontsize=10)

# Ajouter la légende
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Usages', fontsize=9)
plt.tight_layout()
plt.show()
