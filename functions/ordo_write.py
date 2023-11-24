# coding: utf-8

import os
import datetime
import re
from functions.various import hebdo_psalterii_inv, ult_ant_dict, special_months, f_transf_month, first_vendr_mc


def ordo_write(dict_tempo, dict_sancto, current_year, even_year, year_letter, ordo_start, nb_days, paques, christ_roi):
    # Entrer ici les dates des MC votives semailles et récoltes :
    date_semailles = datetime.date(current_year, 5, 6)
    date_recoltes = datetime.date(current_year, 9, 18)

    text_ordo = "\\input{config.tex}"
    text_ordo += "\n\\fancyhead[CO]{\\textbf{Cyclus liturgicus " + \
        year_letter + ("/II" if even_year else "/I") + "}}"
    text_ordo += "\n\\newcommand{\\CurrentYear}{" + str(current_year - 1) + "}"
    text_ordo += "\n\n\\begin{document}"
    text_ordo += "\n\n\\thispagestyle{empty}"
    text_ordo += "\n\n\\begin{center}"
    text_ordo += "\n\\par\\parbox{7.5cm}{\\vspace{1cm}}\\par"
    text_ordo += "\n\\makebox[7.5cm][s]{\\fontsize{68}{0}\\selectfont\\FontFlyLeaf{\\MakeUppercase{O R D O}}\\par}"
    text_ordo += "\n\\vspace{1cm}\\par"
    text_ordo += "\n\\makebox[7.5cm][s]{\\fontsize{24}{0}\\selectfont\\FontFlyLeaf{\\MakeUppercase{missæ celebrandæ}}\\par}"
    text_ordo += "\n\\vspace{0.4cm}\\par"
    text_ordo += "\n\\makebox[7.5cm][s]{\\fontsize{24}{0}\\selectfont\\FontFlyLeaf{\\MakeUppercase{et divini officii}}\\par}"
    text_ordo += "\n\\vspace{0.4cm}\\par"
    text_ordo += "\n\\makebox[7.5cm][s]{\\fontsize{24}{0}\\selectfont\\FontFlyLeaf{\\MakeUppercase{p e r s o l v e n d i}}\\par}"
    text_ordo += "\n\\vspace{1cm}\\par"
    text_ordo += "\n\\makebox[7.5cm][s]{\\fontsize{17}{0}\\selectfont\\FontFlyLeaf{\\MakeUppercase{iuxta ritum romano-}}\\par}"
    text_ordo += "\n\\vspace{0.4cm}\\par"
    text_ordo += "\n\\makebox[7.5cm][s]{\\fontsize{17}{0}\\selectfont\\FontFlyLeaf{\\MakeUppercase{monasticum in abbatia}}\\par}"
    text_ordo += "\n\\vspace{0.4cm}\\par"
    text_ordo += "\n\\makebox[7.5cm][s]{\\fontsize{17}{0}\\selectfont\\FontFlyLeaf{\\MakeUppercase{sancti ioseph claræ vallis}}\\par}"
    text_ordo += "\n\\vspace{1cm}\\par"
    text_ordo += "\n\\makebox[6cm][s]{\\fontsize{28}{0}\\selectfont\\FontFlyLeaf{\\MakeUppercase{\\so{pro anno}}}\\par}"
    text_ordo += "\n\\vspace{0.4cm}\\par"
    text_ordo += "\n\\makebox[6cm][s]{\\fontsize{28}{0}\\selectfont\\FontFlyLeaf{\\MakeUppercase{l i t u r g i c o}}\\par}"
    text_ordo += "\n\\vspace{0.4cm}\\par"
    text_ordo += "\n\\makebox[6cm][s]{\\fontsize{28}{0}\\selectfont\\FontFlyLeaf{\\MakeUppercase{d o m i n i}}\\par}"
    text_ordo += "\n\\vspace{0.4cm}\\par"
    text_ordo += "\n\\makebox[6cm][c]{\\fontsize{28}{0}\\selectfont\\FontFlyLeaf{\\MakeUppercase{" + str(
        current_year - 1) + "-" + str(current_year) + "}}}"
    text_ordo += "\n\n\\end{center}"
    text_ordo += "\n\\newpage"
    text_ordo += "\n\\thispagestyle{empty}\\null\n"
    text_ordo += "\n\\newpage"
    text_ordo += "\n\\thispagestyle{empty}"
    text_ordo += "\n\\ApplyParBox{0.5cm}{\\ApplyGenerTitleHuge{Anno liturgico " + str(
        current_year - 1) + "-" + str(current_year) + "}\n\\smallskip\n\\ApplyGenerTitleLarge{Celebrationes mobiles}}"
    text_ordo += "\n\\medskip\n\\fontsize{12}{12}\\selectfont\n\\setlength{\\parskip}{0.1cm}"
    text_ordo += "\nDominica I Adventus \\dotfill d. " + \
        dict_tempo["fetes_mobiles"]["dim_1_adv"] + "\\par"
    text_ordo += "\nSanctæ Familiæ \\dotfill d. " + \
        dict_tempo["fetes_mobiles"]["ste_famille"] + "\\par"
    text_ordo += "\nBaptisma Domini \\dotfill d. " + \
        dict_tempo["fetes_mobiles"]["bapteme"] + "\\par"
    text_ordo += "\nFeria IV Cinerum \\dotfill d. " + \
        dict_tempo["fetes_mobiles"]["cendres"] + "\\par"
    text_ordo += "\nDominica in Palmis \\dotfill d. " + \
        dict_tempo["fetes_mobiles"]["rameaux"] + "\\par"
    text_ordo += "\nDominica Paschæ \\dotfill d. " + \
        dict_tempo["fetes_mobiles"]["paques"] + "\\par"
    text_ordo += "\nAscensio Domini \\dotfill d. " + \
        dict_tempo["fetes_mobiles"]["ascension"] + "\\par"
    text_ordo += "\nDominica Pentecostes \\dotfill d. " + \
        dict_tempo["fetes_mobiles"]["pentecote"] + "\\par"
    text_ordo += "\nSs.mæ Trinitatis \\dotfill d. " + \
        dict_tempo["fetes_mobiles"]["trinite"] + "\\par"
    text_ordo += "\nSs.mi Corporis et Sanguinis Domini \\dotfill d. " + \
        dict_tempo["fetes_mobiles"]["fete_dieu"] + "\\par"
    text_ordo += "\nSs.mi Cordis Iesu \\dotfill d. " + \
        dict_tempo["fetes_mobiles"]["sacre_coeur"] + "\\par"
    text_ordo += "\nD.N.I.C. universorum Regis \\dotfill d. " + \
        dict_tempo["fetes_mobiles"]["christ_roi"] + "\\par"
    text_ordo += "\n\\vspace{1cm}\n\\ApplyGenerTitleLarge{Cyclus liturgicus}"
    text_ordo += "\n\\ApplyGenerSubTitle{\\textnormal{Dominicalis et festivus: }" + year_letter + "}"
    text_ordo += "\n\\ApplyGenerSubTitle{\\textnormal{Ferialis: }" + (
        "II" if even_year else "I") + "}"
    text_ordo += "\n\\newpage"
    text_ordo += "\n\\thispagestyle{empty}"
    text_ordo += "\n\\ApplyParBox{0cm}{\\ApplyGenerTitleLarge{Clavis signorum}\n \\ApplyGenerTitleLarge{et abbreviationum}}"
    text_ordo += "\n\\setlength{\\tabcolsep}{0cm}"
    text_ordo += "\n\\begin{tabular}{p{1cm} p{7.5cm}}"
    text_ordo += "\n¬ & \\small{Festum de præcepto.}\\\\"
    text_ordo += "\nþ & \\small{Festum cum tempore usque ad Nonam de præcepto, postmeridiem vero laborandum est.}\\\\"
    text_ordo += "\nµ & \\small{Ieiunium regulare cum abstinentia carnium.}\\\\"
    text_ordo += "\nł & \\small{Abstinentia carnium servanda secundum normas Declarationum nostrarum.}\\\\"
    text_ordo += "\nŧ & \\small{Prima dominica in mense: ad Completorium, dicitur antiphona Beatæ Mariæ Virginis in honorem Dominæ Nostræ Ephesini ad intentiones diocesis Smyrnensis (Izmir).}\\\\"
    text_ordo += "\n£ & \\small{Prima feria VI in mense : fit expositio Sanctissimi Sacramenti, in honorem Sacratissimi Cordis Iesu, a Vigiliis usque ad Completorium.}\\\\"
    text_ordo += "\n§ & \\small{Primum sabbatum in mense.}\\\\"
    text_ordo += "\n & \\\\"
    text_ordo += "\n\\small{AM} & \\small{Antiphonale monasticum.}\\\\"
    text_ordo += "\n\\small{CM} & \\small{Collectio Missarum de Beata Maria Virgine 1987 (numerus designat ordinem missarum).}\\\\"
    text_ordo += "\n\\small{GR} & \\small{Graduale romanum.}\\\\"
    text_ordo += "\n\\small{LS} & \\small{Lectionnaire de semaine.}\\\\"
    text_ordo += "\n\\small{MC} & \\small{Missa conventualis.}\\\\"
    text_ordo += "\n\\small{ML} & \\small{Missæ lectæ 1962.}\\\\"
    text_ordo += "\n\\small{MP} & \\small{Missæ Propriæ OSB 1976.}\\\\"
    text_ordo += "\n\\small{MR} & \\small{Missale romanum 2002.}\\\\"
    text_ordo += "\n\\small{Or.} & \\small{Oratio universalis.}\\\\"
    text_ordo += "\n\\small{SO} & \\small{Lectiones de Scriptura occurenti in I nocturno.}\\\\"
    text_ordo += "\n\\end{tabular}\n"
    text_ordo += "\n\\newpage"
    text_ordo += "\n\\thispagestyle{empty}"
    text_ordo += "\n\\setlength{\\parskip}{0cm}"
    text_ordo += "\n\n\\ApplyParBox{0cm}{\\ApplyGenerTitleLarge{Abbreviationes librorum}\n\\ApplyGenerTitleLarge{Sacræ Scripturæ}}"
    text_ordo += "\n\\setlength{\\tabcolsep}{0cm}"
    text_ordo += "\n\\renewcommand{\\arraystretch}{0.8}"
    text_ordo += "\n\\begin{longtable}{>{\\small\\bf}p{1.5cm}<{} >{\\small}p{7cm}<{}}"
    text_ordo += "\nAbd & Liber Abdiæ prophetæ\\\\"
    text_ordo += "\nAct & Actus Apostolorum\\\\"
    text_ordo += "\nAg & Liber Aggæi prophetæ\\\\"
    text_ordo += "\nAm & Liber Amos prophetæ\\\\"
    text_ordo += "\nAp & Apocalypsis beati Ioannis apostoli\\\\"
    text_ordo += "\nBar & Liber Baruch prophetæ\\\\"
    text_ordo += "\nCant & Canticum canticorum\\\\"
    text_ordo += "\n1 et 2 Chr & Libri I et II Chronicorum ( = I et II Paralipomenon)\\\\"
    text_ordo += "\nCol & Epistola beati Pauli apostoli ad Colossenses\\\\"
    text_ordo += "\n1 et 2 Cor & Epistolæ I et II beati Pauli apostoli ad Corinthios\\\\"
    text_ordo += "\nDan & Liber Danielis prophetæ\\\\"
    text_ordo += "\nDeut & Liber Deuteronomii\\\\"
    text_ordo += "\nEph & Epistola beati Pauli apostoli ad Ephesios\\\\"
    text_ordo += "\nEsd & Liber Esdræ ( = I Esdræ)\\\\"
    text_ordo += "\nEst & Liber Esther\\\\"
    text_ordo += "\nEx & Liber Exodus\\\\"
    text_ordo += "\nEz & Liber Ezechielis prophetæ\\\\"
    text_ordo += "\nGal & Epistola beati Pauli apostoli ad Galatas\\\\"
    text_ordo += "\nGen & Liber Genesis\\\\"
    text_ordo += "\nHab & Liber Habacuc prophetæ\\\\"
    text_ordo += "\nHebr & Epistola ad Hebræos\\\\"
    text_ordo += "\nIac & Epistola beati Iacobi apostoli\\\\"
    text_ordo += "\nIer & Liber Ieremiæ prophetæ\\\\"
    text_ordo += "\nIo & Evangelium secundum Ioannem\\\\"
    text_ordo += "\n1, 2 et 3 Io & Epistolæ I, II et III beati Ioannis apostoli\\\\"
    text_ordo += "\nIob & Liber Iob\\\\"
    text_ordo += "\nIoel & Liber Ioelis prophetæ\\\\"
    text_ordo += "\nIon & Liber Ionæ prophetæ\\\\"
    text_ordo += "\nIos & Liber Iosue\\\\"
    text_ordo += "\nIs & Liber Isaiæ prophetæ\\\\"
    text_ordo += "\nIud & Epistola beati Iudæ apostoli\\\\"
    text_ordo += "\nIudic & Liber Iudicum\\\\"
    text_ordo += "\nIudt & Liber Iudith\\\\"
    text_ordo += "\nLam & Lamentationes ( = Threni)\\\\"
    text_ordo += "\nLc & Evangelium secundum Lucam\\\\"
    text_ordo += "\nLev & Liber Leviticus\\\\"
    text_ordo += "\n1 et 2 Mac & Libri I et II Machabæorum\\\\"
    text_ordo += "\nMal & Liber Malachiæ prophetæ\\\\"
    text_ordo += "\nMc & Evangelium secundum Marcum\\\\"
    text_ordo += "\nMic & Liber Michææ prophetæ\\\\"
    text_ordo += "\nMt & Evangelium secundum Matthæum\\\\"
    text_ordo += "\nNah & Liber Nahum prophetæ\\\\"
    text_ordo += "\nNeh & Liber Nehemiæ ( = II Esdræ)\\\\"
    text_ordo += "\nNum & Liber Numeri\\\\"
    text_ordo += "\nOs & Liber Oseæ prophetæ\\\\"
    text_ordo += "\n1 et 2 Petr & Epistolæ I et II beati Petri apostoli\\\\"
    text_ordo += "\nPhil & Epistola beati Pauli apostoli ad Philippenses\\\\"
    text_ordo += "\nPhm & Epistola beati Pauli apostoli ad Philemonem\\\\"
    text_ordo += "\nProv & Liber Proverbiorum\\\\"
    text_ordo += "\nPs & Liber Psalmorum\\\\"
    text_ordo += "\nQoh & Liber Qohelet ( = Ecclesiastes)\\\\"
    text_ordo += "\n1 et 2 Reg & Libri I et II Regum ( = III et IV Regum)\\\\"
    text_ordo += "\nRom & Epistola beati Pauli apostoli ad Romanos\\\\"
    text_ordo += "\nRut & Liber Ruth\\\\"
    text_ordo += "\n1 et 2 Sam & Libri I et II Samuelis ( = I et II Regum)\\\\"
    text_ordo += "\nSap & Liber Sapientiæ\\\\"
    text_ordo += "\nSir & Liber Siracidæ (Ben Sira = Ecclesiasticus)\\\\"
    text_ordo += "\nSoph & Liber Sophoniæ prophetæ\\\\"
    text_ordo += "\n1 et 2 Th & Epistolæ I et II beati Pauli apostoli ad Thessalonicenses\\\\"
    text_ordo += "\n1 et 2 Tim & Epistolæ I et II beati Pauli apostoli ad Timotheum\\\\"
    text_ordo += "\nTit & Epistola beati Pauli apostoli ad Titum\\\\"
    text_ordo += "\nTob & Liber Tobiæ\\\\"
    text_ordo += "\nZac & Liber Zachariæ prophetæ\\\\"
    text_ordo += "\n\\thispagestyle{empty}"
    text_ordo += "\n\\end{longtable}\n"
    text_ordo += "\n\\newpage"
    text_ordo += "\n\\thispagestyle{empty}"
    text_ordo += "\n\\ApplyGenerTitleLarge{Notanda}"
    text_ordo += "\n\\ApplyGenerSubTitle{In Officio}"
    text_ordo += "\n\\ApplyGenerList{\n\\item In dominicis et festis, ad Vigilias, lectiones e Breviario 1962 sumptæ sic distribuuntur, nisi aliter notetur :\\par\t- in nocturno I : lectiones de Scriptura e nocturno I.\\par\t- in nocturno II : anno I, lectiones e nocturno III; anno II : lectiones e nocturno II.\\par\t Post ultimam lectionem, aliquantulum servatur sacrum silentium; signo dato a Superiore, dicitur hymnus \\textit{Te Deum}, quem sequitur oratio conveniens.\n\\item In memoriis maioribus a dominica prima novembris usque ad Pascha, post tres psalmos primi nocturni Vigiliarum, leguntur tres lectiones de Scriptura occurrenti (nisi propriæ sint) quibus adiungitur sine mora responsorium sine Gloria Patri ; deinde legitur lectio de sancto, post quam aliquantulum servatur sacrum silentium ; signo dato a Superiore, dicitur responsorium de sancto cum versiculo Gloria Patri.\n\\item In officiis sanctorum, quando sumitur antiphona propria ad Benedictus vel ad Magnificat, dicendum est versiculum e Laudibus vel e II Vesperis de communi sanctorum aut de officio proprio, nisi aliter notetur.}"
    text_ordo += "\n\\ApplyGenerSubTitle{In ML}"
    text_ordo += "\n\\ApplyGenerList{\n\\item Paramenta celebrantis debent esse coloris convenientis Missæ diei aut alteræ Missæ celebrandæ (cf. \\textit{Rubricæ generales Missalis Romani} n. 117).\n\\item Color paramentorum, in Missis votivis, debet esse cuique Missæ conveniens ; sed in missis votivis lectis IV classis non conventualibus, adhiberi potest etiam color Officii diei, servato tamen colore violaceo et nigro unice pro Missis quibus per se competit (\\textit{Rubricæ generales Missalis Romani} n. 323).\n\\item Missa votiva IV classis est Missa votiva quæ celebrari potest tantum in diebus liturgicis IV classis (\\textit{Rubricæ generales Missalis Romani} n. 387).\n\\item Præfatio de Martyribus dici potest in Missis festivis et votivis Sanctorum Martyrum, nisi aliter notetur.\n\\item Præfatio de Angelis dici potest in missis festivis et votivis Angelorum.\n\\item Missæ defunctorum IV classis sunt Missæ defunctorum «cotidianæ», quæ celebrari possunt, loco Missæ Officio diei respondentis, in feriis IV classis tantum, extra tempus natalicium. Maxime convenit ut hæ Missæ defunctorum IV classis tunc tantum dicantur cum revera pro defunctis, aut in genere aut certo designatis, applicantur (\\textit{Rubricæ generales Missalis Romani} n. 423). In Missis defunctorum «cotidianis» nigro colore utendum est.}"
    text_ordo += "\n\\ApplyGenerSubTitle{In MC}"
    text_ordo += "\n\\ApplyGenerList{\n\\item In feriis cantatur præfatio in tono simplici, sed in memoriis minoribus in tono sollemni.\n\\item Per hebdomadam dicitur semper eadem præfatio, nisi aliter notetur.\\item Singulis diebus, omnes genuflectant ad consecrationem, et ante Communionem quando sacerdos dicit \\textit{Ecce Agnus Dei}. Diebus ieiunii vero, genuflectandum est ab acclamatione \\textit{Sanctus} expleta usque ad finem Precis eucharisticæ.}"
    text_ordo += "\n\\thispagestyle{empty}"
    text_ordo += "\n\\vspace{2cm}\\ApplyGenerTitleLarge{Advertenda}\\par"
    text_ordo += "\n\\setlength{\\parindent}{0.5cm}"
    text_ordo += "\n\\small{Memoriæ sanctorum sunt obligatoriæ vel ad libitum. Memoriæ obligatoriæ designantur litteris rectis (memoria maior - memoria minor), memoriæ ad libitum litteris italicis (\\textit{memoria maior} - \\textit{memoria minor}).\\par E.g., Memoria S. Claræ, virginis, quamvis celebretur gradu memoriæ minoris, est celebratio obligatoria. Memoria Beatæ Virginis Mariæ Reginæ, quamvis sit gradu memoriæ maioris, est tamen celebratio ad libitum.}\n"
    text_ordo += "\n\\newpage"
    text_ordo += "\n\\thispagestyle{empty}"

    # On va chercher dans le dictionnaire various.py/ult_ant_dict la dernière férie libre de l'année, où il faudra insérer les antiennes du XXIVe dim. ap. la Pent. ("Cum videritis" et "Amen dico vobis") :
    ult_ant = ult_ant_dict[christ_roi.day]

    month = 0
    for i in range(nb_days):
        new_day_date = ordo_start + datetime.timedelta(days=i)
        next_day = new_day_date + datetime.timedelta(days=1)
        if (new_day_date.month == 1) and (new_day_date.day == 1):
            text_ordo += "\n\\renewcommand{\\CurrentYear}{" + \
                str(current_year) + "}"
        dict_new_day = dict_tempo[new_day_date].copy()
        if "I_vesp" not in dict_new_day:
            dict_new_day["I_vesp"] = ""
        if "generalities" not in dict_new_day:
            dict_new_day["generalities"] = ""
        if "anniv" not in dict_new_day:
            dict_new_day["anniv"] = ""
        if "hebdo_psalt" not in dict_new_day:
            dict_new_day["hebdo_psalt"] = ""
        if "symbols" not in dict_new_day:
            dict_new_day["symbols"] = ""
        if "body" not in dict_new_day:
            dict_new_day["body"] = ""
        if "II_vesp" not in dict_new_day:
            dict_new_day["II_vesp"] = ""
        if "lectiones_header" not in dict_new_day:
            dict_new_day["lectiones_header"] = ""
        if "lectiones_body" not in dict_new_day:
            dict_new_day["lectiones_body"] = ""
        if "preface_feries" not in dict_new_day:
            dict_new_day["preface_feries"] = ""
        if new_day_date in dict_sancto and i != 0:
            dict_new_day_sancto = dict_sancto[new_day_date].copy()
            if "anniv" in dict_new_day_sancto:
                dict_new_day["anniv"] = dict_new_day_sancto["anniv"]
            if "generalities" in dict_new_day_sancto:
                dict_new_day["generalities"] = dict_new_day_sancto["generalities"]
            force_sancto = dict_new_day_sancto["force"] if "force" in dict_new_day_sancto else 0
            if force_sancto > dict_new_day["force"]:
                dict_new_day["force"] = force_sancto
                dict_new_day["I_vesp"] = dict_new_day_sancto["I_vesp"] if "I_vesp" in dict_new_day_sancto else ""
                dict_new_day["header"] = dict_new_day_sancto["header"] if "header" in dict_new_day_sancto else ""
                dict_new_day["body"] = dict_new_day_sancto["body"] if "body" in dict_new_day_sancto else ""
                # Si pas vendredi du TP (férie ou mém. mineure, pour lesquelles il faut garder l'antienne spéciale),
                # on remplace les IIe Vêpres du tempo par celles du sancto :
                if not(new_day_date > paques and new_day_date < paques + datetime.timedelta(days=39) and ("de ea" in dict_new_day["header"] or "minor" in dict_new_day["header"])):
                    dict_new_day["II_vesp"] = dict_new_day_sancto["II_vesp"] if "II_vesp" in dict_new_day_sancto else ""

            # Cas où l'on veut garder le header du tempo et ajouter le body du sancto (mémoires pendant le carême par ex.) :
            elif force_sancto == dict_new_day["force"]:
                dict_new_day["body"] = dict_new_day_sancto["body"] if "body" in dict_new_day_sancto else ""

        # Cas des vendredis de carême : il faut ajouter dans le body l'indulgence plénière quel que soit le jour (tempo ou sancto) :
        if new_day_date == paques - datetime.timedelta(days=44):
            dict_new_day[
                "body"] += "\n\\item \\textit{Christifideli, qui orationem \\emph{En ego, o bone et dulcissime Iesu} coram Iesu Christi Crucifixi imagine, post communionem, pie recitet, conceditur indulgentia plenaria qualibet feria sexta temporis Quadragesimæ et temporis Passionis \\emph{(Enchiridion Indulgentiarum, concessio n. 22)}.}"
        elif new_day_date > paques - datetime.timedelta(days=46) and new_day_date < paques - datetime.timedelta(days=7) and new_day_date.weekday() == 4:
            dict_new_day["body"] += "\\item \\textit{indulgentia plenaria pro recitatione orationis \\emph{En ego, o bone et dulcissime Iesu}.}"

        # Cas des féries avant l'Ascension : il faut ajouter dans le body le "Nihil fit de Rogationibus…" même en cas de sancto :
        if new_day_date > paques + datetime.timedelta(days=35) and new_day_date < paques + datetime.timedelta(days=39):
            if new_day_date == paques + datetime.timedelta(days=36):
                comment_rogations = "\n\\item Hodie fit processio Rogationum.\n\\item In Officio et in ML nihil fit de Rogationibus, præter antiphonas ad \\textit{Benedictus} et \\textit{Magnificat}." if "de ea" in dict_new_day["header"] else ("\n\\item Hodie fit processio Rogationum.\n\\item In Officio et in ML nihil fit de Rogationibus, præter antiphonam ad \\textit{Magnificat}." if "memoria minor" in dict_new_day["header"] else "\n\\item Hodie fit processio Rogationum.")
            elif new_day_date == paques + datetime.timedelta(days=37):
                comment_rogations = "\n\\item In Officio et in ML nihil fit de Rogationibus, præter antiphonas ad \\textit{Benedictus} et \\textit{Magnificat}." if "de ea" in dict_new_day["header"] else ("\n\\item In Officio et in ML nihil fit de Rogationibus, præter antiphonam ad \\textit{Magnificat}." if "memoria minor" in dict_new_day["header"] else "")
            elif new_day_date == paques + datetime.timedelta(days=38):
                comment_rogations = "\n\\item In Officio et in ML nihil fit de Rogationibus, præter antiphonam ad \\textit{Benedictus}." if "de ea" in dict_new_day["header"] else ""
            dict_new_day["body"] = comment_rogations + dict_new_day["body"]

        # Semailles et récoltes : on ajoute le texte après le body éventuellement existant.
        dict_new_day["body"] = (dict_new_day["body"] if dict_new_day["body"] != "" else "") + ("\n\\item In MC : Missa \\textit{In conserendis agris} (MR 1127 A - GR 654) ; præfatio V de dominicis per annum." if new_day_date == date_semailles else "")
        dict_new_day["body"] = (dict_new_day["body"] if dict_new_day["body"] != "" else "") + ("\n\\item In MC : Missa \\textit{post collectos fructus terræ} (MR 1129 - GR 654) ; præfatio V de dominicis per annum." if new_day_date == date_recoltes else "")

        # Lundi de Pentecôte : "Ad mensam" sans mention de Pentecôte si c'est festum et supra :
        if new_day_date == paques + datetime.timedelta(days=50):
            dict_new_day["generalities"] = dict_new_day["generalities"].replace(
                " cras benedictio de Pentecoste ; a feria III", "") if not "de ea" in dict_new_day["header"] else dict_new_day["generalities"]

        # IIe Vêpres : peuvent être les Ières Vêpres du jour suivant (auquel cas on opère le changement) :
        if i != nb_days - 1:
            next_day = new_day_date + datetime.timedelta(days=1)
            force_tempo_next = dict_tempo[next_day]["force"]
            if force_tempo_next > dict_new_day["force"] and "I_vesp" in dict_tempo[next_day]:
                dict_new_day["II_vesp"] = dict_tempo[next_day]["I_vesp"]
            if next_day in dict_sancto:
                force_sancto_next = dict_sancto[next_day]["force"] if "force" in dict_sancto[next_day] else 0
                if force_sancto_next > dict_new_day["force"] and "I_vesp" in dict_sancto[next_day]:
                    dict_new_day["II_vesp"] = dict_sancto[next_day]["I_vesp"]
        else:
            # Le dernier samedi de l'année liturgique, les IIe Vêpres sont les Ières Vêpres de l'année suivante.
            dict_new_day["II_vesp"] = ""

        # Antiennes du dernier dimanche de l'année à caser à la dernière férie libre :
        if new_day_date.day == ult_ant:
            if new_day_date in dict_sancto and 'body' in dict_sancto[new_day_date] and 'Missa defunctorum pro omnibus benefactoribus nostris defunctis (MR 1225)' in dict_sancto[new_day_date]['body'] and new_day_date.month in [11,12]:
                dict_new_day["body"] = "\n\\item Ad Benedictus: ø \\textit{Cum videritis} (AM 617)." + dict_new_day["body"] + "\n\\item Ad Magnificat: ø \\textit{Amen dico vobis} (AM 618)."
            elif new_day_date.year == current_year and new_day_date.month == 11 and new_day_date.day != 1:
                dict_new_day["body"] = "\n\\item Ad Benedictus: ø \\textit{Cum videritis} (AM 617).\n\\item Ad Magnificat: ø \\textit{Amen dico vobis} (AM 618)."
            elif new_day_date.year == current_year and new_day_date.month == 12 and new_day_date.day == 1:
                dict_new_day["body"] = "\n\\item Ad Benedictus: ø \\textit{Cum videritis} (AM 617).\n\\item \\textit{In ML (Alb.) : Missa de sacratissimo Corde Iesu \\emph{(Gloria)}.}\n\\item MC1V\n\\item Ad Magnificat: ø \\textit{Amen dico vobis} (AM 618)."

        # Enfin on ajoute le dictionnaire courant à l'ordo, en le faisant précéder du mois si besoin :
        text_ordo += "\n" + \
            dict_new_day["generalities"] if dict_new_day["generalities"] != "" else ""
        text_ordo += "\n\\ApplyAnniv{" + \
            dict_new_day["anniv"] + \
            "}\n" if dict_new_day["anniv"] != "" else ""

        if new_day_date.month != month:
            month = new_day_date.month
            special_month = special_months[month]
            text_ordo += "\n\n\\ApplyNewMonthTitles{" + f_transf_month(month) + "}" + (
                "\n\\ApplyNewMonthSubTitles{" + special_month + "}" if special_month != "" else "")

        text_ordo += "\n\\ApplyHebdoPsalt{" + \
            dict_new_day["hebdo_psalt"] + \
            "}" if dict_new_day["hebdo_psalt"] != "" else ""
        text_ordo += "\n\\ApplyHeader{" + (
            dict_new_day["num_day"] if dict_new_day["num_day"] != "" else "")
        text_ordo += dict_new_day["symbols"] if dict_new_day["symbols"] != "" else ""
        text_ordo += (dict_new_day["header"]
                      if dict_new_day["header"] != "" else "") + "}"
        text_ordo += "\n\\ApplyBody{" + dict_new_day["body"] + (
            "}" if dict_new_day["II_vesp"] == "" else "") if dict_new_day["body"] != "" else ""
        text_ordo += (("\n\\ApplyBody{\n" if dict_new_day["body"] == "" else "") +
                      dict_new_day["II_vesp"] + "}") if dict_new_day["II_vesp"] != "" else ""
        text_ordo += "\n\\ApplyLectHeader{" + dict_new_day["lectiones_header"] + \
            "}" if dict_new_day["lectiones_header"] != "" else ""
        text_ordo += "\n\\ApplyLectBody{" + dict_new_day["lectiones_body"] + \
            "}" if dict_new_day["lectiones_body"] != "" else ""
        text_ordo += "\n\\ApplyPrefaceFeries{" + \
            dict_new_day["preface_feries"] + \
            "}" if dict_new_day["preface_feries"] != "" else ""

    text_ordo += "\n\\vspace{1cm}\n\\ApplyHebdoPsalt{\\textbf{Post Nonam explicit}}" + \
        "\n\\ApplyHebdoPsalt{\\textbf{Annus liturgicus " + \
        str(current_year - 1) + "-" + str(current_year) + "}}"

    # Jubilés :
    text_ordo += "\n\n\\newpage"
    text_ordo += "\n\n\\thispagestyle{empty}"
    text_ordo += "\n\\ApplyGenerTitleLarge{Hoc anno celebrabunt iubilæum suum:}}"
    text_ordo += "\n\\begin{center}"
    text_ordo += "\n\\medskip\n\\fontsize{12}{12}\\selectfont\n\\setlength{\\parskip}{0.1cm}"
    text_ordo += "\nDie VIII Decembris 2023: P. Michael Maria (L Prof.)\\par"
    text_ordo += "\nDie XI Novembris 2024: P. Ioannes Maria (L Prof.)\\par"
    text_ordo += "\n\\end{center}"

    # End of document :
    text_ordo += "\n\n\\end{document}"

    # Espaces avant les signes de ponctuation doubles :
    text_ordo = re.sub(r'[  ]([:;!?])', r'\1', text_ordo)
    text_ordo = re.sub(r'([;:!?])', r'~\1', text_ordo)

    # Remplacement des MC des 1ers vendredis du mois, en alternant d'un vendredi sur l'autres les 2 messes possibles (voir various.py) :
    i = 1
    while "MC1V" in text_ordo:
        text_ordo = text_ordo.replace("MC1V", first_vendr_mc[i], 1)
        i = 1 if i == 2 else 2  # Pour alterner d'un vendredi sur l'autre.

    # Écriture du fichier TeX :
    file_out = open(os.path.abspath(".") + "/ordo/" +
                    str(current_year) + ".tex", "w", encoding="utf-8")
    file_out.write(text_ordo)
    file_out.close()
