from random import *

class inventaire:

    def __init__(self):
        self.liste_inventaire = []
    
    def ajouter_objet(self, objet):
        self.liste_inventaire.append(objet)
        print(self.liste_inventaire)    

    def supprimer_objet(self, index):
        self.liste_inventaire.pop(index)
        print(self.liste_inventaire)