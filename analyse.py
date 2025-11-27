import pandas as pd
df = pd.read_csv('C:/Users/6287180/Downloads/comptage_velo_2024.csv', low_memory=False) #a changer lorsque à la maison
df=df.dropna() #nettoyer le fichier

""" section Quelles sont les variables présentes dans le jeu de données?"""
def variable(df):
    return list(df.columns)
print ("voici les variables présentes dans le jeu de donnnées?: ")
print(variable(df))

""" section Combien y a-t-il d'enregistrements (lignes) dans le jeu de données?"""

def enregistrement(df):
    ligne = df.groupby("date")
    print()
    print(f"nombre d'enregistrements dans le jeu de données: ")
    return len(ligne)
print(enregistrement(df))


"""section Quel est le plus grand nombre de vélos comptés en une seule fois? À quel moment cela s'est-il produit (date, heure, emplacement)?"""

def maximum(df):
    print()
    print("plus grand nombre de vélo comptées en une seul fois:")
    maximum = df.groupby("nb_passages")[["date", "heure", "longitude", "latitude"]].max()
    return maximum

print(maximum(df))

""" section Quel est le total de vélos comptés pour l'année 2024?"""
""" section Combien y a-t-il de compteurs de vélos différents?"""
"""section Quelle est la fréquence de prise des données dans le fichier (ex : environ toutes les heures, toutes les 15 minutes, etc.)?"""
"""graphique nombre moyen de passages par heure"""
"""graphique nombre moyen de passages par mois"""
"""graphique nombre de passage par heur et par mois"""
"""graphique localisation des compteur de vélos"""