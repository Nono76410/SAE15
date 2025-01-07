import folium
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("experimentations_5G.csv", sep=";", encoding="cp1252", usecols=["Expérimentateur","Bande de fréquences","Latitude", "Longitude","Commune", "Code INSEE", "Région"])

data = data.fillna(0)


# partie carte de la france et des antennes 5g 

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
        tooltip=["Cliquez-ici ! Commune : ",row["Commune"]," Code INSEE : ",row["Code INSEE"] ],
        popup=["Les Expérimentateur : ",row["Expérimentateur"]," Et les bandes de fréquences : ",row["Bande de fréquences"] ],
        icon=folium.Icon(color=colorping),
    ).add_to(france)
france
