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
    print("Resultat du true or false: ", (verifier_date(du) and verifier_date(au)) )
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
    #print("----------------------",contrevenants_db.contraventions)
    #return render_template('detail.html', contrevenants=contrevenants_db)
    #datetime.strptime('02 novembre 2017', '%d %B %Y')
    return data

@app.route("/getContraventions")
def get_contraventions():
    id = request.args.get('id')
    contraventions = get_db().get_all_contraventions(id)
    j = json.dumps([ob.to_dict() for ob in contraventions])
    return j


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

# if __name__== "__main__":
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)