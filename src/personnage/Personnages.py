from random import randint

class De:
    def jeter_de(self):
        return randint(1, 6)

# créer un joueur avec des points de vie ainsi qu'un stock de potions et de bombes
class Joueur:
    def __init__(self, point_de_vie, potions, bombes):
        self.point_de_vie = point_de_vie
        self.potions = potions
        self.bombes = bombes
        self.de = De()

    # si pv supérieur à 0 le joueur est encore en vie
    def est_vivant(self):
        return self.point_de_vie > 0

    # le joueur jete son dé
    def jeter_de(self):
        return self.de.jeter_de()

    # si le dé du joueur est supérieur au dé du monstre, le monstre perd 2 point de vie
    def attaquer(self, monstre):
        if self.jeter_de() >= monstre.jeter_de():
            monstre.recoit_degat(2)  # Inflige 2 points de dégâts

    # si le dé du monstre est supérieur à 1 le joueur prend des dégâts. PS : nombre de dégâts dans méthode attaquer
    def recoit_degat(self, degats):
        if monstre.jeter_de() > 1:
            self.point_de_vie -= degats

    # si potion encore en stock, potion donne 3 point de vie et enlève 1 au stock
    def utiliser_potion(self):
        if self.potions > 0:
            self.point_de_vie += 3
            self.potions -= 1
            print(f"Vous avez utilisé une potion. PV = {self.point_de_vie}, Potions restantes = {self.potions}")
        else:
            print("Vous n'avez plus de potions.")

    # si bombe encore en stock, bombe inflige 3 point de vie et enlève 1 au stock
    def utiliser_bombe(self, monstre):
        if self.bombes > 0:
            monstre.recoit_degat(3)
            self.bombes -= 1
            print(f"Vous avez utilisé une bombe. Bombes restantes = {self.bombes}")
        else:
            print("Vous n'avez plus de bombes.")

class Monstre:
    def __init__(self, degats, point_de_vie, niveaux):
        self.degats = degats * niveaux
        self.point_de_vie = point_de_vie * niveaux
        self.niveaux = niveaux
        self.de = De()

    # si pv supérieur à 0 le monstre est encore en vie
    def est_vivant(self):
        return self.point_de_vie > 0

    # le monstre jete son dé
    def jeter_de(self):
        return self.de.jeter_de()

    # si le dé du monstre est supérieur au dé du joueur, le joueur perd le nombre de point de vie que vaut dégât quand on appel la classe (ici c'est 3)
    def attaquer(self, joueur):
        if self.jeter_de() > joueur.jeter_de():
            joueur.recoit_degat(self.degats)

    # si le dé du joueur est supérieur à 1 le monstre prend des dégâts. PS : nombre de dégâts dans méthode attaquer
    def recoit_degat(self, degats):
        if joueur.jeter_de() > 1:
            self.point_de_vie -= degats

    # récupère ce qu'il y a dans la méthode attaquer et si le dé du monstre est égal à 6, il inflige 4+2 = 6 dégâts
    # def attaquer(self, joueur):
    #     super().attaquer(joueur)
    #     if self.jeter_de() == 6:
    #         joueur.recoit_degat(self.sort)

joueur = Joueur(30, 2, 1)
monstres = [Monstre(3, 6, 1), Monstre(3, 6, 2)]

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
        if not monstre.est_vivant():
            break
    elif choix == "rien":
        print("Vous avez choisi de ne rien utiliser.")

    while joueur.est_vivant() and monstre.est_vivant():
        joueur.attaquer(monstre)
        if monstre.est_vivant():
            monstre.attaquer(joueur)
        
        # Afficher l'état après chaque tour
        print(f"État du joueur : Points de vie = {joueur.point_de_vie}")
        print(f"État du monstre : Points de vie = {monstre.point_de_vie}")

if joueur.est_vivant():
    print("Le joueur a battu tous les monstres.")
else:
    print(f"Joueur vivant: {joueur.est_vivant()}, Points de vie: {joueur.point_de_vie}")
if monstre.est_vivant():
    print("Le joueur à été battu")
else:
    print(f"Monstre vivant: {monstre.est_vivant()}, Points de vie: {monstre.point_de_vie}")