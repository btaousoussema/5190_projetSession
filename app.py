from flask import Flask
from flask import request
from flask import render_template
from flask import g
from Database import Database

app = Flask(__name__, static_url_path="", static_folder="static")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.route('/')
def page_accueil():
    return render_template('accueil.html')

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