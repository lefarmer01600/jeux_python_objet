from random import randint

class De:
    def jeter_de(self):
        return randint(1, 6)

class Joueur:
    def __init__(self, point_de_vie, potions, bombes):
        self.point_de_vie = point_de_vie
        self.potions = potions
        self.bombes = bombes
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
        if self.jeter_de() > 1:
            self.point_de_vie -= degats

    def utiliser_potion(self):
        if self.potions > 0:
            self.point_de_vie += 3
            self.potions -= 1
            print(f"Vous avez utilisé une potion. Points de vie actuels : {self.point_de_vie}. Potions restantes : {self.potions}")
        else:
            print("Vous n'avez plus de potions.")

    def utiliser_bombe(self, monstre):
        if self.bombes > 0:
            monstre.recoit_degat()
            self.bombes -= 1
            print(f"Vous avez utilisé une bombe. Bombes restantes : {self.bombes}")
        else:
            print("Vous n'avez plus de bombes.")

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
joueur = Joueur(10, 2, 1)  # Le joueur commence avec 2 potions et 1 bombe
monstres = [MonstreNiveau1(3), MonstreNiveau2(4, 2)]

for monstre in monstres:
    if not joueur.est_vivant():
        print("Le joueur a été vaincu.")
        break

    # Choisir un objet avant le combat
    choix = input("Choisissez un objet (potion/bombe/rien) : ").strip().lower()
    if choix == "potion":
        joueur.utiliser_potion()
    elif choix == "bombe":
        joueur.utiliser_bombe(monstre)
        if not monstre.est_vivant:
            continue
    elif choix == "rien":
        print("Vous avez choisi de ne rien utiliser.")

    while joueur.est_vivant() and monstre.est_vivant:
        joueur.attaquer(monstre)
        if monstre.est_vivant:
            monstre.attaquer(joueur)
        
        # Afficher l'état après chaque tour
        print(f"État du joueur : Points de vie = {joueur.point_de_vie}")
        print(f"État du monstre : Vivant = {monstre.est_vivant}")

if joueur.est_vivant():
    print("Le joueur a battu tous les monstres.")
else:
    print(f"Joueur vivant: {joueur.est_vivant()}, Points de vie: {joueur.point_de_vie}"),