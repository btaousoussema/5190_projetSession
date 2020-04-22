from datetime import datetime


class Contrevenant:
    def __init__(self, proprietaire, categorie, etablissement, adresse,
                 ville, description, date_infraction,
                 date_jugement, montant):
        self.proprietaire = proprietaire
        self.categorie = categorie
        self.etablissement = etablissement
        self.adresse = adresse
        self.ville = ville
        self.description = description
        self.date_infraction = self.transform_date(date_infraction)
        self.date_jugement = self.transform_date(date_jugement)
        if (self.date_infraction is None) or (self.date_jugement is None):
            print(date_jugement + " " + date_infraction)
        self.montant = montant

    def print(self):
        print(self.proprietaire, self.categorie, self.etablissement,
              self.adresse, self.adresse, self.ville, self.description,
              self.date_infraction, self.date_jugement, self.montant)

    def transform_date(self, date):
        date_parsed = str(date).split(" ")
        mois = self.traduire_mois(date_parsed[1])
        return datetime.strptime(date_parsed[0] + mois + date_parsed[2],
                                 '%d%B%Y').strftime('%Y-%m-%d')

    def traduire_mois(self, mois):
        if mois == "janvier":
            return "January"
        elif mois == "février":
            return "February"
        elif mois == "mars":
            return "March"
        elif mois == "avril":
            return "April"
        elif mois == "mai":
            return "May"
        elif mois == "juin":
            return "June"
        elif mois == "juillet":
            return "July"
        elif mois == "août":
            return "August"
        elif mois == "septembre":
            return "September"
        elif mois == "octobre":
            return "October"
        elif mois == "novembre":
            return "November"
        elif mois == "décembre":
            return "December"
        else:
            print(mois)
            return None
