import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

from Contrevenant import Contrevenant
from Database import Database

url = 'http://donnees.ville.montreal.qc.ca/dataset/a5c1f0b9-261f-4247-99d8-f28da5000688/resource/92719d9b-8b' \
      'f2-4dfd-b8e0-1021ffcaee2f/download/inspection-aliments-contrevenants.xml'

donnes = urllib.request.urlopen(url).read()
#uh = urllib.request.urlopen(url)
#data = uh.read()

tree = ET.fromstring(donnes)
contrevenants = tree.findall('contrevenant')
contrevenants_tableau = []

#print(lst)
#counts = tree.findall('.//count')
unefois = True
for contevenant in contrevenants:
    contrev = Contrevenant(contevenant[0].text, contevenant[1].text, contevenant[2].text,  contevenant[3].text,
                           contevenant[4].text, contevenant[5].text, contevenant[6].text, contevenant[7].text,
                           contevenant[8].text)
   # contrev.print()
    if unefois:
        database = Database()
        database.get_connection()
        try:
            database.insert_contrevenant(contrev)
            unefois = False
        except:
            print("Ce contrevenant existe déjà.")
            database.insert_contravention(contrev)
