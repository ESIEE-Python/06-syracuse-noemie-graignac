#### Fonctions secondaires
# imports
"""Importer les fichiers nécessaires"""
from plotly.graph_objects import Scatter, Figure
### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """fonction de syracuse défintion"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )
    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################
def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    l = []

    # initialisation des variables
     # tant que la suite n'est pas terminée :
    while n!=1:
        l.append(n)
        #   - calcul du n suivant
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
    l.append(n)
    return l
def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    # votre code ici
    return len(l)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    # votre code ici
    n = 1
    while l[0]<l[n]:
        n+=1
    return n
def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    # votre code ici
    return max(l)
#### Fonction principale

def main():
    """
    Il faut appeler la fonction secondaire
    """
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr)-1)
    print(temps_de_vol_en_altitude(lsyr)-1)
    print(altitude_maximale(lsyr))
if __name__ == "__main__":
    main()
