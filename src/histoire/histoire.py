from random import randint

class histoire:
    def __init__(self, text:str):
        self.text = text
        self.evenements = []

    def add_evenement(self, evenement:str):
        self.evenements.append(evenement)

    def get_text(self):
        return self.text
    
    def get_random_evenements(self):
        return self.evenements[randint(0, len(self.evenements)-1)]


# param lieux
# method creer_histoire
# random event
