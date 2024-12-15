from random import *
from src.personnage.inventaire import *
from src.personnage.Personnages import *

# la classe Combat est responsable de la gestion des tours de jeu et de l'interaction entre les joueurs et les monstres
class Combat:
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
        for joueur in self.joueurs:
            if not joueur.est_vivant():
                continue

            cible = self.choisir_cible(self.monstres)
            if cible:
                joueur.attaquer(cible)

    # la méthode monstres_attaquent est responsable de l'interaction des monstres
    def monstres_attaquent(self):
        for monstre in self.monstres:
            if not monstre.est_vivant():
                continue

            cible = self.choisir_cible(self.joueurs)
            if cible:
                monstre.attaquer(cible)

    # la méthode choisir_cible est responsable de choisir une cible parmi une liste de cibles
    def choisir_cible(self, cibles):
        cibles_vivantes = [c for c in cibles if c.est_vivant()]
        return random.choice(cibles_vivantes) if cibles_vivantes else None

    # la méthode verifier_etat_combat est responsable de vérifier si le combat est terminé
    def verifier_etat_combat(self):
        if not any(j.est_vivant() for j in self.joueurs):
            print("Tous les joueurs sont morts. Les monstres gagnent !")
            exit()
        if not any(m.est_vivant() for m in self.monstres):
            print("Tous les monstres sont morts. Les joueurs gagnent !")
            exit()