import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import folium
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Charger les données pour les programmes
file_path = "experimentations_5G.csv"

# Créer la fenêtre tkinter
fenetre = tk.Tk()
fenetre.title("Graphiques 5G")

# Conteneur pour les graphiques
frame_graphique = tk.Frame(fenetre, borderwidth=2, relief="solid")
frame_graphique.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Fonction pour nettoyer les anciens graphiques
def nettoyer_graphique():
    for widget in frame_graphique.winfo_children():
        widget.destroy()

# Fonction pour afficher un graphique avec un canvas dans Tkinter
def afficher_graphique(fig):
    canvas = FigureCanvasTkAgg(fig, master=frame_graphique)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def antenne_region(file_path):
    data = pd.read_csv(file_path, sep=";", encoding="cp1252", usecols=["Région"])
    data = data.fillna("Non assigné")
    data["Région"] = data["Région"].astype(str)

    region_counts = data["Région"].value_counts()

    fig, ax = plt.subplots(figsize=(12, 8))
    region_counts.plot(kind="bar", color="red", ax=ax)
    ax.set_title("Répartition des antennes 5G par région", fontsize=16)
    ax.set_xlabel("Régions", fontsize=14)
    ax.set_ylabel("Nombre d'antennes", fontsize=14)
    ax.set_xticklabels(region_counts.index, rotation=45, ha="right")
    plt.tight_layout()

    afficher_graphique(fig)

def experimentation_5G(file_path):
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

    fig, ax = plt.subplots(figsize=(12, 6))

    bars = ax.bar(usage_totals.index, usage_totals.values, color='skyblue', edgecolor='black')
    for index, value in enumerate(usage_totals):
        ax.text(index, value + 0.5, str(int(value)), ha='center', fontsize=10, color='black')

    ax.set_title('Nombre de projets par expérimentation 5G', fontsize=14)
    ax.set_ylabel('Nombre de projets', fontsize=12)
    ax.set_xticklabels(usage_totals.index, rotation=45, ha='right', fontsize=10)
    ax.set_xlabel("Type d'expérimentation", fontsize=12)
    plt.tight_layout()

    afficher_graphique(fig)

def techno_region(file_path):
    data = pd.read_csv(file_path, sep=";", encoding="cp1252", usecols=[
        "Région", "Techno - Massive MIMO", "Techno - Beamforming/beamtracking",
        "Techno - Duplexage temporel (mode TDD)", "Techno - Mode de fonctionnement NSA (Non Stand Alone)",
        "Techno - Mode de fonctionnement SA (Stand Alone)", "Techno - Synchronisation de réseaux",
        "Techno - Network slicing", "Techno - Small cells", "Techno - Accès dynamique au spectre",
        "Techno - 5G, 6G…"])
    data = data.dropna(subset=["Région"])
    data["Région"] = data["Région"].str.strip()

    region_totals = data.groupby("Région").sum()
    region_percentages = region_totals.div(region_totals.sum(axis=1), axis=0) * 100

    x_positions = np.arange(len(region_percentages))
    colors = plt.cm.tab20(np.linspace(0, 1, len(region_percentages.columns)))

    fig, ax = plt.subplots(figsize=(14, 8))
    bottoms = np.zeros(len(region_percentages))
    for i, usage in enumerate(region_percentages.columns):
        ax.bar(
            x_positions, region_percentages[usage], bottom=bottoms, color=colors[i], label=usage
        )
        bottoms += region_percentages[usage]

    ax.set_title('Répartition des technologies par région (en %)', fontsize=16)
    ax.set_ylabel('Pourcentage (%)', fontsize=12)
    ax.set_xlabel('Régions', fontsize=12)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(region_percentages.index, rotation=45, ha='right', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Technologies', fontsize=9)
    plt.tight_layout()
    plt.show()

    afficher_graphique(fig)

def usage_region(file_path):
    data = pd.read_csv(file_path, sep=";", encoding="cp1252", usecols=[
        "Région", "Usage - Mobilité connectée", "Usage - Internet des objets",
        "Usage - Ville intelligente", "Usage - Réalité virtuelle", "Usage - Télémédecine",
        "Usage - Industrie du futur", "Usage - Technique ou R&D", "Usage - Autre"])

    data = data.dropna(subset=["Région"])
    data["Région"] = data["Région"].str.strip()

    region_totals = data.groupby("Région").sum()
    region_percentages = region_totals.div(region_totals.sum(axis=1), axis=0) * 100

    x_positions = np.arange(len(region_percentages))
    colors = plt.cm.tab20(np.linspace(0, 1, len(region_percentages.columns)))

    fig, ax = plt.subplots(figsize=(14, 8))
    bottoms = np.zeros(len(region_percentages))
    for i, usage in enumerate(region_percentages.columns):
        ax.bar(
            x_positions, region_percentages[usage], bottom=bottoms, color=colors[i], label=usage
        )
        bottoms += region_percentages[usage]

    ax.set_title('Répartition des usages par région (en %)', fontsize=16)
    ax.set_ylabel('Pourcentage (%)', fontsize=12)
    ax.set_xlabel('Régions', fontsize=12)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(region_percentages.index, rotation=45, ha='right', fontsize=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Usages', fontsize=9)
    plt.tight_layout()
    plt.show()

    afficher_graphique(fig)

def frequence_camembert(file_path):
    data = pd.read_csv(file_path, sep=";", encoding="cp1252", usecols=["Bande de fréquences"])
    data = data.fillna(0)

    counts = data["Bande de fréquences"].value_counts()
    percentages = (counts / counts.sum()) * 100

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(percentages, labels=percentages.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
    ax.set_title("Répartition des bandes de fréquences (en %)", fontsize=16)

    afficher_graphique(fig)

def araigne_usage_techno(file_path):
    tech_data = pd.read_csv(
        file_path,
        sep=";",
        encoding="cp1252",
        usecols=["Région", "Techno - Massive MIMO", "Techno - Beamforming/beamtracking",
                 "Techno - Duplexage temporel (mode TDD)", "Techno - Mode de fonctionnement NSA (Non Stand Alone)",
                 "Techno - Mode de fonctionnement SA (Stand Alone)", "Techno - Synchronisation de réseaux",
                 "Techno - Network slicing", "Techno - Small cells", "Techno - Accès dynamique au spectre", "Techno - 5G, 6G…"]
    )
    usage_data = pd.read_csv(
        file_path,
        sep=";",
        encoding="cp1252",
        usecols=["Région", "Usage - Mobilité connectée", "Usage - Internet des objets",
                 "Usage - Ville intelligente", "Usage - Réalité virtuelle", "Usage - Télémédecine",
                 "Usage - Industrie du futur", "Usage - Technique ou R&D", "Usage - Autre"]
    )

    tech_data = tech_data.dropna(subset=["Région"])
    usage_data = usage_data.dropna(subset=["Région"])

    tech_data["Région"] = tech_data["Région"].str.strip()
    usage_data["Région"] = usage_data["Région"].str.strip()

    tech_data.iloc[:, 1:] = tech_data.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
    usage_data.iloc[:, 1:] = usage_data.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

    tech_totals = tech_data.groupby("Région").sum()
    usage_totals = usage_data.groupby("Région").sum()

    total_technologies = len(tech_data.columns) - 1
    total_usages = len(usage_data.columns) - 1

    tech_proportions = (tech_totals > 0).sum(axis=1) / total_technologies * 100
    usage_proportions = (usage_totals > 0).sum(axis=1) / total_usages * 100

    combined_proportions = pd.concat([tech_proportions, usage_proportions], axis=1)
    combined_proportions.columns = ['Technologies', 'Usages']

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    num_vars = len(combined_proportions)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    values_tech = combined_proportions['Technologies'].tolist() + [combined_proportions['Technologies'][0]]
    values_usage = combined_proportions['Usages'].tolist() + [combined_proportions['Usages'][0]]

    ax.plot(angles, values_tech, color='tab:blue', linewidth=2, linestyle='solid', label='Technologies')
    ax.fill(angles, values_tech, color='tab:blue', alpha=0.25)

    ax.plot(angles, values_usage, color='tab:orange', linewidth=2, linestyle='solid', label='Usages')
    ax.fill(angles, values_usage, color='tab:orange', alpha=0.25)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(combined_proportions.index, fontsize=12, ha='center')

    ax.set_title('Comparaison des proportions de technologies et usages par région', fontsize=14, va='bottom')
    ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1))

    afficher_graphique(fig)

def evolution_temps(file_path):
    data = pd.read_csv(file_path, sep=";", encoding="cp1252")
    data['Début'] = pd.to_datetime(data['Début'], errors='coerce')
    filtered_data = data.dropna(subset=['Début'])
    filtered_data['Année_Début'] = filtered_data['Début'].dt.year

    experiments_per_year = filtered_data['Année_Début'].value_counts().sort_index()

    # Créer la figure et les axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Tracer le graphique
    ax.plot(experiments_per_year.index, experiments_per_year.values, marker='o', linestyle='-', color='r')
    ax.set_title("Évolution temporelle des expérimentations 5G", fontsize=14)
    ax.set_xlabel("Année", fontsize=12)
    ax.set_ylabel("Nombre d'expérimentations", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_xticks(experiments_per_year.index)
    ax.set_xticklabels(experiments_per_year.index, rotation=45)
    plt.tight_layout()

    # Afficher le graphique dans Tkinter
    afficher_graphique(fig)

def folium_map(file_path):
    data = pd.read_csv(file_path, sep=";", encoding="cp1252", usecols=["Expérimentateur", "Bande de fréquences", "Latitude", "Longitude", "Commune", "Code INSEE", "Région", "Description"])
    data = data.fillna(0)
    data["Latitude"] = data["Latitude"].astype(str).str.replace(",", ".").astype(float)
    data["Longitude"] = data["Longitude"].astype(str).str.replace(",", ".").astype(float)

    france = folium.Map(location=[45.6, 3.351828], zoom_start=6)

    for _, row in data.iterrows():
        if row["Bande de fréquences"] == "26 GHz":
            colorping = "green"
        elif row["Bande de fréquences"] == "3,8 GHz":
            colorping = "orange"
        elif row["Bande de fréquences"] == "2,6 GHz TDD":
            colorping = "red"

        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            tooltip=f"Commune: {row['Commune']}, Région: {row['Région']}, Code INSEE: {row['Code INSEE']}",
            popup=f"Expérimentateurs: {row['Expérimentateur']}, Description: {row['Description']}",
            icon=folium.Icon(color=colorping),
        ).add_to(france)

    legend_html = """
        <div style="position: fixed; 
                    bottom: 10px; left: 10px; width: 160px; height: 120px; 
                    background-color: white; border:2px solid grey; z-index:9999; 
                    font-size: 12px; padding: 7px;">
            <b>Légende des bandes de fréquence</b><br>
            <i style="background-color: green; width: 20px; height: 20px; display: inline-block;"></i> 26 GHz<br>
            <i style="background-color: orange; width: 20px; height: 20px; display: inline-block;"></i> 3,8 GHz<br>
            <i style="background-color: red; width: 20px; height: 20px; display: inline-block;"></i> 2,6 GHz TDD
        </div>
    """
    france.get_root().html.add_child(folium.Element(legend_html))    
    
    france.save("carte_antenne_5g.html")
    # Afficher un message indiquant que la carte est installée
    messagebox.showinfo("Carte Installée", "La carte a été installée avec succès ! Vous pouvez l'ouvrir en HTML. Le fichier HTML est dans votre répertoire la ou est le fichier python")

# Interface utilisateur avec Tkinter

# Ajouter un menu
menu_bar = tk.Menu(fenetre)
fenetre.config(menu=menu_bar)
menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Appuyer pour ouvrir le menu", menu=menu)
menu.add_command(label="Antennes par région", command=lambda: [nettoyer_graphique(), antenne_region(file_path)])
menu.add_command(label="Expérimentations 5G", command=lambda: [nettoyer_graphique(), experimentation_5G(file_path)])
menu.add_command(label="Technologies par région", command=lambda: [nettoyer_graphique(), techno_region(file_path)])
menu.add_command(label="Usages par région", command=lambda: [nettoyer_graphique(), usage_region(file_path)])
menu.add_command(label="Répartition des fréquences", command=lambda: [nettoyer_graphique(), frequence_camembert(file_path)])
menu.add_command(label="Comparaison usages et techno", command=lambda: [nettoyer_graphique(), araigne_usage_techno(file_path)])
menu.add_command(label="Evolution du temps de la 5G", command=lambda: [nettoyer_graphique(), evolution_temps(file_path)])
menu.add_command(label="Télécharger la carte folium pour l'ouvrir en HTML", command=lambda: [nettoyer_graphique(), folium_map(file_path)])

fenetre.mainloop()
