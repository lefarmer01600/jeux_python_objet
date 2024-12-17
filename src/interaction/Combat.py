from random import *
from src.personnage.inventaire import *
from src.personnage.Personnages import *


# la classe Combat est responsable de la gestion des tours de jeu et de l'interaction entre les joueurs et les monstres

class Combat:
    """
    La classe Combat est responsable de la gestion des tours de jeu et de l'interaction entre les joueurs et les monstres

    Attributes
    ----------
    joueurs : list
        liste des joueurs
    monstres : list
        liste des monstres

    Methods
    -------
    tour_de_jeu()
        méthode responsable de l'interaction entre les joueurs et les monstres
    joueurs_attaquent()
        méthode responsable de l'interaction des joueurs
    monstres_attaquent()
        méthode responsable de l'interaction des monstres
    choisir_cible(cibles)
        méthode responsable de choisir une cible parmi une liste de cibles
    verifier_etat_combat()
        méthode responsable de vérifier si le combat est terminé

"""
    def __init__(self, joueurs, monstres):
        self.joueurs = joueurs
        self.monstres = monstres

    # la méthode tour_de_jeu est responsable de l'interaction entre les joueurs et les monstres
    def tour_de_jeu(self):
        print("--- Début du tour ---")
        self.joueurs_attaquent()
        self.verifier_etat_combat()
        self.monstres_attaquent()
        self.verifier_etat_combat()

    # la méthode joueurs_attaquent est responsable de l'interaction des joueurs
    def joueurs_attaquent(self):
        for Player in self.joueurs:
            if Player.est_vivant():
                cible = self.choisir_cible(self.monstres)
                Player.attaquer(cible)

    # la méthode monstres_attaquent est responsable de l'interaction des monstres
    def monstres_attaquent(self):
        for mob in self.monstres:
            if mob.est_vivant():
                cible = self.choisir_cible(self.joueurs)
                mob.attaquer(cible)

    # la méthode choisir_cible est responsable de choisir une cible parmi une liste de cibles
    def choisir_cible(self, cibles):
        cibles_vivantes = [c for c in cibles if c.est_vivant()]
        return random.choice(cibles_vivantes) if cibles_vivantes else None

    # la méthode verifier_etat_combat est responsable de vérifier si le combat est terminé
    def verifier_etat_combat(self):
        if self.joueurs.est_vivant() == False:
            print("Tous les joueurs sont morts. Les monstres gagnent !")
            exit()
        elif self.monstres.est_vivant() == False:
            print("Tous les monstres sont morts. Les joueurs gagnent !")
            exit()
        else:
            print("Le combat continue...")