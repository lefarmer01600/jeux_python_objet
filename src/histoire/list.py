from lieux import lieu
from histoire import histoire
from event import event

prairie = lieu("prairie", "Une prairie verdoyante et paisible où les monstres sont faibles")

tmp = histoire("Le chemin ce sépare en deux, vous avez deux options")
tmp.add_evenement(event("fôret", "pénetrer dans la fôret", "zone", "change_zone"))
tmp.add_evenement(event("prairie", "rester dans la prairie", "zone", "change_zone"))
tmp.add_evenement(event("blessure", "Vous marchez sur un piège dissimulé dans l'herbe haute.", "malus", "pv-20"))
tmp.add_evenement(event("embuscade", "Des bandits surgissent des buissons pour vous attaquer !", "combat", "combat_ennemi_boss"))
prairie.add_histoire(tmp)

tmp = histoire("Le chemin ce sépare en deux, vous avez deux options")
tmp.add_evenement(event("fôret", "pénetrer dans la fôret", "zone", "change_zone"))
tmp.add_evenement(event("prairie", "rester dans la prairie", "zone", "change_zone"))
tmp.add_evenement(event("portail", "Un portail apparaît devant vous, vibrant d'énergie.", "zone", "change_zone_portail"))

Ruines = lieu("Ruines", "Les ruines d'un ancien château, ayant vécu de nombreuses batailles")
tmp.add_evenement(event("ruines", "Vous trouvez une entrée menant à d'anciennes ruines.", "exploration", "nouvelle_zone_ruines"))
tmp.add_evenement(event("sorcier", "Un sorcier vous propose un marché étrange en échange de 50 pièces d'or.", "marchand", "gold-50, gain_potion"))
tmp.add_evenement(event("dragon", "Vous apercevez un dragon endormi au loin. Tenter de s'approcher ?", "risque", "combat_dragon, loot_légendaire"))
tmp.add_evenement(event("coffre mystère", "Vous trouvez un coffre entouré d'une aura étrange.", "bonus", "add_object_random"))




print(tmp.get_text())
for evenement in tmp.get_evenements():
    print(f"Nom: {evenement.name}, Description: {evenement.description}, Type: {evenement.type}, Caractéristiques: {evenement.caracteristiques}")

# tmp.add_evenement(event("coffre", "trouve un coffre et l'ouvre", "bonus", "add_object"))
# tmp.add_evenement(event("fôret", "pénetrer dans la fôret", "Nouvelle zone", "nouveaux ennemies"))
# tmp.add_evenement(event("ville", "pénetrer dans la ville", "Nouvelle zone", "nouveaux ennemies"))
# tmp.add_evenement(event("Quête", "Recevez une quête d'un pnj", "histoire", "si quête réussi +n gold et 1 items au choix"))
# tmp.add_evenement(event("faux coffre", "trouver un mimic", "Combat", "lance combat contre coffre et item rare si tuer"))
# tmp.add_evenement(event("Marque bénite", "Obtention d'une marque sacrée", "Obtention de stats", ""))

tmp.add_evenement(event("name", "description", "type", "caracteristiques"))
# remplace les paramaetre : tmp.add_evenement(event("coffre", "trouve un coffre et l'ouvre", "bonus", "add_object")) par ce qui est au dessus:



print(test.get_random_histoire().get_text())
print(test.get_random_histoire().get_random_evenements())