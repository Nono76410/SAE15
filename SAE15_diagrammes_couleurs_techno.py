import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lecture du fichier CSV
file_path = "experimentations_5G.csv"
columns = ["Région", "Techno - Massive MIMO", "Techno - Beamforming/beamtracking", 
           "Techno - Duplexage temporel (mode TDD)", "Techno - Mode de fonctionnement NSA (Non Stand Alone)",
           "Techno - Mode de fonctionnement SA (Stand Alone)", "Techno - Synchronisation de réseaux",
           "Techno - Network slicing", "Techno - Small cells", "Techno - Accès dynamique au spectre", 
           "Techno - 5G, 6G…"]

data = pd.read_csv(file_path, sep=";", encoding="cp1252", usecols=columns)
data = data.fillna(0)

# Conversion en numérique
for col in data.columns[1:]:
    data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)

# Groupement par région et calcul des pourcentages
region_totals = data.groupby("Région").sum()
region_pourcentages = region_totals.div(region_totals.sum(axis=1), axis=0) * 100

# Créer des positions numériques pour les régions
x_positions = np.arange(len(region_pourcentages))

# Couleurs pour les usages
colors = plt.cm.tab20(np.linspace(0, 1, len(region_pourcentages.columns)))

# Créer le graphique empilé
fig, ax = plt.subplots(figsize=(14, 8))
bottoms = np.zeros(len(region_pourcentages))

for i, usage in enumerate(region_pourcentages.columns):
    ax.bar(
        x_positions,  # Utiliser les positions numériques
        region_pourcentages[usage], 
        bottom=bottoms, 
        color=colors[i], 
        label=usage
    )
    bottoms += region_pourcentages[usage]

# Ajouter des titres et des labels et legende
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Usages', fontsize=9)
ax.set_title('Répartition des techno par région (en %)', fontsize=16)
ax.set
