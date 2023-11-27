# Contient des données sous forme de dictionnaires,
# et des fonctions utilisées ça et là dans les scripts python d'Ordomatic.


# coding: utf-8

import datetime

##################################################
# Dictionnaires (base de données) :
##################################################

# Semaines du psautier, et semaines inversées :
hebdo_psalterii = ["I", "II"]
hebdo_psalterii_inv = ["II", "I"]

# Antiennes du Benedictus pour la 3e sem. de l'Avent:
ant_bened_adv_3 = {0: "\n\\item Ad Benedictus: ø \\textit{Egredietur} (AM 220).", 1: "\n\\item Ad Benedictus: ø \\textit{Tu Bethlehem} (AM 221).", 2: "\n\\item Ad Benedictus: ø \\textit{Missus est} (AM 222).", 3: "\n\\item Ad Benedictus: ø \\textit{Vigilate} (AM 223).", 4: "\n\\item Ad Benedictus: ø \\textit{Ex quo facta} (AM 224).", 5: "\n\\item Ad Benedictus: ø \\textit{Quomodo fiet istud} (AM 225)."}

# Antiennes du Benedictus pour la 4e sem. de l'Avent:
ant_bened_adv_4 = {0: "\n\\item Ad Benedictus: ø \\textit{Dicit Dominus} (AM 229).", 1: "\n\\item Ad Benedictus: ø \\textit{Consurge} (AM 230).", 2: "\n\\item Ad Benedictus: ø \\textit{Ponam in Sion} (AM 230).", 3: "\n\\item Ad Benedictus: ø \\textit{Consolamini} (AM 231).", 4: "\n\\item Ad Benedictus: ø \\textit{Ecce completa sunt} (AM 231)."}

# Ultimæ feriæ avant Noël :
ad_omnes_horas = {0: "\n\\item Ad omnes Horas ø \\textit{Ecce veniet} (AM 212).", 1: "\n\\item Ad omnes Horas ø \\textit{Rorate} (AM 213).", 2: "\n\\item Ad omnes Horas ø \\textit{Prophetæ} (AM 215).", 3: "\n\\item Ad omnes Horas ø \\textit{De Sion} (AM 216).", 4: "\n\\item Ad omnes Horas ø \\textit{Constantes} (AM 217).", 5: "\n\\item Ad Laudes et Horas minores: ø \\textit{Intuemini} in variationibus 14."}

# Temps de l'Épiphanie :
ant_bened_temps_epiph = {7: "\n\\item Ad Benedictus: ø \\textit{Ab Oriente} (AM 297).\n\\item In MC: lectiones feriales post Epiphaniam.", 8: "\n\\item Ad Benedictus: ø \\textit{Tria sunt munera} (AM 298).", 9: "\n\\item Ad Benedictus: ø \\textit{Vidimus} (AM 299).", 10: "\n\\item Ad Benedictus: ø \\textit{Omnes nationes} (AM 299).", 11: "\n\\item Ad Benedictus: ø \\textit{Venient ad te} (AM 300).", 12: "\n\\item Ad Benedictus: ø \\textit{Mirabile} (AM 717)."}
ant_magnif_temps_epiph = {7: "\n\\item Ad Magnificat: ø \\textit{Videntes} (AM 298).", 8: "\n\\item Ad Magnificat: ø \\textit{Lux de luce} (AM 298).", 9: "\n\\item Ad Magnificat: ø \\textit{Interrogabat} (AM 299).", 10: "\n\\item Ad Magnificat: ø \\textit{Omnes de Saba} (AM 300).", 11: "\n\\item Ad Magnificat: ø \\textit{Admoniti Magi} (AM 300)."}

# Vendredis du T.P. :
ant_vepres_vendr_tp = {0: "\n\\item Ad Magnificat: ø \\textit{Quis est iste} cum \\textit{alleluia} (AM 945).", 1: "\n\\item Ad Magnificat: ø \\textit{Crucem sanctam} in tono II d (AM 468).", 2: "\n\\item Ad Magnificat: ø \\textit{Erit sanguis} cum \\textit{alleluia} (AM 951).", 3: "\n\\item Ad Magnificat: ø \\textit{Crucifixus} in tono VI f (AM 471)."}

# Octave de Pentecôte :
octave_pentec = {1: {"body": "\n\\item Ad Vigilias, Laudes et Vesperas : hymni æstivi.\n\\item \\textit{In ML (Rub.) : Missa infra octavam \\emph{(Credo)}.}\n\\item In MC : lectiones feriales."}, 2: {"body": "\n\\item \\textit{In ML (Rub.) : Quatuor Temporum Pentecostes \\emph{(Credo)}.}"}, 3: {"body": "\n\\item \\textit{In ML (Rub.) : Missa infra octavam \\emph{(Credo)}.}"}, 4: {"body": "\n\\item \\textit{In ML (Rub.) : Quatuor Temporum Pentecostes \\emph{(Credo)}.}"}} 

# 1er vendredi du mois per annum :
first_vendr_mc = {1: "in MC (Alb.) : Missa votiva de Dei Misericordia (MR 1158) ; præfatio communis II (in tono simplici).", 2: "in MC (Alb.) : Missa votiva de sacratissimo Corde Iesu (MR 492 - GR 660) ; præfatio propria."}

# Mémoires BMV du samedi :
mc_bmv = {}
# 1er sam. de janvier : traité dans le tempo.
mc_bmv[1] = {}
mc_bmv[1][2] = "\n\\item Ad Vigilias : lectio de memoria sabbato 2 ; oratio \\textit{Deus, qui salutis æternæ}.\n\\item Ad Laudes et Horas minores : officium proprium post Nativitatem Domini (AM 716).\n\\item Ad Benedictus : ø \\textit{Mirabile} (AM 717).\n\\item In MC : \\textit{Sanctæ Mariæ, Dei Genetricis} (CM 4) ; præfatio propria."
mc_bmv[1][3] = "\n\\item Ad Vigilias : lectio de memoria sabbato 3 ; oratio \\textit{Deus, qui salutis æternæ}.\n\\item Ad Laudes et Horas minores : officium proprium post Nativitatem Domini (AM 716).\n\\item Ad Benedictus : ø \\textit{Magnum} (AM 716).\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Matris Salvatoris} (CM 5) ; præfatio propria."
mc_bmv[1][4] = "\n\\item Ad Vigilias : lectio de memoria sabbato 4 ; oratio \\textit{Deus, qui salutis æternæ}.\n\\item Ad Laudes et Horas minores : officium proprium post Nativitatem Domini (AM 716).\n\\item Ad Benedictus : ø \\textit{Mirabile} (AM 717).\n\\item In MC : \\textit{Sanctæ Mariæ de Nazareth} (CM 8) ; præfatio propria."
mc_bmv[1][5] = "\n\\item Ad Vigilias : lectio de memoria sabbato 5 ; oratio \\textit{Deus, qui salutis æternæ}.\n\\item Ad Laudes et Horas minores : officium proprium post Nativitatem Domini AM 716.\n\\item Ad Benedictus : ø \\textit{Magnum} (AM 716).\n\\item In MC : \\textit{Beatæ Mariæ Virginis de Cana} (CM 9) ; præfatio propria."
mc_bmv[2] = {}
mc_bmv[2][1] = {}
mc_bmv[2][1]["before_pres"] = "\n\\item Ad Vigilias : lectio de memoria sabbato 1 ; oratio \\textit{Deus, qui salutis æternæ}.\n\\item Ad Laudes et Horas minores : officium proprium post Nativitatem Domini AM 716.\n\\item Ad Benedictus : ø \\textit{Mirabile} (AM 717).\n\\item \\textit{In ML : Immaculati Cordis Beatæ Mariæ Virginis.}\n\\item In MC : \\textit{Immaculati Cordis Beatæ Mariæ Virginis} (CM 28) ; præfatio propria."
mc_bmv[2][1]["after_pres"] = "\n\\item Ad Vigilias : lectio de memoria sabbato 1.\n\\item Ad Benedictus : ø \\textit{Beata es} (AM 1074).\n\\item \\textit{In ML : Immaculati Cordis Beatæ Mariæ Virginis.}\n\\item In MC : \\textit{Immaculati Cordis Beatæ Mariæ Virginis} (CM 28) ; præfatio propria."
mc_bmv[2][2] = "\n\\item Ad Vigilias : lectio de memoria sabbato 2.\n\\item In MC : \\textit{Sanctæ Mariæ, discipulæ Domini} (CM 10) ; præfatio propria."
mc_bmv[2][3] = "\n\\item Ad Vigilias : lectio de memoria sabbato 3.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, iuxta crucem Domini I} (CM 11) ; præfatio propria."
mc_bmv[2][4] = "\n\\item Ad Vigilias : lectio de memoria sabbato 4.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Fontis salutis} (CM 31) ; præfatio propria."
mc_bmv[3] = {}
mc_bmv[3][1] = "\n\\item Ad Vigilias : lectio de memoria sabbato 1.\n\\item Ad Benedictus : ø \\textit{Beata es} (AM 1074).\n\\item \\textit{In ML : Immaculati Cordis Beatæ Mariæ Virginis.}\n\\item In MC : \\textit{Immaculati Cordis Beatæ Mariæ Virginis} (CM 28) ; præfatio propria."
mc_bmv[5] = {}
mc_bmv[5][2] = "\n\\item Ad Vigilias : lectio sabbato 2.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Reginæ Apostolorum} (CM 18) ; præfatio propria."
mc_bmv[5][3] = "\n\\item Ad Vigilias : lectio sabbato 3.\n\\item In MC : \\textit{Beatæ Mariæ Virginis a Cenaculo} (CM 17) ; præfatio propria."
mc_bmv[5][4] = "\n\\item Ad Vigilias : lectio sabbato 4.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Auxilii christianorum} (CM 42) ; præfatio propria."
mc_bmv[5][5] = "\n\\item Ad Vigilias : lectio sabbato 5.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Matris pulchræ dilectionis} (CM 36) ; præfatio propria."
mc_bmv[6] = {}
mc_bmv[6][1] = "\n\\item Ad Vigilias : lectio sabbato 1.\n\\item Ad Benedictus : ø \\textit{Beata es} (AM 1074).\n\\item \\textit{In ML : Immaculati Cordis Beatæ Mariæ Virginis.}\n\\item In MC : \\textit{Immaculati Cordis Beatæ Mariæ Virginis} (CM 28) ; præfatio propria."
mc_bmv[6][2] = "\n\\item Ad Vigilias : lectio sabbato 2.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Matris boni consilii} (CM 33) ; præfatio propria."
mc_bmv[6][3] = "\n\\item Ad Vigilias : lectio sabbato 3.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Matris et mediatricis gratiæ} (CM 30) ; præfatio propria."
mc_bmv[6][4] = "\n\\item Ad Vigilias : lectio sabbato 4.\n\\item In MC : \\textit{Sanctæ Mariæ, Fontis lucis et vitæ} (CM 16) ; præfatio propria."
mc_bmv[6][5] = "\n\\item Ad Vigilias : lectio sabbato 5 (eadem lectio pro sabbato 4).\n\\item In MC : \\textit{Sanctæ Mariæ, Mulieris novæ} (CM 20) ; præfatio propria."
mc_bmv[7] = {}
mc_bmv[7][1] = "\n\\item Ad Vigilias : lectio sabbato 1.\n\\item Ad Benedictus : ø \\textit{Beata es} (AM 1074).\n\\item \\textit{In ML : Immaculati Cordis Beatæ Mariæ Virginis.}\n\\item In MC : \\textit{Immaculati Cordis Beatæ Mariæ Virginis} (CM 28) ; præfatio propria."
mc_bmv[7][2] = "\n\\item Ad Vigilias : lectio sabbato 2.\n\\item In MC : \\textit{Sanctæ Mariæ, Reginæ et Matris misericordiæ} (CM 39) ; præfatio propria."
mc_bmv[7][3] = "\n\\item Ad Vigilias : lectio sabbato 3.\n\\item In MC : \\textit{Sanctæ Mariæ, Ancillæ Domini} (CM 22) ; præfatio propria."
mc_bmv[7][4] = "\n\\item Ad Vigilias : lectio sabbato 4.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Templi Domini} (CM 23) ; præfatio propria."
mc_bmv[7][5] = "\n\\item Ad Vigilias : lectio sabbato 5.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Sedes Sapientiæ} (CM 24) ; præfatio propria."
mc_bmv[8] = {}
mc_bmv[8][1] = "\n\\item Ad Vigilias : lectio sabbato 1.\n\\item Ad Benedictus : ø \\textit{Beata es} (AM 1074).\n\\item \\textit{In ML : Immaculati Cordis Beatæ Mariæ Virginis.}\n\\item In MC : \\textit{Immaculati Cordis Beatæ Mariæ Virginis} (CM 28) ; præfatio propria."
mc_bmv[8][2] = "\n\\item Ad Vigilias : lectio sabbato 2.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Matris consolationis} (CM 41) ; præfatio propria."
mc_bmv[8][3] = "\n\\item Ad Vigilias : lectio sabbato 3.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Salutis infirmorum} (CM 44) ; præfatio propria."
mc_bmv[8][4] = "\n\\item Ad Vigilias : lectio sabbato 4.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Matris reconciliationis} (CM 14) ; præfatio propria."
mc_bmv[8][5] = "\n\\item Ad Vigilias : lectio sabbato 5.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Imaginis et Matris Ecclesiæ I} (CM 25) ; præfatio propria."
mc_bmv[9] = {}
mc_bmv[9][1] = "\n\\item Ad Vigilias : lectio sabbato 1.\n\\item Ad Benedictus : ø \\textit{Beata es} (AM 1074).\n\\item \\textit{In ML : Immaculati Cordis Beatæ Mariæ Virginis.}\n\\item In MC : \\textit{Immaculati Cordis Beatæ Mariæ Virginis} (CM 28) ; præfatio propria."
mc_bmv[9][2] = "\n\\item Ad Vigilias : lectio sabbato 2.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Mater pulchræ dilectionis} (CM 36) ; præfatio propria."
mc_bmv[9][3] = "\n\\item Ad Vigilias : lectio sabbato 3.\n\\item In MC : \\textit{Beatæ Mariæ Virginis de Mercede} (CM 43) ; præfatio propria."
mc_bmv[9][4] = "\n\\item Ad Vigilias : lectio sabbato 4.\n\\item \\textit{In ML (Viol.): Quatuor Temporum Septembris.}\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Causæ nostræ lætitiæ} (CM 34) ; præfatio propria."
mc_bmv[9][5] = "\n\\item Ad Vigilias : lectio sabbato 5.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Fidei præsidii} (CM 35) ; præfatio propria."
mc_bmv[10] = {}
mc_bmv[10][1] = "\n\\item Ad Vigilias : lectio sabbato 1.\n\\item Ad Benedictus : ø \\textit{Beata es} (AM 1074).\n\\item \\textit{In ML : Immaculati Cordis Beatæ Mariæ Virginis.}\n\\item In MC : \\textit{Immaculati Cordis Beatæ Mariæ Virginis} (CM 28) ; præfatio propria."
mc_bmv[10][2] = "\n\\item Ad Vigilias : lectio sabbato 2.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Reginæ pacis} (CM 45) ; præfatio propria."
mc_bmv[10][3] = "\n\\item Ad Vigilias : lectio sabbato 3.\n\\item In MC : \\textit{Beatæ Mariæ Virginis iuxta crucem Domini} (CM 12) ; præfatio propria."
mc_bmv[10][4] = "\n\\item Ad Vigilias : lectio sabbato 4.\n\\item In MC : \\textit{Sanctæ Mariæ, Matris Domini} (CM 19) ; præfatio propria."
mc_bmv[10][5] = "\n\\item Ad Vigilias : lectio sabbato 5.\n\\item In MC : \\textit{Sanctæ Mariæ, Ancillæ Domini} (CM 22) ; præfatio propria."
mc_bmv[11] = {}
mc_bmv[11][1] = "\n\\item Ad Vigilias : lectio de memoria sabbato 1.\n\\item Ad Benedictus : ø \\textit{Beata es} (AM 1074).\n\\item \\textit{In ML : Immaculati Cordis Beatæ Mariæ Virginis.}\n\\item In MC : \\textit{Immaculati Cordis Beatæ Mariæ Virginis} (CM 28) ; præfatio propria."
mc_bmv[11][2] = "\n\\item Ad Vigilias : lectio de memoria sabbato 2.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Divinæ Providentiæ Matris} (CM 40) ; præfatio propria."
mc_bmv[11][3] = "\n\\item Ad Vigilias : lectio de memoria sabbato 3.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Ianuæ cæli} (CM 46) ; præfatio propria."
mc_bmv[11][4] = "\n\\item Ad Vigilias lectio de memoria sabbato 4.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, Imaginis et Matris Ecclesiæ III} (CM 27) ; præfatio propria."
mc_bmv[11][5] = "\n\\item Ad Vigilias lectio de memoria sabbato 5.\n\\item In MC : \\textit{Beatæ Mariæ Virginis, universorum Reginæ} (CM 29) ; præfatio propria."
mc_bmv[12] = {}
mc_bmv[12][1] = "\n\\item Ad Vigilias lectio de memoria sabbato 1.\n\\item Ad Benedictus : ø \\textit{Beata es} (AM 1074).\n\\item \\textit{In ML : Immaculati Cordis Beatæ Mariæ Virginis.}\n\\item In MC : \\textit{Beatæ Mariæ Virginis, universorum Reginæ} (CM 29) ; præfatio propria."

# Jour où il faudra insérer les dernières antiennes de l'année (Cum videritis etc.).
# Le 1er chiffre indique le jour du Christ-Roi, le 2e indique le jour de la 1ère férie libre (en remontant à partir du 1er dim. de l'Avent) :
ult_ant_dict = {20:14, 21:26, 22:27, 23:28, 24:29, 25:29, 26:1}



##################################################
# Fonctions :
##################################################

def f_symbols(day_date, temps_liturg = ""):
	if day_date.weekday() == 2:
		jeune_abst = " ł"
	elif day_date.weekday() == 4:
		jeune_abst = " ł" if temps_liturg != "Quadr" else " µ"
	else:
		jeune_abst = ""

	first_in_month = {4: " £", 5: " §", 6: " ŧ"}
	if day_date.day < 8:
		first_day_in_month = (first_in_month[day_date.weekday()]) if day_date.weekday() in first_in_month else ""
		if first_day_in_month == " £": jeune_abst = (" µ" if temps_liturg != "TP" else " ł")
	else:
		first_day_in_month = ""

	return(jeune_abst, first_day_in_month) # On distingue les deux, car dans certains cas (Vendredi Saint, etc.), on ne voudra que le 2e item du résultat, le 1er étant fixé dans le Temporal.

def f_roman_numbers(chiffre):
	liste_latin = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII","XXVIII", "XXIX", "XXX", "XXXI", "XXXII", "XXXIII", "XXXIV"]
	return(liste_latin[chiffre - 1])

def f_transf_weekday(num_weekday):
	liste_num = [0, 1, 2, 3 ,4 ,5 ,6]
	liste_latin = ["Feria II", "Feria III", "Feria IV", "Feria V", "Feria VI", "Sabbato", ""]
	return(liste_latin[liste_num.index(num_weekday)])

def f_transf_month(num_month):
	liste_num = [1, 2, 3 ,4 ,5 ,6, 7, 8, 9, 10, 11, 12]
	liste_latin = ["Ianuarius", "Februarius", "Martius", "Aprilis", "Maius", "Iunius", "Iulius", "Augustus", "September", "October", "November", "December"]
	return(liste_latin[liste_num.index(num_month)])

def f_transf_month_genitive(num_month):
	liste_num = [1, 2, 3 ,4 ,5 ,6, 7, 8, 9, 10, 11, 12]
	liste_latin = [" ianuarii", " februarii", " martii", " aprilis", " maii", " iunii", " iulii", " augusti", " septembris", " octobris", " novembris", " decembris"]
	return(liste_latin[liste_num.index(num_month)])
	
special_months = ["", "", "", "Sancto Ioseph consecratus", "", "Beatæ Mariæ Virgini consecratus", "SS.MO Cordi Iesu consecratus", "", "", "", "", "", ""]
	
def f_num_prefaces(i):
	num_pref_dim = f_roman_numbers((i + 1) % 8) if ((i + 1) % 8 != 0) else f_roman_numbers(8)
	num_pref_fer = f_roman_numbers((i + 1) % 6) if ((i + 1) % 6 != 0) else f_roman_numbers(6)
	return(num_pref_dim, num_pref_fer)
	
def f_num_summer(date_dim):
	date_month = date_dim.month
	date_day = date_dim.day
	num_dim = (date_day // 7) + 1 if (date_day % 7 != 0) else (date_day // 7)
	return(f_roman_numbers(num_dim), f_transf_month_genitive(date_month))

def f_mc_bmv(date_bmv, paques): # Renvoie le "body" de la messe BMV :
	if date_bmv.day < 8: num_sam = 1
	elif date_bmv.day < 15: num_sam = 2
	elif date_bmv.day < 22: num_sam = 3
	elif date_bmv.day < 29: num_sam = 4
	else: num_sam = 5
	current_month = date_bmv.month
	if current_month == 2 and num_sam == 1:
		return(mc_bmv[2][1]["before_pres"] if date_bmv.day == 1 else mc_bmv[2][1]["after_pres"])
	else:
		# Samedi dans l'octave de Pentecôte:
		if date_bmv > paques + datetime.timedelta(days = 49) and date_bmv < paques + datetime.timedelta(days = 56):
			if num_sam == 1:
				return(mc_bmv[current_month][num_sam].replace("\\textit{In ML : Immaculati Cordis Beatæ Mariæ Virginis.}", "\\textit{In ML (Rub.): Quatuor Temporum Pentecostes (forma Missæ brevior)} (Credo)."))
			else:
				return(mc_bmv[current_month][num_sam].replace("\n\\item In MC", "\n\\item \\textit{In ML (Rub.): Quatuor Temporum Pentecostes (forma Missæ brevior)} (Credo).\n\\item In MC"))
		else:
			return(mc_bmv[current_month][num_sam])
