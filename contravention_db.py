class ContraventionDb:
    def __init__(self, id, proprietaire, description, date_infraction, date_jugement, montant):
        self.id = id
        self.proprietaire = proprietaire
        self.description = description
        self.date_infraction = date_infraction
        self.date_jugement = date_jugement
        self.montant = montant