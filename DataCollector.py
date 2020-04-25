import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

import yaml

import IdNotUniqueError
from Contrevenant import Contrevenant
from Database import Database
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def get_data():
    url = 'http://donnees.ville.montreal.qc.ca/dataset/a5c1f0b9-261f-4247-99d8-f28da5000688/resource/92719d9b-8b' \
          'f2-4dfd-b8e0-1021ffcaee2f/download/inspection-aliments-contrevenants.xml'

    donnes = urllib.request.urlopen(url).read()

    tree = ET.fromstring(donnes)
    contrevenants = tree.findall('contrevenant')
    nouveau_contrevenants = []
    for contevenant in contrevenants:
        contrev = Contrevenant(contevenant[0].text, contevenant[1].text,
                               contevenant[2].text,  contevenant[3].text,
                               contevenant[4].text, contevenant[5].text,
                               contevenant[6].text, contevenant[7].text,
                               contevenant[8].text)
        database = Database()
        database.get_connection()
        try:
            database.insert_contrevenant(contrev)
            nouveau_contrevenants.append(contrev.etablissement)
        except Exception:
            print("Ce contrevenant existe déjà.")
        database.insert_contravention(contrev)
    if len(nouveau_contrevenants) > 0:
        for c in nouveau_contrevenants:
            print(c)
        nom_fichier = "ex.yaml"
        email = lire_fichier(nom_fichier)
        if email is not None:
            envoyer_courriel(email, nouveau_contrevenants)


def lire_fichier(nom_fichier):
    with open("ex.yaml", 'r') as stream:
        try:
            date_load = yaml.safe_load(stream)
            return date_load["email"]
        except yaml.YAMLError as error:
            return None


def envoyer_courriel(email, contrevenants):
    source_address = '5190ouss@gmail.com'
    password = "cours5190"
    destination_address = email
    body = "Voici les nouveaux contrevenants qui sont apparus dans " \
           "la plus récente" \
           " collecte de données : "
    if len(contrevenants) > 0:
        body += contrevenants.pop(0)
    for name in contrevenants:
        body += ", " + name
    body += "."
    subject = "I send mails!"

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = source_address
    msg['To'] = destination_address
    msg['ReplyTo'] = "steve@uqam.ca"

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    print(source_address)
    server.login(source_address, password)
    text = msg.as_string()
    server.sendmail(source_address, destination_address, text)
    server.quit()
