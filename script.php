<?php
    //$PYTHON = 'export PATH="/usr/bin/python3:$PATH"; ';// Serveur
    $PYTHON = 'export PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin/:$PATH"; ';// Local
    shell_exec($PYTHON."python3 ordomatic_main.py ".$_POST["year"]);
    shell_exec("rm ordo.pdf");
    //$LATEX = 'export PATH="/usr/bin/lualatex:$PATH"; ';// Serveur
    $LATEX = 'export PATH="/Library/TeX/texbin:$PATH"; ';// Local
    $retour = shell_exec($LATEX."lualatex ordo.tex");
    print($retour);
?>

