<?php
    $PYTHON = 'export PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin/:$PATH"; ';
    shell_exec($PYTHON."python3 ordomatic_main.py ".$_POST["year"]);
    $LATEX = 'export PATH="/Library/TeX/texbin:$PATH"; ';
    shell_exec("cd /tmp; ".$LATEX."lualatex ordo_final.tex");
    print("OK");
?>

