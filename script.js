$(document).ready(function(){
    $("#go").click(function(){
        $("#overlay_wait").css("display", "flex");
        $.post(
            "script.php",
            {"year": $("#annee").val()},
            function(retour){
                console.log("Retour =", retour);
                $("#overlay_wait").css("display", "none");
                $("#overlay_download").css("display", "flex");
            },
            "text"
        );
    });
    $("#view").click(function(){
        $("#overlay_download").css("display", "none");
    });
});

