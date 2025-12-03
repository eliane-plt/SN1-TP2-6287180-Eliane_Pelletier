import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('C:/Users/Eliane Pelletier/Downloads/comptage_velo_2024.csv', low_memory=False) #a changer lorsque à la maison
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
    max_decroissant = df.sort_values(by="nb_passages", ascending=False)
    max = max_decroissant.iloc[0]
    print("nombre de vélo:",max["nb_passages"])
    print("date:"          ,max["date"])
    print("heure:"         ,max["heure"])
    print("longitude:"     ,max["longitude"])
    print("latitude:"      ,max["latitude"])
maximum(df)

""" section Quel est le total de vélos comptés pour l'année 2024?"""
def total(df):
    print()
    print("nombre total de vélos pour l'année 2024:")
    total = df["nb_passages"].sum()
    return total
print(f"{total(df)} vélos")

""" section Combien y a-t-il de compteurs de vélos différents?"""
def compteurs(df):
    print()
    print("nombre de compteurs de vélo différents:")
    compteur = len(df["id_compteur"].unique())
    return compteur
print(f"{compteurs(df)} compteurs")

"""section Quelle est la fréquence de prise des données dans le fichier (ex : environ toutes les heures, toutes les 15 minutes, etc.)?"""
def fréquence(df):
    print()
    print ("fréquence des prises de données: ")

    minutes = df["heure"].str.slice(0,2).map(int)*60+df["heure"].str.slice(3,5).map(int)

    jours = df["date"].str.slice(8,10).map(int)

    df["date_heure"]= jours * 1440 + minutes

    df = df.sort_values(by="date_heure")

    df["diff"] = df["date_heure"].diff()

    interval = df["diff"].mode()[0]

    print(interval,"minutes")
fréquence(df)

"""graphique nombre moyen de passages par heure (colonne)"""

def graph_heure(df):
    df["heure_simple"]=df["heure"].str.slice(0,2).map(int)
    moyenne = df.groupby("heure_simple")["nb_passages"].mean()
    moyenne.plot(kind="bar")
    plt.xlabel("heure")
    plt.ylabel("comptage moyen par compteur")
    plt.title("nombre moyen de passage par heure")
    plt.show()
graph_heure(df)

"""graphique nombre total de passages par mois"""
def graph_passages(df):
    dict_mois = {
        1: "janvier",
        2: "février",
        3: "mars",
        4: "avril",
        5: "mai",
        6: "juin",
        7: "juillet",
        8: "aout",
        9: "septembre",
        10: "octobre",
        11: "novembre",
        12: "decembre",
    }
    df["numéro_mois"]=df["date"].str.slice(5,7).map(int)
    mois = df.groupby("numéro_mois")["nb_passages"].sum()
    mois.index=mois.index.map(dict_mois)
    mois.plot(kind="bar")
    plt.xlabel("mois")
    plt.ylabel("nombre total de passages")
    plt.title("nombre total de passage par mois")
    plt.show()


graph_passages(df)


""" graphique nombre de passage par heure et par mois"""
def graph_passages_heure(df):
    df["heure_simple"]=df["heure"].str.slice(0,2).map(int)
    df["numéro_mois"] = df["date"].str.slice(5, 7).map(int)
    df_pivot = df.pivot_table(values = "nb_passages",
                              index = "heure_simple",
                              columns = "numéro_mois",
                              aggfunc="sum")
    df_pivot.plot()
    plt.xlabel("heure")
    plt.ylabel("nombre total de passages")
    plt.title("nombre total de passages par heure et par  mois")
    plt.grid(axis = "both", linestyle = "--", linewidth = 0.5)
    plt.legend(title="mois", labels = ["Jan",
                                       "Fev",
                                       "Mar",
                                       "Avr",
                                       "Mai",
                                       "Juin",
                                       "Juil",
                                       "Aoû",
                                       "Sep",
                                       "Oct",
                                       "Nov",
                                       "Déc",])
    plt.show()

graph_passages_heure(df)

"""graphique localisation des compteur de vélos"""

def graph_localisation(df):
    x = df.groupby("id_compteur")["longitude"].mean()
    y = df.groupby("id_compteur")["latitude"].mean()
    z = df.groupby("id_compteur")["nb_passages"].mean()
    plt.scatter(x, y, z*10, alpha=0.5)
    plt.xlabel("longitude")
    plt.ylabel("latitude")
    plt.title("Localisation des compteur de vélos\n(taille proportionnelle au nombre moyen de passages)")
    plt.grid(axis = "both", linestyle = "--", linewidth = 0.5)
    plt.show()
graph_localisation(df)
