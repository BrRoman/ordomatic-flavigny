<?php
    $PYTHON = 'export PATH="/usr/bin/python3:$PATH"; ';
    shell_exec($PYTHON."python3 ordomatic_main.py ${_POST["year"]}");
    $LATEX = 'export PATH="/usr/bin/lualatex:$PATH"; ';
    $retour = shell_exec("rm ordo/*.pdf; $LATEX lualatex ordo/${_POST["year"]}.tex; mv ${_POST["year"]}.* ordo; rm ordo/*.tex; rm ordo/*.log; rm ordo/*.aux");
    print($retour);
?>

