<?php
    $PYTHON = 'export PATH="/usr/bin/python3:$PATH"; ';// Serveur
    shell_exec($PYTHON."python3 ordomatic_main.py ".$_POST["year"]);
    shell_exec("rm ordo.pdf");
    $LATEX = 'export PATH="/usr/bin/lualatex:$PATH"; ';// Serveur
    $retour = shell_exec($LATEX."lualatex ordo.tex");
    print($retour);
?>

