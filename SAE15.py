# importation des libraries nécessaire 
#--------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import folium
import numpy as np
#--------------------------------------------------------------------------------------------------------


# Programme 1 : Antenne par région
#--------------------------------------------------------------------------------------------------------
data = pd.read_csv("experimentations_5G.csv", sep=";", encoding="cp1252", usecols=["Région"])

data = data.fillna("Non assigné")
data["Région"] = data["Région"].astype(str)

# Compter le nombre d'antennes par région
region_counts = data["Région"].value_counts()

# Créer un histogramme
plt.figure(figsize=(12, 8))
region_counts.plot(kind="bar", color="red")
plt.title("Répartition des antennes 5G par région", fontsize=16)
plt.xlabel("Régions", fontsize=14)
plt.ylabel("Nombre d'antennes", fontsize=14)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
#--------------------------------------------------------------------------------------------------------



# Programme 2 : éxperimentation et ces répartitions 
#--------------------------------------------------------------------------------------------------------

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

# mise en sum des 
usage_totals = data.sum()

# mise en place du graphique
plt.figure(figsize=(12, 6))
bars = usage_totals.plot(kind='bar', color='skyblue', edgecolor='black')

# boucle for 
for index, value in enumerate(usage_totals):
    plt.text(index, value + 0.5, str(int(value)), ha='center', fontsize=10, color='black')

# affichage du titre, du x et du y 
plt.title('Répartition des usages des expérimentations 5G', fontsize=14)
plt.ylabel('Nombre de projets', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.xlabel('Usages', fontsize=12)

# affichage du graphique
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------



# Programme 3: Diagrammes en couleur pour le coté techno
#--------------------------------------------------------------------------------------------------------

# Charger les données
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "experimentations_5G.csv"  

# Charger les données et filtrer les lignes valides
data = pd.read_csv(
    file_path, 
    sep=";", 
    encoding="cp1252", 
    usecols=["Région", "Techno - Massive MIMO", "Techno - Beamforming/beamtracking", 
             "Techno - Duplexage temporel (mode TDD)", "Techno - Mode de fonctionnement NSA (Non Stand Alone)",
             "Techno - Mode de fonctionnement SA (Stand Alone)", "Techno - Synchronisation de réseaux",
             "Techno - Network slicing", "Techno - Small cells", "Techno - Accès dynamique au spectre", 
             "Techno - 5G, 6G…"]
)

# Supprimer les lignes avec des régions manquantes
data = data.dropna(subset=["Région"])

# Supprimer les espaces en trop
data["Région"] = data["Région"].str.strip()

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
ax.set_title('Répartition des technologies par région (en %)', fontsize=16)
ax.set_ylabel('Pourcentage (%)', fontsize=12)
ax.set_xlabel('Régions', fontsize=12)
ax.set_xticks(x_positions)
ax.set_xticklabels(region_pourcentages.index, rotation=45, ha='right', fontsize=10)

# Ajouter la légende et affichage
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Technologies', fontsize=9)
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------



# Programme 4 : Diagramme en couleur pour le coté des usages
#--------------------------------------------------------------------------------------------------------

# Charger les données et filtrer les colonnes nécessaires
file_path = "experimentations_5G.csv"  
data = pd.read_csv(
    file_path, 
    sep=";", 
    encoding="cp1252", 
    usecols=["Région", "Usage - Mobilité connectée", 
             "Usage - Internet des objets", 
             "Usage - Ville intelligente", 
             "Usage - Réalité virtuelle", 
             "Usage - Télémédecine", 
             "Usage - Industrie du futur", 
             "Usage - Technique ou R&D", 
             "Usage - Autre"]
)

# Supprimer les lignes où "Région" est manquante
data = data.dropna(subset=["Région"])

# Supprimer les espaces en trop dans la colonne "Région"
data["Région"] = data["Région"].str.strip()

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

# Ajouter la légende et afficher
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Usages', fontsize=9)
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------------------------------



# Programme 5 : Bande Fréquence 
#--------------------------------------------------------------------------------------------------------

# importation du fichier csv uniquement des colonne bande de fréquences
data = pd.read_csv("experimentations_5G.csv", sep=";", encoding="cp1252", usecols=["Bande de fréquences"])

# mise à zéro des colonne vide
data = data.fillna(0)


counts = data["Bande de fréquences"].value_counts()

# calcul du pourcentage
pourcentages = (counts / counts.sum()) * 100

#affichage du graphique en pie (camembert) 
plt.figure(figsize=(8, 8))
plt.pie(pourcentages, labels=pourcentages.index,autopct='%1.1f%%',  startangle=140,colors=plt.cm.tab20.colors 
)
# titre + affichage du graphique
plt.title("Répartition des bandes de fréquences (en %)", fontsize=16)
plt.show()
#--------------------------------------------------------------------------------------------------------


# Programmation : 6 de l'evolution dans le temps 
#--------------------------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------------------------

# Programmation de la carte Interactive
#--------------------------------------------------------------------------------------------------------

# Lecture des données
data = pd.read_csv("experimentations_5G.csv", sep=";", encoding="cp1252", usecols=["Expérimentateur", "Bande de fréquences", "Latitude", "Longitude", "Commune", "Code INSEE", "Région","Description"])

# Remplir les valeurs manquantes par 0
data = data.fillna(0)

# Partie carte de la France et des antennes 5G
data["Latitude"] = data["Latitude"].astype(str).str.replace(",", ".").astype(float)
data["Longitude"] = data["Longitude"].astype(str).str.replace(",", ".").astype(float)

# Initialisation de la carte centrée sur la France
france = folium.Map(location=[45.6, 3.351828], zoom_start=6)

# Ajout des markers pour chaque antenne
for _, row in data.iterrows():
    if row["Bande de fréquences"] == "26 GHz":
        colorping = "green"
    elif row["Bande de fréquences"] == "3,8 GHz":
        colorping = "orange"
    elif row["Bande de fréquences"] == "2,6 GHz TDD":
        colorping = "red"
    
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        tooltip=["Cliquez-ici ! Commune : ", row["Commune"],"Région", row["Région"], " Code INSEE : ", row["Code INSEE"]],
        popup=["Les Expérimentateurs : ", row["Expérimentateur"], f"Description : ", row["Description"]],
        icon=folium.Icon(color=colorping),
    ).add_to(france)

# Ajout de la légende à gauche de la carte avec un div HTML
legend_html = """
    <div style="position: fixed; 
                bottom: 10px; left: 10px; width: 160px; height: 120px; 
                background-color: white; border:2px solid grey; z-index:9999; 
                font-size: 12px; padding: 7px;">
        <b style="font-size: 10px;">Légende des bandes de fréquence</b><br>
        <i style="background-color: green; width: 20px; height: 20px; display: inline-block;"></i> 26 GHz<br>
        <i style="background-color: orange; width: 20px; height: 20px; display: inline-block;"></i> 3,8 GHz<br>
        <i style="background-color: red; width: 20px; height: 20px; display: inline-block;"></i> 2,6 GHz TDD
    </div>
"""
# Ajout de la légende dans la carte avec le HTML
france.get_root().html.add_child(folium.Element(legend_html))

# Afficher la carte
france.save("carte_antenne_5g.html")
france
#--------------------------------------------------------------------------------------------------------
