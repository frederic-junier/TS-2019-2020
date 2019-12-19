import matplotlib.pyplot as plt
import numpy as np
from random import random


def simulation(p):
    """Simule un duel  du jeu suivant :
        joueur A + 1 et joueur B  -1 avec une probabilité de p
        sinon joueur A +1 et joueur B -1
     Retourne le nombre de parties nécessaires pour obtenir un vainqueur
    """
    #numéro de partie
    n = 0
    #ordonnée (score de A)
    yA = 0
    #liste des numéros de partie
    listn = []
    #liste des ordonnées
    listyA = []
    #modifier la condition d'entrée de boucle
    while yA != 5 and yA != -5:
        #expérience aléatoire
        nombre_aleatoire = random()
        #modification de yA
        if nombre_aleatoire < p:
            "à compléter"
            yA = yA + 1
        else:
            "à compléter"
            yA = yA - 1
        #mise à jour des listes d'abscisses et d'ordonnées
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

def simulation2(p):
    """Simule un duel  du jeu suivant :
        joueur A + 1 et joueur B  -1 avec une probabilité de p
        sinon joueur A +1 et joueur B -1
     Retourne le nombre de parties nécessaires pour obtenir un vainqueur sans générer de graphique
    """
    #numéro de partie
    n = 0
    #ordonnée (score de A)
    yA = 0
    #modifier la condition d'entrée de boucle
    while yA != 5 and yA != -5:
        #expérience aléatoire
        nombre_aleatoire = random()
        #modification de yA
        if nombre_aleatoire < p:
            "à compléter"
            yA = yA + 1
        else:
            "à compléter"
            yA = yA - 1
        #mise à jour des listes d'abscisses et d'ordonnées
        n = n + 1       
    return n

def vainqueur(p):
    """Simule un duel du jeu suivant :
        joueur A + 1 et joueur B  -1 avec une probabilité de p
        sinon joueur A +1 et joueur B -1
        Le duel s'arrete des qu'un joueur atteint 5
       Retourne 1 si A vainqueur et 0 sinon
    """
    #numéro de partie
    n = 0
    #ordonnée (score de A)
    yA = 0
    while yA != 5 and yA != -5:
        #expérience aléatoire
        nombre_aleatoire = random()
        #modification de yA
        if nombre_aleatoire < p:
            yA = yA + 1
        else:
            yA = yA - 1
    if yA == 5:
        return 1
    else:
        return 0

def frequenceA_echantillon(nbexp, p):
    """Retourne la fréquence de victoires de A
    sur un échantillon de nbexp duels
    """
    victoireA = 0
    for k in range(nbexp):
        victoireA = victoireA + vainqueur(p)
    return victoireA / nbexp

def frequenceB_echantillon(nbexp, p):
    return 1 - frequenceA_echantillon(nbexp, p)


def nombre_moyen_parties(nbexp, p):
    """Retourne le nombre moyen de parties
    sur un échantillon de nbexp duels"""
    nbParties = 0
    for k in range(nbexp):
        nbParties = nbParties + simulation2(p)
    return nbParties / nbexp
