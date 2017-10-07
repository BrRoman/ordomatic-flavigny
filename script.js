$(document).ready(function(){
<<<<<<< HEAD
    var jours_fr = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"];
    var mois_fr = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"];
    $("#date_debut").change(function(e){
        var date = new Date(e.target.valueAsDate);
        var date_timestamp = Date.parse(date);
        for(var i = 0; i < 5; i++){
            date = new Date(date_timestamp + (i * 24 * 3600 * 1000));
            var weekday = jours_fr[date.getDay()];
            var day = date.getDate();
            var month = mois_fr[date.getMonth()];
            var year = date.getFullYear();
            $("#jour_" + i).text(weekday + " " + day + " " + month + " " + year + " :");}
        $("#output").css("display", "flex");
        document.getElementById("saint_0").focus();
||||||| parent of 81e87d3... OK, except pdf in new tab.
    $("#go").click(function(){
        console.log("Année = " + $("#annee").val());
        $.post(
            "script.php",
            {"year": $("#annee").val()},
            function(retour){
                $("#retour").text(retour);    
            },
            "text"
        );
=======
    $("#go").click(function(){
        $("#overlay_wait").css("display", "flex");
        $.post(
            "script.php",
            {"year": $("#annee").val()},
            function(retour){
                if(retour = "OK");
                    $("#overlay_wait").css("display", "none");
                    $("#overlay_download").css("display", "flex");
            },
            "text"
        );
>>>>>>> 81e87d3... OK, except pdf in new tab.
    });
    $("#view").click(function(){
        $("#overlay_download").css("display", "none");
    });
});

