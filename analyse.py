
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('C:/Users/Eliane Pelletier/Downloads/comptage_velo_2024.csv', low_memory=False) #a changer lorsque à la maison
df=df.dropna()



def variable(df):

    """
    description:
      retourne la première ligne des noms des colonnes
    valeurs retournées:
        le code retourne les noms de chaque colonnes
    """

    return list(df.head(1))
print ("voici les variables présentes dans le jeu de donnnées: ")
print(variable(df))



def enregistrement(df):

    """
    description:
        Cette fonction calcule le nombre d'enregistrement de dates différentes dans le fichier
    variable:
        ligne: nombre de ligne différent dans la colomne
    valeurs retournées:
        le code retourne le nombre de ligne mais avec une fonction len pour que ça soit un nombre entier
    """

    ligne = df.groupby("date")
    print()
    print(f"nombre d'enregistrements dans le jeu de données: ")
    return len(ligne)
print(enregistrement(df))



def maximum(df):

    """
    description:
        identification de la ligne qui correspond au plus grand nombre de passage par vélo
    variables:
        max_decroissante: C'est le nombre de passages en ordre décroissant (plus grand au plus petit)
        max: C'est la première valeur de l'ordre décroissant de la ligne
    valeurs retournées:
        le nombre, la date, l'heure, la longitude et la latitude de la ligne du plus grand nombre de passage sont retourné
    """

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



def total(df):

    """
    description:
        La fonction calcule la somme totale des vélos comptés pour l'année 2024
    variables:
        total: C'est la somme des valeurs de la colonne nb_passage
    valeurs retournées:
        le nombre total de passages enregistré
    """

    print()
    print("nombre total de vélos pour l'année 2024:")
    total = df["nb_passages"].sum()
    return total
print(f"{total(df)} vélos")



def compteurs(df):

    """
    description:
        Cette fonction compte le nombre d'itentifiant différent de compteur son présent
        dans la colone id_compteur
    variables:
        Compteur: nombre d'identifiant trouvées
    valeurs retournées:
        Le nombre de compteur différent
    """

    print()
    print("nombre de compteurs de vélo différents:")
    compteur = len(df["id_compteur"].unique())
    return compteur
print(f"{compteurs(df)} compteurs")



def fréquence(df):

    """
    description:
        Cette fonction trouve l'intervalle de temps (la fréquence) entre chaque données
        en analysant la partie des minutes (caractère 3 à 5) de la colonne heure
    variable:
        valeur: tous les valeur différente dans ma liste
    valeurs retournées:
        affiche le tableau des fréquences de prise de donées
    """

    print()
    print ("fréquence des prises de données: ")
    df["fréquence"] = df["heure"].str.slice(3,5)
    valeur = df["fréquence"].unique()
    print(valeur)
    print("il est possible de constater qu'il y a un intervalle de 15 minutes entre chaque prise de donner")

fréquence(df)



def graph_heure(df):

    """
    description:
        Cette fonction va crée puis afficher un graphique à barre qui montre
        le nombre de passage moyen par heures (24h) de la journée
    variables:
        moyennes: contient le comptage moyen des passages par heure
    fichiers produits:
        un graphique à barre où les x sont les heures et y le nombre de passages
    """

    df["heure_simple"]=df["heure"].str.slice(0,2)
    moyenne = df.groupby("heure_simple")["nb_passages"].mean()
    moyenne.plot(kind="bar")
    plt.xlabel("heure")
    plt.ylabel("comptage moyen par compteur")
    plt.title("nombre moyen de passage par heure")

    plt.savefig("graph_heure.png")
    plt.close()
graph_heure(df)



def graph_passages(df):

    """
    description:
        Cette fonction crée un graphique à barres qui représente le nombre
        total de passages par mois.
    variables:
        dict_mois: Dictionnaire qui sert a associer les numéro de mois aux
        noms des mois
        mois: contient le total de passage regroupé par numéro
        de mois et fait la sommation
    fichiers produits:
        un graphique à barre qui à les mois en x et le nombre total de passages en y
    """
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

    df["numéro_mois"]=df["date"].str.slice(5,7)
    mois= dict_mois.values()
    nb_passage = df.groupby("numéro_mois")["nb_passages"].sum()
    plt.bar(mois, nb_passage)
    plt.xlabel("mois")
    plt.ylabel("nombre total de passages")
    plt.title("nombre total de passage par mois")

    plt.savefig("graph_passages.png")
    plt.close()


graph_passages(df)


def graph_passages_heure(df):

    """
    description:
        Cette fonction crée et affiche un graphique linéaire qui montre les évolution pour
        chaque mois du nombre de passage par heure
    variables:
        df_pivot: créée un tableau croisée dynamique pour calculer la somme des passages
    fichiers produits:
        Un graphique avec plusieur fonction linéaire qui ont tous le mois en x et nombres
        de passages en y
    """

    df["heure_simple"]=df["heure"].str.slice(0,2)
    df["numéro_mois"] = df["date"].str.slice(5, 7)
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



def graph_localisation(df):

    """
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
