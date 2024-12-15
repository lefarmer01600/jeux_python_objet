from src.histoire import lieux, event, histoire

import tkinter as tk
import json
import random

json_lieu_foret = "lieux/foret.json"
json_lieu_maisonAbandonnee = "lieux/maison_abandonnee.json"
json_lieu_montagne = "lieux/montagne.json"
json_lieu_prairie = "lieux/prairie.json"
# test = event.event()
def loadJson(file_path) :
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

DictForet = loadJson(json_lieu_foret)
DictMaisonAbandonnee = loadJson(json_lieu_maisonAbandonnee)
DictMontagne = loadJson(json_lieu_montagne)
DictPrairie = loadJson(json_lieu_prairie)
print("\n")
print("forêt:", DictForet['description'])

# fenêtres
root = tk.Tk()
root.title("Jeu à Choix Multiples")
FrameHistoire = tk.Tk()
FrameHistoire.title("Interactions")


root.title("Interaction")

def selectPlace(DictLieu) :
    return DictLieu['description']

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
(frame2, scrollbar2, text2) = createFrame(FrameHistoire)

def _event(evenement):
    evt = event.event(evenement['nom'], evenement['description'], evenement['type'], evenement['caracteristiques'])
    return evt

def displayPlace(DictLieu, lieu):
    text1.insert("1.0", lieu.get_description()+"\n\n")
    lieu.add_histoire(DictLieu)
    hist = lieu.get_random_histoire()
    hist = histoire.histoire(hist['description'])
    for i in range(len(DictLieu['histoire'])):
        for j in range(len(DictLieu['histoire'][i]['evenement'])):
            e = _event(DictLieu['histoire'][i]['evenement'][j])
            text2.insert("1.0", e.get_name()+"\n\n")

# # Créer les boutons radio pour les options
for i in range(len(options)):
    lieu = lieux.lieu(options[i]['nom'], options[i]['description'])
    radio_button = tk.Button(root, text=texteBoutons[i], command=lambda opt=options[i], lieu=lieu: displayPlace(opt,lieu))
    radio_button.pack(pady=20)
    


# # Bouton pour soumettre la réponse
# boutonForet = tk.Button(root, text="Entrer dans la forêt", command=selectPlace(DictForet))
# boutonForet.pack(pady=20)

# # Lancer la boucle principale
root.mainloop()