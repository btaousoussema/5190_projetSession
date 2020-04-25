Le point A1 a été fait. Pour le tester, il faut cliquer sur le fichier DataCollector.py. 
Le point A2, il faut aller dans la page d'accueil après avoir lancé l'application avec Flask. Ce sont les champs Recherche par rue, nom
et propriétaire. Il faut cliquer sur la touche entrer pour que ca lance la recherche. 
Le point A3 est dans le fichier schedule.py. Si on veut le tester en local, il faut mettre un sleep, ex: time.sleep(9999) et modifier 
les minutes et les heures pour que l'on voit s'il se lance. 
Pour le bouton A4, il faut fair un GET avec les deux champs du et au en format YYYY-MM-DD en paramètres dans le URL. L'url est /api/contrevenants. 
Le point A5 est dans la page d'accueil. Sous le champ, recherche par dates d'infraction, il faut mettre des dates dans les champs du et au, 
selon le format YYYY-MM-DD. On peut ensuite cliquer sur la touche entrer ou bien le bouton en dessous. 
Pour le point A6, il faut choisir dans le menu déroulant en bas de la page d'accueil. 
Pour le point B1, il faut lancer le fichier DataCollector en éliminant un contrevenant de la base de donnée. 
Sinon, il faut faire appel à la fonction envoyer_courriel dans le fichier DataCollector. Il faut modifier l'adresse courriel destination
dans le fichier ex.yaml.  
Pour le point C1, il faut faire un get à l'url /api/nombrecontraventions. 
Pour le point D1, il faut envoyer un POST à l'url /api/inspection. 
Pour le point D2, il faut envoyer un DELETE à l'url /api/inspection/<id>, en spécifiant un id valide.  