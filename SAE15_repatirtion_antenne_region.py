import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("experimentations_5G.csv", sep=";", encoding="cp1252", usecols=["Région"])

data = data.fillna("Non assigné")
data["Région"] = data["Région"].astype(str)

# Compter le nombre d'antennes par région
region_counts = data["Région"].value_counts()

# Créer un histogramme
plt.figure(figsize=(12, 8))
region_counts.plot(kind="bar", color="skyblue")
plt.title("Répartition des antennes 5G par région", fontsize=16)
plt.xlabel("Régions", fontsize=14)
plt.ylabel("Nombre d'antennes", fontsize=14)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()