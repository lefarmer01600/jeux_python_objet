from src.histoire import lieux, event, histoire
from src.interaction import Combat
from src.personnage import inventaire, Personnages

import tkinter as tk
import json
import random, time

# Création des joueurs et des monstres
joueur1 = Personnages.Joueur(50, 10, 10)
joueur2 = Personnages.Joueur(50, 10, 10)
monstreNv1 = Personnages.Monstre(5, 20, 1)
monstreNv2 = Personnages.Monstre(10, 50, 1)

# Création des inventaires pour les joueurs
inventaire_joueur1 = inventaire.inventaire()
inventaire_joueur2 = inventaire.inventaire()

# fichiers JSON
json_lieu_foret = "src/lieux/foret.json"
json_lieu_maisonAbandonnee = "src/lieux/maison_abandonnee.json"
json_lieu_montagne = "src/lieux/montagne.json"
json_lieu_prairie = "src/lieux/prairie.json"

def loadJson(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

DictForet = loadJson(json_lieu_foret)
DictMaisonAbandonnee = loadJson(json_lieu_maisonAbandonnee)
DictMontagne = loadJson(json_lieu_montagne)
DictPrairie = loadJson(json_lieu_prairie)

# fenêtres
root = tk.Tk()
root.title("Jeu à Choix Multiples")
Histoire = tk.Tk()
Histoire.title("Interactions")
evenements = tk.Tk() # Fenêtre pour les événements : jeter des bombes / prendre une potion
evenements.title("Evénements")

# Question et options
options = [DictForet, DictMaisonAbandonnee, DictMontagne, DictPrairie]
texteBoutons = [
    "Entrer dans la forêt",
    "Entrer dans la maison abandonnée",
    "Se téléporter à la montagne",
    "Entrer dans la prairie"
]

def createFrame(fenetre):
    text_frame = tk.Frame(fenetre)
    text_frame.pack(pady=10)

    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text.pack()

    scrollbar.config(command=text.yview)
    return text_frame, scrollbar, text

(frame1, scrollbar1, text1) = createFrame(root)
(frame2, scrollbar2, text2) = createFrame(Histoire)
(frame3, scrollbar3, text3) = createFrame(evenements)



# _event : pour créer un objet event
def _event(evenement):
    return event.event(evenement['nom'], evenement['description'], evenement['type'], evenement['caracteristiques'])

# Event : ---------- en cours d'implémentation ----------
def Event(evenement):
    Evt = _event(evenement)
    text2.insert("1.0", Evt.get_name() + "\n\n")
    text2.insert("1.0", "Description : " + Evt.description + "\n")
    text2.insert("1.0", "Type : " + Evt.type + "\n")
    if Evt.type == 'combat':
        text2.insert("1.0", "Fight!\n")
        combat = Combat.Combat([joueur1, joueur2], [monstreNv1, monstreNv2])
        combat.tour_de_jeu()

        text1.insert("1.0", "Points de vie joueur 1 : "+str(joueur1.point_de_vie)+" \n")
        text1.insert("1.0", "Points de vie joueur 2 : "+str(joueur2.point_de_vie)+"\n")
        text1.insert("1.0", "Points de vie monstre NV1 : "+str(monstreNv1.point_de_vie)+"\n")
        text1.insert("1.0", "Points de vie monstre NV2 :"+str(monstreNv2.point_de_vie)  +"\n")
    text2.insert("1.0", "--------------------------------\n")

# testEvent : créer les boutons pour les évènements
def testEvent(EvtList):
    for Evt in EvtList:
        tk.Button(Histoire, text=Evt['description'], command=lambda var=Evt: Event(var)).pack(pady=20)

# displayPlace : affiche le lieu où l'on se trouve
def displayPlace(DictLieu, lieu):

    text1.insert("1.0", lieu.get_description() + "\n\n")
    lieu.add_histoire(DictLieu)
    hist = lieu.get_random_histoire()
    hist = histoire.histoire(hist['description'])
    for i in range(len(DictLieu['histoire'])):
        for evt in DictLieu['histoire'][i]['evenement']:
            Event(evt)
        testEvent(DictLieu['histoire'][i]['evenement'])

# Créer les boutons radio pour les options
for i in range(len(options)):
    
    lieu = lieux.lieu(options[i]['nom'], options[i]['description'])
    tk.Button(root, text=texteBoutons[i], command=lambda opt=options[i], lieu=lieu: displayPlace(opt, lieu)).pack(pady=20)
    

def monstreCible() :
    return random.choice([monstreNv1, monstreNv2])

if joueur1.est_vivant():
    monstre = monstreCible()
    if monstre.est_vivant() :
        tk.Button(evenements, text="Joueur 1 : Lancer une bombe", command=lambda var=joueur1: joueur1.utiliser_bombe(monstre)).pack(pady=20)
        text3.insert("1.0", "Points de vie monstre attaqué : "+str(monstre.point_de_vie)+" \n")

if joueur2.est_vivant():
    monstre = monstreCible()
    if monstre.est_vivant() :
        tk.Button(evenements, text="Joueur 2 : Lancer une bombe", command=lambda var=joueur2: joueur2.utiliser_bombe(monstre)).pack(pady=20)
        text3.insert("0.0", "Points de vie monstre attaqué : "+str(monstre.point_de_vie)+" \n")

if joueur1.est_vivant() :
        tk.Button(evenements, text="Joueur 1 : utiliser une potion", command=lambda var=joueur1: joueur1.utiliser_potion()).pack(pady=20)
        text3.insert("1.0", "Points de vie joueur 1 : "+str(joueur1.point_de_vie)+" \n")

if joueur2.est_vivant() :
        tk.Button(evenements, text="Joueur 1 : utiliser une potion", command=lambda var=joueur2: joueur2.utiliser_potion()).pack(pady=20)
        text3.insert("1.0", "Points de vie joueur 2 : "+str(joueur2.point_de_vie)+" \n")
root.mainloop()
Histoire.mainloop()
