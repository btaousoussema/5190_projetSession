class ContrevenantDb:
    def __init__(self, id, proprietaire, categorie, etablissement, adresse, ville):
        self.id = id
        self.proprietaire = proprietaire
        self.categorie = categorie
        self.etablissement = etablissement
        self.adresse = adresse
        self.ville = ville

    def ajouter_contraventions(self, contraventions):
        self.contraventions = contraventions