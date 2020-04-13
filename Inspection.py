from datetime import datetime

class Inspection:
    def __init__(self, nom, adresse, ville, date_visite, nom_plaignant, description):
        self.nom = nom
        self.adresse = adresse
        self.ville = ville
        self.date_visite = date_visite
        self.nom_plaignant = nom_plaignant
        self.description = description


    def print(self):
        print(self.nom, self.adresse, self.ville, self.date_visite, self.nom_plaignant, self.description)

    def jsonify(self):
        return {"nom": self.nom, "adresse":self.adresse, "ville": self.ville, "date_visite":self.date_visite,
                "nom_plaignant": self.nom_plaignant, "description": self.description}