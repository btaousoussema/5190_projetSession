import json

# Cette classe représente les contrevenants, issues de la base de données.


class ContrevenantDb(dict):
    def __init__(self, id, proprietaire, categorie, etablissement, adresse,
                 ville):
        self.id = id
        self.proprietaire = proprietaire
        self.categorie = categorie
        self.etablissement = etablissement
        self.adresse = adresse
        self.ville = ville
        self.contraventions = []

    def set_contraventions(self, contraventions):
        self.contraventions = contraventions

    def ajouter_contravention(self, contraventions):
        if type(contraventions) == list:
            for contravention in contraventions:
                self.contraventions.append(contravention)
        else:
            self.contraventions.append(contraventions)

    def print(self):
        print(self.id, self.proprietaire, self.categorie, self.etablissement,
              self.adresse, self.ville)

    def to_dict(self):
        return {"id": self.id, "proprietaire": self.proprietaire,
                "categorie": self.categorie,
                "etablissement": self.etablissement, "adresse": self.adresse,
                "ville": self.ville,
                "contraventions": json.dumps([ob.to_dict() for ob in
                                              self.contraventions]),
                "nombre_contraventions": len(self.contraventions)}

    def __eq__(self, other):
        return self.id == other.id
