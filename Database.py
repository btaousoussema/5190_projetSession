import sqlite3

import IdNotUniqueError


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/contrevenant.db')
        return self.connection

    def insert_contrevenant(self, contrevenant):
        connection = self.get_connection()
        cursor = connection.cursor()
        if self.verify_idunique(contrevenant.proprietaire):
            cursor.execute(("insert into contrevenant(proprietaire, categorie, etablissement, adresse, ville)"
                            "values(?, ?, ?, ?, ?)"), (contrevenant.proprietaire, contrevenant.categorie,
                                                       contrevenant.etablissement, contrevenant.adresse,
                                                       contrevenant.ville))
            connection.commit()
        else:
            raise IdNotUniqueError


    def verify_idunique(self, proprietaire):
        connection = self.get_connection()
        cursor = connection.cursor()
        proprietaire = cursor.execute("Select id from contrevenant where proprietaire = ?", (proprietaire,)).fetchall()
        if len(proprietaire) > 0:
            return False
        return True

    def insert_contravention(self, contrevenant):
        connection = self.get_connection()
        cursor = connection.cursor()
        proprietaire_id = cursor.execute("Select id from contrevenant where proprietaire = ?",
                                         (contrevenant.proprietaire,)).fetchall()
        cursor.execute(("insert into contravention(proprietaire_id, description, date_infraction, date_jugement, "
                        "montant) values(?, ?, ?, ?, ?)"), (proprietaire_id[0], contrevenant.description,
                                                            contrevenant.date_infraction, contrevenant.date_jugement,
                                                            contrevenant.montant))
        connection.commit()
