def proposer_echange(self):
        print("--- Objets disponibles chez le marchand ---")
        for i, item in enumerate(self.inventaire_marchand.liste_inventaire):
            print(f"{i + 1}. {item}")

        print("--- Vos objets ---")
        for i in range(len (self.inventaire_joueur.liste_inventaire)-1):
            print(f"{i + 1}. {item}")

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



