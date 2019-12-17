import matplotlib.pyplot as plt
import numpy as np
from random import random


def partie(p):
    """Simule un duel  du jeu suivant :
        joueur A + 1 et joueur B  -1 avec une probabilité de p
        sinon joueur A +1 et joueur B -1
        Le duel s'arrete des qu'un joueur atteint 5
    """
    n = 0
    yA = 0
    listn = []
    listyA = []
    #modifier la condition d'entrée de boucle
    while yA != 0:
        #expérience aléatoire
        nombre_aleatoire = random()
        #modification de yA
        if nombre_aleatoire < p:
            "à compléter"
            #à compléter
        else:
            "à compléter"
            #à compléter
        n = n + 1
        listn.append(n)
        listyA.append(yA)
    #tracé du graphique
    plt.plot(listn, listyA, 'ro')
    plt.savefig("simulation-p{}.png".format(p))
    plt.grid()
    plt.axhline(0)
    plt.axvline(0)
    plt.title('Score du joueur A, p = {}'.format(p))
    plt.show()
    return n

def vainqueur(p):
    """Simule un duel du jeu suivant :
        joueur A + 1 et joueur B  -1 avec une probabilité de p
        sinon joueur A +1 et joueur B -1
        Le duel s'arrete des qu'un joueur atteint 5
       Retourne 1 si A vainqueur et 0 sinon
    """
    #à compléter