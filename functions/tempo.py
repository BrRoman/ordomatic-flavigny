# coding: utf-8

import datetime
from functions.lectiones import *
from functions.various import hebdo_psalterii, ad_omnes_horas, ant_bened_adv_3, ant_bened_adv_4, ant_bened_temps_epiph, ant_magnif_temps_epiph, ant_vepres_vendr_tp, f_num_prefaces, f_mc_bmv, f_num_summer, octave_pentec, mc_bmv,f_symbols, f_transf_month_genitive, f_roman_numbers, f_transf_weekday

def dict_tempo_create(current_year, even_year, year_letter):
    even_year_num = 0 if even_year else 1
    dict_tempo = {}
    dict_tempo["fetes_mobiles"] = {} # Ce dictionnaire sera utilisé pour le tableau des fêtes mobiles en page 3 de l'ordo.
    
    # Noël:
    noel_date = datetime.date(current_year - 1, 12, 25)
    noel_weekday = noel_date.weekday()
    
    # Samedi avant le 1er dim. de l'Avent:    
    sabb_1_adv_date = noel_date - datetime.timedelta(days = noel_weekday + 23)
    sabb_1_adv = dict_tempo[sabb_1_adv_date] = {}
    sabb_1_adv["force"] = 10
    sabb_1_adv["generalities"] = "\\ApplyParBox{1cm}{\\ApplyGenerTitleHuge{Tempus Adventus}}\n\\ApplyGenerSubTitle{In Adventu}\n\\ApplyGenerList{\n\\item In Missis de tempore silent organa, excepta dominica \\textit{Gaudete} in Missa.\n\\item Ad Completorium : ø \\textit{Alma Redemptoris}.}\n\\ApplyGenerSubTitle{In Officio de tempore}\n\\ApplyGenerList{\n\\item Omnes genua flectunt in Officio feriali ad \\textit{Kyrie eleison}. In memoriis minoribus, standum est ad Laudes ; genuflectendum vero ad alias Horas.\n\\item Ad Vigilias : invitatorium \\textit{Regem venturum} usque ad diem 16 decembris.\n\\item Ad Laudes : dicuntur cantica ferialia, quod servatur etiam in memoriis.\n\\item Ad Benedictus et Magnificat : antiphonæ propriæ.\n\\item Ad Horas minores : antiphonæ dominicæ præcedentis (usque ad diem 17 decembris) ; in memoriis cantatur hymnus in tono Adventus.}\n\\ApplyGenerSubTitle{In MC}\n\\ApplyGenerList{\n\\item Missa propria singulis diebus.\n\\item A prima dominica Adventus usque ad diem 16 decembris dicitur præfatio I de Adventu in Missis de tempore et in ceteris Missis, quæ celebrantur eodem tempore et præfatione propria carent.\n\\item In feriis Adventus : omnia cantantur in tono simplici, præter orationem super oblata, quæ semper in tono solemni cantatur (\\textit{Pater} in tono B).}\n\\ApplyGenerSubTitle{In ML}\n\\ApplyGenerList{\n\\item Dicitur præfatio de Adventu ut supra.\n\\item Quando resumitur Missa de dominica, post graduale omittuntur \\textit{Alleluia} et versiculus sequens.\n\\item Missæ votivæ IV classis et Missæ defunctorum «cotidianæ» non permittuntur.\n\\item In memoriis et festis fit commemoratio feriæ.}\n\\ApplyHebdoPsalt{\\textbf{- Pro breviario 1962 : tomus prior -}}"
    sabb_1_adv["num_day"] = "\\textbf{" + str(sabb_1_adv_date.day) + "} &" + " Sabbato"
    sabb_1_adv["symbols"] = "".join(f_symbols(sabb_1_adv_date))
    sabb_1_adv["header"] = " - de eo - \\textit{Viol.}"
    
    # 2 premiers dimanches de l'Avent et leurs féries:
    for i in range(2):
        new_dim_adv_date = sabb_1_adv_date + datetime.timedelta(days = 1 + (i * 7))
        if i == 0: dict_tempo["fetes_mobiles"]["dim_1_adv"] = str(new_dim_adv_date.day) + f_transf_month_genitive(new_dim_adv_date.month)
        new_dim_adv = dict_tempo[new_dim_adv_date] = {}
        new_dim_adv["force"] = 120
        new_dim_adv["I_vesp"] = "\\item I Vesperæ dominicæ sequentis."
        new_dim_adv["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((new_dim_adv_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
        new_dim_adv["num_day"] = "\\textbf{" + str(new_dim_adv_date.day) + "} &"
        new_dim_adv["symbols"] = "".join(f_symbols(new_dim_adv_date))
        new_dim_adv["header"] = " \\textbf{\\textsc{Dominica " + f_roman_numbers(i + 1) + " Adventus}} - de ea - \\textit{Viol.}"
        new_dim_adv["body"] = ("\\item Ad Vigilias : post lectiones I nocturni, dicitur ¶ lectionis 1 \\textit{Aspiciens a longe}.\n\\item In MC : Missa concluditur benedictione sollemni." if i == 0 else "")
        current_lectiones = lectiones["hebdo_" + str(i + 1) + "_adv"]
        new_dim_adv["lectiones_header"] = "\n" + current_lectiones["header"]
        lectiones_body = "\n\\item[Dom. " + year_letter + "] " + current_lectiones["dim"][year_letter]
        new_dim_adv["II_vesp"] = "\\item Vesperæ dominicæ." if new_dim_adv_date.day == 7 or new_dim_adv_date.day == 8 else ""
        
        for j in range(6):
            if i == 0 and j == 0:
                year_letter_a_or_bc = "A" if year_letter == "A" else "BC"
                lectiones_body += "\n\\item[" + f_transf_weekday(j)+ "] " + current_lectiones[j][year_letter_a_or_bc]
            else:
                lectiones_body += "\n\\item[" + f_transf_weekday(j)+ "] " + current_lectiones[j]
            new_day_adv_date = new_dim_adv_date + datetime.timedelta(days = j + 1)
            new_day_adv = dict_tempo[new_day_adv_date] = {}
            new_day_adv["force"] = 10
            new_day_adv["num_day"] = "\\textbf{" + str(new_day_adv_date.day) + "} & " + f_transf_weekday(new_day_adv_date.weekday())
            new_day_adv["symbols"] = "".join(f_symbols(new_day_adv_date))
            new_day_adv["header"] = " - de ea - \\textit{Viol.}" if j != 5 else " - de eo - \\textit{Viol.}"
            if new_day_adv_date.day < 8:
                if new_day_adv_date.weekday() == 4: new_day_adv["body"] = "\n\\item \\textit{In ML (Alb.) : Missa de sacratissimo Corde Iesu \\emph{(Gloria)}.}"
                if new_day_adv_date.weekday() == 5: new_day_adv["body"] = "\n\\item \\textit{In ML (Alb.)  : Immaculati Cordis Beatæ Mariæ Virginis.}"
        new_dim_adv["lectiones_body"] = lectiones_body
    
    # Ultimæ feriæ :    
    generalities = "\\ApplyGenerSubTitle{A die 17 ad diem 23 decembris inclusive}\n\\ApplyGenerList{\n\\item Ad Vigilias: invitatorium \\textit{Prope est} ; lectiones SO in supplemento 9 et sequentibus pro singulis feriis.\n\\item Ad Laudes: antiphonæ propriæ.\n\\item Ad Benedictus: antiphonæ propriæ.\n\\item Ad Horas et Vesperas: antiphonæ e Laudibus.\n\\item Ad Magnificat: antiphonæ “O” (AM 208 - 211).\n\\item In Missa conventuali: præfatio II de Adventu ; in feriis dicuntur orationes et lectiones diei mensis adsignatæ.}"
    # 3e dim. de l'Avent:
    dim_3_adv_date = new_dim_adv_date + datetime.timedelta(days = 7)
    dim_3_adv = dict_tempo[dim_3_adv_date] = {}
    dim_3_adv["force"] = 120
    if dim_3_adv_date.day == 17:
        dim_3_adv["generalities"] = generalities
        txt_vigiles = "\\item Ad Vigilias: in I nocturno lectiones e dominica III Adventus."
    elif dim_3_adv_date.day < 16:
        txt_vigiles = "\\item Ad Vigilias: continuatur invitatorium \\textit{Regem venturum} usque ad diem 16 decembris."
    else:
        txt_vigiles = ""
    dim_3_adv["I_vesp"] = "\\item I Vesperæ dominicæ sequentis."
    dim_3_adv["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((dim_3_adv_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
    dim_3_adv["num_day"] = "\\textbf{" + str(dim_3_adv_date.day) + "} &"
    dim_3_adv["symbols"] = "".join(f_symbols(dim_3_adv_date))
    dim_3_adv["header"] = " \\textbf{\\textsc{Dominica III Adventus}, Gaudete} - de ea - \\textit{Viol.}"
    dim_3_adv["body"] = txt_vigiles + "\\item Hodie pulsantur organa ad Missam, non vero in aliis Horis."
    # Lectures jusqu'au 17 :
    current_lectiones = lectiones["hebdo_3_adv"]
    dim_3_adv["lectiones_header"] = "\n" + current_lectiones["header"]
    lectiones_body = "\n\\item[Dom. " + year_letter + "] " + current_lectiones["dim"][year_letter]
    if dim_3_adv_date.day != 17:
        for i in range(16 - dim_3_adv_date.day):
            lectiones_body += "\n\\item[" + f_transf_weekday(i) + "] " + current_lectiones[i]
        # Lectures à partir du 17 :
        current_lectiones = lectiones["ultimae_feriae"]
        for i in range(dim_3_adv_date.day - 10):
            if (17 + i) != 21:
                lectiones_body += "\n\\item[" + str(17 + i) + " dec.] " + current_lectiones[17 + i]
            else:
                lectiones_body += "\n\\item[21 dec.] " + (current_lectiones[21]["C"] if year_letter == "C" else current_lectiones[21]["AB"])
    else:
        current_lectiones = lectiones["ultimae_feriae"]
        for i in range(6):
            lectiones_body += "\n\\item[" + str(18 + i) + " dec.] " + (current_lectiones[18 + i] if (18 + i) != 21 else (current_lectiones[21]["C"] if year_letter == "C" else current_lectiones[21]["AB"]))
    dim_3_adv["lectiones_body"] = lectiones_body
    
    # Lectures des Vigiles à prendre dans le Supplément à partir du Mercredi des Quatre-Temps (si avant 17 décembre):
    lect_vigiles = {2: "\\item Ad Vigilias: lectiones SO in supplemento 5.", 3: "\\item Ad Vigilias: lectiones SO in supplemento 6.", 4: "\\item Ad Vigilias: lectiones SO in supplemento 8."}
    
    # Féries de la 3e sem. de l'Avent:
    for i in range(6):
        new_day_date = dim_3_adv_date + datetime.timedelta(days = i + 1)
        new_day = dict_tempo[new_day_date] = {}
        new_day["num_day"] = "\\textbf{" + str(new_day_date.day) + "} & " +  f_transf_weekday(new_day_date.weekday())
        new_day["symbols"] = "".join(f_symbols(new_day_date))
        new_day["header"] = " - de ea - \\textit{Viol.}" if i != 5 else " - de eo - \\textit{Viol.}"
        
        # Rubriques spéciales:
        lect_vigiles_txt = ""
        ad_omnes_horas_txt = ""
        ant_bened_txt = ""
        div_longs_psaumes = ""
        if new_day_date.day < 17:
            new_day["force"] = 10
            lect_vigiles_txt = lect_vigiles[new_day_date.weekday()] if new_day_date.weekday() in lect_vigiles else ""
        else:
            new_day["force"] = 50
            if new_day_date.day == 17: new_day["generalities"] = generalities
            ad_omnes_horas_txt = ad_omnes_horas[new_day_date.weekday()]
            if new_day_date.day == 21:
                ant_bened_txt = "\n\\item Ad Benedictus: ø \\textit{Nolite timere} (AM 219)."
            elif new_day_date.day == 23:
                ant_bened_txt = "\n\\item Ad Benedictus: ø \\textit{Ecce completa sunt} (AM 220)."
            else:
                ant_bened_txt = ant_bened_adv_3[new_day_date.weekday()]
            if new_day_date.weekday() == 3 or new_day_date.weekday() == 4: div_longs_psaumes = "\\item Ad Vesperas: divisiones psalmorum considerantur ut integri psalmi, ita ut eis antiphonæ propriæ sint attribuendæ."

        # Quatre-Temps (= mercredi, vendredi et samedi de la 3e sem. de l'Avent), Office et Messes basses:
        quatre_temps = True if new_day_date.weekday() == 2 or new_day_date.weekday() == 4 or new_day_date.weekday() == 5 else False
        if quatre_temps:
            messe_basse_quatre_temps = "\\item \\textit{In ML: Quatuor Temporum Adventus \\textit{(forma Missæ brevior)}}." if new_day_date.weekday() == 5 else "\\item \\textit{In ML: Quatuor Temporum Adventus}."
            office_quatre_temps = "\\item In Officio: oratio Quatuor Temporum Adventus." if new_day_date.weekday() == 5 else "\\item In Officio: oratio Quatuor Temporum Adventus, quæ dicitur ad omnes Horas, etiam ad Vesperas."
        else:
            messe_basse_quatre_temps = ""
            office_quatre_temps = ""

        # On concatène le tout:
        new_day["body"] = lect_vigiles_txt + ad_omnes_horas_txt + office_quatre_temps + ant_bened_txt + messe_basse_quatre_temps + div_longs_psaumes

    # 4e dim. de l'Avent:
    dim_4_adv_date = dim_3_adv_date + datetime.timedelta(days = 7)
    dim_4_adv = dict_tempo[dim_4_adv_date] = {}
    dim_4_adv["force"] = 120
    dim_4_adv["I_vesp"] = "\\item I Vesperæ dominicæ sequentis (AM 226)."
    dim_4_adv["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((dim_4_adv_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
    dim_4_adv["num_day"] = "\\textbf{" + str(dim_4_adv_date.day) + "} &"
    dim_4_adv["symbols"] = "".join(f_symbols(dim_4_adv_date))
    dim_4_adv["header"] = " \\textbf{\\textsc{Dominica IV Adventus}} - de ea - \\textit{Viol.}"
    if dim_4_adv_date.day == 21: ant_bened_special = "\n\\item Ad Benedictus: ø \\textit{Nolite timere (AM 219)}."
    elif dim_4_adv_date.day == 23: ant_bened_special = "\n\\item Ad Benedictus: ø \\textit{Ecce completa sunt (AM 220)}."
    else: ant_bened_special = ""
    dim_4_adv["body"] = ("\\item Ad Vigilias: in I nocturno lectiones e dominica IV Adventus." + ant_bened_special) if dim_4_adv_date.day != 24 else "\\item Ad Vigilias: Officium fit de Vigilia Nativitatis Domini in dominica præter lectiones I nocturni in supplemento 20 ; invitatorium \\textit{Hodie scietis}.\n\\item Ad Laudes et Horas minores: ø \\textit{Iudæa} (AM 232) cum psalmis festivis.\n\\item \\textit{In ML: Missa de Vigilia.}\n\\item In MC: Missa de dominica IV Adventus ; cantus Missæ \\textit{Hodie} de Vigilia omittuntur."
    dim_4_adv["II_vesp"] = "\\item I Vesperæ sollemnitatis sequentis.\n\\item Completorium omittitur ab his qui solemnem Vigiliam et Missam in nocte intersunt." if dim_4_adv_date.day == 24 else ""
    current_lectiones = lectiones["hebdo_4_adv"]
    dim_4_adv["lectiones_header"] = "\n" + current_lectiones["header"]
    lectiones_body = "\n\\item[Dom. " + year_letter + "] " + current_lectiones["dim"][year_letter]
    current_lectiones = lectiones["ultimae_feriae"]
    for i in range(24 - dim_4_adv_date.day):
        if (dim_4_adv_date.day + i + 1) != 21:
            lectiones_body += "\n\\item[" + str(dim_4_adv_date.day + i + 1) + " dec.] " + current_lectiones[dim_4_adv_date.day + i + 1]
        else:
            lectiones_body += "\n\\item[21 dec.] " + (current_lectiones[21]["C"] if year_letter == "C" else current_lectiones[21]["AB"])
    dim_4_adv["lectiones_body"] = lectiones_body
    
    # Féries de la 4e sem. de l'Avent:
    for i in range(6):
        new_day_date = dim_4_adv_date + datetime.timedelta(days = i + 1)
        if new_day_date.day < 25:
            new_day = dict_tempo[new_day_date] = {}
            new_day["force"] = 50
            new_day["num_day"] = "\\textbf{" + str(new_day_date.day) + "} & " +  f_transf_weekday(new_day_date.weekday())
            new_day["symbols"] = "".join(f_symbols(new_day_date))
            new_day["header"] = " - de ea - \\textit{Viol.}" if i != 5 else " - de eo - \\textit{Viol.}"
        
            # Rubriques propres aux Ultimæ feriæ:
            ad_omnes_horas_txt = ad_omnes_horas[new_day_date.weekday()]
            if new_day_date.day == 21:
                ant_bened_txt = "\n\\item Ad Benedictus: ø \\textit{Nolite timere} (AM 219)."
            elif new_day_date.day == 23:
                ant_bened_txt = "\n\\item Ad Benedictus: ø \\textit{Ecce completa sunt} (AM 220)."
            else:
                ant_bened_txt = ant_bened_adv_4[new_day_date.weekday()] if new_day_date.weekday() != 5 else ""
            if new_day_date.weekday() == 3 or new_day_date.weekday() == 4: div_longs_psaumes = "\\item Ad Vesperas: divisiones psalmorum considerantur ut integri psalmi, ita ut eis antiphonæ propriæ sint attribuendæ."
            
            # On concatène le tout:
            new_day["body"] = ad_omnes_horas_txt + ant_bened_txt + div_longs_psaumes
    
    # Vigile de Noël:
    vigile_noel_date = noel_date - datetime.timedelta(days = 1)
    if vigile_noel_date.weekday() != 6: # Car si 24/12 = dimanche, alors c'est le 4e dim. de l'Avent.
        vigile_noel = dict_tempo[vigile_noel_date] = {}
        vigile_noel["force"] = 50
        vigile_noel["num_day"] = "\\textbf{" + str(vigile_noel_date.day) + "} & " + f_transf_weekday(vigile_noel_date.weekday())
        vigile_noel["symbols"] = "".join(f_symbols(vigile_noel_date))
        vigile_noel["header"] = " - " + ("de ea" if vigile_noel_date.weekday() != 5 else "de eo") + " - \\textsc{Vigilia Nativitatis Domini} - \\textit{Viol.}"
        vigile_noel["body"] = "\\item Ad Vigilias: invitatorium \\textit{Hodie scietis} ; lectiones SO in supplemento 20.\n\\item Ad Laudes: antiphonæ propriæ cum psalmis festivis.\n\\item \\textit{In ML: Missa de Vigilia.}\n\\item In MC: cantus sumuntur e Missa \\textit{Hodie} de Vigilia (GR 38)."
        vigile_noel["II_vesp"] = "\\item I Vesperæ sollemnitatis sequentis.\n\\item Completorium omittitur ab his qui solemnem Vigiliam et Missam in nocte intersunt."
        
    # Noël:
    noel = dict_tempo[noel_date] = {}
    noel["force"] = 120
    noel["generalities"] = "\n\\ApplyGenerSubTitle{Ad mensam}\n\\ApplyGenerList{\\item Benedictio de Nativitate.}" + ("\n\\vspace{1cm}" if noel_date.weekday() != 6 else "") # Car si dimanche, alors "Hebdomada n psalterii", et du coup espace.
    noel["num_day"] = "\\textbf{" + str(noel_date.day) + "} & " + f_transf_weekday(noel_date.weekday())
    noel["header"] = ("Dominica - " if noel_date.weekday() == 6 else " - ") + "¬ \\textbf{\\MakeUppercase{In Nativitate Domini Nostri Iesu Christi} - sollemnitas maior cum octava} - \\textit{Alb}."
    noel["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((noel_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -" if noel_date.weekday() == 6 else ""
    hebdo_psalt_noel = "II" if even_year else "I"# Cette donnée servira pour la Ste Famille.
    noel["body"] = "\\item Ad Vigilias: psalmi hebdomadæ " + hebdo_psalt_noel + ".\n\\item Hodie omnes sacerdotes tres Missas celebrare possunt, dummodo hæ suo tempore celebrentur.\n\\item \\textit{In ML: præfatio et \\emph{Communicantes} de Nativitate per totam octavam.}\n\\item In omnibus Missis Nativitatis ad verba symboli \\textit{Et incarnatus est} omnes genua flectunt.\n\\item Ad Missam in nocte: ad hymnum \\textit{Gloria} pulsantur campanæ ; præfatio I de Nativitate Domini ; \\textit{Communicantes} proprium hodie et per totam octavam ; \\textit{Pater} in tono C (GR 814).\n\\item Laudes in aurora celebrantur ; psalmi 148 et 149 omittuntur.\n\\item Ad Missam in die: præfatio II de Nativitate Domini ; \\textit{Pater} in tono C ; Missa concluditur benedictione sollemni.\n\\item Vesperæ sollemnitatis ; benedictio Sanctissimi Sacramenti."
    noel["lectiones_header"] = "\nIn Nativitate Domini Nostri : lectiones de tempore"
    lectiones_body = "\n\\item[In nocte] Is \\textbf{9}, 2-4.6-7 / Tit \\textbf{2}, 11-14 / Lc \\textbf{2}, 1-14"
    lectiones_body += "\n\\item[In aurora] Is \\textbf{62}, 11-12 / Tit \\textbf{3}, 4-7 / Lc \\textbf{2}, 15-20"
    lectiones_body += "\n\\item[In die] Is \\textbf{52}, 7-10 / Hebr \\textbf{1}, 1-6 / Io \\textbf{1}, 1-18"
    # Cas où la Ste Famille va tomber le 30 ou le 31, on met ici les lectiones du 29 au 31, sauf celles de la Ste Famille :
    if noel_date.weekday() == 0 or noel_date.weekday() == 1 or noel_date.weekday() == 6:
        current_lectiones = lectiones["ste_famille"]
        lectiones_body += "\n\\item[29 dec.] " + current_lectiones[29]
        lectiones_body += "\n\\item[30 dec.] " + current_lectiones[30] if noel_date.weekday() != 1 and noel_date.weekday() != 6 else ""
        lectiones_body += "\n\\item[31 dec.] " + current_lectiones[31] if noel_date.weekday() != 0 else ""
    noel["lectiones_body"] = lectiones_body
    
    # Sainte Famille:
    if noel_weekday == 6: ste_famille_date = noel_date + datetime.timedelta(days = 5)
    else: ste_famille_date = noel_date + datetime.timedelta(days = 6 - noel_weekday)
    dict_tempo["fetes_mobiles"]["ste_famille"] = str(ste_famille_date.day) + f_transf_month_genitive(ste_famille_date.month)
    ste_famille = dict_tempo[ste_famille_date] = {}
    ste_famille["force"] = 100
    ste_famille["num_day"] = "\\textbf{" + str(ste_famille_date.day) + "} &"
    ste_famille["symbols"] = "".join(f_symbols(new_day_date))
    ste_famille["I_vesp"] = "\\item I Vesperæ festi sequentis (AM 265)." if ste_famille_date.weekday() == 6 else ""
    ste_famille["hebdo_psalt"] = ("- Hebdomada " + hebdo_psalterii[((ste_famille_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -") if ste_famille_date.weekday() == 6 else ""
    ste_famille["header"] = " \\textbf{\\textsc{" + ("Dominica I post nativitatem - " if noel_weekday != 6 else "\\textnormal{Feria VI - }") + "Sanctæ Familiæ Iesu, Mariæ et Ioseph}} - \\textbf{festum} - \\textit{Alb}."
    # Hebdo_psalt_vigiles:
    hebdo_psalt_vigiles = ""
    if hebdo_psalt_noel == "I" and hebdo_psalterii[((ste_famille_date - datetime.date(2011, 11, 27)).days // 7) % 2] == "I":
        hebdo_psalt_vigiles = "\n\\item Ad Vigilias: psalmi hebdomadæ II; lectiones sumuntur e nocturnis I et II."
    elif hebdo_psalt_noel == "II" and hebdo_psalterii[((ste_famille_date - datetime.date(2011, 11, 27)).days // 7) % 2] == "II":
        hebdo_psalt_vigiles = "\n\\item Ad Vigilias: psalmi hebdomadæ I; lectiones sumuntur e nocturnis I et II."
    # Antiennes de Bened. et Magnificat:
    if year_letter == "A":
        ste_famille_bened = "\\item Ad Benedictus: ø \\textit{Iacob autem} (AM 836)."
        ste_famille_magnif = "\\item Ad Magnificat: ø \\textit{Puer Iesus} (AM 267)."
    elif year_letter == "B":
        ste_famille_bened = "\\item Ad Benedictus: ø \\textit{Senex puerum} (AM 801)."
        ste_famille_magnif = "\\item Ad Magnificat: ø \\textit{Cum inducerent} (AM 803)."
    else:
        ste_famille_bened = "\\item Ad Benedictus: ø \\textit{Remansit} (AM 301)."
        ste_famille_magnif = "\\item Ad Magnificat: ø \\textit{Fili, quid fecisti} (AM 303)."
    # Cas le plus fréquent, on annonce les lectiones du 29 au 31 :
    if ste_famille_date.day != 30 and ste_famille_date.day != 31:
        ste_famille["body"] = "\n\\item Officium dicitur de dominica infra octavam Nativitatis, præter orationem in supplemento 22* ; invitatorium proprium in supplemento 59." + hebdo_psalt_vigiles + ste_famille_bened + "\n\\item \\textit{In ML: Missa dominicæ I post Epiphaniam, Sanctæ Familiæ, cum præfatione et \\emph{Communicantes} de Nativitate.}\n\\item In MC: præfatio II de Nativitate."
        current_lectiones = lectiones["ste_famille"]
        ste_famille["lectiones_header"] = "\n" + current_lectiones["header"]
        lectiones_body = "\n\\item[Dom. " + year_letter + "] " + current_lectiones["dim"][year_letter]
        for i in range(3):
            if (29 + i) != ste_famille_date.day:
                lectiones_body += "\n\\item[" + str(29 + i) + " dec.] " + current_lectiones[29 + i]
        ste_famille["lectiones_body"] = lectiones_body
    # Si 30 ou 31, les lectiones ont été annoncées après Noël, et on n'a plus qu'à mentionner les lectures de la Ste Famille dans le body de ce jour (ex. : Ordo de 2011-2012) :
    else:
        current_lectiones = lectiones["ste_famille"]
        lectiones_mc = current_lectiones["dim"][year_letter] if ste_famille_date.weekday() == 6 else current_lectiones["feria"]
        ste_famille["body"] = "\n\\item Officium dicitur de dominica infra octavam Nativitatis, præter orationem in supplemento 22* ; invitatorium proprium in supplemento 59." + hebdo_psalt_vigiles + ste_famille_bened + "\n\\item \\textit{In ML: Missa dominicæ I post Epiphaniam, Sanctæ Familiæ, cum præfatione et \\emph{Communicantes} de Nativitate.}\n\\item In MC: lectiones propriæ : " + lectiones_mc + "; præfatio II de Nativitate."
    ste_famille["II_vesp"] = ste_famille_magnif
    
    # Octave de Noël:
    for i in range(7):
        new_day_date = noel_date + datetime.timedelta(days = i + 1)
        if new_day_date != ste_famille_date:
            new_day = dict_tempo[new_day_date] = {}
            new_day["force"] = 50
            new_day["num_day"] = "\\textbf{" + str(new_day_date.day) + "} & " +  f_transf_weekday(new_day_date.weekday())
            new_day["symbols"] = "".join(f_symbols(new_day_date))
            new_day["header"] = " - \\textbf{\\textsc{De Octava Nativitatis}} - \\textit{Alb}."
            benedicamus_domino = "\\item Ad Laudes et Vesperas: ß \\textit{Benedicamus Domino} III." if new_day_date.weekday() != 5 else "\\item Ad Laudes: ß \\textit{Benedicamus Domino} III."
            new_day["body"] = "\\item In Officio: omnia dicuntur sicut in Nativitate præter Vigilias." + benedicamus_domino + "\\item In MC: \\textit{Gloria} ; præfatio II de Nativitate."

    # 2e dim. ap. Noël:
    dim_2_ap_noel_date = noel_date + datetime.timedelta(days = 13 - noel_weekday)
    dim_2_ap_noel = dict_tempo[dim_2_ap_noel_date] = {}
    dim_2_ap_noel["force"] = 100
    dim_2_ap_noel["I_vesp"] = "\\item I Vesperæ dominicæ sequentis (AM 265)."
    dim_2_ap_noel["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((dim_2_ap_noel_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
    dim_2_ap_noel["num_day"] = "\\textbf{" + str(dim_2_ap_noel_date.day) + "} &"
    dim_2_ap_noel["symbols"] = "".join(f_symbols(dim_2_ap_noel_date))
    dim_2_ap_noel["header"] = " \\textbf{\\textsc{Dominica II post Nativitatem}} - de ea - \\textit{Alb}."
    messe_basse = "\\item \\textit{In ML: Dominica infra octavam Nativitatis vel Missa Sanctissimi Nominis Iesu}." if dim_2_ap_noel_date.day == 3 else "\\item \\textit{In ML: Dominica infra octavam Nativitatis.}"
    lectures_mc = "Si \\textbf{24}, 1-2.8-12 / Ep \\textbf{1}, 3-6.15-18 / Io \\textbf{1}, 1-18"
    lect_propres = " Lectiones propriæ: " + lectures_mc + ";" if dim_2_ap_noel_date.day == 5 else ""
    dim_2_ap_noel["body"] = "\\item Ad Laudes et Vesperas: antiphonæ et psalmi de psalterio, reliqua ut in dominica infra octavam Nativitatis (AM 266).\n\\item Ad Horas minores: antiphonæ de Circumcisione, reliqua ut in dominica infra octavam Nativitatis (AM 266)." + messe_basse + "\\item In MC:" + lect_propres + " præfatio III de Nativitate ."
    if dim_2_ap_noel_date.day != 1 and dim_2_ap_noel_date.day != 5: # Car si 1 : on les met dans les généralités "Tempus Nativitatis I", et si 5 : inutile (lectures dans body + pas de féries à la suite).
        dim_2_ap_noel["lectiones_header"] = "\nDominica II post Nativitatem : lectiones de tempore"
        lectiones_body = "\n\\item[Dom. " + year_letter + "]" + lectures_mc
        current_lectiones = lectiones["nativ"]
        for i in range(6 - dim_2_ap_noel_date.day - 1):
            lectiones_body += "\n\\item[" + str(dim_2_ap_noel_date.day + i + 1) + " ian.] " + current_lectiones[dim_2_ap_noel_date.day + i + 1]
        dim_2_ap_noel["lectiones_body"] = lectiones_body

    # Baptême:
    bapteme_date = noel_date + datetime.timedelta(days = 20 - noel_weekday)
    if(bapteme_date.day == 14):
        bapteme_date = bapteme_date + datetime.timedelta(days = -7)
    dict_tempo["fetes_mobiles"]["bapteme"] = str(bapteme_date.day) + f_transf_month_genitive(bapteme_date.month)
    bapteme = dict_tempo[bapteme_date] = {}
    bapteme["force"] = 100
    bapteme["I_vesp"] = "\\item I Vesperæ festi sequentis: omnia ut in festo Epiphaniæ, præter antiphonas in folio separato AM 305* ; oratio AM 304."
    bapteme["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((bapteme_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
    bapteme["num_day"] = "\\textbf{" + str(bapteme_date.day) + "} &"
    bapteme["symbols"] = "".join(f_symbols(bapteme_date)) + (" " if f_symbols(bapteme_date) != "" else "")
    num_dim_post_nat = "II" if noel_date.weekday() == 6 or noel_date.weekday() == 0 else "III"
    bapteme["header"] = " \\textbf{\\textsc{Dominica " + num_dim_post_nat + " post Nativitatem - Dominica in Baptismate Domini}} (I post Epiphaniam) - \\textbf{festum} - \\textit{Alb}."
    lect_bapteme = {"A": "Is \\textbf{42}, 1-4.6-7 / Act \\textbf{10}, 34-38 / Mt \\textbf{3}, 13-17", "B": "Is \\textbf{55}, 1-11 / 1 Io \\textbf{5}, 1-9 / Mc \\textbf{1}, 7-11", "C": "Is \\textbf{40}, 1-5.9-11 / Tit \\textbf{2}, 11-14 ; \\textbf{3}, 4-7 / Lc \\textbf{3}, 15-16.21-22"}
    bapteme["body"] = "\n\\item In Officio: omnia dicuntur sicut in festo Epiphaniæ, præter antiphonas in folio separato AM 305* ; oratio AM 304.\n\\item Ad Vigilias: olim die 13 ianuarii ; in I nocturno lectiones e dominica I post Epiphaniam cum responsorio \\textit{Hodie in Iordane} (post lectionem I).\n\\item \\textit{In ML: Missa in Commemoratione Baptismatis Domini Nostri Iesu Christi.}\n\\item In MC: lectiones propriæ: " + lect_bapteme[year_letter] + " ; præfatio propria."
    bapteme["II_vesp"] = "\n}\n\\ApplyParBox{1cm}{\\begin{center}\\large{\\textit{Post Completorium explicit}}\\par\\large{\\textit{tempus Nativitatis.}}\\end{center}"
    
    # Féries entre Octave de Noël et Baptême:
    for i in range((bapteme_date - noel_date).days + 6):
        new_day_date = noel_date + datetime.timedelta(days = i + 8)
        if new_day_date != dim_2_ap_noel_date and new_day_date != bapteme_date:
            new_day = dict_tempo[new_day_date] = {}
            new_day["force"] = 10
            new_day["num_day"] = "\\textbf{" + str(new_day_date.day) + "} & " +  f_transf_weekday(new_day_date.weekday())
            new_day["symbols"] = "".join(f_symbols(new_day_date))
            new_day["header"] = " - de ea - \\textit{Alb}." if new_day_date.weekday() != 5 else " - de eo - \\textit{Alb}."
            if new_day_date.day == 7 and new_day_date.weekday() != 6:
                current_lectiones = lectiones["nativ"]
                lect_nativ = ""
                for i in range(6 - new_day_date.weekday()):
                    lect_nativ += "\n\\item[" + str(7 + i) + " ian.] " + current_lectiones[7 + i]
                lectiones_body = "\n\\ApplyLectHeader{Post Epiphaniam Domini : lectiones de tempore}\n\\ApplyLectBody{" + lect_nativ + "}"
                new_day["generalities"] = "\n\\newpage\n\\ApplyParBox{0cm}{\\ApplyGenerTitleHuge{Tempus Nativitatis II}}\\ApplyGenerTitleLarge{Ab Epiphania usque ad}\n\\ApplyGenerTitleLarge{festum Baptismatis Domini}\n\\ApplyGenerSubTitle{In Officio}\n\\ApplyGenerList{\n\\item Oratio de Epiphania \\textit{Deus, qui hodierna die}.\n\\item Ad Vigilias: sumitur ordinarium officii ferialis tempore Epiphaniæ; lectiones SO.\n\\item Ad Laudes et Vesperas: antiphonæ et psalmi de feria, reliqua ut in festo Epiphaniæ; ad Benedictus et Magnificat: antiphonæ propriæ (AM 297 et sequentibus).\n\\item ß \\textit{Benedicamus Domino}: ad Laudes VI$_2$; ad Vesperas VI$_1$.\n\\item Ad Horas minores: antiphonæ de Epiphania.\n\\item Continuatur tonus Epiphaniæ ad Horas minores et Completorium.}\n\\ApplyGenerSubTitle{In ML}\n\\ApplyGenerList{\n\\item Præfatio de Epiphania.\n\\item Missæ defunctorum «cotidianæ» non permittuntur.}\n\\ApplyGenerSubTitle{In MC}\n\\ApplyGenerList{\n\\item In lectionario in lingua gallica, lectiones pro die 7 ianuarii sumendæ sunt e feria II post Epiphania ; pro die 8, e feria III, et sic in aliis feriis.\n\\item Præfatio de Epiphania.}\n\\ApplyGenerSubTitle{Ad mensam}\n\\ApplyGenerList{\n\\item Benedictio de Epiphania.}\n\\vspace{1cm}" + lectiones_body + "\n\\medskip"
                vigiles_ap_epiph = "\n\\item Ad Vigilias: lectio \\textit{Veritatem} de epistola ad Romanos"
                vigiles_ap_epiph += " et sic usque ad sabbatum.\\par" if new_day_date.weekday() != 5 else "."
            else:
                vigiles_ap_epiph = ""
            new_day["body"] = vigiles_ap_epiph + (ant_bened_temps_epiph[new_day_date.day] if new_day_date.day in ant_bened_temps_epiph else "") + ("\n\\item \\textit{In ML: Missa de sacratissimo Corde Iesu (\\emph{Gloria}).}" if new_day_date.day < 8 and new_day_date.weekday() == 4 else "") + ("\n\\item \\textit{In ML (Alb.)  : Immaculati Cordis Beatæ Mariæ Virginis.}" if new_day_date.day < 8 and new_day_date.weekday() == 5 else "")
            new_day["II_vesp"] = ant_magnif_temps_epiph[new_day_date.day] if new_day_date.day in ant_magnif_temps_epiph else ""

    # Date de Pâques:
    v1 = current_year - 1900
    v2 = v1 % 19
    v3 = (((v2 * 7) + 1) // 19)
    v4 = ((v2 * 11) + 4 - v3) % 29
    v5 = (v1 // 4)
    v6 = (v1 + v5 + 31 - v4) % 7
    v7 = 25 - v4 - v6
    paques_day = v7 if v7 > 0 else (31 + v7)
    paques_month = 4 if v7 > 0 else 3
    paques_date = datetime.date(current_year, paques_month, paques_day)
    
    # Cendres:
    cendres_date = paques_date - datetime.timedelta(days = 46)
    dict_tempo["fetes_mobiles"]["cendres"] = str(cendres_date.day) + f_transf_month_genitive(cendres_date.month)
    cendres = dict_tempo[cendres_date] = {}
    cendres["force"] = 120
    cendres["generalities"] = "\n\\ApplyParBox{1cm}{\\begin{center}\\large{\\textit{Post Completorium explicit}}\\par\\large{\\textit{pars prior temporis per annum.}}\\end{center}}\n\\newpage\n\\ApplyParBox{1cm}{\\ApplyGenerTitleHuge{Tempus Quadragesimæ}\n\\medskip\n\\ApplyGenerTitleLarge{Usque ad Sabbatum}\n\\ApplyGenerTitleLarge{Hebdomadæ quartæ}}\n\\ApplyGenerSubTitle{In Officio}\n\\ApplyGenerList{\\item Ab initio Vigiliarum Feriæ IV Cinerum sumitur ordinarium officii ferialis temporis Quadragesimæ (in breviario post Dominicam I in Quadragesima vel in AM 336).\n\\item Item omittitur ubique \\textit{Alleluia} usque ad Sabbatum Sanctum. Post \\textit{Deus in adiutorium}, ubi dicebatur \\textit{Alleluia}, dicitur \\textit{Laus tibi, Domine, Rex æternæ gloriæ}.\n\\item In Officio feriali : \\textit{Kyrie}, \\textit{Pater} et oratio dicuntur ad omnes Horas flexis genibus.\n\\item Ad Vigilias : in dominicis, post quatuor lectiones II vel III nocturni cantatur novissimum ¶; deinde sub congruenti ø dicuntur tria cantica \\textit{Deducant} de tempore Quadragesimæ et Passionis; quibus dictis, et repetita ø, hebdomadarius immediate cantat orationem diei post \\textit{Oremus}. In feriis leguntur tres lectiones de homilia cum ¶ 3.\n\\item Ad Laudes : dicuntur cantica ferialia.\n\\item Ad Benedictus et Magnificat : antiphonæ propriæ.\n\\item Memoriæ obligatoriæ occurentes in feriis Quadragesimæ habendæ sunt uti memoriæ ad libitum. Ad Laudes adduntur post orationem conclusivam, in qua omittitur conclusio \\textit{Per Dominum}, antiphona, versiculus et oratio de sancto.}\n\\ApplyGenerSubTitle{In MC}\n\\ApplyGenerList{\\item Missa propria singulis diebus.\n\\item In feriis Quadragesimæ, occurente memoria alicuius sancti, dicitur collecta de sancto, loco collectæ de feria.\n\\item Tractus dicitur in Feria IV Cinerum, dominicis et sollemnitatibus.\n\\item In feriis : omnia cantantur in tono simplici, præter orationem super oblata, quæ semper in tono solemni cantatur (\\textit{Pater} in tono B).\n\\item Dicitur oratio super populum singulis diebus de tempore. Ad ritum conclusionis missæ, post \\textit{Dominus vobiscum}, diaconus vel ipse sacerdos cantat \\textit{Inclinate vos ad benedictionem}, postquam omnes profunde se inclinant dum sacerdos cantat, manibus extensis super eos, orationem super populum. Hac expleta, omnes surgunt et respondent \\textit{Amen}, postquam iterum se inclinant sub benedictionem sacerdotis, more solito, quam sequitur dimissio.}\n\\ApplyGenerSubTitle{In ML}\n\\ApplyGenerList{\\item Missa propria singulis diebus (Missæ votivæ et Missæ defunctorum «cotidianæ» non permittuntur).\n\\item Dicitur præfatio de Quadragesima in Missis de tempore et in ceteris Missis quæ celebrantur eodem tempore et præfatione propria carent.\n\\medskip\n\\item Cras ieiunium ecclesiasticum cum abstinentia carnium.}\n\\medskip"
    cendres["num_day"] = "\\textbf{" + str(cendres_date.day) + "} &"
    cendres["symbols"] = " µ"
    cendres["header"] = " \\textsc{Feria IV Cinerum} - \\textit{Viol.}"
    cendres["body"] = "\n\\item In MC : post Evangelium, benedictio et impositio cinerum ; Or. n. 8 ; præfatio IV de Quadragesima (et sic in feriis sequentibus)."
    current_lectiones = lectiones["post_cineres"]
    cendres["lectiones_header"] = current_lectiones["header"]
    lectiones_body = ""
    for i in range(4):
        lectiones_body += "\n\\item[" + f_transf_weekday(i + 2) + "] " + current_lectiones[i]
    cendres["lectiones_body"] = lectiones_body
    
    # Féries entre les Cendres et le 1er dim. de Carême:
    for i in range(3):
        new_day_date = cendres_date + datetime.timedelta(days = i + 1)
        new_day = dict_tempo[new_day_date] = {}
        new_day["force"] = 10
        new_day["num_day"] = "\\textbf{" + str(new_day_date.day) + "} & " +  f_transf_weekday(new_day_date.weekday())
        new_day["symbols"] = "".join(f_symbols(new_day_date, "Quadr"))
        new_day["header"] = " - de ea - \\textit{Viol.}" if i != 2 else " - de eo - \\textit{Viol.}"
    
    # Dimanches de carême et leurs féries:
    for i in range(4):
        new_dim_careme_date = cendres_date + datetime.timedelta(days = 4 + (i * 7))
        new_dim_careme = dict_tempo[new_dim_careme_date] = {}
        new_dim_careme["force"] = 120
        new_dim_careme["I_vesp"] = "\\item I Vesperæ dominicæ sequentis."
        new_dim_careme["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((new_dim_careme_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
        new_dim_careme["num_day"] = "\\textbf{" + str(new_dim_careme_date.day) + "} &"
        new_dim_careme["symbols"] = "".join(f_symbols(new_dim_careme_date))
        dim_laetare = ", Lætare}" if i == 3 else "}"
        new_dim_careme["header"] = " \\textbf{\\textsc{Dominica " + f_roman_numbers(i + 1) + " in Quadragesima}" + dim_laetare + " - de ea - \\textit{Viol.}"
        lectures_annee_A = " tres lectiones Anno A ;" if (i == 2 or i == 3) and year_letter != "A" else ""
        orgue = "\n\\item Hodie pulsantur organa ad Missam, non vero in aliis Horis." if i == 3 else ""
        new_dim_careme["body"] = orgue + "\n\\item In MC :" + lectures_annee_A + " præfatio propria. "
        new_dim_careme["II_vesp"] = "\n\\item Vesperæ dominicæ." if new_dim_careme_date.month == 3 and (new_dim_careme_date.day == 19 or new_dim_careme_date.day == 25) else ""# Cas où un dimanche de carême tombe pour la saint Joseph ou l'Annonciation : la solennité est reportée et les Vêpres sont celles du dimanche.  
        new_dim_careme["preface_feries"] = "\n\\item In feriis: præfatio " + f_roman_numbers(i + 1) + " de Quadragesima, nisi aliter notetur."
        current_lectiones = lectiones["hebdo_" + str(i + 1) + "_quadr"]
        new_dim_careme["lectiones_header"] = current_lectiones["header"]
        lect_first_line_A = "\n\\item[Dom. A] " + current_lectiones["dim"]["A"] if (i == 2 or i == 3) and year_letter != "A" else ""
        lectiones_body = lect_first_line_A + "\n\\item[Dom. " + year_letter + "] " + current_lectiones["dim"][year_letter]
        new_dim_careme["II_vesp"] = "\\item Vesperæ dominicæ." if new_dim_careme_date.month == 3 and (new_dim_careme_date.day == 18 or new_dim_careme_date.day == 19) else ""
        
        for j in range(6):
            lectiones_body += "\n\\item[" + f_transf_weekday(j) + "] " + current_lectiones[j]
            new_day_careme_date = new_dim_careme_date + datetime.timedelta(days = j + 1)
            new_day_careme = dict_tempo[new_day_careme_date] = {}
            new_day_careme["force"] = 10
            new_day_careme["num_day"] = "\\textbf{" + str(new_day_careme_date.day) + "} &" + f_transf_weekday(new_day_careme_date.weekday())
            new_day_careme["symbols"] = "".join(f_symbols(new_day_careme_date, "Quadr"))
            new_day_careme["header"] = " - de ea - \\textit{Viol.}" if j != 5 else " - de eo - \\textit{Viol.}"
        new_dim_careme["lectiones_body"] = lectiones_body
        
    # Dim. de la Passion:
    passion_date = new_dim_careme_date + datetime.timedelta(days = 7)
    passion = dict_tempo[passion_date] = {}
    passion["force"] = 120
    passion["I_vesp"] = "\\item I Vesperæ dominicæ sequentis."
    passion["generalities"] = "\n\\medskip\n\\ApplyGenerList{\n\\item A I Vesperis dominicæ V in Quadragesima sumitur ordinarium Officii temporis Passionis (AM 382).\n\\item ß \\textit{Gloria Patri} dicitur de more (pro cantu huius versiculi in responsorio brevi, vide in AM 1044 vel 336).\n\\item Ad Vigilias : invitatorium \\textit{Hodie si vocem} ; quarta stropha psalmi 94 incipit a verbis \\textit{Sicut in exacerbatione}.\n\\item Cruces et imagines per ecclesiam cooperiuntur.\n\\item In ML de tempore : non dicitur psalmus \\textit{Iudica} ante confessionem, neque \\textit{Gloria} ad introitum et post psalmum \\textit{Lavabo}.}"
    passion["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((passion_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
    passion["num_day"] = "\\textbf{" + str(passion_date.day) + "} &"
    passion["symbols"] = "".join(f_symbols(passion_date))
    passion["header"] = " \\textbf{\\textsc{Dominica V in Quadragesima}} (I Passionis) - de ea - \\textit{Viol.}"
    passion["body"] = "\\item In MC :" + (" tres lectiones Anno A ;" if year_letter != "A" else "") + " præfatio propria."
    passion["preface_feries"] = "\n\\item In feriis : præfatio I de Passione Domini, nisi aliter notetur."
    current_lectiones = lectiones["hebdo_5_quadr"]
    passion["lectiones_header"] = current_lectiones["header"]
    lect_first_line_A = "\n\\item[Dom. A] " + current_lectiones["dim"]["A"] if year_letter != "A" else ""
    lectiones_body = lect_first_line_A + "\n\\item[Dom. " + year_letter + "] " + current_lectiones["dim"][year_letter]
    passion["II_vesp"] = "\\item Vesperæ dominicæ." if passion_date.month == 3 and (passion_date.day == 18 or passion_date.day == 19) else ""
        
    # Féries de la 5e sem. de Carême:
    for i in range(6):
        # if i == 0:
        #     lectiones_body += "\n\\item[" + f_transf_weekday(i) + "] " + (current_lectiones[i]["C"] if year_letter == "C" else current_lectiones[i]["AB"])
        # else:
        #     lectiones_body += "\n\\item[" + f_transf_weekday(i) + "] " + current_lectiones[i]
        lectiones_body += "\n\\item[" + f_transf_weekday(i) + "] " + current_lectiones[i]
        new_day_date = passion_date + datetime.timedelta(days = i + 1)
        new_day = dict_tempo[new_day_date] = {}
        new_day["force"] = 10
        new_day["num_day"] = "\\textbf{" + str(new_day_date.day) + "} & " +  f_transf_weekday(new_day_date.weekday())
        new_day["symbols"] = "".join(f_symbols(new_day_date, "Quadr"))
        new_day["header"] = " - de ea - \\textit{Viol.}" if i != 5 else " - de eo - \\textit{Viol.}"
        passion["lectiones_body"] = lectiones_body
    
    # Rameaux:
    rameaux_date = passion_date + datetime.timedelta(days = 7)
    dict_tempo["fetes_mobiles"]["rameaux"] = str(rameaux_date.day) + f_transf_month_genitive(rameaux_date.month)
    rameaux = dict_tempo[rameaux_date] = {}
    rameaux["force"] = 120
    rameaux["I_vesp"] = "\\item I Vesperæ dominicæ sequentis."
    rameaux["generalities"] = "\n\\newpage\n\\ApplyParBox{1cm}{\\ApplyGenerTitleHuge{Hebdomada Sancta}}"
    rameaux["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((rameaux_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
    rameaux["num_day"] = "\\textbf{" + str(rameaux_date.day) + "} &"
    rameaux["symbols"] = "".join(f_symbols(rameaux_date))
    rameaux["header"] = " \\textbf{\\textsc{Dominica in Palmis de Passione Domini}} - de ea - \\textit{Rub.}"
    rameaux["body"] = "\\item Ad Vigilias : in II nocturno sumuntur lectiones 7 et 8 cum ¶~8. Cantato ¶, omissis canticis, hebdomadarius immediate cantat orationem diei post \\textit{Oremus}.\\item Ad Laudes : psalmi 148 et 149 omittuntur. \\item \\textit{In ML (Viol.) : ante lectionem historiæ Passionis omittuntur \\emph{Dominus vobiscum} et cætera (uti indicatur in Missali) ; post lectionem non respondetur \\emph{Laus tibi Christe} et celebrans non osculatur librum (quod servatur etiam feria III et IV) ; legitur in fine (loco Evangelii sancti Ioannis) Evangelium ut in benedictione ramorum.}\n\\item In MC : ante Missam, benedictio et processio palmarum ; omittitur antiphona ad introitum ; circa finem historiæ Passionis, genuflectitur et pausatur aliquantulum ; præfatio propria."
    rameaux["preface_feries"] = "\n\\item In feriis : præfatio II de Passione Domini, nisi aliter notetur."
    current_lectiones = lectiones["rameaux"]
    rameaux["lectiones_header"] = current_lectiones["header"]
    lectiones_body = "\n\\item[Dom. " + year_letter + "] " + "\\textit{Ante processionem:} " + current_lectiones["ante_proc"][year_letter]
    lectiones_body += "\n\\item[Dom. " + year_letter + "] " + current_lectiones["dim"][year_letter]
    for i in range(3):
        lectiones_body += "\n\\item[" + f_transf_weekday(i) + "] " + current_lectiones[i]
    rameaux["lectiones_body"] = lectiones_body
    rameaux["II_vesp"] = "\\item Vesperæ dominicæ." if rameaux_date.month == 3 and (rameaux_date.day == 18 or rameaux_date.day == 19) else ""
        
    # Semaine Sainte:
    lundi_saint_date = rameaux_date + datetime.timedelta(days = 1)
    lundi_saint = dict_tempo[lundi_saint_date] = {}
    lundi_saint["force"] = 120
    lundi_saint["num_day"] = "\\textbf{" + str(lundi_saint_date.day) + "} &"
    lundi_saint["header"] = " \\textbf{\\textsc{Feria II Hebdomadæ Sanctæ}} - de ea - \\textit{Viol.}"
    lundi_saint["body"] = "\\item Ad Laudes et Horas minores : antiphonæ propriæ."
    
    mardi_saint_date = rameaux_date + datetime.timedelta(days = 2)
    mardi_saint = dict_tempo[mardi_saint_date] = {}
    mardi_saint["force"] = 120
    mardi_saint["num_day"] = "\\textbf{" + str(mardi_saint_date.day) + "} &"
    mardi_saint["header"] = " \\textbf{\\textsc{Feria III Hebdomadæ Sanctæ}} - de ea - \\textit{Viol.}"
    mardi_saint["body"] = "\\item Ad Laudes et Horas minores : antiphonæ propriæ."
    
    mercredi_saint_date = rameaux_date + datetime.timedelta(days = 3)
    mercredi_saint = dict_tempo[mercredi_saint_date] = {}
    mercredi_saint["force"] = 120
    mercredi_saint["num_day"] = "\\textbf{" + str(mercredi_saint_date.day) + "} &"
    mercredi_saint["symbols"] = " ł"
    mercredi_saint["header"] = " \\textbf{\\textsc{Feria IV Hebdomadæ Sanctæ}} - de ea - \\textit{Viol.}"
    mercredi_saint["body"] = "\\item Ad Laudes et Horas minores : antiphonæ propriæ."
    
    jeudi_saint_date = rameaux_date + datetime.timedelta(days = 4)
    jeudi_saint = dict_tempo[jeudi_saint_date] = {}
    jeudi_saint["force"] = 120
    jeudi_saint["num_day"] = "\\textbf{" + str(jeudi_saint_date.day) + "} &"
    jeudi_saint["header"] = " \\textbf{\\textsc{Feria V Hebdomadæ Sanctæ}} - de ea - \\textit{Viol.}"
    jeudi_saint["body"] = "\n\\item A Vigiliis usque ad Nonam : omnia ut in feriis præcedentibus.\n\\item Ad Vigilias : in I nocturno, lectiones de eadem feria V e II nocturno cum ¶ de III nocturno ; in II nocturno, ut in ordinario officii ferialis temporis Passionis.\n\\item Ad Laudes et Horas minores : antiphonæ de feria V in Cena Domini cum psalmis de feria V in psalterio ; reliqua ut in ordinario temporis Passionis.}"# On ferme l'accolade.
    evg_vp = {}
    evg_vp["A"] = "Mt \\textbf{28}, 1-10"
    evg_vp["B"] = "Mc \\textbf{16}, 1-8"
    evg_vp["C"] = "Lc \\textbf{24}, 1-12"
    jeudi_saint["II_vesp"] = "\n\\ApplyParBox{1cm}{\\begin{center}\\large{\\textit{Cum Missa Vespertina in Cena Domini}}\\par\\large{\\textit{incipit Sacrum Triduum Paschale.}}\\end{center}}\n\\ApplyParBox{4cm}{}\n\\ApplyParBox{2cm}{\\ApplyGenerTitleHuge{Sacrum Triduum Paschale}\n\\ApplyGenerList{\n\\item ß \\textit{Gloria Patri} dicitur de more.\n\\item Feria VI in Passione Domini et Sabbato Sancto : post Sextam, commemoratio pro defunctis omittitur.}\n\\ApplyLectHeader{Sacrum Triduum Paschale: lectiones}\n\\ApplyLectHeader{Feria V in Cena Domini in Missa}\n\\ApplyLectTriduum{Ex \\textbf{12}, 1-8.11-14 / 1 Co \\textbf{11}, 23-26 / Io \\textbf{13}, 1-15}\n\\ApplyLectHeader{Feria VI in Passione Domini in officio Passionis}\n\\ApplyLectTriduum{Is \\textbf{52}, 13 – \\textbf{53}, 12 / Heb \\textbf{4}, 14-16 ; \\textbf{5}, 7-9 / Io \\textbf{18}, 1 – \\textbf{19}, 1-42}\n\\ApplyLectHeader{Vigilia Paschalis in celebratione Vigiliæ}\n\\ApplyLectTriduum{(1L) Gen \\textbf{1} – \\textbf{2}, 1-2 / (2L) Gen \\textbf{22}, 1-18 / (3L) Ex \\textbf{14}, 15 – \\textbf{15}, 1a / (4L) Is \\textbf{54}, 5-14 / (5L) Is \\textbf{55}, 1-11 / (6L) Bar \\textbf{3}, 9-15.32 – \\textbf{4}, 1-4 / (7L) Ez \\textbf{36}, 16-17a.18-28 / (8L) Rom \\textbf{6}, 3-11 / (Ev) " + evg_vp[year_letter] + "}\n\\ApplyLectHeader{In Resurrectione Domini Nostri in Missa}\n\\ApplyLectTriduum{Act \\textbf{10}, 34a 37-43 / " + ("1 Co \\textbf{5}, 6b-8" if even_year else "Col \\textbf{3}, 1-4") + " / Io \\textbf{20}, 1-9}}\n\\newpage\n\\ApplyHeader{\\textbf{" + str(jeudi_saint_date.day) + "} & \\textbf{\\MakeUppercase{Missa in Cena Domini}} - Alb.}{\n\\ApplyBody{\n\\item In Missa : \\textit{Gloria} (pulsantur campanæ) ; post Evangelium fit lotio pedum quæ concluditur oratione fidelium n. 10 ; pro offertorio cantatur \\textit{Ubi Caritas} (in GR 168) ; præfatio I de Sanctissima Eucharistia ; \\textit{Communicantes}, \\textit{Hanc igitur} et \\textit{Qui pridie} propria ; in fine Missæ, omittuntur ritus conclusionis ; post missam, sollemnis translatio ac repositio Sanctissimi Sacramenti : cantatur hymnus \\textit{Pange Lingua} (GR 170), cum \\textit{Tantum ergo} : indulgentia plenaria.\n\\item Vesperæ omittuntur ab his qui Missam vespertinam intersunt.\n\\item Expleta celebratione, denudatur altare et aufertur crux ab ecclesia.\n\\item Ad cenam : ß \\textit{Christus factus est}.\n\\item Ad Completorium : superior, signo dato, indicat initiandum esse examen conscientiæ, quo absoluto dicitur \\textit{Confiteor} ; oratio \\textit{Visita} quæ concluditur sub silentio. Hodie et cras omittitur aspersio."
    
    vendredi_saint_date = rameaux_date + datetime.timedelta(days = 5)
    vendredi_saint = dict_tempo[vendredi_saint_date] = {}
    vendredi_saint["force"] = 120
    vendredi_saint["generalities"] = "\n\\ApplyGenerList{\\item Cras ieiunium ecclesiasticum cum abstinentia carnium.}"
    vendredi_saint["anniv"] = "\\textit{Cras incipiunt preces novendiales ad Divinam Misericordiam.}"
    vendredi_saint["num_day"] = "\\textbf{" + str(vendredi_saint_date.day) + "} &"
    vendredi_saint["symbols"] = " µ" + f_symbols(vendredi_saint_date)[1]
    vendredi_saint["header"] = " \\textbf{\\MakeUppercase{Feria VI In Passione Domini}} - \\textit{Rub}."
    vendredi_saint["body"] = "\n\\item \\textit{indulgentia plenaria pro recitatione orationis \\emph{En ego, o bone et dulcissime Iesu}.}\n\\item In Officio : altare omnino nudum sit, sine cruce et sine candelabris. In Vigiliis et Laudibus, candelabrum triangulare cum quindecim cereis adhibetur. Non pulsantur organa ad cantum sustentandum nec in Officio nec in celebratione Passionis.\n\\item Ad mensam : ß \\textit{Christus factus est}.\n\\item Celebratio Passionis Domini incipienda est circa horam nonam diei (Adoratio Sanctæ Crucis : indulgentia plenaria) ; expleta celebratione denudatur altare, relictis tamen cruce et candelabris.\n\\item Hodie post Crucis detectionem et cras usque ad Vigiliam paschalem exclusive, cruci genuflectitur.\n\\item Vesperæ omittuntur ab his qui sollemnem actionem liturgicam intersunt.\n\\item Ad Completorium : ut heri, sed ante Officium cantatur hymnus \\textit{Stabat Mater} (Besnier 174)."
    
    samedi_saint_date = rameaux_date + datetime.timedelta(days = 6)
    samedi_saint = dict_tempo[samedi_saint_date] = {}
    samedi_saint["force"] = 120
    samedi_saint["num_day"] = "\\textbf{" + str(samedi_saint_date.day) + "} &"
    samedi_saint["symbols"] = " ł" + f_symbols(samedi_saint_date)[1]
    samedi_saint["header"] = " \\textbf{\\MakeUppercase{Sabbato Sancto}} - \\textit{Viol.}"
    samedi_saint["body"] = "\n\\item In Officio : altare nudum sit, cum cruce tamen et quatuor candelabris accensis. In Vigiliis et Laudibus, candelabrum triangulare cum quindecim cereis adhibetur. Non pulsantur organa usque ad hymnum \\textit{Gloria} in Missa Vigiliæ paschalis.\n\\item Ad mensam : ß \\textit{Principes}.\n\\item Vesperæ celebrantur hora consueta.\n\\item Completorium necnon et Vigiliæ omittuntur ab his qui Vigiliam paschalem intersunt.}\n\\bigskip"# On ferme l'accolade.
    samedi_saint["II_vesp"] = "\n\\ApplyHeader{ &\\MakeUppercase{\\textbf{Vigilia paschalis}} - \\textit{Alb.}}\n\\ApplyBody{\n\\item Celebratio huius Vigiliæ peragenda est nocte.\n\\item In Missa : ad hymnum \\textit{Gloria} pulsantur campanæ ; post Evangelium, renovatio promissionum baptismalium : indulgentia plenaria ; Or. n. 11 ; præfatio paschalis I (\\textit{in hac potissimum nocte}) ; \\textit{Communicantes} et \\textit{Hanc igitur} propria ; \\textit{Pater} in tono C (GR 814) ; Missa concluditur benedictione sollemni ; \\textit{Ite Missa est} cum duobus \\textit{Alleluia}."
    
    # Pâques:
    dim_paques_date = paques_date
    dict_tempo["fetes_mobiles"]["paques"] = str(dim_paques_date.day) + f_transf_month_genitive(dim_paques_date.month)
    dim_paques = dict_tempo[dim_paques_date] = {}
    dim_paques["force"] = 100
    dim_paques["generalities"] = "\n\\medskip\n\\ApplyGenerSubTitle{A dominica Paschæ usque ad Pentecosten}\n\\ApplyGenerList{\n\\item Loco \\textit{Angelus Domini} dicitur \\textit{Regina Cæli} stando.\n\\item Ad aspersionem aquæ benedictæ, dominica : ø \\textit{Vidi aquam}.\n\\item Post prandium : loco psalmi \\textit{Miserere mei} dicitur psalmus \\textit{Confitemini}.}\n\\ApplyGenerSubTitle{Ad mensam}\n\\ApplyGenerList{\n\\item Ad benedictionem, dicitur ß \\textit{Hæc dies} (usque ad dominicam sequentem inclusive).}"
    dim_paques["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((dim_paques_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
    dim_paques["num_day"] = "\\textbf{" + str(dim_paques_date.day) + "} &"
    dim_paques["symbols"] = "".join(f_symbols(dim_paques_date)) + (" " if f_symbols(dim_paques_date) != "" else "")
    dim_paques["header"] = "\\textbf{\\MakeUppercase{Dominica Paschæ in Resurrectione Domini}} - \\textbf{sollemnitas maior cum octava} - \\textit{Alb}."
    dim_paques["body"] = "\n\\item Ad Laudes : Officium dominicæ Resurrectionis incipitur ab invitatorio Paschæ : \\textit{Domine labia mea aperies}, et statim psalmus 66 \\textit{Deus misereatur nostri}, cum sua antiphona \\textit{Surrexit Dominus vere alleluia}, quod sequuntur Laudes ; psalmi 148 et 149 omittuntur ; \\textit{Benedicamus Domino} cum duobus \\textit{Alleluia}.\n\\item In MC : sequentia ; præfatio paschalis I (\\textit{in hac potissimum die}) ; \\textit{Communicantes} et \\textit{Hanc igitur} propria ; \\textit{Pater} in tono C (GR 814) ; Missa concluditur benedictione sollemni ; \\textit{Ite Missa est} cum duobus \\textit{Alleluia}."
    dim_paques["II_vesp"] = "\n\\item Vesperæ sollemnitatis ; \\textit{Benedicamus Domino} cum duobus \\textit{Alleluia} ; benedictio Sanctissimi Sacramenti.\n\\item Ad Completorium : ø \\textit{Regina Cæli}.}\n\\newpage\n\\ApplyGenerTitleHuge{Tempus paschale I}\n\\smallskip\n\\ApplyGenerTitleLarge{Usque ad Ascensionem Domini}\n\\ApplyGenerSubTitle{In Officio}\n\\ApplyGenerList{\n\\item Ordinarium invenitur in breviario vel in AM 466.\n\\item Additur unus \\textit{Alleluia} ad invitatorium et versiculum ubi iam non habetur.\n\\item In Officio feriali : ad Benedictus et Magnificat antiphonæ propriæ.\n\\item Ad Laudes : pro antiphona ad Benedictus sabbato, sumitur antiphona \\textit{Regina cæli} (AM 718), nisi aliter notetur.\n\\item Ad Horas minores et Completorium : tonus paschalis etiam in memoriis et festis quæ non sunt de Beata Maria Virgine.}\n\\ApplyGenerSubTitle{In ML}\n\\ApplyGenerList{\n\\item In omnibus Missis, loco gradualis, dicuntur quatuor Alleluia cum ß tempori Paschali assignatis, adduntur duo \\textit{Alleluia} ad introitum, unus ad offertorium et communionem ubi iam non adsunt.\n\\item Præfatio paschalis dicitur etiam in ceteris Missis quæ præfatione propria carent.\n\\item Infra hebdomadam : quando resumitur Missa dominicæ præcedentis dicuntur \\textit{Gloria} et præfatio paschalis.}\n\\ApplyGenerSubTitle{In MC}\n\\ApplyGenerList{\n\\item In feriis : orationes propriæ.\\par}\n\\ApplyGenerSubTitle{Infra octavam}\n\\ApplyGenerList{\n\\item Ad Laudes, Vesperas et Horas minores : omnia ut in die Paschæ, præter antiphonas ad Benedictus, Magnificat et orationem.\n\\item In MC : \\textit{Gloria} ; quando cantatur \\textit{Alleluia}, dicitur sequentia \\textit{Victimæ paschali} ; præfatio paschalis I (\\textit{in hac potissimum die}) ; \\textit{Communicantes} et \\textit{Hanc igitur} propria ; \\textit{Ite Missa est} cum duobus \\textit{Alleluia}."
    current_lectiones = lectiones["in_albis"]
    dim_paques["lectiones_header"] = current_lectiones["header"]
    lectiones_body = ""
    
    # Octave de Pâques:
    for i in range(6):
        lectiones_body += "\n\\item[" + f_transf_weekday(i) + "] " + current_lectiones[i]
        fer_ap_paques_date = paques_date + datetime.timedelta(days = i + 1)
        fer_ap_paques = dict_tempo[fer_ap_paques_date] = {}
        fer_ap_paques["force"] = 100
        fer_ap_paques["num_day"] = "\\textbf{" + str(fer_ap_paques_date.day) + "} &" + f_transf_weekday(fer_ap_paques_date.weekday())
        fer_ap_paques["symbols"] = "".join(f_symbols(fer_ap_paques_date, "TP"))
        fer_ap_paques["header"] = " - \\textbf{\\textsc{De Octava Paschæ}} - \\textit{Alb}." if i != 5 else " - \\textbf{\\textsc{De Octava Paschæ}} (Sabbato in Albis) - \\textit{Alb.}"
        txt_body = ""
        if i == 0:
            txt_body = "\n\\item Ad Vigilias : psalmi de festo hebdomada I.\n\\item \\textit{postmeridiani laboris datur vacatio}."
        elif i == 1:
            txt_body = "\n\\item Ad Vigilias : psalmi de festo hebdomada II."
        elif i == 2:
            txt_body = "\n\\item Ad Vigilias : psalmi de feria cum antiphonis propriis et sic usque ad sabbatum in Albis."
        if txt_body != "": fer_ap_paques["body"] = txt_body
    dim_paques["lectiones_body"] = lectiones_body
    
    # Dimanches de Pâques et féries du Temps pascal:
    for i in range(5):
        dim_ap_paques_date = paques_date + datetime.timedelta(days = (i + 1) * 7)
        dim_ap_paques = dict_tempo[dim_ap_paques_date] = {}
        dim_ap_paques["force"] = 120
        dim_ap_paques["I_vesp"] = "\n\\item Ad Vesperas : antiphonæ et psalmi ut in die Paschæ ; capitulum de dominica \\textit{in Albis} ; ß \\textit{Hæc dies quam fecit Dominus} ; ad Magnificat : ø \\textit{Cum esset sero} (AM 475) ; ß \\textit{Benedicamus Domino} cum duobus \\textit{Alleluia}." if i == 0 else "\n\\item I Vesperæ dominicæ sequentis." + ("\n\\item \\textit{ante Completorium, cantantur litaniæ lauretanæ Beatæ Mariæ Virginis ad vocationes sacerdotales ac religiosas impetrandas pro die universali vocationum.}" if i == 2 else "")
        dim_ap_paques["anniv"] = "Indulgentia plenaria conceditur, suetis sub condicionibus (nempe Sacramentali Confessione, Eucharistica Communione et Oratione ad mentem Summi Pontificis) christifideli, qui, die Dominica II Paschæ seu de Divina Misericordia, in quacumque ecclesia vel oratorio, animo quidem omnino elongato ab affectu erga quodcumque peccatum, etiam veniale, pium exercitium in honorem Divinæ Misericordiæ participaverit, vel saltem coram SS.mo Eucharistiæ Sacramento, publice exposito vel etiam in tabernaculo adservato, Orationem Dominicam ac Symbolum Fidei recitaverit, addita pia aliqua invocatione ad Misericordem Iesum (e.g. “Misericors Iesu in Te confido”)." if i == 0 else ""
        dim_ap_paques["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((dim_ap_paques_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
        dim_ap_paques["num_day"] = "\\textbf{" + str(dim_ap_paques_date.day) + "} &"
        dim_ap_paques["symbols"] = "".join(f_symbols(dim_ap_paques_date))
        dim_ap_paques["header"] = (" \\textbf{\\textsc{Dominica " + f_roman_numbers(i + 2) + " Paschæ}} (seu Dominica " + f_roman_numbers(i + 1) + " post Pascha) - de ea - \\textit{Alb.}") if i != 0 else " \\textbf{\\textsc{Dominica II Paschæ}} seu \\textbf{\\textsc{De Divina Misericordia}} (Dominica in Albis) - de ea - \\textit{Alb.}"
        dim_ap_paques["body"] = ""
        if i == 0:
            dim_ap_paques["body"] = "\n\\item Officium huius diei persolvitur ut in die Paschæ præter ea quæ sequuntur.\n\\item Ad Vigilias : lectiones, ¶ et oratio e dominica \\textit{in Albis}.\n\\item Ad omnes Horas : capitula et oratio e dominica \\textit{in Albis} ; ß \\textit{Hæc dies}.\n\\item Ad Laudes et Vesperas : ß \\textit{Benedicamus Domino} cum duobus \\textit{Alleluia}.\n\\item Ad Benedictus : ø \\textit{Cum esset sero} (AM 475).\n\\item In MC : sequentia ; præfatio paschalis I (\\textit{in hac potissimum die}) ; \\textit{Communicantes} et \\textit{Hanc igitur} propria ; \\textit{Ite Missa est} cum duobus \\textit{Alleluia}.\n\\item Ad Magnificat : ø \\textit{Post dies octo} (AM 477)."
        elif i == 1:
            dim_ap_paques["body"] = "\n\\item Ad Vigilias : in nocturno I : lectiones 3 et 4 (cum titulo : \\textit{De Actibus Apostolórum}) ; ¶ lectionis 4."
            dim_ap_paques["body"] += "\n\\item In MC: præfatio pascalis III."
        else:
            dim_ap_paques["body"] += "\n\\item In MC: præfatio pascalis " + (f_roman_numbers(i + 2) if i != 4 else "II") + "."
        dim_ap_paques["preface_feries"] = ("\n\\item Ad Vigilias : in Officio feriali, lectio brevis \\textit{De Osea}, vel in memoriis, lectio unica de sancto, et sic usque ad dominicam I novembris." if i == 0 else "") + "\n\\item In feriis : præfatio paschalis " + (f_roman_numbers(i + 2) if i != 4 else "II") + ", nisi aliter notetur."
        current_lectiones = lectiones["hebdo_" + str(i + 2) + "_paques"]
        dim_ap_paques["lectiones_header"] = current_lectiones["header"]
        lectiones_body = "\n\\item[Dom. " + year_letter + "] " + current_lectiones["dim"][year_letter]            
        
        for j in range(6):
            if (i == 2) and (j == 0):
                lectiones_body += "\n\\item[" + f_transf_weekday(j) + "] " + (current_lectiones[j]["A"] if year_letter == "A" else current_lectiones[j]["BC"])
            else :
                lectiones_body += "\n\\item[" + f_transf_weekday(j) + "] " + current_lectiones[j] if j in current_lectiones else ""
            fer_tp_date = dim_ap_paques_date + datetime.timedelta(days = j + 1)
            fer_tp = dict_tempo[fer_tp_date] = {}
            fer_tp["force"] = 10
            fer_tp["num_day"] = "\\textbf{" + str(fer_tp_date.day) + "} &" + f_transf_weekday(fer_tp_date.weekday())
            fer_tp["symbols"] = "".join(f_symbols(fer_tp_date, "TP"))
            fer_tp["header"] = " - de ea - \\textit{Alb}." if j != 5 else " - de eo - \\textit{Alb}."
            if j == 4:
                fer_tp["body"] = "\n\\item \\textit{In ML: Missa de sacratissimo Corde Iesu (\\emph{Gloria}).}" if fer_tp_date.day < 8 else ""
                fer_tp["II_vesp"] = ant_vepres_vendr_tp[i] if i in ant_vepres_vendr_tp else ""
            if j == 5:
                fer_tp["body"] = "\n\\item \\textit{In ML: Immaculati Cordis Beatæ Mariæ Virginis.}" if fer_tp_date.day < 8 else ""
        dim_ap_paques["lectiones_body"] = lectiones_body
        if i == 4:
            current_lectiones = lectiones["ascension"]
            lectiones_ascension = "\n\\ApplyLectHeader{" + current_lectiones["header"] + "}"
            lectiones_ascension += "\n\\ApplyLectBody{\n\\item[Anno " + year_letter + "] " + current_lectiones["asc"][year_letter] + "\\smallskip"
            for i in range(2):
                lectiones_ascension += "\n\\item[" + f_transf_weekday(i + 4) + "] " + current_lectiones[i]
            dim_ap_paques["lectiones_body"] += "}\n" + lectiones_ascension
    
    # Ascension:
    ascension_date = paques_date + datetime.timedelta(days = 39)
    dict_tempo["fetes_mobiles"]["ascension"] = str(ascension_date.day) + f_transf_month_genitive(ascension_date.month)
    ascension = dict_tempo[ascension_date] = {}
    ascension["force"] = 100
    ascension["I_vesp"] = "\n\\item I Vesperæ solemnitatis sequentis."
    ascension["generalities"] = "\n\\newpage\n\\ApplyGenerSubTitle{Ad mensam}\n\\ApplyGenerList{\n\\item Benedictio de Ascensione.\n\\vspace{1cm}}"
    ascension["num_day"] = "\\textbf{" + str(ascension_date.day) + "} &" + " Feria V"
    ascension["header"] = " - ¬ \\textbf{\\MakeUppercase{In Ascensione Domini}} - \\textbf{sollemnitas maior} - \\textit{Alb}."
    ascension["body"] = "\n\\item In MC : præfatio I de Ascensione Domini ; \\textit{Communicantes} proprium ; \\textit{Pater} in tono C (GR 814) ; Missa concluditur benedictione sollemni."
    ascension["II_vesp"] = "\n\\item Vesperæ sollemnitatis ; benedictio Sanctissimi Sacramenti."
    
    # Féries entre 6e dim. de Pâques et Ascension:
    for i in range((ascension_date - dim_ap_paques_date).days - 1):
        new_day_date = dim_ap_paques_date + datetime.timedelta(days = i + 1)
        new_day = dict_tempo[new_day_date] = {}
        new_day["force"] = 10
        new_day["num_day"] = "\\textbf{" + str(new_day_date.day) + "} & " +  f_transf_weekday(new_day_date.weekday())
        new_day["symbols"] = "".join(f_symbols(new_day_date, "TP"))
        new_day["header"] = " - de ea - \\textit{Alb}."
        new_day["body"] = "\\item \\textit{In ML: Missa de Vigilia Ascensionis.}" if i == 2 else ""
    
    # Féries entre l'Ascension et le 7e dim. de Pâques:
    for i in range(2):
        new_day_date = ascension_date + datetime.timedelta(days = i + 1)
        new_day = dict_tempo[new_day_date] = {}
        new_day["force"] = 10
        new_day["generalities"] = "\n\\newpage\n\\ApplyParBox{1cm}{\\ApplyGenerTitleHuge{Tempus paschale II}}\n\n\\ApplyGenerTitleLarge{post Ascensionem Domini}\n\\ApplyGenerSubTitle{Ad mensam}\n\\ApplyGenerList{\n\\item Benedictio de Ascensione.}\n\\ApplyGenerSubTitle{In Officio}\n\\ApplyGenerList{\n\\item Ad Benedictus et Magnificat : antiphonæ ut in die Ascensionis, nisi aliter notetur.\n\\item Ad Vesperas : in Officio dominicali et feriali, cantantur ¶ \\textit{Spiritus Paraclitus} et hymnus \\textit{Veni Creator} (AM 518).}\n\\ApplyGenerSubTitle{In ML et MC}\n\\ApplyGenerList{\n\\item Præfatio de Ascensione dicitur, etiam in ceteris Missis quæ præfatione propria carent.\n\\item In feriis : præfatio I de Ascensione, nisi aliter notetur.}\n\\medskip" if i == 0 else ""
        new_day["num_day"] = "\\textbf{" + str(new_day_date.day) + "} & " +  f_transf_weekday(new_day_date.weekday())
        new_day["symbols"] = "".join(f_symbols(new_day_date, "TP"))
        new_day["header"] = " - de ea - \\textit{Alb}." if i != 1 else " - de eo - \\textit{Alb}."
        new_day["body"] = "\n\\item Ad Benedictus : ø \\textit{Regina cæli} (AM 718)." if i == 1 else ""
        new_day["body"] += "\n\\item \\textit{In ML: Missa de sacratissimo Corde Iesu (\\emph{Gloria}).}" if new_day_date.day < 8 and new_day_date.weekday() == 4 else ""
    
    # 7e dim. de pâques:
    dim_7_paques_date = dim_ap_paques_date + datetime.timedelta(days = 7)
    dim_7_paques = dict_tempo[dim_7_paques_date] = {}
    dim_7_paques["force"] = 100
    dim_7_paques["I_vesp"] = "\n\\item I Vesperæ dominicæ sequentis."
    dim_7_paques["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((dim_7_paques_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
    dim_7_paques["num_day"] = "\\textbf{" + str(dim_7_paques_date.day) + "} &"
    dim_7_paques["symbols"] = "".join(f_symbols(dim_7_paques_date))
    dim_7_paques["header"] = " \\textbf{\\textsc{Dominica VII Paschæ}} (seu Dominica post Ascensionem vel infra octavam Ascensionis) - de ea - \\textit{Alb}."
    dim_7_paques["body"] = "\n\\item Ad Vigilias : invitatorium de Ascensione.\n\\item Ad Laudes et Horas minores : antiphonæ et psalmi de dominica in psalterio tempore paschali.\n\\item In MC : præfatio II de Ascensione.\n\\item Vesperæ dominicæ : antiphonæ et psalmi de dominica in psalterio tempore paschali ; ¶ et hymnus in AM 518."
    dim_7_paques["preface_feries"] = "\n\\item In feriis : præfatio II de Ascensione, nisi aliter notetur."
    current_lectiones = lectiones["hebdo_7_paques"]
    dim_7_paques["lectiones_header"] = current_lectiones["header"]
    lectiones_body = "\n\\item[Dom. " + year_letter + "] " + current_lectiones["dim"][year_letter]
    for i in range(6):
        lectiones_body += "\n\\item[" + f_transf_weekday(i) + "] " + current_lectiones[i]
    dim_7_paques["lectiones_body"] = lectiones_body
    
    # Féries entre le 7e dim. de Pâques et la Pentecôte:
    for i in range(6):
        new_day_date = dim_7_paques_date + datetime.timedelta(days = i + 1)
        new_day = dict_tempo[new_day_date] = {}
        new_day["force"] = 10
        new_day["num_day"] = "\\textbf{" + str(new_day_date.day) + "} & " +  f_transf_weekday(new_day_date.weekday())
        new_day["symbols"] = "".join(f_symbols(new_day_date, "TP"))
        new_day["header"] = " - de ea - \\textit{Alb}." if i != 5 else " - de eo - \\textit{Alb}."
        new_day["body"] = "\n\\item Ad Benedictus : ø \\textit{Caritas Dei} (AM 531).\n\\item \\textit{In ML (Rub.) : Missa de Vigilia Pentecostes.}" if i == 5 else ("\n\\item \\textit{In ML: Missa de sacratissimo Corde Iesu (\\emph{Gloria}).}" if new_day_date.day < 8 and new_day_date.weekday() == 4 else "")
    
    # Pentecôte:
    pentecote_date = ascension_date + datetime.timedelta(days = 10)
    dict_tempo["fetes_mobiles"]["pentecote"] = str(pentecote_date.day) + f_transf_month_genitive(pentecote_date.month)
    pentecote = dict_tempo[pentecote_date] = {}
    pentecote["force"] = 120
    pentecote["I_vesp"] = "\n\\item I Vesperæ sollemnitatis sequentis ; ß \\textit{Benedicamus Domino} cum duobus \\textit{Alleluia}.}\n\\ApplyGenerSubTitle{Ad mensam}\n\\ApplyGenerList{\n\\item Benedictio de Pentecoste."
    pentecote["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((pentecote_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
    pentecote["num_day"] = "\\textbf{" + str(pentecote_date.day) + "} &"
    pentecote["symbols"] = "".join(f_symbols(pentecote_date)) + (" " if f_symbols(pentecote_date) != "" else "")
    pentecote["header"] = "\\textbf{\\MakeUppercase{Dominica Pentecostes}} - \\textbf{sollemnitas maior} - \\textit{Rub}."
    pentecote["body"] = "\n\\item Ad Vigilias et Laudes : ß \\textit{Benedicamus Domino} cum duobus \\textit{Alleluia}\n\\item In MC : sequentia ; præfatio et \\textit{Communicantes} propria ; \\textit{Pater} in tono C (GR 814) ; Missa concluditur benedictione sollemni ; \\textit{Ite Missa est, Alleluia Alleluia} ut in die Paschæ."
    pentecote["II_vesp"] = "\n\\item Vesperæ sollemnitatis : hymnus \\textit{Veni, Creator}  : indulgentia plenaria ; ß \\textit{Benedicamus Domino} cum duobus \\textit{Alleluia} ; benedictio Sanctissimi Sacramenti."
    pentecote["lectiones_header"] = "Dominica Pentecostes : lectiones"
    pentecote["lectiones_body"] = "\n\\item[Dom.] Act \\textbf{2}, 1-11 / 1 Co \\textbf{12}, 3b-7.12-13 / Io \\textbf{20}, 19-23"

    # (La Trinité sera traitée dans les Dimanches per annum.)

    # Fête-Dieu:
    fete_dieu_date = pentecote_date + datetime.timedelta(days = 11)
    dict_tempo["fetes_mobiles"]["fete_dieu"] = str(fete_dieu_date.day) + f_transf_month_genitive(fete_dieu_date.month)
    fete_dieu = dict_tempo[fete_dieu_date] = {}
    fete_dieu["force"] = 115 # Ainsi cette solennité l'emporte sur saint J.B.
    fete_dieu["I_vesp"] = "\n\\item I Vesperæ sollemnitatis sequentis." 
    fete_dieu["num_day"] = "\\textbf{" + str(fete_dieu_date.day) + "} &" + " Feria V"
    fete_dieu["header"] = " - ¬ \\textbf{\\MakeUppercase{Ss.mi Corporis et Sanguinis Christi} - sollemnitas maior} - \\textit{Alb}."
    lectiones_fd = {"A": "Deut \\textbf{8}, 2-3.14b-16a / 1 Co \\textbf{10}, 16-17 / Io \\textbf{6}, 51-59", "B": "Ex \\textbf{24}, 3-8 / Hebr \\textbf{9}, 11-15 / Mc \\textbf{14}, 12-16.22-26", "C": "Gen \\textbf{14}, 18-20 / 1 Co \\textbf{11}, 23-26 / Lc \\textbf{9}, 11b-17"}
    fete_dieu["body"] = "\n\\item \\textit{In ML: præfatio de Sanctissimo Sacramento.}\n\\item In MC: MR 489; lectiones: " + lectiones_fd[year_letter] + "; sequentia; præfatio II de Sanctissima Eucharistia ; \\textit{Pater} in tono C (GR 814)."
    fete_dieu["II_vesp"] = "\n\\item Vesperæ sollemnitatis; post Vesperas, sollemnis processio Sanctissimi Sacramenti ; benedictio Sanctissimi Sacramenti : \\textit{Tantum ergo} cum ß \\textit{Panem de cælo} cum \\textit{Alleluia} (indulgentia plenaria)."

    # Sacré-Cœur:
    sacre_coeur_date = fete_dieu_date + datetime.timedelta(days = 8)
    dict_tempo["fetes_mobiles"]["sacre_coeur"] = str(sacre_coeur_date.day) + f_transf_month_genitive(sacre_coeur_date.month)
    sacre_coeur = dict_tempo[sacre_coeur_date] = {}
    sacre_coeur["force"] = 115 # Ainsi cette solennité l'emporte sur saint J.B. et SS. Pierre et Paul.
    sacre_coeur["I_vesp"] = "\n\\item I Vesperæ sollemnitatis sequentis." 
    sacre_coeur["num_day"] = "\\textbf{" + str(sacre_coeur_date.day) + "} &" + " Feria VI"
    sacre_coeur["symbols"] = " ł" + f_symbols(sacre_coeur_date)[1]
    sacre_coeur["header"] = " - þ \\textbf{\\MakeUppercase{Sacratissimi Cordis Iesu}} - \\textbf{sollemnitas minor} - \\textit{Alb}."
    lectiones_sc = {"A": "Deut \\textbf{7}, 6-11 / 1 Io \\textbf{4}, 7-16 / Mt \\textbf{11}, 25-30", "B": "Os \\textbf{11}, 1.3-4.8c-9 / Ep \\textbf{3}, 8-12.14-19 / Io \\textbf{19}, 31-37", "C": "Ez \\textbf{34}, 11-16 / Rom \\textbf{5}, 5b-11 / Lc \\textbf{15}, 3-7"}
    sacre_coeur["body"] = "\n\\item In MC: MR 492 ; lectiones: " + lectiones_sc[year_letter] + "; præfatio propria."
    sacre_coeur["II_vesp"] = "\n\\item Vesperæ sollemnitatis ; ad benedictionem Sanctissimi Sacramenti recitetur \\textit{Reparationis actus Sacratissimo Cordi Iesu} : indulgentia plenaria."
    
    # Cœur Immaculé de Marie:
    coeur_imm_marie_date = sacre_coeur_date + datetime.timedelta(days = 1)
    coeur_imm_marie = dict_tempo[coeur_imm_marie_date] = {}
    coeur_imm_marie["force"] = 50 # Pour être plus fort qu'une mémoire majeure du Sancto.
    coeur_imm_marie["num_day"] = "\\textbf{" + str(coeur_imm_marie_date.day) + "} &" + " Sabbato"
    coeur_imm_marie["symbols"] = " µ" if sacre_coeur_date.day < 8 else "" + f_symbols(coeur_imm_marie_date, "")[1]
    coeur_imm_marie["header"] = " - \\textsc{Immaculati Cordis Beatæ Mariæ Virginis} - \\textbf{memoria maior} - \\textit{Alb}."
    coeur_imm_marie["body"] = "\\item In Officio: omnia de Communi festorum Beatæ Mariæ Virginis, præter sequentia.\n\\item Oratio in supplemento 129.\n\\item Ad Vigilias: lectio et ¶ in supplemento 128 ; in II nocturno lectio brevis et ß ut ad Sextam.\n\\item Ad Benedictus : ø \\textit{Beata es} (AM 1074).\n\\item \\textit{In ML: olim die 22 augusti (non dicitur \\emph{Credo}).}\n\\item In MC: MR 761 ; lectiones propriæ: Is \\textbf{61}, 9-11 / Lc \\textbf{2}, 41-51 ; præfatio de Immaculato Corde Beatæ Mariæ Virginis (CM 28)."
    
    # Christ-Roi:
    noel_next = datetime.date(current_year, 12, 25)
    noel_next_weekday = noel_next.weekday()
    christ_roi_date = noel_next - datetime.timedelta(days = noel_next_weekday + 29)
    dict_tempo["fetes_mobiles"]["christ_roi"] = str(christ_roi_date.day) + f_transf_month_genitive(christ_roi_date.month)

    # Dimanches per annum entre le Baptême et le Carême:
    nb_dim_per_annum_ap_bapteme = ((cendres_date + datetime.timedelta(days = 4) - bapteme_date).days // 7)
    for i in range(nb_dim_per_annum_ap_bapteme):
        new_dim_date = bapteme_date + datetime.timedelta(days = i * 7)
        if i != 0:
            # Numéro du Dimanche per annum:
            num_dim_per_annum = f_roman_numbers(i + 1)
            # Numéro du Dimanche après l'Épiphanie ou bien Septuagésime, Sexagésime etc. et commentaires :
            comment_septua = "\\item In Officio: omnia dicuntur sicut in psalterio, præter antiphonas ad Benedictus et Magnificat." + ("\n\\item {\\itshape In ML (Viol.): non dicitur \\emph{Gloria} in Missis de tempore ab hac Dominica usque ad feriam IV Hebdomadæ Sanctæ inclusive.}" if new_dim_date == cendres_date - datetime.timedelta(days = 17) else "\n\\item {\\itshape In ML: Viol.}") 
            if (new_dim_date == cendres_date - datetime.timedelta(days = 17)):
                forme_extra = "Septuagesima"
                forme_extra_I_vesp = ". Omnia ut in psalterio, præter ad Magnificat: ø \\textit{Dixit Dominus} (AM 311); dicitur \\textit{Benedicamus Domino} sine \\textit{Alleluia, Alleluia}"
            elif (new_dim_date == cendres_date - datetime.timedelta(days = 10)):
                forme_extra = "Sexagesima"
                forme_extra_I_vesp = " ut in psalterio, præter antiphonam ad Magnificat"
            elif (new_dim_date == cendres_date - datetime.timedelta(days = 3)):
                forme_extra = "Quinquagesima"
                forme_extra_I_vesp = " ut in psalterio, præter antiphonam ad Magnificat"
            else:
                forme_extra = f_roman_numbers(i + 1) + " post Epiphaniam"
                forme_extra_I_vesp = ""
                comment_septua = ""
            # Numéros des préfaces:
            num_pref_dim, num_pref_fer = f_num_prefaces(i)

            # Création du Dimanche per annum :
            new_dim = dict_tempo[new_dim_date] = {}
            new_dim["force"] = 80
            new_dim["I_vesp"] = "\n\\item I Vesperæ " + ("festi" if new_dim_date.day == 2 and new_dim_date.month == 2 else "dominicæ") + " sequentis" + forme_extra_I_vesp + "."
            new_dim["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((new_dim_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
            new_dim["num_day"] = "\\textbf{" + str(new_dim_date.day) + "} &"
            new_dim["header"] = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + " per annum}} (" + forme_extra + ")" + " - de ea - \\textit{Vir.}"
            new_dim["symbols"] = "".join(f_symbols(new_dim_date))
            new_dim["body"] = comment_septua + "\n\\item In MC: præfatio " + num_pref_dim + " de dominicis." + ("\n\\item Ad benedictionem Sanctissimi Sacramenti, post canticum expositionis, cantatur \\textit{Ubi Caritas} in Besnier 275 (hebdomada pro christianorum unitate)." if new_dim_date.day < 25 and new_dim_date.day >= 18 and new_dim_date.month == 1 else "")
            new_dim["II_vesp"] = "}\n\\ApplyGenerSubTitle{In Officio}\n\\ApplyGenerList{\n\\item In feriis usque ad tempus quadragesimæ : antiphona ad Benedictus ut in psalterio; ad Magnificat vero antiphona propria (AM 316 et sequentibus).}\n\\ApplyGenerSubTitle{In ML}\n\\ApplyGenerList{\n\\item Post graduale dicitur tractus, præterquam in feriis quando resumitur Missa dominicæ.\n\\item In feriis Septuagesimæ, quando sacerdos celebrat paramentis violaceis, dicere debet vel Missam dominicæ præcedentis vel Missam votivam ex eis quæ celebrantur colore violaceo." if new_dim_date == cendres_date - datetime.timedelta(days = 17) else ""
            new_dim["preface_feries"] = "\n\\item In feriis: præfatio communis " + num_pref_fer + ", nisi aliter notetur."
            current_lectiones = lectiones["hebdo_" + str(i + 1) + "_per_annum"]
            new_dim["lectiones_header"] = current_lectiones["header"]
            lectiones_body = "\n\\item[Dom. " + year_letter + "] " + current_lectiones["dim"][year_letter]

        else:
            current_lectiones = lectiones["hebdo_1_per_annum"]
            lectiones_body = "\n\\ApplyLectHeader{" + current_lectiones["header"] + "}"
            lectiones_body += "\n\\ApplyLectBody{"
            for j in range(6):
                lectiones_body += "\n\\item[" + f_transf_weekday(j) + "] " + current_lectiones[j][even_year_num] + " / " + current_lectiones[j][2]
            lectiones_body += "}"

        # Féries qui suivent ce Dimanche per annum :
        for j in range(6 if i != (nb_dim_per_annum_ap_bapteme - 1) else 2): # Lectures après la Quinquagésime : seulement lundi et mardi.
            lectiones_body += "\n\\item[" + f_transf_weekday(j) + "] " + current_lectiones[j][even_year_num] + " / " + current_lectiones[j][2] if i != 0 else ""
            new_day_date = new_dim_date + datetime.timedelta(days = j + 1)
            if new_day_date < cendres_date:
                new_day = dict_tempo[new_day_date] = {}
                new_day["force"] = 10
                new_day["generalities"] = ("\n\\newpage\n\\ApplyParBox{1cm}{\\ApplyGenerTitleHuge{Tempus Per annum}}\n\\ApplyGenerSubTitle{In Officio}\n\\ApplyGenerList{\n\\item In feriis : hebdomada I per annum vel I post Epiphaniam.}\n\\ApplyGenerSubTitle{Ad mensam}\n\\ApplyGenerList{\n\\item Benedictio de tempore per annum.}" + lectiones_body + "\n\\ApplyGenerList{\n\\item Præfatio communis I, nisi aliter notetur.}\n\\medskip") if i == 0 and j == 0 else ""
                new_day["num_day"] = "\\textbf{" + str(new_day_date.day) + "} & " +  f_transf_weekday(new_day_date.weekday())
                new_day["symbols"] = "".join(f_symbols(new_day_date))
                new_day["header"] = " - de ea - \\textit{Vir.}"
                new_day["body"] = "\n\\item \\textit{In ML: Viol.}" if new_day_date > cendres_date - datetime.timedelta(days = 17) else ""
                if new_day_date.day < 8 and new_day_date.weekday() == 4: # 1er vendredi du mois.
                    new_day["body"] = "\n\\item \\textit{In ML (Alb.) : Missa de sacratissimo Corde Iesu \\emph{(Gloria)}.}\n\\item MC1V" # La balise MC1V sera remplacée tout à la fin (voir ordo_write.py) par l'une des 2 MC possibles.
                if new_day_date.weekday() == 5: # Samedis BMV.
                    new_day["force"] = 30 # Entre mémoire mineure et majeure.
                    new_day["header"] = "  - \\textsc{De Beata} - \\textit{\\textbf{memoria maior}} - \\textit{Alb.}"
                    new_day["body"] = f_mc_bmv(new_day_date, paques_date)
        if i != 0: new_dim["lectiones_body"] = lectiones_body

    # Dimanches per annum entre la Pentecôte et le Christ-Roi :
    # Leur nombre :
    nb_dim_ap_pentec = (christ_roi_date - pentecote_date).days // 7 + 1
    # Numéro de la semaine de départ du Temps per annum (= Numéro du dimanche de la Pentecôte si la Pentecôte était un dimanche Per annum) :
    start_week = f_roman_numbers(35 - nb_dim_ap_pentec)
    for i in range(nb_dim_ap_pentec):
        new_dim_date = pentecote_date + datetime.timedelta(days = i * 7)
        num_summer = ""
        if i != 0:
            if i == 1: # Trinité.
                dict_tempo["fetes_mobiles"]["trinite"] = str(new_dim_date.day) + f_transf_month_genitive(new_dim_date.month)
                # Numéro du Dimanche per annum:
                num_dim_per_annum = f_roman_numbers(36 - nb_dim_ap_pentec)
                # Numéros de la préface commune pour les féries:
                num_pref_fer = f_roman_numbers((36 - nb_dim_ap_pentec) % 6) if ((i + 1) % 6 != 0) else "VI"
                # Création du Dimanche de la Trinité:
                trinite = dict_tempo[new_dim_date] = {}
                trinite["force"] = 120
                trinite["I_vesp"] = "\n\\item I Vesperæ solemnitatis sequentis}\n\\ApplyHebdoPsalt{\\textbf{- Pro breviario 1962: tomus alter -}"
                trinite["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((new_dim_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
                trinite["num_day"] = "\\textbf{" + str(new_dim_date.day) + "} &"
                trinite["symbols"] = "".join(f_symbols(new_dim_date)) + (" " if f_symbols(new_dim_date) != "" else "")
                trinite["header"] = "\\textbf{\\textsc{Dominica " + num_dim_per_annum + " per annum}" + " - \\MakeUppercase{Sanctissimæ Trinitatis}} (I post Pentecosten) " + " - \\textbf{sollemnitas minor} - \\textit{Alb}."
                trinite["body"] = "\n\\item In MC: MR 485 ; præfatio propria."
                trinite["preface_feries"] = "\n\\item In feriis: præfatio communis " + num_pref_fer + " , nisi aliter notetur."
                trinite_lectiones = {"A": "Ex \\textbf{34}, 4b-6.8-9 / 2 Co \\textbf{13}, 11-13 / Io \\textbf{3}, 16-18", "B": "Deut \\textbf{4}, 32-34.39-40 / Rom \\textbf{8}, 14-17 / Mt \\textbf{28}, 16-20", "C": "Prov \\textbf{8}, 22-31 / Rom \\textbf{5}, 1-5 / Io \\textbf{16}, 12-15"}
                current_lectiones = lectiones["hebdo_" + str(36 - nb_dim_ap_pentec) + "_per_annum"]
                lectiones_body = "\n\\ApplyLectHeader{" + current_lectiones["header"] + "}"
                lectiones_body += "\n\\ApplyLectBody{"
                for j in range(6):
                    lectiones_body += "\n\\item[" + f_transf_weekday(j) + "] " + current_lectiones[j][even_year_num] + " / " + current_lectiones[j][2]
                trinite["II_vesp"] = "\n\\item Vesperæ sollemnitatis ; benedictio Sanctissimi Sacramenti.}\n\\ApplyLectHeader{Dominica Sanctissimæ Trinitatis: lectiones}\n\\ApplyLectBody{\n\\item[Anno " + year_letter + "] " + trinite_lectiones[year_letter] + "\n\\smallskip}" + lectiones_body

            elif i == nb_dim_ap_pentec - 1: # Christ-Roi.
                christ_roi = dict_tempo[christ_roi_date] = {}
                christ_roi["force"] = 120
                christ_roi["I_vesp"] = "\n\\item I Vesperæ sollemnitatis sequentis. Officium invenitur in breviario circa finem mensis octobris et in AM 1088."
                christ_roi["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((new_dim_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
                christ_roi["num_day"] = "\\textbf{" + str(christ_roi_date.day) + "} &"
                num_summer = f_num_summer(christ_roi_date)[0] if f_num_summer(christ_roi_date)[0] == "III" else ("V" if even_year else "IV")
                christ_roi["header"] = "\\textbf{\\textsc{Dominica XXXIV per annum} - \\MakeUppercase{Domini nostri Iesu Christi Universorum Regis}} (XXIV post Pentecosten - " + num_summer + " novembris) - \\textbf{sollemnitas minor} - \\textit{Alb}."
                christ_roi["body"] = "\n\\item Ad Vigilias : in nocturno II : lectiones 5 et 6 cum ¶ lectionis 8 ; in nocturno III : lectiones 11 et 12.\n\\item In MC : præfatio propria."
                num_pref_dim, num_pref_fer = f_num_prefaces(33)
                christ_roi["preface_feries"] = "\n\\item In feriis: præfatio communis " + num_pref_fer + ", nisi aliter notetur."
                current_lectiones = lectiones["hebdo_34_per_annum"]
                lectiones_feries = "\n\\ApplyLectHeader{" + current_lectiones["header_feries"] + "}"
                lectiones_feries += "\n\\ApplyLectBody{"
                for j in range(6):
                    lectiones_feries += "\n\\item[" + f_transf_weekday(j) + "] " + current_lectiones[j][even_year_num] + " / " + current_lectiones[j][2]
                lectiones_feries += "}"
                christ_roi["II_vesp"] = "\n\\item Vesperæ sollemnitatis ; ad benedictionem Sanctissimi Sacramenti recitetur \\textit{Actus dedicationis humani generis Iesu Christo Regi} : indulgentia plenaria.\n\\ApplyLectHeader{" + current_lectiones["header_dim"] + "}\n\\ApplyLectBody{\\item[Anno " + year_letter + "] " + current_lectiones["dim"][year_letter] + "}\n\\smallskip" + lectiones_feries

            else:
                # Numéro du Dimanche per annum:
                num_dim_per_annum = f_roman_numbers(i + 35 - nb_dim_ap_pentec)
                # Numéro du dimanche après la Pentecôte:
                num_dim_ap_pentec = f_roman_numbers(i) + " post Pentecosten" if i < 24 else f_roman_numbers(i - nb_dim_ap_pentec + 8) + " post Epiphaniam"
                if i == 2:
                    num_dim_ap_pentec = "II post Pentecosten vel infra octavam Ss. Corporis Christi" if i < 24 else f_roman_numbers(i - nb_dim_ap_pentec + 8) + " post Epiphaniam"
                elif i == 3:
                    num_dim_ap_pentec = "III post Pentecosten vel infra octavam Ss. Cordis Iesu" if i < 24 else f_roman_numbers(i - nb_dim_ap_pentec + 8) + " post Epiphaniam"
                # Numéro du dimanche d'été (août à novembre):
                num_summer = " - " + f_num_summer(new_dim_date)[0] + f_num_summer(new_dim_date)[1] if (new_dim_date.month >= 8) and (new_dim_date.month <= 11) else ""
                # Numéros des préfaces:
                num_pref_dim, num_pref_fer = f_num_prefaces(i + 34 - nb_dim_ap_pentec)

                # Création du Dimanche per annum (sous la forme "Dim. X per annum (Y post Pentecosten, Z Augusti)"):
                new_dim = dict_tempo[new_dim_date] = {}
                new_dim["force"] = 80
                #new_dim["generalities"] = "\n\\medskip\n\\ApplyGenerList{\\item Ad Vigilias: lectiones nocturnorum I et II sumuntur in supplemento 52*. Et sic in feriis hebdomadæ II novembris.}\n\\medskip" if num_summer == " - II novembris" else ("\n\\medskip\n\\ApplyGenerList{\\item Ad Vigilias: in feriis, lectiones SO.}\n\\medskip" if num_summer == " - I novembris" else "")
                new_dim["I_vesp"] = "\n\\item I Vesperæ dominicæ sequentis" + (" (hymnus tono hiemali)" if num_summer == " - I octobris" else "") + "." + ("}\n\\medskip\n\\ApplyPrefaceFeries{\n\\item A dominica I octobris usque ad Adventum: dicitur hymnus hiemalis ad Vigilias, Laudes et Vesperas." if num_summer == " - I octobris" else "")
                new_dim["hebdo_psalt"] = "- Hebdomada " + hebdo_psalterii[((new_dim_date - datetime.date(2011, 11, 27)).days // 7) % 2] + " psalterii -"
                new_dim["num_day"] = "\\textbf{" + str(new_dim_date.day) + "} &"
                new_dim["header"] = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + " per annum}} (" + num_dim_ap_pentec + num_summer + ")" + " - de ea - \\textit{Vir.}"
                new_dim["symbols"] = "".join(f_symbols(new_dim_date))
                if i == 2: body_special = "\n\\item Officium totum dicitur ut in dominicis per annum, præter antiphonas ad Benedictus et Magnificat in AM 557-558."
                elif i == 3: body_special = "\n\\item Officium totum dicitur ut in dominicis per annum præter antiphonas ad Benedictus et Magnificat."
                elif num_summer == " - I augusti": body_special = "\n\\item Ad Vigilias: lectiones nocturnorum I et II sumendæ sunt e dominica I augusti, lectiones nocturni III e dominica post Pentecosten, et sic usque ad Adventum." 
                elif num_summer == " - V octobris": body_special = "\n\\item Ad Vigilias: lectiones nocturnorum I et II in supplemento 51*." if even_year else "\n\\item Ad Vigilias: lectiones nocturni I in supplemento 51*."
                elif num_summer == " - II novembris": body_special = "\n\\item Ad Vigilias: lectiones nocturnorum I et II sumuntur in supplemento 52*. Et sic in feriis hebdomadæ II novembris." if even_year else "\n\\item Ad Vigilias: lectiones nocturni I sumuntur in supplemento 52*. Et sic in feriis hebdomadæ II novembris."
                else: body_special = ""
                new_dim["body"] = body_special + "\n\\item In MC: præfatio " + num_pref_dim + " de dominicis."
                new_dim["preface_feries"] = "\n\\item In feriis: præfatio communis " + num_pref_fer + ", nisi aliter notetur."
                if num_summer == " - I novembris": new_dim["preface_feries"] += "\n\\item Ad Vigilias: in feriis, lectiones SO." 
                current_lectiones = lectiones["hebdo_" + str(i + 35 - nb_dim_ap_pentec) + "_per_annum"]
                new_dim["lectiones_header"] = current_lectiones["header"]
                lectiones_body = ("\n\\item[Dom. " + year_letter + "] " + current_lectiones["dim"][year_letter]) if new_dim_date != datetime.date(current_year, 6, 24) and new_dim_date != datetime.date(current_year, 6, 29) and new_dim_date != datetime.date(current_year, 7, 11) and new_dim_date != datetime.date(current_year, 8, 6) and new_dim_date != datetime.date(current_year, 8, 15) and new_dim_date != datetime.date(current_year, 9, 7) and new_dim_date != datetime.date(current_year, 9, 14) and new_dim_date != datetime.date(current_year, 11, 1) and new_dim_date != datetime.date(current_year, 11, 2) and new_dim_date != datetime.date(current_year, 11, 9) else "" # Ne pas mentionner les lectures du dimanche si ce dimanche est une solennité ou une fête du Seigneur (lectures propres).
        
        else: # Si i == 0 : lectiones semaine Pentecôte.
            current_lectiones = lectiones["hebdo_" + str(35 - nb_dim_ap_pentec) + "_per_annum"]
            lectiones_body = "\n\\ApplyLectHeader{" + current_lectiones["header"] + "}"
            lectiones_body += "\n\\ApplyLectBody{"
            for j in range(6):
                lectiones_body += "\n\\item[" + f_transf_weekday(j) + "] " + current_lectiones[j][even_year_num] + " / " + current_lectiones[j][2]
            lectiones_body += "}"
            
        # Féries qui suivent ce Dimanche per annum:
        for j in range(6):
            if i != 0:
                if num_dim_per_annum == "XVIII" and j in [0, 1]:
                    year_letter_a_or_bc = "A" if year_letter == "A" else "BC"
                    lectiones_body += "\n\\item[" + f_transf_weekday(j) + "] " + current_lectiones[j][year_letter_a_or_bc][even_year_num] + " / " + current_lectiones[j][year_letter_a_or_bc][2]
                else:
                    lectiones_body += "\n\\item[" + f_transf_weekday(j) + "] " + current_lectiones[j][even_year_num] + " / " + current_lectiones[j][2]
            else:
                lectiones_body += ""
            new_day_date = new_dim_date + datetime.timedelta(days = j + 1)
            if new_day_date != fete_dieu_date and new_day_date != sacre_coeur_date and new_day_date != coeur_imm_marie_date:
                new_day = dict_tempo[new_day_date] = {}
                new_day["force"] = 10
                if i == nb_dim_ap_pentec - 1 and j == 0 and even_year and f_num_summer(christ_roi_date)[0] != "III": new_day["generalities"] = "\n\\medskip\n\\ApplyGenerList{\\item Ad Vigilias: in feriis sumuntur lectiones hebdomadæ V novembris.}\n\\medskip" # Après le Christ-Roi, si IVe sem. de Novembre et années paires : lectures de la Ve sem. de novembre.
                new_day["num_day"] = "\\textbf{" + str(new_day_date.day) + "} & " +  f_transf_weekday(new_day_date.weekday())
                new_day["symbols"] = "".join(f_symbols(new_day_date))
                new_day["header"] = " - de ea - \\textit{Vir.}"
                if i == 0: # Octave de Pentecôte :
                    if j == 0: # Lundi de Pentecôte :
                        new_day["force"] = 50
                        new_day["header"] = " - \\textsc{Beatæ Mariæ Virginis, Ecclesiæ Matris} - \\textbf{memoria maior} - \\textit{Alb.}" 
                        new_day["generalities"] = "\n\\ApplyParBox{1cm}{\\begin{center}\\large{\\textit{Post Completorium extinguitur cereus paschalis}}\\par\\large{\\textit{et explicit tempus paschale.}}\\end{center}}\n\\newpage\n\\ApplyParBox{1cm}{\\ApplyGenerTitleHuge{Tempus per annum}\n\\medskip\n\\ApplyGenerTitleLarge{ab hebdomada " + start_week + "}}\n\\ApplyGenerList{\n\\item Dicitur \\textit{Angelus Domini}.\n\\item Ad Completorium : ø \\textit{Salve Regina}.}\n\\ApplyGenerSubTitle{Ad mensam}\n\\ApplyGenerList{\n\\item Benedictio de tempore per annum.}" + lectiones_body + "\n\\ApplyGenerList{\n\\item In officio feriali : oratio et antiphonæ de octava, nisi aliter notetur.\n\\item In feriis : præfatio communis " + f_num_prefaces(34 - nb_dim_ap_pentec)[1] + ", nisi aliter notetur.\\vspace{0.5cm}}"
                        new_day["body"] = "\n\\item De communi beatæ Mariæ Virginis, præter sequentia.\n\\item Oratio propria in supplemento 52* vel in AM 527*.\n\\item Ad Vigilias : lectio in supplemento 49*.\n\\item Ad Laudes : hymnus proprius (AM 525*); ad Benedictus: ø \\textit{Perseverabant unanimiter} (AM 526*).\n\\item \\textit{In ML (Rub.): Missa infra octavam (Credo).}\n\\item In MC : Missa de Beata Maria Ecclesiæ Matre (MR 1172); lectiones propriæ: Act \\textbf{1}, 12-14 / Io \\textbf{19}, 25-34; præfatio I de Beata Maria Virgine."
                        new_day["II_vesp"] = "\n\\item Ad Magnificat: ø \\textit{Dixit Dominus} (AM 527*)."
                    elif j != 5: # Autres féries de l'octave de Pentecôte, sauf samedi :
                        # new_day["force"] = 30 # Entre mémoire mineure et majeure.
                        new_day["force"] = 10
                        new_day["body"] = octave_pentec[j]["body"]
                # Quatre-temps de septembre:
                if num_summer == " - III septembris" and new_day_date.weekday() in [2, 4, 5]:
                    new_day["body"] = "\n\\item \\textit{In ML (Viol.): Quatuor Temporum Septembris (forma Missæ brevior).}"
                # 1er vendredi du mois (hors octave Pentecôte):
                if new_day_date.day < 8 and new_day_date.weekday() == 4 and not (new_day_date > paques_date + datetime.timedelta(days=49) and new_day_date < paques_date + datetime.timedelta(days=56)):
                    new_day["body"] = "\n\\item \\textit{In ML (Alb.) : Missa de sacratissimo Corde Iesu \\emph{(Gloria)}.}" + "\n\\item MC1V" # Les balises MC1V ("Messe conventuelle 1er vendredi") seront remplacées ultérieurement alternativement par l'une des 2 MC possibles (voir ordo_write.py).
                # Samedis BMV:
                if new_day_date.weekday() == 5:
                    new_day["force"] = 30 
                    new_day["header"] = "  - \\textsc{De Beata} - \\textit{\\textbf{memoria maior}} - \\textit{Alb.}"
                    if (i == 0 and new_day_date == new_dim_date + datetime.timedelta(days = 6) and new_day_date.month == 6 and new_day_date.day > 14 and new_day_date.day < 22):
                        new_day["body"] = "\n\\item Ad Vigilias : lectio sabbato 3 (in supplemento 202).\n\\item In MC : Beatæ Mariæ Virginis, Matris et mediatricis gratiæ (CM 30) ; præfatio I de Beata Maria Virgine."
                    elif i == nb_dim_ap_pentec - 1:
                        new_day["body"] = mc_bmv[12][1] if new_day_date.month == 12 else mc_bmv[11][5]
                    else: new_day["body"] = f_mc_bmv(new_day_date, paques_date)
        if (i != 0) and (i != 1) and (i != nb_dim_ap_pentec - 1): new_dim["lectiones_body"] = lectiones_body

    # Nombre de jours de l'ordo de cette année:
    nb_days = (christ_roi_date - sabb_1_adv_date - datetime.timedelta(days = 1)).days + 8

    return(dict_tempo, sabb_1_adv_date, nb_days, paques_date, nb_dim_ap_pentec, christ_roi_date)
