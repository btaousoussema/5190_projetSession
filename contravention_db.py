import _json

class ContraventionDb(dict):
    def __init__(self, id, proprietaire, description, date_infraction, date_jugement, montant):
        self.id = id
        self.proprietaire = proprietaire
        self.description = description
        self.date_infraction = date_infraction
        self.date_jugement = date_jugement
        self.montant = montant

    def afficher(self):
        print(self.id, self.proprietaire, self.description, self.date_infraction, self.date_jugement, self.montant)

    def to_dict(self):
        return {"id":self.id, "proprietaire":self.proprietaire, "description":self.description,
                "date_infraction":self.date_infraction, "date_jugement":self.date_jugement, "montant":self.montant}

    def __eq__(self, other):
        return self.id == other.id