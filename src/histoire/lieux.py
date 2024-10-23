from random import randint

class lieu:
    def __init__(self, nom:str, description:str):
        self.nom = nom
        self.description = description
        self.histoires = []
        
    def get_nom(self):
        return self.nom
    
    def get_description(self):
        return self.description
    
    def add_histoire(self, histoire):
        self.histoires.append(histoire)

    def get_random_histoire(self):
        return self.histoires[randint(0, len(self.histoires)-1)]