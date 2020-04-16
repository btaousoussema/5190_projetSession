import os
import re

from flask import Flask
from flask import request
from flask import render_template
from flask import g
from flask import jsonify
from flask_json_schema import JsonSchema
from flask_json_schema import JsonValidationError
from Database import Database
import json

from Inspection import Inspection
from schemas import infraction_insert_schema
from schemas import infraction_delete_schema

app = Flask(__name__, static_url_path="", static_folder="static")
schema = JsonSchema(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.errorhandler(JsonValidationError)
def validation_error(e):
    errors = [validation_error.message for validation_error in e.errors]
    return jsonify({'error': e.message, 'errors': errors}), 400


@app.route('/')
def page_accueil():
    contrevenants = get_db().get_all_contrevenant()
    print(len(contrevenants))
    return render_template('accueil.html', contrevenants=contrevenants)


# @app.route('/')
# def page_accueil():
#     return render_template('accueil.html')

@app.route('/rechercheNom')
def recherche_nom():
    nom = request.args.get('recherche_nom')
    contrevenants_db = get_db().recherche_nom(nom)
    # for i in contrevenants:
    #     print(contrevenants[i])
    # print("-----------------------------", contrevenants_db[0])
    # print("\n Les contravenntionsssss \n" , contrevenants_db[0].contraventions)
    return render_template('detail.html', contrevenants=contrevenants_db)


@app.route('/rechercheProprietaire')
def recherche_proprietaire():
    proprietaire = request.args.get('recherche_proprietaire')
    contrevenants_db = get_db().recherche_proprietaire(proprietaire)
    # for i in contrevenants:
    #     print(contrevenants[i])
    # print("-----------------------------", contrevenants_db[0])
    # print("\n Les contravenntionsssss \n" , contrevenants_db[0].contraventions)
    return render_template('detail.html', contrevenants=contrevenants_db)


@app.route('/rechercheRue')
def recherche_rue():
    adresse = request.args.get('recherche_rue')
    contrevenants_db = get_db().recherche_adresse(adresse)
    # for i in contrevenants:
    #     print(contrevenants[i])
    # print("-----------------------------", contrevenants_db[0])
    # print("\n Les contravenntionsssss \n" , contrevenants_db[0].contraventions)
    return render_template('detail.html', contrevenants=contrevenants_db)


@app.route('/rechercheDate')
def rechercher_selon_date():
    du = request.args.get('du')
    au = request.args.get('au')
    print("Resultat du true or false: ", (verifier_date(du) and verifier_date(au)))
    if verifier_date(du) and verifier_date(au):
        contrevenants_db = get_db().contrevenant_entre_deux_dates(du, au)
        for i in contrevenants_db:
            print(len(i.contraventions))
        data = json.dumps([ob.to_dict() for ob in contrevenants_db])
        print(data)
        return data
    else:
        return {}
        # message = "Les dates doivent être en format AAAA-MM-JJ. "
        # return render_template("accueil.html", message=message, du=du, au=au)

    # for v in j:
    #     print(len(v["contraventions"]))
    # print("----------------------",contrevenants_db.contraventions)
    # return render_template('detail.html', contrevenants=contrevenants_db)
    # datetime.strptime('02 novembre 2017', '%d %B %Y')
    return data

# Route A6
@app.route("/getContraventions")
def get_contraventions():
    id = request.args.get('id')
    contraventions = get_db().get_all_contraventions(id)
    j = json.dumps([ob.to_dict() for ob in contraventions])
    return j

#Route C1, il faut ordonner en décroissant tho!!
@app.route('/getContrevenant')
def get_contrevenant():
    contrevenants = get_db().get_all_contrevenant()
    json_data = nombre_infractions(contrevenants)
    return json_data


@app.route('/inspection')
def formulaire_inspection():
    print("on est dans le GET.")
    return render_template('inspection.html')


@app.route('/api/inspection', methods=['POST'])
@schema.validate(infraction_insert_schema)
def ajouter_inspection():
    nom = request.json.get('nom')
    adresse = request.json.get('adresse')
    ville = request.json.get('ville')
    date_visite = request.json.get('date_visite')
    nom_plaignant = request.json.get('nom_plaignant')
    description = request.json.get('description')
    message_erreur = verifier_champs(nom, adresse, ville, nom_plaignant, description)
    print(message_erreur)
    if verifier_date(date_visite) and message_erreur == "":
        inspection = Inspection(nom, adresse, ville, date_visite, nom_plaignant, description)
        id = get_db().insert_inspection(inspection)
        #return render_template("confirmation.html", inspection=inspection)
        print(id)
        return json.dumps({"id": int(id), "nom":inspection.nom, "adresse": inspection.adresse, "ville": inspection.ville, "date_visite": inspection.date_visite,
                      "nom_plaignant":inspection.nom_plaignant, "description": inspection.description}),200
    else:
        return json.dumps(message_erreur), 400


@app.route('/api/inspection/<id>', methods=['DELETE'])
def delete_inspection(id):
    inspection = get_db().get_inspection(id)
    if inspection is None:
        print("None")
        return "", 404
    else:
        get_db().delete_inspection(id)
        return "", 200


@app.route('/confirmation.html/<id>')
def confirmer(id):
    inspection = get_db().get_inspection(id)
    return render_template('confirmation.html', inspection=inspection)

def verifier_date(date):
    date_parse = date.split("-")
    if str(date_parse[0]).isdigit() and str(date_parse[1]).isdigit() and str(date_parse[2]).isdigit():
        return len(date_parse[0]) == 4 and len(date_parse[2]) == 2 and len(date_parse[1]) == 2 and \
               verifier_mois(date_parse[1]) and verifier_jour(date_parse[2])
    else:
        return False


def verifier_mois(mois):
    return 1 <= int(mois) < 13


def verifier_jour(jour):
    return 1 <= int(jour) <= 31


def nombre_infractions(contrevenants):
    donnes = []
    for contrevenant in contrevenants:
        donnes.append({"contrevenant": contrevenant.etablissement,
                       "nombre_contraventions": len(contrevenant.contraventions)})
    json_data = json.dumps(donnes)
    return json_data

def verifier_champs(nom, adresse, ville, nom_plaignant, description):
    message = ""
    erreur = valider_texte(nom, "nom de l'établissement")
    if erreur is not None:
        message += erreur
    erreur = valider_non_vide(adresse, "adresse")
    if erreur is not None:
        message += erreur
    erreur = valider_non_vide(ville, "ville")
    if erreur is not None:
        message += erreur
    erreur = valider_texte(nom_plaignant, "nom")
    if erreur is not None:
        message += erreur
    erreur = valider_non_vide(description, "description")
    if erreur is not None:
        message += erreur
    return message


def valider_texte(valeur, champ):
    message = valider_non_vide(valeur, champ)
    if message is None:
        valeur_parsed = valeur.split("-")
        for string in valeur_parsed:
            if not re.match('^[a-zA-Z]+$', string):
                message = "Il ne faut pas qu'il y ait des caractères " \
                          "spéciaux pour les champs, sauf les '-'. "
    return message


def valider_non_vide(valeur, champ):
    message = None
    if valeur is None or valeur == "":
        message = "Il ne faut pas que le champ " + champ + " soit vide. "
    return message

# if __name__== "__main__":
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
