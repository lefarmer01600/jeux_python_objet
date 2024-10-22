from lieux import lieu
from histoire import histoire
from event import event

prairie = lieu("prairie", "Une prairie verdoyante et paisible où les monstres sont faibles")

tmp = histoire("Le chemin ce sépare en deux, vous avez deux options")
tmp.add_evenement(event("fôret", "pénetrer dans la fôret", "zone", "change_zone"))
tmp.add_evenement(event("prairie", "rester dans la prairie", "zone", "change_zone"))
prairie.add_histoire(tmp)

tmp = histoire("Le chemin ce sépare en deux, vous avez deux options")
tmp.add_evenement(event("fôret", "pénetrer dans la fôret", "zone", "change_zone"))
tmp.add_evenement(event("prairie", "rester dans la prairie", "zone", "change_zone"))



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