<?php
    if(is_file("Archives/${_POST["year"]}.pdf")){
        print(json_encode("Archives/${_POST["year"]}.pdf"));
    }
    else{
        print(json_encode("Fichier non trouvé"));
    }
?>

