function chercherContrevenant(){
    var du = document.getElementById("du").value;
    var au = document.getElementById("au").value;
    if (verifierDates(du, au)){
      document.getElementById("erreurDate").hidden=true;
      var params = "du="+du+"&au="+au;
      var valeur = document.getElementById("valeur");
      var xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
            var data = JSON.parse(xhr.responseText);
            valeur.innerHTML = process(data); //data[0].etablissement + " " +data[0].nombre_contraventions;
            console.log(xhr.responseText);
            valeur.value = "";
          } else {
            console.log('Erreur avec le serveur');
          }
        }
      };
      var url = "/api/contrevenants?"+params;
      xhr.open("GET", url, true);
      xhr.send();
  }else{
    document.getElementById("erreurDate").hidden=false;
  }
}

function verifierUneDate(date){
  var reg = new RegExp("^[0-9]{4}-[0-1][0-9]-[0-3][0-9]$");
  if (reg.exec(date) == null){
    return false;
  }
  return true;
}

function verifierDates(du, au){
  return verifierUneDate(du) && verifierUneDate(au);
}

function process(data){
  if (Object.keys(data).length === 0){
    return html = "Il n'y a aucune contravention pour ces dates";
  }else{
    var i;
    html = "<table class='table'><thead><tr><th>Nom de l'établissement</th><th>Nombres de contraventions</th></tr></thead><tbody>";
    for(i=0;i<data.length;i++){
   
      html += "<tr><td>" + data[i].etablissement + "</td><td>" + data[i].nombre_contraventions + "</td></tr>";
    }
    html += "</tbody></table>";
    return html;
  }
}

function getContraventions(){
  var id = document.getElementById("choixContrevenant");
  var selected = id.options[id.selectedIndex].value;
  var HTML = document.getElementById("infractions");
  if (selected != 0){
  var params = "id=" + selected;
  var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          var data = JSON.parse(xhr.responseText);
          HTML.innerHTML = htmlInfractions(data); //data[0].etablissement + " " +data[0].nombre_contraventions;
          console.log(xhr.responseText);
        } else {
          console.log('Erreur avec le serveur');
        }
      }
    };
    var url = "/api/contraventions?"+params;
    xhr.open("GET", url, true);
    xhr.send();
  }
  else{
    HTML.innerHTML="";
  }
}

function htmlInfractions(data){
  var i;
  html = "<table class='table'><thead><tr><th>Description</th><th>Date d'infraction</th><th>Date de jugement</th><th>montant</th></tr></thead>";
  html += "<tbody>";
  if (data.length==0){
    html += "<tr>Il n'y a aucune contravention pour ce contrevenant. <tr>"
  }
  for(i=0;i<data.length;i++){
    html += "<tr><td>" + data[i].description + "</td><td>" + data[i].date_infraction + "</td> <td> " + data[i].date_jugement+ "</td><td>" +data[i].montant + "</td></tr>";
  }
  html += "</tbody></table>";
  return html;
}

function creerInfraction(){
  var nom = document.getElementById("nom").value;
  var adresse = document.getElementById("adresse").value;
  var ville = document.getElementById("ville").value;
  var date_visite = document.getElementById("date_visite").value;
  var nom_plaignant = document.getElementById("nom_plaignant").value;
  var description = document.getElementById("description").value;
  if(verifierUneDate(date_visite)){
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        var data = JSON.parse(xhr.responseText);
        console.log(xhr.responseText);
        window.location.replace("/confirmation.html/"+data.id);
      } else {
        document.getElementById("messageErreur").innerHTML = JSON.parse(xhr.responseText);
        document.getElementById("messageErreur").hidden = false;
        console.log(xhr.responseText);
        console.log('Erreur avec le serveur');
      }
    }
  };
  var url = "/api/inspection";
  xhr.open('POST', url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  console.log(JSON.stringify({nom:nom, adresse:adresse, ville:ville, date_visite: date_visite, nom_plaignant: nom_plaignant, description: description}));
  xhr.send(JSON.stringify({nom:nom, adresse:adresse, ville:ville, date_visite:date_visite, nom_plaignant:nom_plaignant,description:description}));
  } else{
    document.getElementById("erreurDate").hidden=false;
  }
  //xhr.send()
}