from src.histoire import lieux, event, histoire
from src.interaction import Combat
from src.personnage import inventaire, Personnages

import tkinter as tk
import json

joueur1 = Personnages.Joueur(100, 10, 10)
joueur2 = Personnages.Joueur(100, 10, 10)
# commbat contient listes de joueurs et de monstres
"""
##### fonctions

# loadJson : récupérer un fichier Json et retourne un dictionnaire
# createFrame : créer une frame dans une fenêtre
# _event : pour créer un objet event
# Event : ---------- en cours d'implémentation ----------
# testEvent : créer les boutons pour les évènements
# displayPlace : affiche le lieu où l'on se trouve

"""





## fichiers JSON
json_lieu_foret = "lieux/foret.json"
json_lieu_maisonAbandonnee = "lieux/maison_abandonnee.json"
json_lieu_montagne = "lieux/montagne.json"
json_lieu_prairie = "lieux/prairie.json"

def loadJson(file_path) :
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

# # Question et options
# question = "Quelle est la capitale de la France?"
options = [DictForet, DictMaisonAbandonnee, DictMontagne, DictPrairie]
texteBoutons = [
    "Entrer dans la forêt",
    "Entrer dans la maison abandonnée",
    "Se téléporter à la montagne",
    "Entrer dans la prairie"
]
# correct_answer = "Paris"

# Créer un widget Text avec une barre de défilement
def createFrame(fenetre) :
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

def _event(evenement):
    evt = event.event(evenement['nom'], evenement['description'], evenement['type'], evenement['caracteristiques'])
    return evt

def Event(Evt) :
    text2.insert("1.0", "Description : "+Evt['description']+"\n")
    text2.insert("1.0", "Type : "+Evt['type']+"\n")
    text2.insert("1.0", "--------------------------------")

def testEvent(Evt) :
    j=0
    lengthEvt = len(Evt)
    radio_button = None
    while j<lengthEvt and radio_button == None :
        radio_button = tk.Button(Histoire, text=Evt[j]['description'], command=lambda var=Evt[j]:Event(var))
        radio_button.pack(pady=20)
        j+=1
    return

 
def displayPlace(DictLieu, lieu):
    text1.insert("1.0", lieu.get_description()+"\n\n")
    lieu.add_histoire(DictLieu)
    hist = lieu.get_random_histoire()
    hist = histoire.histoire(hist['description'])
    for i in range(len(DictLieu['histoire'])):
        #e = _event(DictLieu['histoire'][i]['evenement'])
#       text2.insert("1.0", e.get_name()+"\n\n")
        testEvent(DictLieu['histoire'][i]['evenement'])
        # text2.insert("1.0", DictLieu['histoire'][i]['texte'])

# # Créer les boutons radio pour les options
for i in range(len(options)):
    lieu = lieux.lieu(options[i]['nom'], options[i]['description'])
    radio_button = tk.Button(root, text=texteBoutons[i], command=lambda opt=options[i], lieu=lieu: displayPlace(opt,lieu))
    radio_button.pack(pady=20)

root.mainloop()
Histoire.mainloop()