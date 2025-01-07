import pandas as pd
import matplotlib.pyplot as plt

file_path = 'experimentations_5G.csv'  
usage_columns = [
    "Techno - Massive MIMO", "Techno - Beamforming/beamtracking", 
    "Techno - Duplexage temporel (mode TDD)", "Techno - Mode de fonctionnement NSA (Non Stand Alone)",
    "Techno - Mode de fonctionnement SA (Stand Alone)", "Techno - Synchronisation de réseaux",
    "Techno - Network slicing", "Techno - Small cells", 
    "Techno - Accès dynamique au spectre", "Techno - 5G, 6G…", 
    "Usage - Mobilité connectée", "Usage - Internet des objets", 
    "Usage - Ville intelligente", "Usage - Réalité virtuelle", 
    "Usage - Télémédecine", "Usage - Industrie du futur", 
    "Usage - Technique ou R&D", "Usage - Autre"
]

data = pd.read_csv(file_path, sep=";", encoding="cp1252", usecols=usage_columns)

usage_totals = data.sum()

plt.figure(figsize=(12, 6))
bars = usage_totals.plot(kind='bar', color='skyblue', edgecolor='black')

for index, value in enumerate(usage_totals):
    plt.text(index, value + 0.5, str(int(value)), ha='center', fontsize=10, color='black')

plt.title('Répartition des usages des expérimentations 5G', fontsize=14)
plt.ylabel('Nombre de projets', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.xlabel('Usages', fontsize=12)

plt.tight_layout()
plt.show()
