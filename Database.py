import sqlite3

import IdNotUniqueError
from contravention_db import ContraventionDb
from contrevenant_db import ContrevenantDb


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
                                        (contrevenant.proprietaire,)).fetchone()
        cursor.execute(("insert into contravention(proprietaire_id, description, date_infraction, date_jugement, "
                       "montant) values(?, ?, ?, ?, ?)"), (proprietaire_id[0], contrevenant.description,
                                                            contrevenant.date_infraction, contrevenant.date_jugement,
                                                            contrevenant.montant))
        connection.commit()

    def recherche_nom(self,recherche):
        connection = self.get_connection()
        cursor = connection.cursor()
        query = cursor.execute("Select * from contrevenant where etablissement like ?", ('%' + recherche + '%',)).fetchall()
        Contrevenants = []
        for elem in query:
            contrevenant = ContrevenantDb(elem[0], elem[1], elem[2], elem[3], elem[4],
                                        elem[5])
            contraventions = self.get_all_contraventions(contrevenant.id)
            contrevenant.ajouter_contraventions(contraventions)
            Contrevenants.append(contrevenant)
        return Contrevenants

    def recherche_proprietaire(self, recherche):
        connection = self.get_connection()
        cursor = connection.cursor()
        query = cursor.execute("Select * from contrevenant where proprietaire like ?",
                               ('%' + recherche + '%',)).fetchall()
        Contrevenants = []
        for elem in query:
            contrevenant = ContrevenantDb(elem[0], elem[1], elem[2], elem[3], elem[4],
                                          elem[5])
            contraventions = self.get_all_contraventions(contrevenant.id)
            contrevenant.ajouter_contraventions(contraventions)
            Contrevenants.append(contrevenant)
        return Contrevenants

    def recherche_adresse(self, recherche):
        connection = self.get_connection()
        cursor = connection.cursor()
        query = cursor.execute("Select * from contrevenant where adresse like ?",
                               ('%' + recherche + '%', )).fetchall()
        Contrevenants = []
        for elem in query:
            contrevenant = ContrevenantDb(elem[0], elem[1], elem[2], elem[3], elem[4],
                                          elem[5])
            contraventions = self.get_all_contraventions(contrevenant.id)
            contrevenant.ajouter_contraventions(contraventions)
            Contrevenants.append(contrevenant)
        return Contrevenants

    def get_all_contraventions(self, id):
        connection = self.get_connection()
        cursor = connection.cursor()
        query = cursor.execute("Select * from contravention where proprietaire_id = ?", (id,)).fetchall()
        contraventions = []
        for elem in query:
            contravention = ContraventionDb(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5])
            contraventions.append(contravention)
        return contraventions