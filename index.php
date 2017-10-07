<!DOCTYPE html>
<html>
	<head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="styles.css" />
        <title>Livrets retraites</title>
	</head>
	<body>
        <div id="page">
            <h1>†</h1>
            <h2>
            Livrets de messe</br>
            pour les retraitants
            </h2>

            <div id="input">
                <label for="date_debut">Retraite du : </label><input id="date_debut" type="date" name="date_debut" />
            </div>

            <div id="output">
                <?php
                    for($i = 0; $i <= 4; $i++){
                        $code = "";
                        $code = $code."<div class='jour' id='jour_".$i."'>Jour ".$i." :</div>";
                        $code = $code."<table>";
                        $code = $code."<tbody>";
                        $code = $code."<tr>";
                        $code = $code."<td class='label'>Saint : </td>";
                        $code = $code."<td><input type='text' id='saint_".$i."' style='width:300px'></td>";
                        $code = $code."</tr>";
                        $code = $code."<tr>";
                        $code = $code."<td class='label'>Rang : </td>";
                        $code = $code."<td><select id='rang_".$i."' style='width:200px'><option value='solennite'>Solennité</option><option value='fete'>Fête</option><option value='mem_maj'>Mémoire majeure</option><option value='mem_min'>Mémoire mineure</option></select></td>";
                        $code = $code."</tr>";
                        $code = $code."<tr>";
                        $code = $code."<td class='label'>Oraisons : </td>";
                        $code = $code."<td><input type='text' id='oraisons_".$i."' style='width:300px'></td>";
                        $code = $code."</tr>";
                        $code = $code."<tr>";
                        $code = $code."<td class='label'>Lectures : </td>";
                        $code = $code."<td><input type='text' id='lectures_".$i."' style='width:300px'></td>";
                        $code = $code."</tr>";
                        $code = $code."</tbody>";
                        $code = $code."</table>";
                        print($code);}
                ?>
            </div>
        </div>
        <div id="overlay_wait">
            <img src="wait.gif" style="margin-bottom:20px"></br>
            <p>Votre ordo est en cours de préparation…</p>
            <p>Veuillez patienter quelques instants…</p>
        </div>
        <form id="overlay_download" action="file:///private/tmp/ordo_final.pdf" target="_blank">
            Votre ordo est prêt !</br>
            <input id="view" type="submit" value="Afficher" style="margin-top:20px" />
        </form>

        <script src="jquery-3.2.1.js"></script>
        <script src="script.js"></script>
	</body>
</html>

