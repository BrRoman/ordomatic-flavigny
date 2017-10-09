<!DOCTYPE html>
<html>
	<head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="styles.css" />
        <title>Ordomatic</title>
	</head>
	<body>
        <div id="page">
            <h1>†</h1>
            <h2>
            Bienvenue sur Ordomatic !
            </h2>

            <div id="input">
                <label for="annee">Année de l'ordo : </label><input id="annee" type="number" name="annee" value=<?php print(getdate()["year"]); ?> /><input id="go" type="button" value="Go !" />
            </div>
        </div>
        <div id="overlay_wait">
            <img src="wait.gif" style="margin-bottom:20px"></br>
            <p>Votre ordo est en cours de préparation…</p>
            <p>Veuillez patienter quelques instants…</p>
        </div>
        <form id="overlay_download" action="ordo.pdf" target="_blank">
            Votre ordo est prêt !</br>
            <input id="view" type="submit" value="Afficher" style="margin-top:20px" />
        </form>

        <script src="jquery-3.2.1.js"></script>
        <script src="script.js"></script>
	</body>
</html>

