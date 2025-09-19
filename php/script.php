<?php
    $PYTHON = 'export PATH="/usr/bin/python3:$PATH"; ';
    shell_exec($PYTHON."python3 ../python/ordomatic_main.py ${_POST["year"]}");
    $LATEX = 'export PATH="/usr/bin/lualatex:$PATH"; ';
    $retour = shell_exec("$LATEX lualatex ../latex/${_POST["year"]}.tex; mv ${_POST["year"]}.* ../latex; rm ../latex/*.log; rm ../latex/*.aux");
    print($retour);
?>
