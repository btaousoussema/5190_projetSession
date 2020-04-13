create table contrevenant(
  id integer primary key AUTOINCREMENT,
  proprietaire varchar(100) unique,
  categorie varchar(100),
  etablissement varchar(100),
  adresse varchar(100),
  ville varchar(50)
);

create table contravention(
  id integer primary key autoincrement,
  proprietaire_id integer, 
  description varchar(50),
  date_infraction varchar(100),
  date_jugement text,
  montant varchar(10),
  foreign key(proprietaire_id) references contrevenant(id)
);

create table inspection(
 id integer primary key autoincrement,
 Etablissement varchar(50),
 adresse varchar(40),
 ville varchar(50),
 date_visite text,
 nom varchar(50),
 description varchar(200)
);