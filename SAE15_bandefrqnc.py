import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("experimentations_5G.csv", sep=";", encoding="cp1252", usecols=["Bande de fréquences"])

data = data.fillna(0)
# partie graphique

counts = data["Bande de fréquences"].value_counts()

pourcentages = (counts / counts.sum()) * 100

plt.figure(figsize=(8, 8))
plt.pie(pourcentages, labels=pourcentages.index,autopct='%1.1f%%',  startangle=140,colors=plt.cm.tab20.colors 
)

plt.title("Répartition des bandes de fréquences (en %)", fontsize=16)
plt.show()