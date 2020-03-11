

class Contrevenant:
    def __init__(self, proprietaire, categorie, etablissement, adresse, ville, description, date_infraction,
                 date_jugement, montant):
        self.proprietaire = proprietaire
        self.categorie = categorie
        self.etablissement = etablissement
        self.adresse = adresse
        self.ville = ville
        self.description = description
        self.date_infraction = date_infraction
        self.date_jugement = date_jugement
        self.montant = montant

    def print(self):
        print(self.proprietaire, self.categorie, self.etablissement, self.adresse, self.adresse, self.ville,
              self.description, self.date_infraction, self.date_jugement, self.montant)