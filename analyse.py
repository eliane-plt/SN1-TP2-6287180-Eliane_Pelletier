"""
description:
    Les 4 lignes servent à lire le fichier CSV et de le nettoyer
paramètre:
    le paramètre utiliser tout au long de la tp est le dataframe
import:
    J'ai importé mathplotlib et pandas pour m'aider à faire la Tp
"""

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('C:/Users/Eliane Pelletier/Downloads/comptage_velo_2024.csv', low_memory=False) #a changer lorsque à la maison
df=df.dropna() #nettoyer le fichier

""" section Quelles sont les variables présentes dans le jeu de données?
description:
    retourne la liste des noms des colonnes (variables) présent dans le Dataframe
valeurs retournées: 
    le code retourne une liste de chaînes de caractère qui son les noms des colonnes
"""

def variable(df):
    return list(df.columns)
print ("voici les variables présentes dans le jeu de donnnées?: ")
print(variable(df))

""" section Combien y a-t-il d'enregistrements (lignes) dans le jeu de données?
description: 
    Cette fonction calcule le nombre d'enregistrement de date différente dans le fichier 
variable:
    ligne: nombre de ligne différent dans la colomne 
valeurs retournées: 
    le code retourne le nombre de ligne mais avec une fonction len pour que ça soit un nombre entier   
"""

def enregistrement(df):
    ligne = df.groupby("date")
    print()
    print(f"nombre d'enregistrements dans le jeu de données: ")
    return len(ligne)
print(enregistrement(df))

"""section Quel est le plus grand nombre de vélos comptés en une seule fois? À quel moment cela s'est-il produit (date, heure, emplacement)?
description:
    identification de la ligne qui correspond au plus grand nombre de passage par vélo
variables:
    max_decroissante: C'est le nb_passages en ordre décroissant
    max: C'est la première ligne du max_decroissant
valeurs retournées:
    le nombre, la date, l'heure, la longitude et la latitude de la ligne du plus grand nombre de passage sont retourné
"""

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

""" section Quel est le total de vélos comptés pour l'année 2024?
description:
    La fonction calcule la somme totale des vélos comptés pour l'année 2024
variables: 
    total: C'est ;a somme des valeurs de la colonne nb_passage
valeurs retournées:
    le nombre total de passages enregistré
"""

def total(df):
    print()
    print("nombre total de vélos pour l'année 2024:")
    total = df["nb_passages"].sum()
    return total
print(f"{total(df)} vélos")

""" section Combien y a-t-il de compteurs de vélos différents?
description:
    Cette fonction compte le nombre d'itentifiant différent de compteur son présent
    dans la colone id_compteur
variables: 
    Compteur: nombre d'identifiant trouvées
valeurs retournées:
    Le nombre de compteur différent
"""

def compteurs(df):
    print()
    print("nombre de compteurs de vélo différents:")
    compteur = len(df["id_compteur"].unique())
    return compteur
print(f"{compteurs(df)} compteurs")

"""section Quelle est la fréquence de prise des données dans le fichier (ex : environ toutes les heures, toutes les 15 minutes, etc.)?
description:
    Cette fonction trouve l'intervalle de temps (la fréquence) entre chaque données
    en analysant la partie des minutes (caractère 3 à 5) de la colonne heure
variable: 
    valeur_unique Tableau des minutes unique sous forme de chaine de caractères
    valeur_trier: liste triée des minutes uniques sous forme d'entiers
    a: la deuxième valeur de minute unique 
    b: la troisième valeur de minute unique 
* J'ai utiliser la deuxième et troisième pour pas avoir de 0*
  mais techiquement ça devrait revenir au même pour ensuite calculer le delta
  delta = final - initial (C'était sa ma logique) *
    intervalle: la différence entre b et a qui est la fréquence en minutes
valeurs retournées: 
    affiche la fréquence estimé en minutes
"""

def fréquence(df):
    print()
    print ("fréquence des prises de données: ")
    df["fréquence"] = df["heure"].str.slice(3,5)
    valeur_unique = df["fréquence"].unique()
    valeur_trier = sorted(map(int,valeur_unique))
    a= valeur_trier[1]
    b= valeur_trier[2]
    intervalle = b-a

    print(f" à chaque {intervalle} minutes")

fréquence(df)

"""graphique nombre moyen de passages par heure (colonne)
description:
    Cette fonction va crée puis affichier un graphique a barre qui montre 
    le nombre de passage moyen par heures (24h) de la journée
variables: 
    moyennes: série de Pandas qui contient le comptage moyen des passages par heure  
fichiers produits:
    un graphique à barre de Matplolib ou les x sont les heure et y nombre de passage
"""

def graph_heure(df):
    df["heure_simple"]=df["heure"].str.slice(0,2).map(int)
    moyenne = df.groupby("heure_simple")["nb_passages"].mean()
    moyenne.plot(kind="bar")
    plt.xlabel("heure")
    plt.ylabel("comptage moyen par compteur")
    plt.title("nombre moyen de passage par heure")
    plt.savefig("graph_heure.png")
    plt.close()
graph_heure(df)

"""graphique nombre total de passages par mois
description:
    Cette fonction crée un graphique à barres qui représente le nombre 
    total de passages par mois.
variables: 
    dict_mois: Dictionnaire qui sert a mapper les numéro de mois aux 
    noms des mois
    mois: Série Pandas qui contient le total de passage regroupé par numéro 
    de mois
fichiers produits:
    un graphique à barre qui à les mois en x et le nombre total de passage en y 
"""

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
    plt.savefig("graph_passages.png")
    plt.close()


graph_passages(df)

""" graphique nombre de passage par heure et par mois
description: 
    Cette fonction crée et affiche un graphique linéaire qui montre les évolution pour 
    chaque mois du nombre de passage par heure  
variables:
    df_pivot: Table croisée des heures simple en index et numéro_mois en colonnes 
    qui contient la somme des passage 
fichiers produits: 
    Un graphique avec plusieur fonction linéaire qui ont tous le mois en x et nombre
    de passage en y 
"""

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
    plt.savefig("graph_passage_heure.png")
    plt.close()

graph_passages_heure(df)

"""graphique localisation des compteur de vélos
description: 
    Crée et afficher un nuage de point où la taille des points
    est proportionnelle au nombre moyen de passages par compteur qui 
    indique la longitude et latitude 
variables: 
    x: séries Pandas des longitudes moyennes regroupé dans id_compteur 
    y: Séries Pandas des latitudes moyennes regroupées dans id_compteur 
    z: Série Pandans des passages moyens regroupées dans id_compteur
fichiers produits:
    un graphique avec des point qui a tout les variables à leur endroit 
    ( ex: x sur la ligne des x... ) 

"""

def graph_localisation(df):
    x = df.groupby("id_compteur")["longitude"].mean()
    y = df.groupby("id_compteur")["latitude"].mean()
    z = df.groupby("id_compteur")["nb_passages"].mean()
    plt.scatter(x, y, z*10, alpha=0.5)
    plt.xlabel("longitude")
    plt.ylabel("latitude")
    plt.title("Localisation des compteur de vélos\n(taille proportionnelle au nombre moyen de passages)")
    plt.grid(axis = "both", linestyle = "--", linewidth = 0.5)
    plt.savefig("graph_localisation.png")
    plt.close()
graph_localisation(df)
