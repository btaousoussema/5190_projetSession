import os

from flask import Flask
from flask import request
from flask import render_template
from flask import g
from Database import Database
import json
app = Flask(__name__, static_url_path="", static_folder="static")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


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
    #print("-----------------------------", contrevenants_db[0])
    #print("\n Les contravenntionsssss \n" , contrevenants_db[0].contraventions)
    return render_template('detail.html', contrevenants=contrevenants_db)

@app.route('/rechercheProprietaire')
def recherche_proprietaire():
    proprietaire = request.args.get('recherche_proprietaire')
    contrevenants_db = get_db().recherche_proprietaire(proprietaire)
    # for i in contrevenants:
    #     print(contrevenants[i])
    #print("-----------------------------", contrevenants_db[0])
    #print("\n Les contravenntionsssss \n" , contrevenants_db[0].contraventions)
    return render_template('detail.html', contrevenants=contrevenants_db)

@app.route('/rechercheRue')
def recherche_rue():
    adresse = request.args.get('recherche_rue')
    contrevenants_db = get_db().recherche_adresse(adresse)
    # for i in contrevenants:
    #     print(contrevenants[i])
    #print("-----------------------------", contrevenants_db[0])
    #print("\n Les contravenntionsssss \n" , contrevenants_db[0].contraventions)
    return render_template('detail.html', contrevenants=contrevenants_db)

@app.route('/rechercheDate')
def rechercher_selon_date():
    du = request.args.get('du')
    au = request.args.get('au')
    contrevenants_db = get_db().contrevenant_entre_deux_dates(du, au)
    for i in contrevenants_db:
        print(len(i.contraventions))
    j = json.dumps([ob.to_dict() for ob in contrevenants_db])
    print(j)
    # for v in j:
    #     print(len(v["contraventions"]))
    #print("----------------------",contrevenants_db.contraventions)
    #return render_template('detail.html', contrevenants=contrevenants_db)
    #datetime.strptime('02 novembre 2017', '%d %B %Y')
    return j

@app.route("/getContraventions")
def get_contraventions():
    id = request.args.get('id')
    contraventions = get_db().get_all_contraventions(id)
    j = json.dumps([ob.to_dict() for ob in contraventions])
    return j


# if __name__== "__main__":
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)