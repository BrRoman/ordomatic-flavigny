$(document).ready(function(){
    $("#go").click(function(){
        $.post(
            "check_archives.php",
            {"year": $("#annee").val()},
            function(retour){
                if(retour == "Fichier non trouvé"){
                    $("#overlay_wait").css("display", "flex");
                    $.post(
                        "script.php",
                        {"year": $("#annee").val()},
                        function(retour){
                            $("#overlay_wait").css("display", "none");
                            $("#overlay_download").attr("action", "ordo/" + $("#annee").val() + ".pdf");
                            $("#overlay_download").css("display", "flex");
                        },
                        "text"
                    );
                }
                else{
                    window.open(retour, "");
                }
            },
            "json"
        );
    });

    $("#view").click(function(){
        $("#overlay_download").css("display", "none");
    });
});

