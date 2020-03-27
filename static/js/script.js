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
      var url = "/rechercheDate?"+params;
      xhr.open("GET", url, true);
      xhr.send();
  }else{
    document.getElementById("erreurDate").hidden=false;
  }
}

function verifierDates(du, au){
  var reg = new RegExp("^[0-9]{4}-[0-1][0-9]-[0-3][0-9]$");
  if (reg.exec(du) == null || reg.exec(au) == null){
    return false;
  }
  return true;
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
    var url = "/getContraventions?"+params;
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