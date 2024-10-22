


class event:
    def __init__(self, name, description, type, caracteristiques):
        self.name = name
        self.description = description
        self.type = type
        self.caracteristiques = caracteristiques

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_type(self):
        return self.type

    def get_caracteristiques(self):
        return self.caracteristiques
