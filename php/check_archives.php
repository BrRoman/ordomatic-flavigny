<?php
    if(is_file("../archives/${_POST["year"]}.pdf")){
        print(json_encode("archives/${_POST["year"]}.pdf"));
    }
    else{
        print(json_encode("Fichier non trouvé"));
    }
?>
