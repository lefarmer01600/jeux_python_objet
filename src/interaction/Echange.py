from src.personnage.inventaire import *
from src.personnage.Personnages import *

class Echange:
    """
    Classe représentant un échange entre le joueur et le marchand.
    ---------
    Attributs:
    ----------

    inventaire_joueur : Inventaire
        L'inventaire du joueur.
    inventaire_marchand : Inventaire
        L'inventaire du marchand.

    Méthodes:
    ---------
    proposer_echange():
        Propose un échange entre le joueur et le marchand en affichant les objets disponibles
        et en permettant au joueur de choisir un objet à échanger.
    """
    def __init__(self, inventaire_joueur, inventaire_marchand):
        self.inventaire_joueur = inventaire_joueur
        self.inventaire_marchand = inventaire_marchand

    # Méthode permettant de proposer un échange entre le joueur et le marchand
    def proposer_echange(self):  
        print("--- Objets disponibles chez le marchand ---")
        for index in range(len(self.inventaire_marchand.liste_inventaire)):
            item = self.inventaire_marchand.liste_inventaire[index]
            print(f"{index + 1}. {item}")

        print("--- Vos objets ---")
        for index in range(len(self.inventaire_joueur.liste_inventaire)):
            item = self.inventaire_joueur.liste_inventaire[index]
            print(f"{index + 1}. {item}")


        try:
            choix_joueur = int(input("Entrez le numéro de l'objet que vous souhaitez échanger (chez vous) : ")) - 1
            choix_marchand = int(input("Entrez le numéro de l'objet que vous souhaitez obtenir (chez le marchand) : ")) - 1

            if choix_joueur < len(self.inventaire_joueur.liste_inventaire) and choix_marchand < len(self.inventaire_marchand.liste_inventaire):
                objet_joueur = self.inventaire_joueur.liste_inventaire[choix_joueur]
                objet_marchand = self.inventaire_marchand.liste_inventaire[choix_marchand]

                self.inventaire_joueur.supprimer_objet(objet_joueur)
                self.inventaire_joueur.ajouter_objet(objet_marchand)

                self.inventaire_marchand.supprimer_objet(objet_marchand)
                self.inventaire_marchand.ajouter_objet(objet_joueur)

                print(f"Echange reussi ! \n Vous avez obtenu {objet_marchand} en échange de {objet_joueur}.")
            else:
                print("Echange impossible : choix invalide.")
        except ValueError:
            print("Entrée invalide, veuillez entrer des numéros valides.")