# importation des librairie
import pandas as pd 
import matplotlib.pyplot as plt

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