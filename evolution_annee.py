import pandas as pd
import matplotlib.pyplot as plt

# Charger les données à partir d'un fichier CSV
file_path = 'experimentations_5G.csv'  # Remplacez par le chemin réel du fichier
data = pd.read_csv(file_path, delimiter=';', encoding='cp1252')  # Définir le délimiteur ";" si nécessaire

# Convertir les colonnes "Début" et "Fin" en format datetime pour l'analyse temporelle
data['Début'] = pd.to_datetime(data['Début'], errors='coerce')
data['Fin'] = pd.to_datetime(data['Fin'], errors='coerce')

# Supprimer les lignes avec des dates invalides
filtered_data = data.dropna(subset=['Début'])

# Extraire l'année de début des expérimentations
filtered_data['Année_Début'] = filtered_data['Début'].dt.year

# Compter le nombre d'expérimentations par année
experiments_per_year = filtered_data['Année_Début'].value_counts().sort_index()

# Tracer l'évolution dans le temps
plt.figure(figsize=(10, 6))
plt.plot(experiments_per_year.index, experiments_per_year.values, marker='o', linestyle='-', color='r')
plt.title("Évolution temporelle des expérimentations 5G", fontsize=14)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Nombre d'expérimentations", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(experiments_per_year.index, rotation=45)
plt.tight_layout()
plt.show()
