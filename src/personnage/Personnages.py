from random import randint

class De:
    def jeter_de(self):
        return randint(1, 6)

class Joueur:
    def __init__(self, point_de_vie):
        self.point_de_vie = point_de_vie
        self.de = De()

    def est_vivant(self):
        return self.point_de_vie > 0

    def jeter_de(self):
        return self.de.jeter_de()

    def attaquer(self, monstre):
        de_joueur = self.jeter_de()
        de_monstre = monstre.jeter_de()
        if de_joueur >= de_monstre:
            monstre.recoit_degat()

    def recoit_degat(self, degats):
        if self.jeter_de() > 2:
            self.point_de_vie -= degats

class MonstreNiveau1:
    def __init__(self, degats):
        self.degats = degats
        self.est_vivant = True
        self.de = De()

    def jeter_de(self):
        return self.de.jeter_de()

    def attaquer(self, joueur):
        de_monstre = self.jeter_de()
        de_joueur = joueur.jeter_de()
        if de_monstre > de_joueur:
            joueur.recoit_degat(self.degats)

    def recoit_degat(self):
        self.est_vivant = False

class MonstreNiveau2(MonstreNiveau1):
    def __init__(self, degats, sort):
        super().__init__(degats)
        self.sort = sort

    def attaquer(self, joueur):
        super().attaquer(joueur)
        if self.jeter_de() == 6:
            joueur.recoit_degat(self.sort)

# Exemple d'utilisation
joueur = Joueur(10)
monstre1 = MonstreNiveau1(3)
monstre2 = MonstreNiveau2(4, 2)

# Simuler une attaque
joueur.attaquer(monstre1)
monstre1.attaquer(joueur)
monstre2.attaquer(joueur)

print(f"Joueur vivant: {joueur.est_vivant()}, Points de vie: {joueur.point_de_vie}")
print(f"Monstre 1 vivant: {monstre1.est_vivant}")
print(f"Monstre 2 vivant: {monstre2.est_vivant}")