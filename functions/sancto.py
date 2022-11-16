# coding: utf-8

from calendar import weekday
import datetime
from functions.lectiones import *
from functions.various import hebdo_psalterii_inv, f_roman_numbers, f_num_summer


def dict_sancto_create(current_year, even_year, year_letter, dict_tempo, paques, nb_dim_ap_pentec):
    # Servira pour les solennité qui tombent un dimanche après la Pentecôte.
    pentecote = paques + datetime.timedelta(days=49)

    def is_septuagesime(date):
        if date > paques - datetime.timedelta(days=63):
            return True
        else:
            return False

    def is_careme(date):
        if date > paques - datetime.timedelta(days=46) and date < paques:
            return True
        else:
            return False

    def is_near_paques(date):
        if date >= paques - datetime.timedelta(days=7) and date <= paques + datetime.timedelta(days=7):
            return True
        else:
            return False

    def is_oct_pent(date):
        if date > paques + datetime.timedelta(days=49) and date < paques + datetime.timedelta(days=56):
            return True
        else:
            return False

    def is_third_week_of_september(date):
        sunday_before = (
            date - datetime.timedelta(days=date.weekday() + 1)).day
        return date.month == 9 and (15 <= sunday_before <= 21)

    dict_sancto = {}

    ###################################
    # ENTRER ICI LES MESSES MANUELLES :
    ###################################

    # Anniversaire de l'élection du Pape :
    # Attention : ça peut être current_year - 1.
    anniv_pape_date = datetime.date(current_year, 3, 13)
    anniv_pape = dict_sancto[anniv_pape_date] = {}
    anniv_pape[
        "anniv"] = "Cras recurrit anniversarium electionis S.S. D.N. Francisci, quem Dominus viviﬁcet et beatum faciat (2013)."
    # 1ère Messe défunts :
    messe_defunts_date = datetime.date(current_year, 2,  1)
    messe_defunts = dict_sancto[messe_defunts_date] = {}
    messe_defunts["force"] = 10
    messe_defunts["body"] = "\n\\item in MC (\\textit{Nigr.}) : Missa defunctorum pro omnibus benefactoribus nostris defunctis (MR 1225) ; lectiones propriæ : Rom \\textbf{5}, 6b-11 / Mt \\textbf{5}, 1-12a ; præfatio II de defunctis." 
    
    # 2e Messe défunts :
    messe_defunts_date = datetime.date(current_year, 6, 15)
    messe_defunts = dict_sancto[messe_defunts_date] = {}
    messe_defunts["force"] = 10
    messe_defunts["body"] = "\n\\item in MC (\\textit{Nigr.}) : Missa defunctorum pro omnibus benefactoribus nostris defunctis (MR 1225) ; lectiones propriæ : Rom \\textbf{8}, 14-17 / Lc \\textbf{12}, 35-40 ; præfatio III de defunctis."
    
    # 3e Messe défunts :
    messe_defunts_date = datetime.date(current_year, 9, 5)
    messe_defunts = dict_sancto[messe_defunts_date] = {}
    messe_defunts["force"] = 10
    messe_defunts["body"] = "\n\\item in MC (\\textit{Nigr.}) : Missa defunctorum pro omnibus benefactoribus nostris defunctis (MR 1225) ; lectiones propriæ : 1 Io \\textbf{3}, 14.16-20 / Io \\textbf{5}, 24-29 ; præfatio IV de defunctis."
    
    # 4e Messe défunts :
    messe_defunts_date = datetime.date(current_year, 11, 14)
    messe_defunts = dict_sancto[messe_defunts_date] = {}
    messe_defunts["force"] = 10
    messe_defunts["body"] = "\n\\item in MC (\\textit{Nigr.}) : Missa defunctorum pro omnibus benefactoribus nostris defunctis (MR 1225) ; lectiones propriæ : Ap \\textbf{20}, 11 – \\textbf{21}, 1 / Io \\textbf{14}, 1-6 ; præfatio V de defunctis."
    # Semailles et récoltes : voir ordo_write.py.

    ###################################
    # FIN DES MESSES MANUELLES
    ###################################

    # NOVEMBRE:

    saint_andre_date = datetime.date(current_year - 1, 11, 30)
    saint_andre = dict_sancto[saint_andre_date] = {}
    saint_andre["force"] = 70
    saint_andre["anniv"] = "Cras incipiunt preces novendiales ante sollemnitatem Immaculatæ Conceptionis Beatæ Mariæ Virginis."
    saint_andre["header"] = " - \\textbf{\\textsc{S. Andreæ, apostoli}} - \\textbf{festum} - \\textit{Rub.}"
    year = saint_andre_date.year
    even = year % 2 == 0
    var_benedictus = "\\item ad Benedictus: ø \\textit{Unus ex duobus} (AM 754)." if even else ""
    saint_andre["body"] = var_benedictus + \
        "\\item in MC: lectiones propriæ: Rom \\textbf{10}, 9-18 / Mt \\textbf{4}, 18-22 ; præfatio II de Apostolis."

    # DÉCEMBRE:

    saint_franc_xav_date = datetime.date(current_year - 1, 12, 3)
    saint_franc_xav = dict_sancto[saint_franc_xav_date] = {}
    saint_franc_xav["force"] = 40
    saint_franc_xav["header"] = " - \\textsc{S. Francisci Xavier}, presbyteri - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_franc_xav[
        "body"] = "\n\\item ad Vigilias: lectio de memoria in supplemento 60.\n\\item ad Benedictus: ø \\textit{Euntes} (AM 484).\n\\item in MC: præfatio de sanctis virginibus et religiosis."
    saint_franc_xav[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Alias oves} (AM 486)."

    saint_nicolas_date = datetime.date(current_year - 1, 12, 6)
    saint_nicolas = dict_sancto[saint_nicolas_date] = {}
    # Pour qu'un éventuel 1er vendredi du mois soit + fort (ML = Sacré-Cœur).
    saint_nicolas["force"] = 9
    saint_nicolas["body"] = "\n\\item \\textit{in ML (Alb.): Missa S. Nicolai.}"

    nd_lorette_date = datetime.date(current_year - 1, 12, 10)
    nd_lorette = dict_sancto[nd_lorette_date] = {}
    nd_lorette["force"] = 40
    nd_lorette["header"] = " - Beatæ Mariæ Virginis de Loreto - \\textit{memoria minor} - \\textit{Viol.}"
    nd_lorette["body"] = "\n\\item ad Benedictus: ø \\textit{Beatam} (AM 711); oratio in supplemento 60*.\n\\item \\textit{in ML: Alb.}\n\\item in MC \\textit{(Alb.)}: Commune Beatæ Mariæ Virginis (MR 905) ; præfatio I de Beata Maria Virgine."

    saint_ambroise_date = datetime.date(current_year - 1, 12, 7)
    saint_ambroise = dict_sancto[saint_ambroise_date] = {}
    saint_ambroise["force"] = 40
    saint_ambroise["header"] = " - \\textsc{S. Ambrosii}, episcopi et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_ambroise["body"] = "\n\\item ad Benedictus: ø \\textit{Paraclitus} (AM 531).\n\\item \\textit{in ML: Missa in proprio sanctorum vel in PAL.}\n\\item in MC: præfatio de sanctis pastoribus."

    if datetime.date(current_year - 1, 12, 8).weekday() != 6:
        imm_conc_date = datetime.date(current_year - 1, 12, 8)
    else:
        imm_conc_date = datetime.date(current_year - 1, 12, 9)
    imm_conc = dict_sancto[imm_conc_date] = {}
    imm_conc["force"] = 110
    imm_conc["I_vesp"] = "\n\\item I Vesperæ sollemnitatis sequentis."
    imm_conc["header"] = " - ¬ \\textbf{\\MakeUppercase{In Conceptione Immaculata Beatæ Mariæ Virginis} - sollemnitas maior} - \\textit{Alb.}"
    imm_conc[
        "body"] = "\n\\item ad Vigilias: in nocturno II: lectiones 5, 6 et 7 cum ¶ lectionis 8 ; in nocturno III: lectiones 9 et 10.\n\\item in MC: lectiones propriæ: Gen \\textbf{3}, 9-15.20 / Ep \\textbf{1}, 3-6.11-12 / Lc \\textbf{1}, 26-38 ; præfatio propria."
    imm_conc["II_vesp"] = "\n\\item Vesperæ sollemnitatis ; benedictio Sanctissimi Sacramenti." if imm_conc_date.weekday(
    ) != 5 else "\n\\item I Vesperæ Dominicæ."

    nd_guadalupe_date = datetime.date(current_year - 1, 12, 12)
    nd_guadalupe = dict_sancto[nd_guadalupe_date] = {}
    nd_guadalupe["force"] = 20
    nd_guadalupe["header"] = " - Beatæ Mariæ Virginis de Guadalupe - \\textit{memoria minor} - \\textit{Viol.}"
    nd_guadalupe["body"] = "\n\\item ad Benedictus: ø \\textit{Viderunt eam} (AM 1073) ; oratio in supplemento 60*.\n\\item \\textit{in ML: Alb.}\n\\item in MC \\textit{(Alb.)}: Commune Beatæ Mariæ Virginis (MR 905) ; præfatio I de Beata Maria Virgine."

    sainte_lucie_date = datetime.date(current_year - 1, 12, 13)
    sainte_lucie = dict_sancto[sainte_lucie_date] = {}
    sainte_lucie["force"] = 40
    sainte_lucie["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus Reverendissimi Patris Fulgentii Mariæ \\textsc{Lagrace}, prioris, qui die 13 decembris 1966 in Abbatia Dominæ Nostræ Mayliliensis obdormivit in Domino."
    sainte_lucie["header"] = " - \\textsc{S. Luciæ}, virginis et martyris - \\textbf{memoria maior} - \\textit{Rub.}"
    var_vesperas = ", vesperas" if sainte_lucie_date.weekday() != 5 else ""
    sainte_lucie[
        "body"] = "\n\\item ad Vigilias pro breviario veteri: in supplemento 60.\n\\item ad Laudes" + var_vesperas + " et Horas minores: antiphonæ propriæ.\n\\item ad Laudes: hymnus \\textit{Iesu corona} (AM 677).\n\\item in MC: Commune virginis martyris (MR 924) ; præfatio de sanctis martyribus."
    var_magnif = " ; ad Magnificat: ø \\textit{In tua patientia} (AM 769)" if not even_year else ""
    sainte_lucie["II_vesp"] = "\n\\item ad Vesperas: hymnus \\textit{Iesu corona} ut supra" + var_magnif + "."

    saint_jean_de_la_croix_date = datetime.date(current_year - 1, 12, 14)
    saint_jean_de_la_croix = dict_sancto[saint_jean_de_la_croix_date] = {}
    saint_jean_de_la_croix["force"] = 40
    saint_jean_de_la_croix["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus Reverendissimi Patris Emmanuel Mariæ \\textsc{Sarramagnan}, prioris, qui die 14 decembris 2005 in Abbatia Dominæ Nostræ Mayliliensis obdormivit in Domino."
    # Car si mercredi, forcément Quatre-Temps.
    vigiles_quatre_temps = "lectiones SO in supplemento 5; " if saint_jean_de_la_croix_date.weekday() == 2 else ""
    saint_jean_de_la_croix[
        "header"] = " - \\textsc{S. Ioannis a Cruce}, presbyteri et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.} (olim die 24 novembris)."
    saint_jean_de_la_croix["body"] = "\n\\item ad Vigilias: " + vigiles_quatre_temps + \
        "lectio de memoria in supplemento 61.\n\\item ad Benedictus: ø \\textit{Qui vult} (AM 644).\n\\item \\textit{in ML: Missa in PAL.}\n\\item in MC: præfatio de sanctis virginibus et religiosis."

    anniv_fr_joseph_date = datetime.date(current_year - 1, 12, 17)
    anniv_fr_joseph = dict_sancto[anniv_fr_joseph_date] = {}
    anniv_fr_joseph["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus fratris nostri Ioseph Mariæ \\textsc{Bumat}, qui die 17 decembris 1997 obdormivit in Domino."

    anniv_dom_marechaux_date = datetime.date(current_year - 1, 12, 24)
    anniv_dom_marechaux = dict_sancto[anniv_dom_marechaux_date] = {}
    anniv_dom_marechaux["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus Reverendissimi Patris Bernardi Mariæ \\textsc{Maréchaux}, abbatis, qui die 24 decembris 1927 in Monasterio Dominæ Nostræ Sanctæ Spei Mesnili obdormivit in Domino."

    saint_etienne_date = datetime.date(current_year - 1, 12, 26)
    saint_etienne = dict_sancto[saint_etienne_date] = {}
    saint_etienne["force"] = 70
    saint_etienne["header"] = " - \\textbf{\\textsc{S. Stephani, protomartyris}} - \\textbf{festum} - \\textit{Rub.}"
    saint_etienne["body"] = "\n\\item in MC: lectiones propriæ: Act \\textbf{6}, 8-10 ; \\textbf{7}, 54-60 / Mt \\textbf{10}, 17-22 ; præfatio I de Nativitate."
    saint_etienne["II_vesp"] = "\n\\item ad Vesperas: antiphonæ et psalmi de Nativitate ; a capitulo de festo."

    saint_jean_date = datetime.date(current_year - 1, 12, 27)
    saint_jean = dict_sancto[saint_jean_date] = {}
    saint_jean["force"] = 70
    saint_jean["header"] = " - \\textbf{\\textsc{S. Ioannis, apostoli et evangelistæ}} - \\textbf{festum} - \\textit{Alb.}"
    saint_jean["body"] = "\n\\item in MC: lectiones propriæ: 1 Io \\textbf{1}, 1-4 / Io \\textbf{20}, 2-8 ; præfatio I de Nativitate."
    saint_jean["II_vesp"] = "\n\\item ad Vesperas: antiphonæ et psalmi de Nativitate ; a capitulo de festo."

    saints_innocents_date = datetime.date(current_year - 1, 12, 28)
    saints_innocents = dict_sancto[saints_innocents_date] = {}
    saints_innocents["force"] = 70
    saints_innocents["header"] = " - \\textbf{\\textsc{Ss. Innocentium, martyrum}} - \\textbf{festum} - \\textit{Rub.}"
    saints_innocents["body"] = "\n\\item in MC: lectiones propriæ: 1 Io \\textbf{1}, 5–2, 2 / Mt \\textbf{2}, 13-18 ; præfatio I de Nativitate."
    saints_innocents["II_vesp"] = "\n\\item ad Vesperas: antiphonæ et psalmi de Nativitate ; a capitulo de festo."

    # JANVIER:

    sainte_marie_mere_de_dieu_date = datetime.date(current_year, 1, 1)
    sainte_marie_mere_de_dieu = dict_sancto[sainte_marie_mere_de_dieu_date] = {
    }
    sainte_marie_mere_de_dieu["force"] = 110
    sainte_marie_mere_de_dieu[
        "I_vesp"] = "\\item Vesperæ sollemnitatis Sanctæ Dei Genetricis Mariæ.\n\\item ante Completorium: cantatur hymnus \\textit{Te Deum} cum versiculis et oratione in gratiarum actionem (GR 841): indulgentia plenaria."
    sainte_marie_mere_de_dieu["header"] = (" \\textbf{\\textsc{Dominica I post Nativitatem}}" if sainte_marie_mere_de_dieu_date.weekday(
    ) == 6 else "") + " - ¬ \\textbf{\\MakeUppercase{sollemnitas Sanctæ Dei Genetricis Mariæ}} - \\textbf{sollemnitas maior} - \\textit{Alb.}"
    sainte_marie_mere_de_dieu[
        "body"] = "\n\\item Officium et Missæ lectæ dicuntur de octava Nativitatis (vel Circumcisione) præter invitatorium in supplemento 58.\n\\item in MC: cantatur hymnus \\textit{Veni Creator} sine versiculo neque oratione (AM 1254), prima stropha dicitur flexis genibus post formulam salutationis et ante Tertiam (indulgentia plenaria) ; lectiones propriæ: Num \\textbf{6}, 22-27 / Gal \\textbf{4}, 4-7 / Lc \\textbf{2}, 16-21 ; præfatio I de Beata Maria Virgine (\\textit{Et te in maternitate}) ; \\textit{Communicantes} proprium."
    sainte_marie_mere_de_dieu["II_vesp"] = "\n\\item Vesperæ sollemnitatis ; benedictio Sanctissimi Sacramenti."
    # Si 1er vendredi du mois, reporter le jeûne au lendemain:
    if sainte_marie_mere_de_dieu_date.weekday() == 4:
        dict_tempo[sainte_marie_mere_de_dieu_date]["symbols"] = dict_tempo[sainte_marie_mere_de_dieu_date]["symbols"].replace(
            " µ", " ł")
        dict_tempo[sainte_marie_mere_de_dieu_date + datetime.timedelta(
            days=1)]["symbols"] = " µ" + dict_tempo[sainte_marie_mere_de_dieu_date + datetime.timedelta(days=1)]["symbols"]

    saints_basile_gregoire_date = datetime.date(current_year, 1, 2)
    saints_basile_gregoire = dict_sancto[saints_basile_gregoire_date] = {}
    saints_basile_gregoire["force"] = 40
    feast_day = saints_basile_gregoire_date.weekday()
    if feast_day != 6:
        current_lectiones = lectiones["nativ"]
        lect_nativ = ""
        for i in range(6 - feast_day):
            if i < 4:
                lect_nativ += "\n\\item[" + \
                    str(2 + i) + " ian.] " + current_lectiones[2 + i]
        lectures = "\n\\ApplyLectHeader{Lectiones de tempore}\n\\ApplyLectBody{" + lect_nativ + "}"
    else:
        lectures = ""
    saints_basile_gregoire["generalities"] = "\n\\newpage\n\\ApplyParBox{1cm}{\\ApplyGenerTitleHuge{Tempus Nativitatis I}}\n\\ApplyGenerTitleLarge{Usque ad nonam diei 5 ianuarii}\n\\ApplyGenerSubTitle{in Officio:}\n\\ApplyGenerList{\\item ad Vigilias: omnia ut in ordinario officii ferialis tempore Nativitatis (in supplemento 28 pro breviario veteri), præter capitulum Hebr. 1, 10 ut in psalterio ; lectiones SO (in supplemento 30 pro breviario veteri).\n\\item ad Laudes et Vesperas: antiphonæ et psalmi de feria, reliqua ut in die 1 ianuarii, nisi aliter notetur.\n\\item ß \\textit{Benedicamus Domino}: ad Laudes VI$_2$; ad Vesperas VI$_1$.\n\\item ad Horas minores: antiphonæ et reliqua ut in die 1 ianuarii.\n\\item continuatur tonus Nativitatis ad Horas minores et Completorium.}\n\\ApplyGenerSubTitle{in ML:}\n\\ApplyGenerList{\\item præfatio de Nativitate.\n\\item Missæ defunctorum «cotidianæ» non permittuntur.}\n\\ApplyGenerSubTitle{in MC:}\n\\ApplyGenerList{\\item præfatio de Nativitate III, nisi aliter notetur.}\n\\ApplyGenerSubTitle{ad mensam:}\n\\ApplyGenerList{\\item benedictio de Nativitate.}" + lectures + "\n\\medskip"
    saints_basile_gregoire["header"] = " - \\textsc{Ss. Basilii Magni et Gregorii Nazianzeni}, episcoporum et Ecclesiæ doctorum - \\textbf{memoria maior} - \\textit{Alb.}"
    saints_basile_gregoire["body"] = "\n\\item in Officio: oratio in supplemento 65*.\n\\item ad Vigilias: hymnus \\textit{Inclitos Christi} in supplemento 66 ; lectiones SO ; lectio de memoria in supplemento 63*.\n\\item ad Laudes et Vesperas: antiphonæ et psalmi de feria, a capitulo ut in variationibus 26 et sequentibus.\n\\item ad Benedictus: ø \\textit{Qui sperant} in variationibus 31.\n\\item ad Horas minores: antiphonæ, capitulum et versiculi ut in variationibus 25.\n\\item \\textit{in ML: Missa plurium confessorum pontificum in PAL.}\n\\item in MC: lectiones feriales ; præfatio de sanctis pastoribus."
    saints_basile_gregoire[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Sapientiam sanctorum} (AM 981)."

    saint_nom_jesus_date = datetime.date(current_year, 1, 3)
    saint_nom_jesus = dict_sancto[saint_nom_jesus_date] = {}
    saint_nom_jesus["force"] = 40
    saint_nom_jesus["header"] = " - \\textsc{Sanctissimi Nominis Iesu} - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_nom_jesus[
        "body"] = "\n\\item in Officio: oratio in supplemento 67*.\n\\item ad Vigilias: invitatorium, hymnus et lectio de memoria in supplemento 65*.\n\\item ad Laudes et Horas minores: AM 279.\n\\item \\textit{in ML: olim dominica a die 2 ad diem 5 ianuarii occurrente (non dicitur \\emph{Credo}).} \n\\item in MC: lectiones propriæ: Phil \\textbf{2}, 1-11 / Lc \\textbf{2}, 21-24."
    txt_vesp = "\\item ad Vesperas: AM 283." if even_year else "\\item ad Vesperas: AM 276 ; ad Magnificat: ø \\textit{Vocabis} (AM 283)."
    saint_nom_jesus["II_vesp"] = txt_vesp

    vigile_epiphanie_date = datetime.date(current_year, 1, 5)
    vigile_epiphanie = dict_sancto[vigile_epiphanie_date] = {}
    vigile_epiphanie["force"] = 10
    vigile_epiphanie["body"] = "\n\\item ad Benedictus: ø \\textit{Illuminare} (AM 586)." + ("\n\\item \\textit{in ML: Missa de sacratissimo Corde Iesu (\\emph{Gloria}).}" if vigile_epiphanie_date.weekday(
    ) == 4 else "") + ("\n\\item \\textit{in ML (Alb.)  : Immaculati Cordis Beatæ Mariæ Virginis.}" if vigile_epiphanie_date.weekday() == 5 else "")

    epiphanie_date = datetime.date(current_year, 1, 6)
    epiphanie = dict_sancto[epiphanie_date] = {}
    epiphanie["force"] = 110
    epiphanie["generalities"] = "\n\\ApplyGenerSubTitle{ad mensam:}\n\\ApplyGenerList{\n\\item benedictio de Epiphania.}\n\\vspace{0.5cm}"
    epiphanie["I_vesp"] = "\\item I Vesperæ sollemnitatis sequentis."
    epiphanie["header"] = " - ¬ \\textbf{\\MakeUppercase{In Epiphania Domini}} - \\textbf{sollemnitas maior} - \\textit{Alb.}" if epiphanie_date.weekday(
    ) != 6 else " \\textbf{\\textsc{Dominica II post Nativitatem}} - ¬  \\textbf{\\MakeUppercase{In Epiphania Domini}} - \\textbf{sollemnitas maior} - \\textit{Alb.}"
    epiphanie["body"] = "\n\\item in MC: lectiones propriæ: Is \\textbf{60}, 1-6 / Ep \\textbf{3}, 2-3a 5-6 / Mt \\textbf{2}, 1-12 ; præfatio et \\textit{Communicantes} de Epiphania."
    epiphanie["II_vesp"] = "\n\\item Vesperæ sollemnitatis ; benedictio Sanctissimi Sacramenti."
    # Si 1er vendredi du mois, reporter le jeûne au lendemain:
    if epiphanie_date.weekday() == 4:
        dict_tempo[epiphanie_date]["symbols"] = dict_tempo[epiphanie_date]["symbols"].replace(
            " µ", " ł")
        dict_tempo[epiphanie_date + datetime.timedelta(
            days=1)]["symbols"] = " µ" + dict_tempo[epiphanie_date + datetime.timedelta(days=1)]["symbols"]

    """
    saint_greg_nysse_date = datetime.date(current_year, 1, 10)
    saint_greg_nysse = dict_sancto[saint_greg_nysse_date] = {}
    saint_greg_nysse["force"] = 40
    saint_greg_nysse["header"] = ""
    saint_greg_nysse["body"] = ""
    """

    saint_hilaire_date = datetime.date(current_year, 1, 13)
    saint_hilaire = dict_sancto[saint_hilaire_date] = {}
    saint_hilaire["force"] = 40
    saint_hilaire[
        "header"] = " - \\textsc{S. Hilarii}, episcopi et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.} (olim die 14 huius)."
    saint_hilaire["body"] = "\n\\item ad Vigilias: lectio de memoria in supplemento 65.\n\\item in MC: collecta in MR, reliqua in MP ; præfatio de sanctis pastoribus."

    saint_remi_date = datetime.date(current_year, 1, 14)
    saint_remi = dict_sancto[saint_remi_date] = {}
    saint_remi["force"] = 20
    saint_remi["header"] = " - S. Remigii, episcopi - \\textit{memoria minor} - \\textit{Vir.}"
    saint_remi["body"] = "\n\\item ad Benedictus: ø \\textit{Sacerdos} (AM 656) ; oratio in supplemento 66.\n\\item \\textit{in ML (Alb.): olim die 1 octobris.}\n\\item in MC \\textit{(Alb.)}: omnia in MP."

    ss_maur_placide_date = datetime.date(current_year, 1, 15)
    ss_maur_placide = dict_sancto[ss_maur_placide_date] = {}
    ss_maur_placide["force"] = 40
    ss_maur_placide[
        "header"] = " - \\textsc{Ss. Mauri et Placidi}, discipulorum SPN Benedicti - \\textbf{memoria maior} - \\textit{Alb.} (olim die 5 octobris)."
    ant_bened = "\\item ad Benedictus: ø \\textit{O beatum virum} (AM 777)." if even_year else "\\item ad Benedictus: ø \\textit{Cum Placidus} (AM 965)."
    var_vesperas = ", Vesperas" if ss_maur_placide_date.weekday() != 5 else ""
    ss_maur_placide["body"] = "\n\\item in Officio: oratio in supplemento 70 vel in variationibus 28.\n\\item ad Vigilias: hymnus proprius in supplemento 66 ; lectio de memoria in supplemento 67.\n\\item ad Laudes" + var_vesperas + " et Horas minores: Officium dicitur ut in AM 778." + ant_bened + \
        "\\item \\textit{in ML: Missa plurium confessorum non pontificum in PAL cum Evangelio S. Mauri (die 15 ianuarii in supplemento OSB).}\n\\item in MC: collecta in MP ; Commune sanctorum et sanctarum (MR 962) ; lectiones propriæ: Sir \\textbf{51}, 12-19a.20.27 / Mt \\textbf{14}, 22-33 ; præfatio de sanctis virginibus et religiosis."
    ss_maur_placide["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Hodie} (AM 782)."

    anniv_pere_augustin_date = datetime.date(current_year, 1, 16)
    anniv_pere_augustin = dict_sancto[anniv_pere_augustin_date] = {}
    anniv_pere_augustin["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus Reverendissimi ac dilectissimi Patris Augustini Mariæ \\textsc{Joly}, abbatis et fundatoris Monasterii nostri, qui die 16 ianuarii 2006 obdormivit in Domino."

    saint_antoine_date = datetime.date(current_year, 1, 17)
    saint_antoine = dict_sancto[saint_antoine_date] = {}
    saint_antoine["force"] = 40
    saint_antoine[
        "anniv"] = "Cras recurrit anniversarium erectionis S. Ioseph Claræ Vallis in titulum abbatialem (1992)."
    saint_antoine["header"] = " - \\textsc{S. Antonii}, abbatis - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_antoine["body"] = "\n\\item in MC: præfatio de sanctis virginibus et religiosis."
    saint_antoine[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Vos qui reliquistis} (AM 624)."

    unite_chretiens_date = datetime.date(current_year, 1, 18)
    unite_chretiens = dict_sancto[unite_chretiens_date] = {}
    unite_chretiens["anniv"] = "Cras incipit hebdomada precibus pro christianorum unitate dedicata."
    unite_chretiens_body = "\n\\item \\textit{in ML (Viol): Missa votiva pro Ecclesiæ unitate n. 20.}\n\\item in MC \\textit{(Viol)}: Missa pro unitate christianorum A (MR 1111) ; lectiones propriæ: 1 Io \\textbf{4}, 9-15 / Io \\textbf{17}, 20-26 ; præfatio propria."
    if datetime.date(current_year, 1, 18).weekday() == 6:
        unite_chretiens_transf_date = datetime.date(current_year, 1, 19)
        unite_chretiens_transf = dict_sancto[unite_chretiens_transf_date] = {}
        unite_chretiens_transf["force"] = 10
        unite_chretiens_transf["body"] = unite_chretiens_body
    elif datetime.date(current_year, 1, 18).weekday() == 5:
        unite_chretiens_transf_date = datetime.date(current_year, 1, 23)
        unite_chretiens_transf = dict_sancto[unite_chretiens_transf_date] = {}
        unite_chretiens_transf["force"] = 10
        unite_chretiens_transf["body"] = unite_chretiens_body
    else:
        unite_chretiens["force"] = 10
        unite_chretiens["body"] = unite_chretiens_body

    saint_sebastien_date = datetime.date(current_year, 1, 20)
    saint_sebastien = dict_sancto[saint_sebastien_date] = {}
    saint_sebastien["force"] = 20
    saint_sebastien["header"] = " - S. Sebastiani, martyris - \\textit{memoria minor} - \\textit{Vir.} "
    saint_sebastien["body"] = "\n\\item ad Benedictus: ø \\textit{Iste sanctus} (AM 639) ; oratio in supplemento 71.\n\\item \\textit{in ML: Rub.}\n\\item in MC \\textit{(Rub.)}: Commune martyrum (MR 917)."

    sainte_agnes_date = datetime.date(current_year, 1, 21)
    sainte_agnes = dict_sancto[sainte_agnes_date] = {}
    sainte_agnes["force"] = 40
    sainte_agnes["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus Henrici \\textsc{Vergez}, sacerdotis et benefactoris, qui die 21 ianuarii 1973 obdormivit in Domino."
    sainte_agnes["header"] = " - \\textsc{S. Agnetis}, virginis et martyris - \\textbf{memoria maior} - \\textit{Rub.}"
    var_vesperas = ", Vesperas" if sainte_agnes_date.weekday() != 5 else ""
    sainte_agnes[
        "body"] = "\n\\item ad Vigilias pro breviario veteri: lectio de memoria in supplemento 71.\n\\item ad Laudes" + var_vesperas + " et Horas minores: antiphonæ propriæ.\n\\item in MC: Commune virginis martyris (MR 924) ; lectiones propriæ: 1 Co \\textbf{1}, 26-31 / Mt \\textbf{13}, 44-46 ; præfatio de sanctis martyribus."
    sainte_agnes["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Beata Agnes} (AM 785)." if not even_year else ""

    saint_vincent_date = datetime.date(current_year, 1, 22)
    saint_vincent = dict_sancto[saint_vincent_date] = {}
    saint_vincent["force"] = 20
    saint_vincent["header"] = " - S. Vincentii, diaconi et martyris - \\textit{memoria minor} - \\textit{Vir.}"
    saint_vincent["body"] = "\n\\item ad Benedictus: ø \\textit{Si mihi} (AM 320).\n\\item \\textit{in ML (Rub.): Missa in supplemento OSB.}\n\\item in MC \\textit{(Rub.)}: Commune martyrum (MR 915)."

    saint_francois_de_sales_date = datetime.date(current_year, 1, 24)
    saint_francois_de_sales = dict_sancto[saint_francois_de_sales_date] = {}
    saint_francois_de_sales["force"] = 40
    saint_francois_de_sales[
        "header"] = " - \\textsc{S. Francisci de Sales}, episcopi et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.} (olim die 29 huius)."
    saint_francois_de_sales[
        "body"] = "\n\\item ad Vigilias: lectio de memoria in supplemento 73.\n\\item ad Benedictus: ø \\textit{Sapientiam} (AM 981).\n\\item \\textit{in ML: Missa in PAL.}\n\\item in MC: præfatio de sanctis pastoribus."

    conv_saint_paul_date = datetime.date(current_year, 1, 25)
    conv_saint_paul = dict_sancto[conv_saint_paul_date] = {}
    conv_saint_paul["force"] = 40
    conv_saint_paul["header"] = " - \\textbf{\\textsc{In Conversione S. Pauli apostoli}} - \\textbf{festum} - \\textit{Alb.}"
    conv_saint_paul[
        "body"] = "\n\\item ad Vigilias: in supplemento 74 pro breviario 62 ; invitatorium proprium.\n\\item ad Benedictus: ø \\textit{Vade Anania} (AM 791).\n\\item \\textit{in ML: non dicitur \\emph{Credo}.}\n\\item in MC: lectiones propriæ: Act \\textbf{22}, 3-16 / Mc \\textbf{16}, 15-18 ; præfatio I de Apostolis."

    abbes_cist_date = datetime.date(current_year, 1, 26)
    abbes_cist = dict_sancto[abbes_cist_date] = {}
    abbes_cist["force"] = 20
    abbes_cist[
        "header"] = " - Ss. Roberti, Alberici et Stephani, abbatum Cisterciensium - \\textit{memoria minor} - \\textit{Vir.} "
    abbes_cist["body"] = "\n\\item ad Benedictus: ø \\textit{Ecce quam bonum} in tono VIII g (AM 821), ß \\textit{Exsultabunt} (AM 739) ; oratio in supplemento 91.\n\\item \\textit{in ML (Alb.): Missa plurium confessorum non pontificum in PAL.}\n\\item in MC \\textit{(Alb.)}: collecta in MP ; Commune sanctorum et sanctarum (MR 952)."

    sainte_angele_merici_date = datetime.date(current_year, 1, 27)
    sainte_angele_merici = dict_sancto[sainte_angele_merici_date] = {}
    sainte_angele_merici["force"] = 20
    sainte_angele_merici[
        "header"] = " - S. Angelæ Merici, virginis - \\textit{memoria minor} - \\textit{Vir.}"
    sainte_angele_merici["body"] = "\n\\item ad Benedictus: ø \\textit{Simile est} (AM 680) ; oratio in supplemento 91.\n\\item \\textit{in ML (Alb.): olim die 1 iunii.}\n\\item in MC \\textit{(Alb.)}: Commune sanctorum et sanctarum (MR 965)."

    saint_thomas_aquin_date = datetime.date(current_year, 1, 28)
    saint_thomas_aquin = dict_sancto[saint_thomas_aquin_date] = {}
    saint_thomas_aquin["force"] = 40
    saint_thomas_aquin[
        "anniv"] = "Cras recurrit anniversarium approbationis Constitutionum Sancti Ioseph Claræ Vallis ab episcopo Divionensi (1988)."
    saint_thomas_aquin[
        "header"] = " - \\textsc{S. Thomæ de Aquino}, presbyteri et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.} (olim die 7 martii)."
    alleluia_ml = "\\item \\textit{in ML: \\emph{ß} Alleluia ut in Communi doctorum.}" if not is_septuagesime(
        saint_thomas_aquin_date) else ""
    saint_thomas_aquin["body"] = "\n\\item ad Benedictus: ø \\textit{Sapientia clamitat} (AM 581)." + \
        alleluia_ml + \
        "\\item in MC: Commune doctorum Ecclesiæ (MR 943) ; præfatio I de sanctis."

    sainte_bathilde_date = datetime.date(current_year, 1, 30)
    sainte_bathilde = dict_sancto[sainte_bathilde_date] = {}
    sainte_bathilde["force"] = 20
    sainte_bathilde["header"] = " - S. Bathildis, monialis - \\textit{memoria minor} - \\textit{Vir.} "
    sainte_bathilde["body"] = "\n\\item ad Benedictus: ø \\textit{Simile est} (AM 685) ; oratio in supplemento 91.\n\\item \\textit{in ML (Alb.): Missa pro nec virgine nec martyre.}\n\\item in MC \\textit{(Alb.)}: collecta in MP ; Commune sanctorum et sanctarum (MR 960)."

    saint_jean_bosco_date = datetime.date(current_year, 1, 31)
    saint_jean_bosco = dict_sancto[saint_jean_bosco_date] = {}
    saint_jean_bosco["force"] = 40
    saint_jean_bosco["header"] = " - \\textsc{S. Ioannis Bosco}, presbyteri - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_jean_bosco[
        "body"] = "\n\\item in Officio: oratio in supplemento 92 vel in variationibus 19.\n\\item ad Vigilias: lectio de memoria in supplemento 91.\n\\item ad Benedictus: ø \\textit{Fili, præbe mihi} (AM 566).\n\\item in MC: Commune sanctorum et sanctarum (MR 965) ; præfatio II de sanctis."
    saint_jean_bosco[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Amen dico vobis} in tono I f (AM 829)."

    # FÉVRIER:

    presentation_date = datetime.date(current_year, 2, 2)
    presentation = dict_sancto[presentation_date] = {}
    presentation["force"] = 90
    presentation["anniv"] = "Cras celebratur dies ad vitam religiosam atque ad vocationes ecclesiasticas petendas dedicata."
    # Si dimanche, il faut calculer quel dimanche c'est dans la forme extraordinaire (dans la forme ordinaire, c'est forcément le IVe dim. Per annum).
    if presentation_date.weekday() == 6:
        pres_dim = " \\textbf{\\textsc{Dominica IV per annum}}"
        if presentation_date.day == paques - datetime.timedelta(days=63):
            pres_dim += " (Septuagesima)"
        elif presentation_date.day == paques - datetime.timedelta(days=56):
            pres_dim += " (Sexagesima)"
        elif presentation_date.day == paques - datetime.timedelta(days=49):
            pres_dim += " (Quinquagesima)"
        else:
            pres_dim += " (IV post Epiphaniam)"
    else:
        pres_dim = ""
    presentation["header"] = pres_dim + \
        " - \\textbf{\\textsc{In Præsentatione Domini}} (vel Purificationis Beatæ Mariæ Virginis) - \\textbf{festum} - \\textit{Alb.}"
    if presentation_date.weekday() == 6:
        lectures_mc = " Mal \\textbf{3}, 1-4 / Hebr \\textbf{2}, 14-18"
    elif even_year:
        lectures_mc = " Hebr \\textbf{2}, 14-18"
    else:
        lectures_mc = " Mal \\textbf{3}, 1-4"
    aspersion = " aspersio omittitur;" if presentation_date.weekday() == 6 else ""
    vepres = "\n\\item Vesperæ Festi." if presentation_date.weekday() == 5 else ""
    presentation["body"] = "\n\\item in MC: ante Missam conventualem peragitur benedictio ac processio candelarum. Post processionem cantantur introitus Missæ et psalmodia Tertiæ ;" + \
        aspersion + " lectiones propriæ:" + lectures_mc + \
        " / Lc \\textbf{2}, 22-40 ; præfatio propria." + vepres + \
        "\n\\item post Completorium dicitur ø \\textit{Ave Regina Cælorum}."
    # Si 1er vendredi du mois, reporter le jeûne au lendemain:
    if presentation_date.weekday() == 4:
        dict_tempo[presentation_date]["symbols"] = dict_tempo[presentation_date]["symbols"].replace(
            " µ", " ł")
        dict_tempo[presentation_date + datetime.timedelta(
            days=1)]["symbols"] = " µ" + dict_tempo[presentation_date + datetime.timedelta(days=1)]["symbols"]

    saint_anschaire_date = datetime.date(current_year, 2, 3)
    saint_anschaire = dict_sancto[saint_anschaire_date] = {}
    saint_anschaire["force"] = 20
    saint_anschaire["header"] = " - S. Ansgarii, episcopi - \\textit{memoria minor} - \\textit{Vir.}"
    saint_anschaire["body"] = "\n\\item ad Benedictus: ø \\textit{Euntes in mundum} (AM 484) ; oratio in supplemento 93.\n\\item \\textit{in ML (Alb.): Missa pro confessore pontifice.}\n\\item in MC (Alb.): Commune pastorum (MR 938)."

    sainte_agathe_date = datetime.date(current_year, 2, 5)
    sainte_agathe = dict_sancto[sainte_agathe_date] = {}
    if is_careme(sainte_agathe_date):
        sainte_agathe["force"] = 10
        sainte_agathe["body"] = "\n\\item ad Laudes: pro commemoratione S. Agathæ ø \\textit{Paganorum} (AM 809).\n\\item in MC: collecta de sancta.\n\\item ad Vesperas: pro commemoratione S. Agathæ ø \\textit{Stans beata} (AM 806)."
    else:
        sainte_agathe["force"] = 40
        sainte_agathe["header"] = " - \\textsc{S. Agathæ}, virginis et martyris - \\textbf{memoria maior} - \\textit{Rub.}"
        var_vesperas = ", Vesperas" if sainte_agathe_date.weekday() != 5 else ""
        sainte_agathe[
            "body"] = "\n\\item ad Vigilias: lectio de memoria in supplemento 93 pro breviario veteri.\n\\item ad Laudes" + var_vesperas + " et Horas minores: antiphonæ propriæ.\n\\item in MC: Commune virginis martyris (MR 924) ; lectiones propriæ: 1 Co \\textbf{1}, 26-31 / Lc \\textbf{9}, 23-26 ; præfatio de sanctis martyribus."

    saint_paul_miki_date = datetime.date(current_year, 2, 6)
    saint_paul_miki = dict_sancto[saint_paul_miki_date] = {}
    if is_careme(saint_paul_miki_date):
        saint_paul_miki["force"] = 10
        saint_paul_miki[
            "body"] = "\n\\item ad Laudes: pro commemoratione S. Pauli Miki et sociorum ø \\textit{Beati eritis} (AM 1121) ; oratio in supplemento 96.\n\\item in MC: collecta de sanctis."
    else:
        saint_paul_miki["force"] = 40
        saint_paul_miki["header"] = " - \\textsc{Ss. Pauli Miki et sociorum}, martyrum - \\textbf{memoria maior} - \\textit{Rub.}"
        saint_paul_miki[
            "body"] = "\n\\item ad Vigilias: lectio de memoria in supplemento 94.\n\\item ad Benedictus: ø \\textit{Beati eritis} (AM 1121).\n\\item \\textit{in ML: Missa pro pluribus martyribus.}\n\\item in MC: Commune martyrum (MR 909) ; præfatio de sanctis martyribus."
    saint_paul_miki[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Gaudent in cælis} (AM 653)."

    saint_jerome_emilien_date = datetime.date(current_year, 2, 8)
    saint_jerome_emilien = dict_sancto[saint_jerome_emilien_date] = {}
    if not is_careme(saint_jerome_emilien_date):
        saint_jerome_emilien["force"] = 20
        saint_jerome_emilien[
            "header"] = " - S. Hieronymi Emiliani - \\textit{memoria minor} - \\textit{Vir.}"
        saint_jerome_emilien["body"] = "\n\\item ad Benedictus: ø \\textit{O viri misericordiæ} in tono 1 d (AM 973) ; oratio in supplemento 96.\n\\item \\textit{in ML (Alb.): olim die 20 iulii.}\n\\item in MC \\textit{(Alb.)}: Commune sanctorum et sanctarum (MR 965)."

    sainte_scholastique_date = datetime.date(current_year, 2, 10)
    sainte_scholastique = dict_sancto[sainte_scholastique_date] = {}
    sainte_scholastique["force"] = 70
    sainte_scholastique[
        "anniv"] = "Cras recurrit anniversarium publicæ renovationis votorum nostrorum (1988)."
    sainte_scholastique["header"] = " - \\textsc{\\textbf{S. Scholasticæ, virginis}, sororis SPN Benedicti} - \\textbf{festum} - \\textit{Alb.}"
    sainte_scholastique["body"] = "\n\\item ad Vigilias: Officium schema I (breviarium 62).\n\\item \\textit{in ML: Missa propria in supplemento OSB ; sequentia ; non dicitur \\emph{Credo}.}\n\\item in MC: omnia in MP ; lectiones propriæ: Cant \\textbf{8}, 6-7 / Lc \\textbf{10}, 38-42 ; præfatio de sanctis virginibus et religiosis."
    sainte_scholastique[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Exsultet} (AM 814)." if not even_year else ""

    nd_lourdes_date = datetime.date(current_year, 2, 11)
    nd_lourdes = dict_sancto[nd_lourdes_date] = {}
    if is_careme(nd_lourdes_date):
        nd_lourdes["force"] = 10
        nd_lourdes[
            "body"] = "\n\\item ad Laudes: pro commemoratione Beatæ Mariæ Virginis de Lourdes ø \\textit{Præclara} cum suo ß in variationibus 39 ; oratio in variationibus 38.\n\\item in MC: collecta in MP."
    else:
        nd_lourdes["force"] = 40
        nd_lourdes["header"] = " - \\textsc{Beatæ Mariæ Virginis de Lourdes} - \\textbf{\\textit{memoria maior}} - \\textit{Alb.}"
        nd_lourdes[
            "body"] = "\n\\item in Officio: oratio in supplemento 98 vel in variationibus 38.\n\\item ad Vigilias: in supplemento 96 ; invitatorium in supplemento 58.\n\\item ad Benedictus: ø \\textit{Præclara} in variationibus 39.\n\\item in MC: omnia in MP ; præfatio I de Beata Maria Virgine (\\textit{Et te in Conceptione immaculata})."
    nd_lourdes["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Ave Maria} (AM 862), ß \\textit{Immaculata} in variationibus 39."

    saint_benoit_aniane_date = datetime.date(current_year, 2, 12)
    saint_benoit_aniane = dict_sancto[saint_benoit_aniane_date] = {}
    if is_careme(saint_benoit_aniane_date):
        saint_benoit_aniane["force"] = 10
        saint_benoit_aniane[
            "body"] = "\n\\item ad Laudes: pro commemoratione S. Benedicti Anianensis ø \\textit{Serve bone} (AM 673) ; oratio in supplemento 99.\n\\item in MC: collecta in MP."
    else:
        saint_benoit_aniane["force"] = 40
        saint_benoit_aniane["header"] = " - \\textsc{S. Benedicti Anianensis}, abbatis - \\textbf{\\textit{memoria maior}} - \\textit{Alb.}"
        saint_benoit_aniane[
            "body"] = "\n\\item in Officio: oratio in supplemento 99.\n\\item ad Vigilias: lectio de memoria in supplemento 98.\n\\item \\textit{in ML: Missa pro abbate.}\n\\item in MC: collecta in MP ; Commune sanctorum et sanctarum (MR 958) ; præfatio de sanctis pastoribus."

    saints_cyrille_methode_date = datetime.date(current_year, 2, 14)
    saints_cyrille_methode = dict_sancto[saints_cyrille_methode_date] = {}
    saints_cyrille_methode["force"] = 70
    saints_cyrille_methode[
        "header"] = " - \\textsc{\\textbf{Ss. Cyrilli, monachi, et Methodii, episcopi}, Europæ patronorum} - \\textbf{festum} - \\textit{Alb.} (olim die 7 iulii)."
    var_vesperas = ", Vesperas" if saints_cyrille_methode_date.weekday() != 5 else ""
    saints_cyrille_methode[
        "body"] = "\n\\item ad Vigilias: de Communi confessoris pontificis, præter lectiones et orationem in supplemento 99.\n\\item ad Laudes" + var_vesperas + " et Horas minores: ut in variationibus 25 et sequentibus.\n\\item \\textit{in ML: præfatio de sanctis.}\n\\item in MC: lectiones propriæ: Act \\textbf{13}, 46-49 / Lc \\textbf{10}, 1-9 ; præfatio I de sanctis."

    sept_saints_fondateurs_date = datetime.date(current_year, 2, 17)
    sept_saints_fondateurs = dict_sancto[sept_saints_fondateurs_date] = {}
    if not is_careme(sept_saints_fondateurs_date):
        sept_saints_fondateurs["force"] = 20
        sept_saints_fondateurs[
            "header"] = " - Ss. Septem Fundatorum Ordinis Servorum Beatæ Mariæ Virginis - \\textit{memoria minor} - \\textit{Vir.} (olim die 12 februarii)."
        sept_saints_fondateurs[
            "body"] = "\n\\item Ad Benedictus: ø \\textit{Ecce quam} in tono VIII g (AM 821), ß \\textit{Hi viri}; oratio in supplemento 103.\n\\item \\textit{in ML: Alb.}\n\\item in MC (Alb.): Commune sanctorum et sanctarum (MR 961)."

    sainte_bernadette_date = datetime.date(current_year, 2, 18)
    sainte_bernadette = dict_sancto[sainte_bernadette_date] = {}
    sainte_bernadette["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus Reverendissimi Patris Irenæi HENRIOT, abbatis Dominæ Nostræ Septem Fontium, qui die 18 februarii 2020 obdormivit in Domino."

    if is_careme(sainte_bernadette_date):
        sainte_bernadette["force"] = 10
        sainte_bernadette[
            "body"] = "\n\\item ad Laudes: pro commemoratione S. Mariæ Bernardæ Soubirous ø \\textit{Candor} cum suo ß in variationibus 39 ; oratio in variationibus 40.\n\\item in MC: collecta in MP."
    else:
        sainte_bernadette["force"] = 20
        sainte_bernadette[
            "header"] = " - S. Mariæ Bernardæ Soubirous, virginis - \\textit{memoria minor} - \\textit{Vir.} "
        sainte_bernadette[
            "body"] = "\n\\item ad Benedictus: ø \\textit{Candor} cum suo ß in variationibus 39 ; oratio in variationibus 40.\n\\item \\textit{in ML (Alb.): Missa pro virgine.}\n\\item in MC \\textit{(Alb.)}: collecta in MP ; Commune virginum (MR 947)."

    saint_pierre_damien_date = datetime.date(current_year, 2, 21)
    saint_pierre_damien = dict_sancto[saint_pierre_damien_date] = {}
    if is_careme(saint_pierre_damien_date):
        saint_pierre_damien["force"] = 10
        saint_pierre_damien[
            "body"] = "\n\\item ad Laudes: pro commemoratione S. Petri Damiani ø \\textit{Euge} (AM 661) ; oratio: olim die 23 huius.\n\\item in MC: collecta de sancto."
    else:
        saint_pierre_damien["force"] = 40
        saint_pierre_damien[
            "header"] = " - \\textsc{S. Petri Damiani}, episcopi et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.} (olim die 23 huius)."
        saint_pierre_damien[
            "body"] = "\n\\item ad Vigilias: lectio in supplemento 104.\n\\item in MC: Commune doctorum Ecclesiæ (MR 944) ; præfatio de sanctis pastoribus."

    chaire_saint_pierre_date = datetime.date(current_year, 2, 22)
    chaire_saint_pierre = dict_sancto[chaire_saint_pierre_date] = {}
    chaire_saint_pierre["force"] = 70
    chaire_saint_pierre[
        "anniv"] = "Cras recurrit anniversarium fundationis Monasterii nostri (1972)."
    chaire_saint_pierre["header"] = " - \\textbf{\\textsc{Cathedræ S. Petri, apostoli}} - \\textbf{festum} - \\textit{Alb.}"
    chaire_saint_pierre[
        "body"] = "\n\\item ad Vigilias pro breviario 62: in supplemento 105 ; invitatorium proprium.\n\\item in MC: lectiones propriæ: 1 Pe \\textbf{5}, 1-4 / Mt \\textbf{16}, 13-19 ; præfatio I de Apostolis."
    chaire_saint_pierre[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Tu es pastor} (AM 823)."

    saint_polycarpe_date = datetime.date(current_year, 2, 23)
    saint_polycarpe = dict_sancto[saint_polycarpe_date] = {}
    if is_careme(saint_polycarpe_date):
        saint_polycarpe["force"] = 10
        saint_polycarpe[
            "body"] = "\n\\item ad Laudes: pro commemoratione S. Polycarpi ø \\textit{Qui odit} (AM 642) ; oratio : olim die 26 ianuarii vel in supplemento 110.\n\\item in MC: collecta de sancto."
    else:
        saint_polycarpe["force"] = 40
        saint_polycarpe[
            "header"] = " - \\textsc{S. Polycarpi}, episcopi et martyris - \\textbf{memoria maior} - \\textit{Rub.} (olim die 26 ianuarii)."
        saint_polycarpe[
            "body"] = "\n\\item ad Vigilias: lectio in supplemento 109.\n\\item in MC: Commune martyrum (MR 915) ; præfatio de sanctis martyribus."

    # MARS:

    anniv_premier_mars_date = datetime.date(current_year, 3, 1)
    anniv_premier_mars = dict_sancto[anniv_premier_mars_date] = {}
    anniv_premier_mars[
        "anniv"] = "Cras recurrit anniversarium fundationis Monasterii Dominæ Nostræ Mayliliensis (1946) ; anniversarium benedictionis Ecclesiæ Sanctissimi Cordis Iesu (1979) ; \\textup{†} anniversarium obitus RP Ludovici Mariæ \\textsc{Barrielle}, benefactoris (1983) ; \\textup{†} anniversarium obitus Eminentissimi Cardinalis Ioannis \\textsc{Balland}, benefactoris (1998)."

    saintes_perpetue_felicitee_date = datetime.date(current_year, 3, 7)
    saintes_perpetue_felicitee = dict_sancto[saintes_perpetue_felicitee_date] = {
    }
    if is_careme(saintes_perpetue_felicitee_date):
        saintes_perpetue_felicitee["force"] = 10
        saintes_perpetue_felicitee[
            "body"] = "\n\\item ad Laudes: pro commemoratione Ss. Perpetuæ et Felicitatis, ø \\textit{Istarum} (AM 748) ; oratio vide ad diem 6 martii.\n\\item in MC: collecta de sanctis."
    else:
        saintes_perpetue_felicitee["force"] = 40
        saintes_perpetue_felicitee[
            "header"] = " - \\textsc{Ss. Perpetuæ et Felicitatis}, martyrum - \\textbf{memoria maior} - \\textit{Rub.} (olim die 6 martii)."
        saintes_perpetue_felicitee[
            "body"] = "\n\\item ad Vigilias pro breviario veteri: lectio in supplemento 111.\n\\item ad Benedictus et Magnificat: ø \\textit{Istarum} (AM 691).\n\\item in MC: Commune martyrum (MR 909) ; præfatio de sanctis martyribus."

    saint_jean_de_dieu_date = datetime.date(current_year, 3, 8)
    saint_jean_de_dieu = dict_sancto[saint_jean_de_dieu_date] = {}
    if not is_careme(saint_jean_de_dieu_date):
        saint_jean_de_dieu["force"] = 20
        saint_jean_de_dieu[
            "header"] = " - S. Ioannis a Deo, religiosi - \\textit{memoria minor} - \\textit{Vir.}"
        saint_jean_de_dieu[
            "body"] = "\n\\item ad Benedictus: ø \\textit{Sanctorum} in tono VIII g (AM 829) ; oratio in supplemento 112.\n\\item in MC: Commune sanctorum et sanctarum (MR 961)."

    sainte_francoise_romaine_date = datetime.date(current_year, 3, 9)
    sainte_francoise_romaine = dict_sancto[sainte_francoise_romaine_date] = {}
    if is_careme(sainte_francoise_romaine_date):
        sainte_francoise_romaine["force"] = 10
        sainte_francoise_romaine[
            "body"] = "\n\\item ad Laudes: pro commemoratione S. Franciscæ Romanæ, ø \\textit{Simile est} (AM 685).\n\\item in MC: collecta de sancta."
    else:
        sainte_francoise_romaine["force"] = 40
        sainte_francoise_romaine["header"] = " - \\textsc{S. Franciscæ Romanæ}, religiosæ - \\textbf{memoria maior} - \\textit{Alb.}"
        sainte_francoise_romaine[
            "body"] = "\n\\item ad Vigilias: lectio in supplemento 112.\n\\item ad Benedictus: ø \\textit{Simile est} (AM 685).\n\\item in MC: Commune sanctorum et sanctarum (MR 962) ; præfatio de sanctis virginibus et religiosis."

    saint_patrick_date = datetime.date(current_year, 3, 17)
    saint_patrick = dict_sancto[saint_patrick_date] = {}
    saint_patrick["force"] = 10
    saint_patrick[
        "body"] = "\n\\item ad Laudes: pro commemoratione S. Patricii, ø \\textit{Euntes in mundum} sine \\textit{Alleluia} (AM 484*) ; oratio in supplemento 113.\n\\item in MC: collecta de sancto."

    saint_cyrille_jerusalem_date = datetime.date(current_year, 3, 18)
    saint_cyrille_jerusalem = dict_sancto[saint_cyrille_jerusalem_date] = {}
    saint_cyrille_jerusalem["force"] = 10
    saint_cyrille_jerusalem[
        "body"] = "\n\\item ad Laudes: pro commemoratione S. Cyrilli Hierosolymitani, ø \\textit{Amavit} (AM 663).\n\\item in MC: collecta de sancto."

    saint_joseph_date = datetime.date(current_year, 3, 19)
    if is_near_paques(saint_joseph_date):
        saint_joseph_date = paques - datetime.timedelta(days=8)
    elif saint_joseph_date.weekday() == 6:
        saint_joseph_date = saint_joseph_date + datetime.timedelta(days=1)
    saint_joseph = dict_sancto[saint_joseph_date] = {}
    saint_joseph["force"] = 110
    saint_joseph["I_vesp"] = "\\item I Vesperæ sollemnitatis sequentis."
    saint_joseph["header"] = " - ¬ \\MakeUppercase{\\textbf{S. Ioseph, sponsi Beatæ Mariæ Virginis}}, \\textsc{Ecclesiæ universæ et huius monasterii patroni} - \\textbf{sollemnitas maior} - \\textit{Alb.}"
    evg_mc = "Lc \\textbf{2}, 41-51a" if even_year else "Mt \\textbf{1}, 16.18-21.24a"
    saint_joseph["body"] = "\n\\item in MC: lectiones propriæ: 2 Sam \\textbf{7}, 4-5a.12-14a.16 / Rom \\textbf{4}, 13.16-18.22 / " + \
        evg_mc + " ; præfatio propria (\\textit{Et te in sollemnitate})."
    saint_joseph["II_vesp"] = "\n\\item Vesperæ sollemnitatis ; benedictio Sanctissimi Sacramenti."
    # Si vendredi de carême, reporter le jeûne au lendemain:
    if saint_joseph_date.weekday() == 4 and saint_joseph_date < paques:
        dict_tempo[saint_joseph_date]["symbols"] = dict_tempo[saint_joseph_date]["symbols"].replace(
            " µ", " ł")
        dict_tempo[saint_joseph_date + datetime.timedelta(
            days=1)]["symbols"] = " µ" + dict_tempo[saint_joseph_date + datetime.timedelta(days=1)]["symbols"]

    saint_benoit_transitus_date = datetime.date(current_year, 3, 21)
    saint_benoit_transitus = dict_sancto[saint_benoit_transitus_date] = {}
    saint_benoit_transitus["force"] = 70
    saint_benoit_transitus["header"] = " - \\textsc{\\textbf{Transitus S.P.N. Benedicti}, abbatis} - \\textbf{festum} - \\textit{Alb.}"
    # Si 19/03 et 21/03 appartiennent à la même semaine, on inverse la semaine du psautier pour les Vigiles:
    inv_sem_vigiles = "\n\\item ad Vigilias: antiphonæ et psalmi hebdomadæ " + hebdo_psalterii_inv[(
        (saint_benoit_transitus_date - datetime.date(2011, 11, 27)).days // 7) % 2] + "." if saint_joseph_date.weekday() <= 4 else ""
    saint_benoit_transitus["body"] = "\n\\item \\textit{hodie in Ecclesiis ordinis nostri, indulgentia plenaria acquiri una potest pia ecclesiæ visitatione, in qua recitatur oratio dominica et fidei symbolum.}" + inv_sem_vigiles + \
        "\n\\item \\textit{in ML: Missa et præfatio propria in supplemento OSB ; sequentia ; non dicitur \\emph{Credo}.}\n\\item in MC: omnia in MP ; lectiones propriæ: Gen \\textbf{12}, 1-4a / Io \\textbf{17}, 20-26 ; præfatio propria."
    saint_benoit_transitus[
        "II_vesp"] = "\n\\item ad Vesperas: ¶ breve, tono simplici (AM 961)."
    # Si vendredi de carême, reporter le jeûne au lendemain:
    if saint_benoit_transitus_date.weekday() == 4 and saint_benoit_transitus_date < paques:
        dict_tempo[saint_benoit_transitus_date]["symbols"] = dict_tempo[saint_benoit_transitus_date]["symbols"].replace(
            " µ", " ł")
        dict_tempo[saint_benoit_transitus_date + datetime.timedelta(
            days=1)]["symbols"] = " µ" + dict_tempo[saint_benoit_transitus_date + datetime.timedelta(days=1)]["symbols"]

    annonciation_date = datetime.date(current_year, 3, 25)
    if is_near_paques(annonciation_date):
        annonciation_date = paques + datetime.timedelta(days=8)
    elif annonciation_date.weekday() == 6:
        annonciation_date = annonciation_date + datetime.timedelta(days=1)
    annonciation = dict_sancto[annonciation_date] = {}
    annonciation["force"] = 110
    annonciation["I_vesp"] = "\\item I Vesperæ sollemnitatis sequentis."
    annonciation["header"] = " - þ \\textbf{\\MakeUppercase{In annuntiatione Domini}} - \\textbf{sollemnitas minor} - \\textit{Alb.}"
    annonciation["body"] = "\n\\item in MC: lectiones propriæ: Is \\textbf{7}, 10-14 ; \\textbf{8}, 10 / Hebr \\textbf{10}, 4-10 / Lc \\textbf{1}, 26-38 ; ad verba symboli \\textit{Et incarnatus est} omnes genua ﬂectunt ; præfatio propria."
    annonciation["II_vesp"] = "\n\\item Vesperæ sollemnitatis ; benedictio Sanctissimi Sacramenti."
    # Si vendredi de carême, reporter le jeûne au lendemain:
    if annonciation_date.weekday() == 4 and annonciation_date < paques:
        dict_tempo[annonciation_date]["symbols"] = dict_tempo[annonciation_date]["symbols"].replace(
            " µ", " ł")
        dict_tempo[annonciation_date + datetime.timedelta(
            days=1)]["symbols"] = " µ" + dict_tempo[annonciation_date + datetime.timedelta(days=1)]["symbols"]

    anniv_pere_emm_andre_date = datetime.date(current_year, 3, 31)
    anniv_pere_emm_andre = dict_sancto[anniv_pere_emm_andre_date] = {}
    anniv_pere_emm_andre["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus Reverendissimi ac dilectissimi Patris Emmanuel Mariæ \\textsc{André}, abbatis Dominæ Nostræ Sanctæ Spei Mesnili, qui die 31 martii 1903 obdormivit in Domino."

    # AVRIL:

    anniv_pere_ducruet_date = datetime.date(current_year, 4, 5)
    anniv_pere_ducruet = dict_sancto[anniv_pere_ducruet_date] = {}
    anniv_pere_ducruet["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus Reverendissimi Patris Bernardi DUCRUET, abbatis Sancti Benedicti Floriacensis, qui die 5 aprilis 2020 obdormivit in Domino."

    saint_jb_de_la_salle_date = datetime.date(current_year, 4, 7)
    saint_jb_de_la_salle = dict_sancto[saint_jb_de_la_salle_date] = {}
    if is_careme(saint_jb_de_la_salle_date):
        saint_jb_de_la_salle["force"] = 10
        saint_jb_de_la_salle[
            "body"] = "\n\\item ad Laudes: pro commemoratione S. Ioannis Baptistæ de la Salle, ø \\textit{Amen dico vobis} (AM 974) ; oratio in supplemento 115.\n\\item in MC: collecta de sancto."
    else:
        saint_jb_de_la_salle["force"] = 40
        saint_jb_de_la_salle[
            "header"] = " - \\textsc{S. Ioannis Baptistæ de la Salle}, presbyteri - \\textbf{memoria maior} - \\textit{Alb.} (olim die 15 maii)."
        saint_jb_de_la_salle[
            "body"] = "\n\\item ad Vigilias: lectio, ¶ et oratio in supplemento 114.\n\\item ad Benedictus: ø \\textit{Observa fili} cum \\textit{alleluia} (AM 582).\n\\item in MC: Commune sanctorum et sanctarum (MR 965) ; præfatio de sanctis virginibus et religiosis."
        saint_jb_de_la_salle[
            "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{O viri misericordiæ} cum \\textit{alleluia} in tono I f (AM 973)."

    saint_stanislas_ep_date = datetime.date(current_year, 4, 11)
    if not is_careme(saint_stanislas_ep_date):
        saint_stanislas_ep = dict_sancto[saint_stanislas_ep_date] = {}
        saint_stanislas_ep["force"] = 20
        saint_stanislas_ep[
            "header"] = " - S. Stanislai, episcopi et martyris - \\textit{memoria minor} - \\textit{Alb.} (olim die 7 maii)."
        saint_stanislas_ep["body"] = "\n\\item ad Benedictus: ø \\textit{Lux perpetua} (AM 632) ; oratio in supplemento 115.\n\\item \\textit{in ML: Rub.}\n\\item in MC \\textit{(Rub.)}: Commune martyrum (MR 921)."

    saint_martin_Ier_date = datetime.date(current_year, 4, 13)
    if not is_careme(saint_martin_Ier_date):
        saint_martin_Ier = dict_sancto[saint_martin_Ier_date] = {}
        saint_martin_Ier["force"] = 20
        saint_martin_Ier[
            "header"] = " - S. Martini I, papæ et martyris - \\textit{memoria minor} - \\textit{Alb.} (olim die 12 novembris)."
        ant_bened = "\\item ad Benedictus: ø \\textit{Fulgebunt iusti} (AM 633) ; oratio in supplemento 115" if saint_martin_Ier_date > paques else "\\item ad Benedictus: ø \\textit{Qui odit} (AM 642) ; oratio in supplemento 115."
        saint_martin_Ier["body"] = ant_bened + \
            "\\item \\textit{in ML: Rub.}\n\\item in MC \\textit{(Rub.)}: Commune pastorum (MR 927)."

    anniv_pere_debroc_date = datetime.date(current_year, 4, 16)
    anniv_pere_debroc = dict_sancto[anniv_pere_debroc_date] = {}
    anniv_pere_debroc["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus RP Hervæus de BROC, sacerdotis, qui die 16 aprilis 2020, in abbatia Sancti Petri Solesmensis, obdormivit in Domino."

    saint_anselme_date = datetime.date(current_year, 4, 21)
    saint_anselme = dict_sancto[saint_anselme_date] = {}
    saint_anselme["force"] = 40
    saint_anselme["header"] = " - \\textsc{S. Anselmi}, episcopi et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_anselme["body"] = "\n\\item in Officio: oratio \\textit{Ecclesiam tuam}.\n\\item ad Vigilias: officii schema II (pro breviario 62) ; lectio contracta (pro breviario veteri).\n\\item ad Benedictus: ø propria.\n\\item \\textit{in ML: Missa in supplemento OSB.}\n\\item in MC: Commune doctorum Ecclesiæ (MR 943) ; præfatio de sanctis pastoribus."
    saint_anselme["II_vesp"] = "\n\\item ad Vesperas: hymnus proprius."

    saint_marc_date = datetime.date(current_year, 4, 25)
    saint_marc = dict_sancto[saint_marc_date] = {}
    saint_marc["force"] = 70
    saint_marc["header"] = " - \\textbf{\\textsc{S. Marci, evangelistæ}} - \\textbf{festum} - \\textit{Rub.}"
    saint_marc["body"] = "\n\\item in MC: lectiones propriæ: 1 Pe \\textbf{5}, 5b-14 / Mc \\textbf{16}, 15-20 ; præfatio II de Apostolis."

    dedicace_dijon_date = datetime.date(current_year, 4, 27)
    dedicace_dijon = dict_sancto[dedicace_dijon_date] = {}
    dedicace_dijon["force"] = 70
    dedicace_dijon["header"] = " - \\textbf{\\textsc{In Dedicatione Ecclesiæ Cathedralis Divionensis}} - \\textbf{festum} - \\textit{Alb.}"
    dedicace_dijon[
        "body"] = "\n\\item Omnia de Communi dedicationis ecclesiæ ritu paschali: in fine cuiuslibet responsorii, ante versum, additur \\textit{Alleluia} nisi iam habeatur.\n\\item \\textit{in ML: præfatio de dedicatione ecclesiæ \\emph{(Gloria, Credo)}.}\n\\item in MC: Missa de Communi dedicationis ecclesiæ (MR 895) ; lectiones propriæ: Apoc \\textbf{21}, 1-5a / Io \\textbf{2}, 13-22 ; præfatio de dedicatione ecclesiæ II."

    saint_louis_marie_date = datetime.date(current_year, 4, 28)
    saint_louis_marie = dict_sancto[saint_louis_marie_date] = {}
    saint_louis_marie["force"] = 20
    saint_louis_marie[
        "header"] = " - S. Ludovici Mariæ Grignion de Montfort, presbyteri - \\textit{memoria minor} - \\textit{Alb.} "
    saint_louis_marie["body"] = "\n\\item ad Benedictus: ø \\textit{Cum vidisset} cum \\textit{alleluia} (AM 867) ; oratio in supplemento 116*.\n\\item \\textit{in ML (Alb.): Missa in PAL.}\n\\item in MC \\textit{(Alb.)}: collecta propria  ; Commune pastorum (MR 933)."

    sainte_catherine_sienne_date = datetime.date(current_year, 4, 29)
    sainte_catherine_sienne = dict_sancto[sainte_catherine_sienne_date] = {}
    sainte_catherine_sienne["force"] = 70
    sainte_catherine_sienne[
        "header"] = " - \\textbf{\\textsc{S. Catharinæ Senensis, Europæ Patronæ, virginis et Ecclesiæ doctoris}} - \\textbf{festum} - \\textit{Alb.} (olim die 30 huius)."
    sainte_catherine_sienne[
        "body"] = "\n\\item in Officio: omnia de Communi virginis, præter sequentia.\n\\item oratio in supplemento 118*.\n\\item ad Vigilias: lectiones II nocturni in supplemento 117*.\n\\item ad Benedictus: ø \\textit{O beata anima} cum \\textit{alleluia} (AM 1131).\n\\item \\textit{in ML: præfatio de sanctis.}\n\\item in MC: lectiones propriæ: 1 Io \\textbf{1}, 5 – \\textbf{2}, 2 / Mt \\textbf{11}, 25-30 ; præfatio de sanctis virginibus et religiosis."
    sainte_catherine_sienne[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{O dignissima} cum \\textit{alleluia} (AM 1133)."

    saint_pie_V_date = datetime.date(current_year, 4, 30)
    saint_pie_V = dict_sancto[saint_pie_V_date] = {}
    saint_pie_V["force"] = 20
    saint_pie_V[
        "header"] = " - S. Pii V, Papæ - \\textit{memoria minor} - \\textit{Alb.} (olim die 5 maii)."
    saint_pie_V["body"] = "\n\\item ad Benedictus: ø \\textit{Dum esset} (AM 663).\n\\item in MC: Commune pastorum (MR 927)."

    # MAI:

    saint_joseph_artisan_date = datetime.date(current_year, 5, 1)
    saint_joseph_artisan = dict_sancto[saint_joseph_artisan_date] = {}
    saint_joseph_artisan["force"] = 40
    saint_joseph_artisan["header"] = " - \\textsc{S. Ioseph Opificis} - \\textbf{memoria maior} - \\textit{Alb.}"
    lect_mc = " Col \\textbf{3}, 14-15.17.23-24" if even_year else " Gen \\textbf{1}, 26–\\textbf{2}, 3"
    var_vesperas = ", Vesperas" if saint_joseph_artisan_date.weekday() != 5 else ""
    saint_joseph_artisan["body"] = "\n\\item in Officio: oratio \\textit{Rerum conditor} in supplemento 118* vel in breviario 62 (Officium schema I).\n\\item ad Vigilias: Officium schema I, præter sequentia: antiphonæ, psalmi et ß de feria ; lectio in supplemento 118 ; in II nocturno lectio brevis et ß ut ad Sextam (in breviario 62: Officium schema I).\n\\item ad Laudes" + var_vesperas + " et Horas minores: omnia ut in AM 886, præter orationem ut supra.\n\\item in MC: lectiones propriæ:" + \
        lect_mc + \
        "/ Mt \\textbf{13}, 54-58 ; præfatio propria \\textit{(Et te in commemoratione)}."

    saint_athanase_date = datetime.date(current_year, 5, 2)
    saint_athanase = dict_sancto[saint_athanase_date] = {}
    saint_athanase["force"] = 40
    saint_athanase["header"] = " - \\textsc{S. Athanasii}, episcopi et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_athanase[
        "body"] = "\n\\item ad Benedictus: ø \\textit{Unus est} cum \\textit{alleluia} (AM 356).\n\\item in MC: præfatio de sanctis pastoribus."
    #saint_athanase["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Quid vobis videtur} (AM 609)."

    sts_philippe_jacques_date = datetime.date(current_year, 5, 3)
    sts_philippe_jacques = dict_sancto[sts_philippe_jacques_date] = {}
    sts_philippe_jacques["force"] = 70
    sts_philippe_jacques[
        "header"] = " - \\textbf{\\textsc{Ss. Philippi et Iacobi, apostolorum}} - \\textbf{festum} - \\textit{Rub.} (olim die 1 maii [AM] et 11 maii [ML])."
    sts_philippe_jacques[
        "body"] = "\n\\item in MC: lectiones propriæ: 1 Co \\textbf{15}, 1-8 / Io \\textbf{14}, 6-14 ; præfatio I de Apostolis."
    sts_philippe_jacques[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Non turbetur} (AM 892)." if not even_year else ""

    abbes_cluny_date = datetime.date(current_year, 5, 11)
    # TODO: octave Pentecôte
    abbes_cluny = dict_sancto[abbes_cluny_date] = {}
    abbes_cluny["force"] = 40
    abbes_cluny[
        "header"] = " - \\textsc{Ss. Odonis, Maioli, Odilonis, Hugonis et B. Petri Venerabilis}, abbatum Cluniacensium - \\textbf{memoria maior} - \\textit{Alb.} (olim die 29 aprilis)."
    abbes_cluny[
        "body"] = "\n\\item ad Vigilias: ut in breviario, die 29 aprilis ; invitatorium proprium.\n\\item ad Laudes et Horas minores: omnia ut in AM 877.\n\\item ad Benedictus: ø \\textit{O viri misericordiæ} cum \\textit{alleluia} in tono I g (AM 973).\n\\item \\textit{in ML: Missa in supplemento OSB.}\n\\item in MC: collecta in MP ; Commune sanctorum et sanctarum (MR 954) ; lectiones propriæ: Apoc \\textbf{19}, 1. 5-9a / Io \\textbf{15}, 9-17 ; præfatio de sanctis virginibus et religiosis."
    abbes_cluny[
        "II_vesp"] = "\n\\item ad Vesperas: omnia ut hucusque in I Vesperis (AM 874)."

    nd_fatima_date = datetime.date(current_year, 5, 13)
    # TODO: octave Pentecôte
    nd_fatima = dict_sancto[nd_fatima_date] = {}
    nd_fatima["force"] = 20
    if nd_fatima_date < paques + datetime.timedelta(days=49):
        couleur = "\\textit{Alb.}"
        messe_lue = "\\item \\textit{in ML: Missa de die 11 februarii.}"
        messe_conv = "\\item in MC: Commune Beatæ Mariæ Virginis (MR 908) ; præfatio I de Beata Maria Virgine."
    else:
        couleur = "\\textit{Vir.}"
        messe_lue = "\\item \\textit{in ML (Alb): Missa de die 11 februarii.}"
        messe_conv = "\\item in MC \\textit{(Alb.)}: Commune Beatæ Mariæ Virginis (MR 903) ; præfatio I de Beata Maria Virgine."
    nd_fatima["header"] = " - Beatæ Mariæ Virginis de Fatima - \\textit{memoria minor} - " + couleur
    nd_fatima["body"] = "\n\\item ad Benedictus: ø \\textit{Ait Dominus} (AM 765) ; oratio in supplemento 118*." + \
        messe_lue + messe_conv

    saint_matthias_date = datetime.date(current_year, 5, 14)
    # TODO: octave Pentecôte
    saint_matthias = dict_sancto[saint_matthias_date] = {}
    saint_matthias["force"] = 70
    saint_matthias[
        "header"] = " - \\textbf{\\textsc{S. Matthiæ, apostoli}} - \\textbf{festum} - \\textit{Rub.} (olim die 24 februarii)."
    if saint_matthias_date < paques + datetime.timedelta(days=49):
        office = "\\item in Officio: omnia ut in Communi Apostolorum tempore paschali præter lectiones trium nocturnorum ad Vigilias in breviario cum responsoriis tamen tempore paschali."
        messe_lue = "\\item \\textit{in ML : Missa \\emph{Protexisti} (Commune martyrum tempore paschali), cum orationibus et lectionibus e die 24 februarii.}"
    else:
        office = ""
        messe_lue = ""
    saint_matthias["body"] = office + messe_lue + \
        "\\item in MC: lectiones propriæ: Ac \\textbf{1}, 15-17.20a.20c-26 / Io \\textbf{15}, 9-17 ; præfatio II de Apostolis."

    saint_pacome_date = datetime.date(current_year, 5, 15)
    # TODO: octave Pentecôte
    saint_pacome = dict_sancto[saint_pacome_date] = {}
    saint_pacome["force"] = 40
    saint_pacome["header"] = " - \\textsc{S. Pacomii}, abbatis - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_pacome[
        "body"] = "\n\\item in Officio: oratio in supplemento 120 vel in variationibus 21.\n\\item ad Vigilias: lectio in supplemento 119.\n\\item \\textit{in ML: Missa pro abbate.}\n\\item in MC: collecta in MP ; Commune sanctorum et sanctarum (MR 958) ; præfatio I de sanctis."

    saint_jean_Ier_date = datetime.date(current_year, 5, 18)
    # TODO: octave Pentecôte
    saint_jean_Ier = dict_sancto[saint_jean_Ier_date] = {}
    saint_jean_Ier["force"] = 20
    if saint_jean_Ier_date < paques + datetime.timedelta(days=49):
        couleur = "\\textit{Alb.}"
        ant_bened = "\\item ad Benedictus: ø \\textit{Lux perpetua} (AM 632) ; oratio in supplemento 120."
    else:
        couleur = "\\textit{Vir.}"
        ant_bened = "\\item ad Benedictus: ø \\textit{Iste Sanctus} (AM 639) ; oratio in supplemento 120."
    saint_jean_Ier["header"] = " - S. Ioannis I, papæ et martyris - \\textit{memoria minor} - " + couleur
    saint_jean_Ier["body"] = ant_bened + \
        "\\item \\textit{in ML (Rub.): Missa de Communi summorum pontificum.}\n\\item in MC \\textit{(Rub.)}: Commune pastorum (MR 927)."

    saint_pierre_celestin_date = datetime.date(current_year, 5, 19)
    # TODO: octave Pentecôte
    saint_pierre_celestin = dict_sancto[saint_pierre_celestin_date] = {}
    saint_pierre_celestin["force"] = 20
    if saint_pierre_celestin_date < paques + datetime.timedelta(days=49):
        couleur = "\\textit{Alb.}"
        messe_lue = ""
        messe_conv = "\\item in MC: collecta in MP ; Commune pastorum (MR 928)."
    else:
        couleur = "\\textit{Vir.}"
        messe_lue = "\\item \\textit{in ML: Alb.}"
        messe_conv = "\\item in MC \\textit{(Alb.)}: collecta in MP ; Commune pastorum (MR 928)."
    saint_pierre_celestin[
        "header"] = " - S. Petri Celestini, papæ et eremitæ - \\textit{memoria minor} - " + couleur
    saint_pierre_celestin[
        "body"] = "\n\\item ad Benedictus: ø \\textit{Sacerdos et pontifex} (AM 656)." + messe_lue + messe_conv

    anniv_pere_bernard_date = datetime.date(current_year, 5, 21)
    anniv_pere_bernard = dict_sancto[anniv_pere_bernard_date] = {}
    anniv_pere_bernard["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus RP Bernardi Mariæ \\textsc{Dewilde}, religiosi, qui die 21 maii 2014 obdormivit in Domino."

    saint_bede_date = datetime.date(current_year, 5, 25)
    saint_bede = dict_sancto[saint_bede_date] = {}
    saint_bede["force"] = 40
    saint_bede[
        "header"] = " - \\textsc{S. Bedæ venerabilis}, presbyteri et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.} (olim die 27 huius)."
    alleluia_bened = " cum \\textit{alleluia}" if saint_bede_date < paques + \
        datetime.timedelta(days=49) else ""
    if is_oct_pent(saint_bede_date):
        repons_vigiles = "\n\\item ad Vigilias: post lectionem dicitur ¶ \\textit{In medio} sine Alleluia."
        if saint_bede_date.weekday() in [2, 4, 5]:
            messe_lue = "\n\\item \\textit{in ML (Rub): Quatuor Temporum Pentecostes} (Credo)."
        else:
            messe_lue = "\n\\item \\textit{in ML (Rub): Missa infra octavam} (Credo)."
    else:
        repons_vigiles = ""
        messe_lue = ""
    saint_bede["body"] = repons_vigiles + "\n\\item ad Benedictus: ø \\textit{Qui verbum}" + alleluia_bened + \
        " (AM 325).\n" + messe_lue + \
        "\n\\item in MC: Commune doctorum Ecclesiæ (MR 943) ; præfatio de sanctis virginibus et religiosis."

    saint_gregoire_VII_date = datetime.date(current_year, 5, 26)
    # TODO: octave Pentecôte
    saint_gregoire_VII = dict_sancto[saint_gregoire_VII_date] = {}
    saint_gregoire_VII["force"] = 20
    if saint_gregoire_VII_date < paques + datetime.timedelta(days=49):
        couleur = "\\textit{Alb.}"
        messe_lue = ""
        messe_conv = "\\item in MC: Commune pastorum (MR 927)."
    else:
        couleur = "\\textit{Vir.}"
        messe_lue = "\\item \\textit{in ML}: Alb."
        messe_conv = "\\item in MC \\textit{(Alb.)}: Commune pastorum (MR 927)."
    saint_gregoire_VII["header"] = " - S. Gregorii VII, papæ - \\textit{memoria minor} - \\textit{" + \
        couleur + "} (vide die 25 huius mensis)."
    saint_gregoire_VII["body"] = "\n\\item ad Benedictus: ø \\textit{Dum esset} (AM 663)." + \
        messe_lue + messe_conv

    saint_augustin_cantorbery_date = datetime.date(current_year, 5, 27)
    # TODO: octave Pentecôte
    saint_augustin_cantorbery = dict_sancto[saint_augustin_cantorbery_date] = {
    }
    saint_augustin_cantorbery["force"] = 20
    if saint_augustin_cantorbery_date < paques + datetime.timedelta(days=49):
        couleur = "\\textit{Alb.}"
        messe_lue = ""
        messe_conv = "\\item in MC: Commune pastorum (MR 938)."
    else:
        couleur = "\\textit{Vir.}"
        messe_lue = "\\item \\textit{in ML: Alb.}"
        messe_conv = "\\item in MC \\textit{(Alb.)}: Commune pastorum (MR 938)."
    saint_augustin_cantorbery["header"] = " - S. Augustini Cantuariensis, episcopi - \\textit{memoria minor} - \\textit{" + \
        couleur + "} (olim die 26 huius, vel 28 in ML)."
    saint_augustin_cantorbery[
        "body"] = "\n\\item ad Benedictus: ø \\textit{Amavit eum} (AM 663)." + messe_lue + messe_conv

    sainte_jeanne_arc_date = datetime.date(current_year, 5, 30)
    # TODO: octave Pentecôte
    sainte_jeanne_arc = dict_sancto[sainte_jeanne_arc_date] = {}
    sainte_jeanne_arc["force"] = 40
    sainte_jeanne_arc["header"] = " - \\textsc{S. Ioannæ d’Arc}, virginis, patronæ secundariæ Galliæ - \\textbf{memoria maior} - \\textit{Alb.}"
    if is_oct_pent(sainte_jeanne_arc_date):
        if sainte_jeanne_arc_date.weekday() in [2, 4, 5]:
            messe_lue = "\n\\item \\textit{in ML (Rub): Quatuor Temporum Pentecostes} (Credo)."
        else:
            messe_lue = "\n\\item \\textit{in ML (Rub): Missa infra octavam} (Credo)."
    else:
        messe_lue = "\n\\item \\textit{in ML: Missa in PAL ; præfatio de sanctis.}"
    lectures_mc = "1 Co \\textbf{1}, 26-31" if even_year else "Sap \\textbf{8}, 9-15"
    sainte_jeanne_arc[
        "body"] = "\n\\item in Officio: oratio in supplemento 122, vel in variationibus 45.\n\\item ad Vigilias: lectio in supplemento 121.\n\\item ad Benedictus: ø \\textit{Stans beata} in variationibus 44." + messe_lue + "\n\\item in MC: omnia in MP; lectiones propriæ: " + lectures_mc + " / Mt \\textbf{16}, 24-27 ; præfatio I de sanctis."
    sainte_jeanne_arc["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Hæc est} in variationibus 45."

    visitation_date = datetime.date(current_year, 5, 31)
    # TODO: octave Pentecôte
    visitation = dict_sancto[visitation_date] = {}
    visitation["force"] = 70
    visitation[
        "header"] = " - \\textbf{\\textsc{In Visitatione Beatæ Mariæ Virginis}} - \\textbf{festum} - \\textit{Alb.} (olim die 2 iulii)."
    suppl_vigiles = "\\item ad Vigilias: in supplemento 122 ; invitatorium proprium in supplemento 58. " if visitation_date < paques + \
        datetime.timedelta(days=56) else ""
    messe_lue = "\n\\item \\textit{in ML (Rub): Quatuor Temporum Pentecostes} (Credo)." if is_oct_pent(visitation_date) and visitation_date.weekday() in [2, 4, 5] else ""
    lectures_mc = "Rom \\textbf{12}, 9-16b" if even_year else "Soph \\textbf{3}, 14-18"
    visitation["body"] = suppl_vigiles + messe_lue + "\\item in MC: lectiones propriæ: " + \
        lectures_mc + \
        " / Lc \\textbf{1}, 39-56 ; præfatio II de Beata Maria Virgine."

    # JUIN:

    saint_justin_date = datetime.date(current_year, 6, 1)
    saint_justin = dict_sancto[saint_justin_date] = {}
    saint_justin["force"] = 40
    saint_justin[
        "header"] = " - \\textsc{S. Iustini}, martyris - \\textbf{memoria maior} - \\textit{Rub.} (olim die 14 aprilis)."
    if is_oct_pent(saint_justin_date):
        repons_vigiles = " Post lectionem dicitur ¶ \\textit{In medio} sine Alleluia."
        if saint_justin_date.weekday() in [2, 4, 5]:
            messe_lue = "\n\\item \\textit{in ML (Rub): Quatuor Temporum Pentecostes} (Credo)."
        else:
            messe_lue = "\n\\item \\textit{in ML (Rub): Missa infra octavam} (Credo)."
    else:
        repons_vigiles = ""
        messe_lue = ""
    saint_justin["body"] = "\n\\item in Officio: oratio in supplemento 130.\n\\item ad Vigilias: lectio in supplemento 130." + repons_vigiles + "\n\\item ad Benedictus: ø \\textit{Beati eritis" + (
        "} cum \\textit{alleluia" if saint_justin_date < paques + datetime.timedelta(days=49) else "") + "} (AM 1121)." + messe_lue + "\n\\item in MC: præfatio de sanctis martyribus."

    saint_pothin_date = datetime.date(current_year, 6, 2)
    saint_pothin = dict_sancto[saint_pothin_date] = {}
    saint_pothin["force"] = 20
    if saint_pothin_date < paques + datetime.timedelta(days=49):
        couleur = "\\textit{Alb.}"
        ant_bened = "\\item ad Benedictus: ø \\textit{Filiæ Jerusalem} (AM 636) ; oratio in supplemento 131."
        messe_lue = "\\item \\textit{in ML (Rub.): Missa pro pluribus martyribus tempore paschali.}"
        messe_conv = "(MR 918)"
    else:
        couleur = "\\textit{Vir.}"
        ant_bened = "\\item ad Benedictus: ø \\textit{Vestri capilli} (AM 650) ; oratio in supplemento 131."
        if is_oct_pent(saint_pothin_date):
            if saint_pothin_date.weekday() in [2, 4, 5]:
                messe_lue = "\n\\item \\textit{in ML (Rub): Quatuor Temporum Pentecostes} (Credo)."
            else:
                messe_lue = "\n\\item \\textit{in ML (Rub): Missa infra octavam} (Credo)."
        else:
            messe_lue = "\n\\item \\textit{in ML (Rub.): Missa pro pluribus martyribus extra tempus paschale.}"
        messe_conv = "(MR 909)"
    saint_pothin[
        "header"] = " - Ss. Pothini, episcopi, et sociorum, martyrum - \\textit{memoria minor} - " + couleur
    saint_pothin["body"] = ant_bened + messe_lue + \
        "\\item in MC \\textit{(Rub.)}: collecta in MP ; Commune martyrum " + \
        messe_conv + "."

    saint_charles_lwanga_date = datetime.date(current_year, 6, 3)
    # TODO: octave Pentecôte
    saint_charles_lwanga = dict_sancto[saint_charles_lwanga_date] = {}
    saint_charles_lwanga["force"] = 40
    saint_charles_lwanga["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus RP Francisci Xavier Mariæ \\textsc{Gaillot-Drevon}, sacerdotis, qui die 3 iunii 2018 obdormivit in Domino."
    saint_charles_lwanga["header"] = " - \\textsc{Ss. Caroli Lwanga et sociorum}, martyrum - \\textbf{memoria maior} - \\textit{Rub.}"
    if saint_charles_lwanga_date < paques + datetime.timedelta(days=49):
        ant_bened = "\n\\item ad Benedictus: ø \\textit{Lux perpetua} (AM 632)."
        messe_lue = "\n\\item \\textit{in ML: Missa pro pluribus martyribus tempore paschali.}"
        ant_magnif = "\n\\item ad Magnificat: ø \\textit{Sancti tui} (AM 632)."
    else:
        ant_bened = "\n\\item ad Benedictus: ø \\textit{Et ipsi} (AM 949)."
        if is_oct_pent(saint_charles_lwanga_date):
            if saint_charles_lwanga_date.weekday() in [2, 4, 5]:
                messe_lue = "\n\\item \\textit{in ML (Rub): Quatuor Temporum Pentecostes} (Credo)."
            else:
                messe_lue = "\n\\item \\textit{in ML (Rub): Missa infra octavam} (Credo)."
        else:
            messe_lue = "\n\\item \\textit{in ML (Rub.): Missa pro pluribus martyribus extra tempus paschale.}"
        ant_magnif = "\n\\item ad Magnificat: ø \\textit{Isti sunt} in tono I d (AM 929)."
    saint_charles_lwanga["body"] = "\n\\item in Officio: oratio in supplemento 132.\n\\item ad Vigilias: lectio in supplemento 131." + \
        ant_bened + messe_lue + "\\item in MC: præfatio de sanctis martyribus."
    saint_charles_lwanga["II_vesp"] = ant_magnif

    saint_boniface_date = datetime.date(current_year, 6, 5)
    # TODO: octave Pentecôte
    saint_boniface = dict_sancto[saint_boniface_date] = {}
    saint_boniface["force"] = 40
    messe_conv = "(MR 921)" if saint_boniface_date < paques + \
        datetime.timedelta(days=49) else "(MR 915)"
    saint_boniface["header"] = " - \\textsc{S. Bonifatii}, episcopi et martyris - \\textbf{memoria maior} - \\textit{Rub.}"
    if is_oct_pent(saint_boniface_date):
        if saint_boniface_date.weekday() in [2, 4, 5]:
            messe_lue = "\n\\item \\textit{in ML (Rub): Quatuor Temporum Pentecostes} (Credo)."
        else:
            messe_lue = "\n\\item \\textit{in ML (Rub): Missa infra octavam} (Credo)."
    else:
        messe_lue = ""
    saint_boniface["body"] = messe_lue + "\n\\item in MC: Commune martyrum " + \
        messe_conv + " ; præfatio de sanctis martyribus."

    saint_ephrem_date = datetime.date(current_year, 6, 9)
    # TODO: octave Pentecôte
    saint_ephrem = dict_sancto[saint_ephrem_date] = {}
    saint_ephrem["force"] = 20
    if saint_ephrem_date < paques + datetime.timedelta(days=49):
        couleur = "\\textit{Alb.}"
        messe_lue = ""
        messe_conv = ""
    else:
        couleur = "\\textit{Vir.}"
        messe_lue = "\\item \\textit{in ML: Alb.}"
        messe_conv = " \\textit{(Alb.)}"
    saint_ephrem["header"] = " - S. Ephræm, diaconi et Ecclesiæ doctoris - \\textit{memoria minor} - " + \
        couleur + " (olim die 18 iunii)."
    saint_ephrem["body"] = "\n\\item ad Benedictus: ø \\textit{Similabo eum} (AM 669)." + \
        messe_lue + "\\item in MC" + messe_conv + \
        ": Commune doctorum Ecclesiæ (MR 944)."

    saint_barnabe_date = datetime.date(current_year, 6, 11)
    # TODO: octave Pentecôte
    saint_barnabe = dict_sancto[saint_barnabe_date] = {}
    saint_barnabe["force"] = 40
    saint_barnabe["header"] = " - \\textsc{S. Barnabæ, apostoli} - \\textbf{memoria maior} - \\textit{Rub.}"
    vigiles = "\\item ad Vigilias: invitatorium et hymnus de Communi Apostolorum extra tempus paschale ; lectio in supplemento 132 cum ¶ extra tempus paschale ; in II nocturno lectio brevis in supplemento 133 vel ut ad Sextam in Communi Apostolorum." if saint_barnabe_date < paques + \
        datetime.timedelta(days=56) else "\\item ad Vigilias: lectio in supplemento 132 pro breviario veteri ; in II nocturno lectio brevis in supplemento 133 vel ut ad Sextam in Communi Apostolorum."
    saint_barnabe["body"] = vigiles + \
        "\\item \\textit{in ML: dicitur \\emph{Credo}.}\n\\item in MC: lectiones propriæ: Act \\textbf{11}, 21b-26 ; \\textbf{13}, 1-3 / Mt \\textbf{10}, 7-13 ; præfatio I de Apostolis."
    ant_magnif = " cum \\textit{alleluia}" if saint_barnabe_date < paques + \
        datetime.timedelta(days=49) else ""
    saint_barnabe["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Tradent enim vos}" + \
        ant_magnif + " (AM 621)."

    saint_antoine_padoue_date = datetime.date(current_year, 6, 13)
    # TODO: octave Pentecôte
    saint_antoine_padoue = dict_sancto[saint_antoine_padoue_date] = {}
    saint_antoine_padoue["force"] = 40
    messe_conv = "(MR 921)" if saint_antoine_padoue_date < paques + \
        datetime.timedelta(days=49) else "(MR 915)"
    saint_antoine_padoue["header"] = " - \\textsc{S. Antonii de Padova}, presbyteri et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.}"
    in_officio = "\\item in Officio: oratio in supplemento 134." if saint_antoine_padoue_date < paques + \
        datetime.timedelta(days=56) else ""
    ant_bened = "\\textit{Exi cito} (AM 558)" if even_year else "\\textit{Quod autem} (AM 324)"
    saint_antoine_padoue["body"] = in_officio + "\\item ad Vigilias: lectio in supplemento 133.\n\\item ad Benedictus: ø " + ant_bened + \
        ".\n\\item \\textit{in ML: Missa in proprio sanctorum vel in PAL.}\n\\item in MC: Commune Sanctorum et Sanctarum (MR 962) ; præfatio I de sanctis."

    saint_romuald_date = datetime.date(current_year, 6, 19)
    # TODO: octave Pentecôte
    saint_romuald = dict_sancto[saint_romuald_date] = {}
    saint_romuald["force"] = 40
    saint_romuald[
        "header"] = " - \\textsc{S. Romualdi}, abbatis - \\textbf{memoria maior} - \\textit{Alb.} (olim die 7 februarii)."
    saint_romuald[
        "body"] = "\n\\item ad Vigilias: lectio et oratio in supplemento 134.\n\\item in MC: Commune sanctorum et sanctarum (MR 958) ; præfatio de sanctis virginibus et religiosis."
    #saint_romuald["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Hic vir despiciens} (AM 675)."

    saint_louis_gonzague_date = datetime.date(current_year, 6, 21)
    saint_louis_gonzague = dict_sancto[saint_louis_gonzague_date] = {}
    saint_louis_gonzague["force"] = 20
    saint_louis_gonzague[
        "header"] = " - S. Aloisii Gonzaga, religiosi - \\textit{memoria minor} - \\textit{Vir.}"
    saint_louis_gonzague[
        "body"] = "\n\\item ad Benedictus: ø \\textit{Sanctorum velut} (AM 652).\n\\item \\textit{in ML: Alb.}\n\\item in MC: \\textit{Alb.}"

    saint_john_fisher_date = datetime.date(current_year, 6, 22)
    saint_john_fisher = dict_sancto[saint_john_fisher_date] = {}
    saint_john_fisher["force"] = 20
    saint_john_fisher[
        "header"] = " - Ss. Ioannis Fisher, episcopi et Thomæ More, martyrum - \\textit{memoria minor} - \\textit{Vir.}"
    saint_john_fisher["body"] = "\n\\item ad Benedictus: ø \\textit{Sancti per fidem} (AM 652) ; oratio in supplemento 135.\n\\item \\textit{in ML (Rub.): Missa pro pluribus martyribus.}\n\\item in MC \\textit{(Rub.)}: Commune martyrum (MR 909)."

    vigile_saint_jean_baptiste_date = datetime.date(current_year, 6, 23) if paques != datetime.date(
        current_year, 4, 25) and paques != datetime.date(current_year, 4, 17) else datetime.date(current_year, 6, 24)
    vigile_saint_jean_baptiste = dict_sancto[vigile_saint_jean_baptiste_date] = {
    }
    vigile_saint_jean_baptiste["force"] = 10
    vigile_saint_jean_baptiste[
        "body"] = "\n\\item \\textit{in ML (Viol): Missa de Vigilia Nativitatis S. Ioannis Baptistæ.}"

    # Saint Jean-Baptiste 24 juin. Exceptions :
    # Si Sacré-Cœur = 24 juin, on célèbre saint JB la veille.
    # Si Fête-Dieu = 24 juin, on reporte saint JB au lendemain.
    if paques == datetime.date(current_year, 4, 17):
        saint_jean_baptiste_date = datetime.date(current_year, 6, 23)
    elif paques == datetime.date(current_year, 4, 25):
        saint_jean_baptiste_date = datetime.date(current_year, 6, 25)
    else:
        saint_jean_baptiste_date = datetime.date(current_year, 6, 24)
    saint_jean_baptiste = dict_sancto[saint_jean_baptiste_date] = {}
    saint_jean_baptiste["force"] = 110
    saint_jean_baptiste["I_vesp"] = "\\item I Vesperæ sollemnitatis sequentis."
    if saint_jean_baptiste_date.weekday() == 6:
        num_dim_ap_pentec = (saint_jean_baptiste_date - pentecote).days // 7
        num_dim_per_annum = f_roman_numbers(
            num_dim_ap_pentec + 35 - nb_dim_ap_pentec)
        if num_dim_ap_pentec == 2:
            text_ap_pentec = "II post Pentecosten vel infra octavam Ss. Corporis Christi"
        elif num_dim_ap_pentec == 3:
            text_ap_pentec = "III post Pentecosten vel infra octavam Ss. Cordis Iesu"
        else:
            text_ap_pentec = f_roman_numbers(
                num_dim_ap_pentec) + " post Pentecosten"
        text_dim = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + \
            " per annum}}" + " (" + text_ap_pentec + ")"
    else:
        text_dim = ""
    saint_jean_baptiste["header"] = text_dim + \
        " - þ \\textbf{\\MakeUppercase{In nativitate S. Ioannis Baptistæ}} - \\textbf{sollemnitas minor} - \\textit{Alb.}"
    hymne_laudes = "\n\\item ad Laudes : hymnus \\textit{Antra deserti} (AM 928a)." if saint_jean_baptiste_date.day == 25 or paques == datetime.date(
        current_year, 4, 24) or paques == datetime.date(current_year, 4, 16) else ""
    saint_jean_baptiste["body"] = hymne_laudes + \
        "\n\\item \\textit{in ML: præfatio propria.}\n\\item in MC: lectiones propriæ: Is \\textbf{49}, 1-6 / Act \\textbf{13}, 22-26 / Lc \\textbf{1}, 57-66.80 ; præfatio propria."
    hymne_vepres = " ; hymnus \\textit{O nimis felix} (AM 926)" if saint_jean_baptiste_date.day == 25 or paques == datetime.date(
        current_year, 4, 24) or paques == datetime.date(current_year, 4, 16) else ""
    saint_jean_baptiste["II_vesp"] = "\n\\item Vesperæ sollemnitatis" + \
        hymne_vepres + "."

    anniv_pere_jean_pouchet_txt = "\\textup{†} Cras recurrit anniversarium obitus RP Ioannis Mariæ \\textsc{Pouchet}, sacerdotis, qui die 25 iunii 2012, in Abbatia Dominæ Nostræ Mayliliensis, obdormivit in Domino."
    # Car si Fête-Dieu ou Sacré-Cœur le 24, alors S.J.B le 25, et il ne faut pas écraser la solennité avec l'anniversaire.
    if paques != datetime.date(current_year, 4, 25) and paques != datetime.date(current_year, 4, 17):
        anniv_pere_jean_pouchet_date = datetime.date(current_year, 6, 25)
        anniv_pere_jean_pouchet = dict_sancto[anniv_pere_jean_pouchet_date] = {}
        anniv_pere_jean_pouchet["anniv"] = anniv_pere_jean_pouchet_txt
    else:
        saint_jean_baptiste["anniv"] = anniv_pere_jean_pouchet_txt

    saint_cyrille_alexandrie_date = datetime.date(current_year, 6, 27)
    saint_cyrille_alexandrie = dict_sancto[saint_cyrille_alexandrie_date] = {}
    saint_cyrille_alexandrie["force"] = 20
    saint_cyrille_alexandrie[
        "header"] = " - S. Cyrilli Alexandrini, episcopi et Ecclesiæ doctoris - \\textit{memoria minor} - \\textit{Vir.} (olim die 9 februarii)."
    ant_bened = "\\item ad Benedictus: ø \\textit{Super muros tuos} (AM 592) ; oratio in AM 797 vel in supplemento 135." if even_year else "\\item ad Benedictus: ø \\textit{Maternitas tua} (AM 1085) ; oratio in AM 797 vel in supplemento 135."
    saint_cyrille_alexandrie["body"] = ant_bened + \
        "\\item \\textit{in ML: Alb.}\n\\item in MC \\textit{(Alb.)}: Commune pastorum (MR 929)."

    saint_irenee_date = datetime.date(current_year, 6, 28)
    saint_irenee = dict_sancto[saint_irenee_date] = {}
    saint_irenee["force"] = 40
    saint_irenee["header"] = " - \\textsc{S. Irenæi}, episcopi, Ecclesiæ doctoris et martyris - \\textbf{memoria maior} - \\textit{Rub.}"
    saint_irenee[
        "body"] = "\n\\item in Officio: oratio in supplemento 136.\n\\item ad Vigilias: lectio in supplemento 136.\n\\item ad Benedictus: ø \\textit{Qui me confessus} (AM 640).\n\\item \\textit{in ML: olim die 3 iulii.}\n\\item in MC: præfatio de sanctis martyribus."

    # On envisage le cas où Sacré-Cœur le 29. À ce moment-là, on décale S.P.P. au 28.
    saints_pierre_et_paul_date = datetime.date(current_year, 6, 29) if paques != datetime.date(
        current_year, 4, 22) else datetime.date(current_year, 6, 28)
    saints_pierre_et_paul = dict_sancto[saints_pierre_et_paul_date] = {}
    saints_pierre_et_paul["force"] = 110
    saints_pierre_et_paul[
        "I_vesp"] = "\\item I Vesperæ sollemnitatis sequentis ; ad Magnificat: ø \\textit{Gloriosi} (AM 958)."
    if saints_pierre_et_paul_date.weekday() == 6:
        num_dim_ap_pentec = (saints_pierre_et_paul_date - pentecote).days // 7
        num_dim_per_annum = f_roman_numbers(
            num_dim_ap_pentec + 35 - nb_dim_ap_pentec)
        if num_dim_ap_pentec == 2:
            text_ap_pentec = "II post Pentecosten vel infra octavam Ss. Corporis Christi"
        elif num_dim_ap_pentec == 3:
            text_ap_pentec = "III post Pentecosten vel infra octavam Ss. Cordis Iesu"
        else:
            text_ap_pentec = f_roman_numbers(
                num_dim_ap_pentec) + " post Pentecosten"
        text_dim = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + \
            " per annum}}" + " (" + text_ap_pentec + ")"
    else:
        text_dim = ""
    saints_pierre_et_paul["header"] = text_dim + \
        " - þ \\textbf{\\MakeUppercase{Ss. Petri et Pauli, Apostolorum}} - \\textbf{sollemnitas minor} - \\textit{Rub.}"
    saints_pierre_et_paul["body"] = "\n\\item ad Benedictus: ø \\textit{Petrus} (AM 959).\n\\item in MC: lectiones propriæ: Act \\textbf{12}, 1-11 / 2 Tim \\textbf{4}, 6-8.16-18 / Mt \\textbf{16}, 13-19 ; præfatio propria."
    saints_pierre_et_paul[
        "II_vesp"] = "\n\\item Vesperæ sollemnitatis ut in AM 939, præter antiphonas et capitulum de commemoratione S. Pauli Apostoli (AM 941), cum psalmis ut in II Vesperis de Communi Apostolorum."

    # Car si Sacré-Cœur le 29, alors S.P.P. le 30, et il ne faut pas écraser la solennité avec les Protomartyrs.
    if paques != datetime.date(current_year, 4, 22):
        saints_protomartyrs_date = datetime.date(current_year, 6, 30)
        saints_protomartyrs = dict_sancto[saints_protomartyrs_date] = {}
        saints_protomartyrs["force"] = 20
        saints_protomartyrs[
            "header"] = " - Ss. Protomartyrum S. Romanæ Ecclesiæ - \\textit{memoria minor} - \\textit{Vir.}"
        saints_protomartyrs["body"] = "\n\\item ad Benedictus: ø \\textit{Hi sunt} (AM 949) ; oratio in supplemento 137.\n\\item \\textit{in ML (Rub.): Missa pro pluribus martyribus.}\n\\item in MC \\textit{(Rub.)}: Commune martyrum (MR 910)."

    # JUILLET:

    saint_thomas_ap_date = datetime.date(current_year, 7, 3)
    saint_thomas_ap = dict_sancto[saint_thomas_ap_date] = {}
    saint_thomas_ap["force"] = 70
    saint_thomas_ap[
        "header"] = " - \\textbf{\\textsc{S. Thomæ, apostoli}} - \\textbf{festum} - \\textit{Rub.} (olim die 21 decembris)."
    # Si 29/06 et 03/07 appartiennent à la même semaine, on inverse la semaine du psautier pour les Vigiles:
    inv_sem_vigiles = "; antiphonæ et psalmi hebdomadæ " + hebdo_psalterii_inv[((saints_pierre_et_paul_date - datetime.date(
        2011, 11, 27)).days // 7) % 2] if saints_pierre_et_paul_date.weekday() == 6 or saints_pierre_et_paul_date.weekday() < saint_thomas_ap_date.weekday() else ""
    saint_thomas_ap["body"] = "\n\\item ad Vigilias: in supplemento 138" + inv_sem_vigiles + \
        ".\n\\item ad Benedictus: ø \\textit{Quia vidisti} (AM 479).\n\\item in MC: lectiones propriæ: Ep \\textbf{2}, 19-22 / Io \\textbf{20}, 24-29 ; præfatio I de Apostolis."
    saint_thomas_ap[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Misi digitum} (AM 480)."
    # Si 1er vendredi du mois, reporter le jeûne au lendemain:
    if saint_thomas_ap_date.weekday() == 4:
        dict_tempo[saint_thomas_ap_date]["symbols"] = dict_tempo[saint_thomas_ap_date]["symbols"].replace(
            " µ", " ł")
        dict_tempo[saint_thomas_ap_date + datetime.timedelta(
            days=1)]["symbols"] = " µ" + dict_tempo[saint_thomas_ap_date + datetime.timedelta(days=1)]["symbols"]

    sainte_maria_goretti_date = datetime.date(current_year, 7, 6)
    sainte_maria_goretti = dict_sancto[sainte_maria_goretti_date] = {}
    sainte_maria_goretti["force"] = 20
    sainte_maria_goretti[
        "header"] = " - S. Mariæ Goretti, virginis et martyris - \\textit{memoria minor} - \\textit{Vir.}"
    sainte_maria_goretti["body"] = "\n\\item ad Benedictus: ø \\textit{Exhibeamus} (AM 909) ; oratio in supplemento 142.\n\\item \\textit{in ML (Rub.): Missa in PAL.}\n\\item in MC \\textit{(Rub.)}: Commune virginis martyris (MR 924)."

    saint_benoit_date = datetime.date(current_year, 7, 11)
    saint_benoit = dict_sancto[saint_benoit_date] = {}
    saint_benoit["force"] = 110
    saint_benoit["I_vesp"] = "\n\\item I Vesperæ sollemnitatis sequentis."
    if saint_benoit_date.weekday() == 6:
        num_dim_ap_pentec = (saint_benoit_date - pentecote).days // 7
        num_dim_per_annum = f_roman_numbers(
            num_dim_ap_pentec + 35 - nb_dim_ap_pentec)
        text_ap_pentec = f_roman_numbers(
            num_dim_ap_pentec) + " post Pentecosten"
        text_dim = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + \
            " per annum}}" + " (" + text_ap_pentec + ")"
    else:
        text_dim = ""
    saint_benoit["header"] = text_dim + \
        " - ¬ \\textbf{\\MakeUppercase{S. P. N. Benedicti, Abbatis,}} \\textsc{Europæ patroni} - \\textbf{sollemnitas maior} - \\textit{Alb.}"
    saint_benoit["body"] = "\n\\item ad Vigilias: in nocturno III: lectio 9.\n\\item \\textit{in ML: Missa in supplemento OSB ; præfatio propria.}\n\\item in MC: omnia in MP ; lectiones propriæ: Pr \\textbf{2}, 1-9 / Ep \\textbf{4}, 1-6 / Mt \\textbf{19}, 27-29 ; sequentia ; præfatio propria."
    saint_benoit["II_vesp"] = "\n\\item Vesperæ sollemnitatis ; benedictio Sanctissimi Sacramenti."

    saint_jean_gualbert_date = datetime.date(current_year, 7, 12)
    saint_jean_gualbert = dict_sancto[saint_jean_gualbert_date] = {}
    saint_jean_gualbert["force"] = 20
    saint_jean_gualbert[
        "header"] = " - S. Ioannis Gualberti, abbatis - \\textit{memoria minor} - \\textit{Vir.}"
    saint_jean_gualbert["body"] = "\n\\item ad Benedictus: ø \\textit{Estote} in tono I f (AM 538).\n\\item \\textit{in ML: Alb.}\n\\item in MC \\textit{(Alb.)}: collecta in MP ; Commune sanctorum et sanctarum (MR 962)."

    saint_camille_date = datetime.date(current_year, 7, 14)
    saint_camille = dict_sancto[saint_camille_date] = {}
    saint_camille["force"] = 20
    saint_camille[
        "header"] = " - S. Camilli de Lellis, presbyteri - \\textit{memoria minor} - \\textit{Vir.} (olim die 18 hujus)."
    saint_camille["body"] = "\n\\item ad Benedictus: ø \\textit{Amen dico vobis} (AM 829 in tono I f) ; oratio in supplemento 143.\n\\item \\textit{in ML: Alb.}\n\\item in MC \\textit{(Alb.)}: Commune sanctorum et sanctarum (MR 963)."

    saint_bonaventure_date = datetime.date(current_year, 7, 15)
    saint_bonaventure = dict_sancto[saint_bonaventure_date] = {}
    saint_bonaventure["force"] = 40
    saint_bonaventure[
        "header"] = " - \\textsc{S. Bonaventuræ}, episcopi et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.} (olim die 14 huius)."
    saint_bonaventure["body"] = "\n\\item in MC: Commune pastorum (MR 931) ; præfatio de sanctis pastoribus."
    #saint_bonaventure["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Sapientiam sanctorum} (AM 981)."

    nd_mont_carmel_date = datetime.date(current_year, 7, 16)
    nd_mont_carmel = dict_sancto[nd_mont_carmel_date] = {}
    nd_mont_carmel["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus RP Benedicti Mariæ \\textsc{Constantin}, sacerdotis, qui die 16 iulii 1965, in Abbatia Dominæ Nostræ Mayliliensis, obdormivit in Domino."
    ant_bened = "\\item ad Benedictus: ø \\textit{Gloria Libani} (AM 971)." if even_year else "\\item ad Benedictus: ø \\textit{Caput tuum} (AM 971)."
    if nd_mont_carmel_date.weekday() == 5:
        nd_mont_carmel["force"] = 40
        nd_mont_carmel[
            "header"] = " - \\textsc{Beatæ Mariæ Virginis de Monte Carmelo} - \\textbf{memoria maior} - \\textit{Alb.}"
        nd_mont_carmel["body"] = "\n\\item officium totum dicitur de Maria in sabbato præter orationem in supplemento 143 et ø ad Benedictus.\n\\item ad Vigilias: lectio sabbato 3 (in supplemento 204 pro breviario veteri)." + \
            ant_bened + \
            "\\item in MC \\textit{(Alb.)}: CM 32 ; præfatio I de Beata Maria Virgine."
    else:
        nd_mont_carmel["force"] = 20
        nd_mont_carmel[
            "header"] = " - Beatæ Mariæ Virginis de Monte Carmelo - \\textit{memoria minor} - \\textit{Vir.}"
        nd_mont_carmel["body"] = ant_bened + \
            "\\item \\textit{in ML: Alb.}\n\\item in MC \\textit{(Alb.)}: CM 32 ; præfatio I de Beata Maria Virgine."

    anniv_pere_gorce_date = datetime.date(current_year, 7, 17)
    anniv_pere_gorce = dict_sancto[anniv_pere_gorce_date] = {}
    anniv_pere_gorce["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus Reverendissimi ac dilectissimi Patris Augustini Mariæ \\textsc{Gorce}, abbatis et fundatoris Dominæ Nostræ Mayliliensis, qui die 17 iulii 1962 obdormivit in Domino."

    saint_laurent_brindisi_date = datetime.date(current_year, 7, 21)
    saint_laurent_brindisi = dict_sancto[saint_laurent_brindisi_date] = {}
    saint_laurent_brindisi["force"] = 20
    saint_laurent_brindisi[
        "header"] = " - S. Laurentii de Brindisi, presbyteri et Ecclesiæ doctoris - \\textit{memoria minor} - \\textit{Vir.} "
    saint_laurent_brindisi["body"] = "\n\\item ad Benedictus: ø \\textit{Similabo eum} (AM 669) ; oratio in supplemento 143.\n\\item \\textit{in ML (Alb.): Missa in PAL.}\n\\item in MC \\textit{(Alb.)}: Commune pastorum (MR 934)."

    sainte_marie_madeleine_date = datetime.date(current_year, 7, 22)
    sainte_marie_madeleine = dict_sancto[sainte_marie_madeleine_date] = {}
    sainte_marie_madeleine["force"] = 70
    sainte_marie_madeleine["header"] = " - \\textbf{\\textsc{S. Mariæ Magdalenæ}} - \\textbf{festum} - \\textit{Alb.}"
    sainte_marie_madeleine[
        "body"] = "\n\\item in Officio : omnia de Communi nec virginis nec martyris præter sequentia.\n\\item oratio propria.\n\\item ad Vigilias : invitatorium proprium ; hymnus proprius ; lectio in secundo nocturno in supplemento 143*.\n\\item ad Laudes : hymnus proprius ; ad Benedictus : ø \\textit{In diebus illis} (AM 975).\n\\item in MC : lectiones propriæ : 2 Co \\textbf{5}, 14-17 / Io \\textbf{20}, 1.11-18 ; præfatio propria."
    sainte_marie_madeleine[
        "II_vesp"] = "\n\\item ad Vesperas : hymnus proprius ; ad Magnificat : ø \\textit{Mulier} (AM 978)."

    sainte_brigitte_date = datetime.date(current_year, 7, 23)
    sainte_brigitte = dict_sancto[sainte_brigitte_date] = {}
    sainte_brigitte["force"] = 70
    sainte_brigitte[
        "header"] = " - \\textbf{\\textsc{S. Birgittæ, religiosæ, Europæ patronæ}} - \\textbf{festum} - \\textit{Alb.} (olim die 8 octobris)."
    lectures_mc = "Ga \\textbf{2}, 19-20 / Mc \\textbf{3}, 31-35" if even_year else "Tb \\textbf{8}, 4b-7 / Jn \\textbf{15}, 1-8"
    sainte_brigitte["body"] = "\n\\item in Officio: omnia de Communi nec virginis nec martyris præter sequentia.\n\\item oratio in supplemento 146*.\n\\item ad Vigilias: antiphonæ et psalmi hebdomadæ " + hebdo_psalterii_inv[((sainte_marie_madeleine_date - datetime.date(
        2011, 11, 27)).days // 7) % 2] + "; lectio II nocturni in supplemento 144*.\n\\item \\textit{in ML: præfatio de sanctis.}\n\\item in MC: Commune sanctorum et sanctarum (MR 966) ; lectiones propriæ: " + lectures_mc + " ; præfatio I de sanctis."

    saint_jacques_date = datetime.date(current_year, 7, 25)
    saint_jacques = dict_sancto[saint_jacques_date] = {}
    saint_jacques["force"] = 70
    saint_jacques["header"] = " - \\textbf{\\textsc{S. Iacobi, apostoli}} - \\textbf{festum} - \\textit{Rub.}"
    saint_jacques["body"] = "\n\\item ad Benedictus: ø \\textit{Assumpsit Iesus} (AM 998).\n\\item in MC: lectiones propriæ: 2 Co \\textbf{4}, 7-15 / Mt \\textbf{20}, 20-28 ; præfatio II de Apostolis."

    saints_joachim_anne_date = datetime.date(current_year, 7, 26)
    saints_joachim_anne = dict_sancto[saints_joachim_anne_date] = {}
    saints_joachim_anne["force"] = 40
    saints_joachim_anne["header"] = " - \\textsc{Ss. Ioachim et Annæ}, parentum Beatæ Mariæ Virginis - \\textbf{memoria maior} - \\textit{Alb.}"
    var_vesperas = ", Vesperas" if saints_joachim_anne_date.weekday() != 5 else ""
    saints_joachim_anne[
        "body"] = "\n\\item ad Vigilias pro breviario veteri: in supplemento 144.\n\\item ad Laudes" + var_vesperas + " et Horas minores: antiphonæ propriæ.\n\\item \\textit{in ML: Missa in supplemento OSB.}\n\\item in MC: lectiones propriæ: Si \\textbf{44}, 1.10-15 / Mt \\textbf{13}, 16-17 ; præfatio II de sanctis."
    saints_joachim_anne[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Benedictionem} (AM 979)." if not even_year else ""

    saints_marthe_marie_lazare_date = datetime.date(current_year, 7, 29)
    saints_marthe_marie_lazare = dict_sancto[saints_marthe_marie_lazare_date] = {
    }
    saints_marthe_marie_lazare["force"] = 40
    saints_marthe_marie_lazare["header"] = " - \\textsc{Ss. Marthæ, Mariæ et Lazari}, hospitum Domini - \\textbf{memoria maior} - \\textit{Alb.}"
    evg_mc = " Io \\textbf{11}, 19-27" if even_year else " Lc \\textbf{10}, 38-42"
    saints_marthe_marie_lazare[
        "body"] = "\n\\item in Officio: oratio in supplemento 148.\n\\item ad Vigilias: in supplemento 146 ; invitatorium \\textit{Mirabilem} in supplemento 59 vel in variationibus 35.\n\\item ad Laudes: a capitulo ut in variationibus 26 (die 5 octobris) ; ad Benedictus: ø \\textit{Maria ergo} (AM 977).\n\\item ad Horas: antiphonæ, capitula et ß ut in variationibus 25.\n\\item \\textit{in ML: S. Marthæ, virginis.}\n\\item in MC: omnia in MP ; lectiones propriæ: 1 Io \\textbf{4}, 7-16 /" + evg_mc + "; præfatio II de sanctis."
    saints_marthe_marie_lazare[
        "II_vesp"] = "\n\\item ad Vesperas: a capitulo ut in variationibus 29, præter ad Magnificat: ø \\textit{Domine si} (AM 380)."

    saint_pierre_chrysologue_date = datetime.date(current_year, 7, 30)
    saint_pierre_chrysologue = dict_sancto[saint_pierre_chrysologue_date] = {}
    saint_pierre_chrysologue["force"] = 20
    saint_pierre_chrysologue[
        "header"] = " - S. Petri Chrysologi, episcopi et Ecclesiæ doctoris - \\textit{memoria minor} - \\textit{Vir.} (olim die 4 decembris)."
    saint_pierre_chrysologue["body"] = "\n\\item ad Benedictus: ø \\textit{Sacerdos} (AM 656) ; oratio in supplemento 148.\n\\item \\textit{in ML: Alb.}\n\\item in MC \\textit{(Alb.)}: Commune doctorum Ecclesiæ (MR 944)."

    saint_ignace_loyola_date = datetime.date(current_year, 7, 31)
    saint_ignace_loyola = dict_sancto[saint_ignace_loyola_date] = {}
    saint_ignace_loyola["force"] = 40
    saint_ignace_loyola["header"] = " - \\textsc{S. Ignatii de Loyola}, presbyteri - \\textbf{memoria maior} - \\textit{Alb.}"
    var_vesperas = ", Vesperas" if saint_ignace_loyola_date.weekday() != 5 else ""
    saint_ignace_loyola[
        "body"] = "\n\\item ad Laudes" + var_vesperas + " et Horas minores: antiphonæ e Communi confessoris non pontificis.\n\\item ad Benedictus: ø \\textit{Ignem} (AM 564).\n\\item in MC: lectiones propriæ: 1 Co \\textbf{10}, 31–\\textbf{11}, 1 / Lc \\textbf{14}, 25-33 ; præfatio de sanctis virginibus et religiosis.\n\\item ad Magnificat: ø \\textit{Estote} (AM 628)."

    # AOÛT:

    saint_alphonse_liguori_date = datetime.date(current_year, 8, 1)
    saint_alphonse_liguori = dict_sancto[saint_alphonse_liguori_date] = {}
    saint_alphonse_liguori["force"] = 40
    saint_alphonse_liguori[
        "header"] = " - \\textsc{S. Alfonsi de Liguori}, episcopi et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.} (olim die 2 huius)."
    saint_alphonse_liguori[
        "body"] = "\n\\item ad Vigilias: lectio in supplemento 149.\n\\item ad Benedictus: ø \\textit{Observa} (AM 582).\n\\item in MC: præfatio de sanctis pastoribus."

    saint_pierre_julien_date = datetime.date(current_year, 8, 2)
    saint_pierre_julien = dict_sancto[saint_pierre_julien_date] = {}
    saint_pierre_julien["force"] = 20
    saint_pierre_julien[
        "header"] = " - S. Petri Iuliani Eymard, presbyteri - \\textit{memoria minor} - \\textit{Vir.}"
    ant_bened = "\\item ad Benedictus: ø \\textit{Calicem} (AM 429)" if even_year else "\\item ad Benedictus: ø \\textit{Ego sum} 2 (AM 553)"
    saint_pierre_julien["body"] = ant_bened + \
        " ; oratio in supplemento 150*.\n\\item \\textit{in ML (Alb.): Missa pro confessore non pontifice.}\n\\item in MC \\textit{(Alb.)}: Commune sanctorum et sanctarum (MR 961)."

    saint_jm_vianney_date = datetime.date(current_year, 8, 4)
    saint_jm_vianney = dict_sancto[saint_jm_vianney_date] = {}
    saint_jm_vianney["force"] = 40
    saint_jm_vianney["header"] = " - \\textsc{S. Ioannis Mariæ Vianney}, presbyteri - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_jm_vianney[
        "body"] = "\n\\item in Officio: oratio in supplemento 151.\n\\item ad Vigilias: lectio in supplemento 150.\n\\item ad Benedictus: ø \\textit{Vivo ego} in tono III b (AM 5).\n\\item \\textit{in ML: olim die 8 augusti in PAL.}\n\\item in MC: omnia in MP; præfatio I de sanctis."
    saint_jm_vianney[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Hoc genus} (AM 584)."

    dedicace_nd_neiges_date = datetime.date(current_year, 8, 5)
    dedicace_nd_neiges = dict_sancto[dedicace_nd_neiges_date] = {}
    dedicace_nd_neiges["force"] = 20
    dedicace_nd_neiges[
        "header"] = " - Dedicatio basilicæ S. Mariæ - \\textit{memoria minor} - \\textit{Vir.}"
    dedicace_nd_neiges["body"] = "\n\\item ad Benedictus: ø \\textit{Beata es, Maria} (AM 709).\n\\item \\textit{in ML: Alb.}\n\\item in MC \\textit{(Alb.)}: Commune Beatæ Mariæ Virginis (MR 898) ; præfatio I de Beata Maria Virgine."

    transfiguration_date = datetime.date(current_year, 8, 6)
    transfiguration = dict_sancto[transfiguration_date] = {}
    if transfiguration_date.weekday() == 6:
        transfiguration["I_vesp"] = "\n\\item I Vesperæ festi sequentis."
        transfiguration["force"] = 90
        num_dim_ap_pentec = (transfiguration_date - pentecote).days // 7
        num_dim_per_annum = f_roman_numbers(
            num_dim_ap_pentec + 35 - nb_dim_ap_pentec)
        num_summer = " - " + \
            f_num_summer(transfiguration_date)[
                0] + f_num_summer(transfiguration_date)[1]
        text_ap_pentec = f_roman_numbers(
            num_dim_ap_pentec) + " post Pentecosten" + num_summer
        text_dim = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + \
            " per annum}}" + " (" + text_ap_pentec + ")"
    else:
        transfiguration["force"] = 70
        text_dim = ""
    transfiguration["header"] = text_dim + \
        " - \\textbf{\\textsc{in Transfiguratione Domini}} - \\textbf{festum} - \\textit{Alb.}"
    evang_mc = {"A": "Mt \\textbf{17}, 1-9",
                "B": "Mc \\textbf{9}, 2-10", "C": "Lc \\textbf{9}, 28b-36"}
    if transfiguration_date.weekday() == 6:
        lectures_mc = "Dan \\textbf{7}, 9-10.13-14 / 2 Petr \\textbf{1}, 16-19" + \
            " / " + evang_mc[year_letter]
    elif even_year:
        lectures_mc = "2 Petr \\textbf{1}, 16-19" + \
            " / " + evang_mc[year_letter]
    else:
        lectures_mc = "Dan \\textbf{7}, 9-10.13-14" + \
            " / " + evang_mc[year_letter]
    transfiguration["body"] = "\n\\item ad Horas et Completorium, tonus proprius pro hymnis.\n\\item in MC: lectiones propriæ: " + \
        lectures_mc + " ; præfatio propria."
    if even_year:
        vesp_festi = "\n\\item Vesperæ festi." if transfiguration_date.weekday() == 5 else ""
    else:
        vesp_festi = ("\n\\item Vesperæ festi; ad Magnificat: ø \\textit{Christus Iesus} (AM 997)." if transfiguration_date.weekday(
        ) == 5 else "\n\\item ad Magnificat: ø \\textit{Christus Iesus} (AM 997).") if transfiguration_date.weekday() != 6 else ""
    transfiguration["II_vesp"] = vesp_festi

    saint_dominique_date = datetime.date(current_year, 8, 8)
    saint_dominique = dict_sancto[saint_dominique_date] = {}
    saint_dominique["force"] = 40
    saint_dominique[
        "header"] = " - \\textsc{S. Dominici}, presbyteri - \\textbf{memoria maior} - \\textit{Alb.} (olim die 4 huius)."
    saint_dominique[
        "body"] = "\n\\item ad Vigilias pro breviario veteri: lectio XII cum ¶ suo.\n\\item ad Benedictus: ø \\textit{Vos qui reliquistis omnia} (AM 624).\n\\item in MC: præfatio de sanctis virginibus et religiosis."
    saint_dominique[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Qui me confessus} (AM 640)."

    sainte_edith_stein_date = datetime.date(current_year, 8, 9)
    sainte_edith_stein = dict_sancto[sainte_edith_stein_date] = {}
    sainte_edith_stein["force"] = 70
    sainte_edith_stein["header"] = " - \\textbf{\\textsc{S. Teresiæ Benedictæ a Cruce} (Edith Stein), \\textsc{virginis, martyris et Europæ patronæ}} - \\textbf{festum} - \\textit{Rub.}"
    sainte_edith_stein[
        "body"] = "\n\\item in Officio: omnia de Communi virginis martyris, præter sequentia.\n\\item oratio in supplemento 153*.\n\\item ad Vigilias: lectio I nocturni de libro Ecclesiastici \\textbf{51}, 1-17 in breviario monastico 172* ; lectio II nocturni in supplemento 151*.\n\\item ad Benedictus: ø \\textit{Ego sum} (AM 982).\n\\item \\textit{in ML: Missa pro virgine et martyre ; præfatio de sanctis.}\n\\item in MC: Commune virginis martyris (MR 924) ; lectiones propriæ: Os \\textbf{2}, 16b. 17b. 21-22 / Mt \\textbf{25}, 1-13 ; præfatio de sanctis martyribus."
    sainte_edith_stein[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Elevare} (AM 222)."

    saint_laurent_date = datetime.date(current_year, 8, 10)
    saint_laurent = dict_sancto[saint_laurent_date] = {}
    saint_laurent["force"] = 70
    saint_laurent["header"] = " - \\textbf{\\textsc{S. Laurentii, diaconi et martyris}} - \\textbf{festum} - \\textit{Rub.}"
    saint_laurent["body"] = "\n\\item \\textit{in ML: præfatio de sanctis martyribus.}\n\\item in MC: lectiones propriæ: 2 Co \\textbf{9}, 6-10 / Io \\textbf{12}, 24-26 ; præfatio de sanctis martyribus."
    saint_laurent[
        "II_vesp"] = "" if even_year else "\n\\item ad Magnificat: ø \\textit{Levita Laurentius} (AM 1005), ß \\textit{Gloria et honore} (AM 1005)."

    sainte_claire_date = datetime.date(current_year, 8, 11)
    sainte_claire = dict_sancto[sainte_claire_date] = {}
    sainte_claire["force"] = 40
    sainte_claire[
        "header"] = " - S. Claræ, virginis - memoria minor - \\textit{Alb.} (olim die 12 huius)."
    ant_bened = "\\item ad Benedictus: ø \\textit{Dedit mihi} (AM 819)."
    sainte_claire["body"] = ant_bened + \
        "\\item in MC: Commune virginum (MR 947)."
    #sainte_claire["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Nolite} (AM 1003)."

    sainte_jeanne_chantal_date = datetime.date(current_year, 8, 12)
    sainte_jeanne_chantal = dict_sancto[sainte_jeanne_chantal_date] = {}
    sainte_jeanne_chantal["force"] = 40
    sainte_jeanne_chantal[
        "header"] = " - S. Ioannæ Franciscæ Frémiot de Chantal, viduæ - memoria minor - \\textit{Alb.}"
    sainte_jeanne_chantal["body"] = "\n\\item ad Benedictus: ø \\textit{Date ei} (AM 688) ; oratio in supplemento 60*.\n\\item \\textit{in ML: olim die 21 augusti.}\n\\item in MC: Commune sanctorum et sanctarum (MR 962)."

    saint_max_kolbe_date = datetime.date(current_year, 8, 14)
    saint_max_kolbe = dict_sancto[saint_max_kolbe_date] = {}
    saint_max_kolbe["force"] = 40
    saint_max_kolbe["header"] = " - \\textsc{S. Maximiliani Mariæ Kolbe}, presbyteri et martyris - \\textbf{memoria maior} - \\textit{Rub.}"
    saint_max_kolbe[
        "body"] = "\n\\item in Officio: oratio in supplemento 153.\n\\item ad Vigilias: lectio in supplemento 152.\n\\item ad Benedictus: ø \\textit{Majorem caritatem} (AM 622).\n\\item \\textit{in ML: Missa pro martyre non pontifice.}\n\\item in MC: præfatio de sanctis martyribus."

    assomption_date = datetime.date(current_year, 8, 15)
    assomption = dict_sancto[assomption_date] = {}
    assomption["force"] = 110
    assomption["I_vesp"] = "\\item I Vesperæ sollemnitatis sequentis."
    if assomption_date.weekday() == 6:
        num_dim_ap_pentec = (assomption_date - pentecote).days // 7
        num_dim_per_annum = f_roman_numbers(
            num_dim_ap_pentec + 35 - nb_dim_ap_pentec)
        num_summer = " - " + \
            f_num_summer(assomption_date)[0] + f_num_summer(assomption_date)[1]
        text_ap_pentec = f_roman_numbers(
            num_dim_ap_pentec) + " post Pentecosten" + num_summer
        text_dim = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + \
            " per annum}}" + " (" + text_ap_pentec + ")"
    else:
        text_dim = ""
    assomption["header"] = text_dim + \
        " - ¬ \\textbf{\\MakeUppercase{In assumptione Beatæ Mariæ Virginis}}, \\textsc{patronæ principalis Galliæ} - \\textbf{sollemnitas maior} - \\textit{Alb.}"
    assomption[
        "body"] = "\n\\item ad Vigilias: in breviario 62 primum Officium. In nocturno I: lectiones 1 et 2 cum ¶ lectionis 4 ; in nocturno II: lectiones 5 et 6 cum ¶ lectionis 8 ; in nocturno III: lectiones 9, 10, 11 et 12.\n\\item in MC: lectiones propriæ: Apoc \\textbf{11}, 19a ; \\textbf{12}, 1-6a.10ab / 1 Co \\textbf{15}, 20-27a / Lc \\textbf{1}, 39-56 ; præfatio de Assumptione."
    assomption[
        "II_vesp"] = "\n\\item post Vesperas sollemnitatis incipiuntur Litaniæ Beatæ Mariæ Virginis pro sollemni supplicatione iuxta votum Regis Ludovici \\textsc{xiii} et fit processio ; benedictio Sanctissimi Sacramenti.\n\\item ad Completorium: ø \\textit{Ave Regina cælorum} (AM 175)."

    saint_bernard_tolomei_date = datetime.date(current_year, 8, 19)
    saint_bernard_tolomei = dict_sancto[saint_bernard_tolomei_date] = {}
    saint_bernard_tolomei["force"] = 40
    saint_bernard_tolomei[
        "header"] = " - \\textsc{S. Bernardi Tolomæi}, abbatis - \\textbf{memoria maior} - \\textit{Alb.} (olim die 21 huius)."
    saint_bernard_tolomei[
        "body"] = "\n\\item in Officio: oratio in variationibus 22.\n\\item ad Vigilias: lectio in supplemento 154*.\n\\item ad Benedictus: ø \\textit{Ex domo} (AM 779).\n\\item \\textit{in ML: Missa in supplemento OSB.}\n\\item in MC: collecta in MP ; Commune pastorum (MR 934) ; præfatio de sanctis virginibus et religiosis."
    saint_bernard_tolomei[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Pastor bonus} (AM 483)."

    saint_bernard_date = datetime.date(current_year, 8, 20)
    saint_bernard = dict_sancto[saint_bernard_date] = {}
    saint_bernard["force"] = 70
    saint_bernard["header"] = " - \\textbf{\\textsc{S. Bernardi, abbatis et Ecclesiæ doctoris}} - \\textbf{festum} - \\textit{Alb.}"
    #lectures_mc = "Cant \\textbf{8}, 6-7" if even_year else "Sir \\textbf{2}, 1-9"
    saint_bernard[
        "body"] = "\n\\item ad Vigilias: hymnus proprius ; lectiones in folio supplementi.\n\\item ad Laudes: hymnus proprius et antiphona ad Benedictus propria.\n\\item \\textit{in ML: Missa in PAL.}\n\\item in MC: lectiones propriæ: Si \\textbf{15}, 1-6 / Jn \\textbf{17}, 20-26 ; præfatio de sanctis virginibus et religiosis."
    saint_bernard["II_vesp"] = "\n\\item ad Vesperas: hymnus proprius."

    saint_pie_X_date = datetime.date(current_year, 8, 21)
    saint_pie_X = dict_sancto[saint_pie_X_date] = {}
    saint_pie_X["force"] = 40
    saint_pie_X[
        "header"] = " - \\textsc{S. Pii X}, papæ - \\textbf{memoria maior} - \\textit{Alb.} (olim die 3 septembris)."
    saint_pie_X[
        "body"] = "\n\\item in Officio: oratio in supplemento 157 vel in variationibus 23.\n\\item ad Vigilias pro breviario veteri: lectio in supplemento 156.\n\\item ad Benedictus: ø \\textit{Homo quidam} (AM 557).\n\\item in MC: præfatio de sanctis pastoribus."
    saint_pie_X["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Dum esset} (AM 663)."

    marie_reine_date = datetime.date(current_year, 8, 22)
    marie_reine = dict_sancto[marie_reine_date] = {}
    marie_reine["force"] = 40
    marie_reine["header"] = " - \\textsc{Beatæ Mariæ Virginis Reginæ} - \\textbf{\\textit{memoria maior}} - \\textit{Alb.}"
    marie_reine[
        "body"] = "\n\\item in Officio: oratio in supplemento 157.\n\\item ad Vigilias: lectio, ¶ et capitulum in supplemento 157*.\n\\item ad Benedictus: ø \\textit{Beata Mater} (AM 713).\n\\item \\textit{in ML: olim die 31 maii (non dicitur \\emph{Credo}).}\n\\item in MC: præfatio I de Beata Maria Virgine."
    marie_reine["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Sancta Maria} (AM 705)."

    saint_barthelemy_date = datetime.date(current_year, 8, 24)
    saint_barthelemy = dict_sancto[saint_barthelemy_date] = {}
    saint_barthelemy["force"] = 70
    saint_barthelemy["header"] = " - \\textbf{\\textsc{S. Bartholomæi, apostoli}} - \\textbf{festum} - \\textit{Rub.}"
    saint_barthelemy["body"] = "\n\\item in MC: lectiones propriæ: Apoc \\textbf{21}, 9b-14 / Io \\textbf{1}, 45-51 ; præfatio I de Apostolis."
    saint_barthelemy[
        "II_vesp"] = "\n\\item ad Magnificat: \\textit{Tradent enim} (AM 621)."

    saint_louis_date = datetime.date(current_year, 8, 25)
    saint_louis = dict_sancto[saint_louis_date] = {}
    saint_louis["force"] = 20
    saint_louis["header"] = " - S. Ludovici IX, regis - \\textit{memoria minor} - \\textit{Vir.}"
    saint_louis["body"] = "\n\\item ad Benedictus: ø \\textit{Si culmen} (AM 324) ; oratio in supplemento 157.\n\\item \\textit{in ML: Alb.}\n\\item in MC \\textit{(Alb.)}: omnia in MP."

    sainte_monique_date = datetime.date(current_year, 8, 27)
    sainte_monique = dict_sancto[sainte_monique_date] = {}
    sainte_monique["force"] = 40
    sainte_monique[
        "header"] = " - \\textsc{S. Monicæ, viduæ} - \\textbf{memoria maior} - \\textit{Alb.} (olim die 4 maii)."
    sainte_monique[
        "body"] = "\n\\item ad Vigilias: invitatorium \\textit{Mirabilem} in supplemento 59 vel in variationibus 35, lectio, ¶ et oratio in supplemento 158*.\n\\item ad Benedictus: ø \\textit{Absterget Deus} (AM 652).\n\\item in MC: Commune sanctorum et sanctarum (MR 967) ; præfatio II de sanctis."
    sainte_monique[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Tristitia implevit} (AM 490)."

    saint_augustin_date = datetime.date(current_year, 8, 28)
    saint_augustin = dict_sancto[saint_augustin_date] = {}
    saint_augustin["force"] = 40
    saint_augustin["header"] = " - \\textsc{S. Augustini}, episcopi et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_augustin[
        "body"] = "\n\\item ad Vigilias pro breviario veteri: lectio XII cum ¶ suo.\n\\item ad Benedictus: ø \\textit{Omnes autem} (AM 357).\n\\item \\textit{in ML: Missa in proprio sanctorum vel in PAL.}\n\\item in MC: lectiones propriæ: 1 Io \\textbf{4}, 7-16 / Mt \\textbf{23}, 8-12 ; præfatio de sanctis pastoribus."

    passion_saint_jb_date = datetime.date(current_year, 8, 29)
    passion_saint_jb = dict_sancto[passion_saint_jb_date] = {}
    passion_saint_jb["force"] = 40
    passion_saint_jb["header"] = " - \\textsc{In Passione S. Ioannis Baptistæ} - \\textbf{memoria maior} - \\textit{Rub.}"
    passion_saint_jb["body"] = "\n\\item ad Vigilias: in supplemento 159 pro breviario veteri ; In II nocturno, lectio brevis et ß de Communi unius martyris in psalterio.\n\\item ad Laudes" + ("" if passion_saint_jb_date.weekday(
    ) == 5 else " , Vesperas") + " et Horas minores: antiphonæ propriæ.\n\\item \\textit{in ML: præfatio propria.}\n\\item in MC: lectiones propriæ: Ier \\textbf{1}, 17-19 / Mc \\textbf{6}, 17-29 ; præfatio propria."

    # SEPTEMBRE:

    saint_gregoire_date = datetime.date(current_year, 9, 3)
    saint_gregoire = dict_sancto[saint_gregoire_date] = {}
    saint_gregoire["force"] = 70
    saint_gregoire[
        "header"] = " - \\textbf{\\textsc{S. Gregorii I, papæ et Ecclesiæ doctoris}} - \\textbf{festum} - \\textit{Alb.} (olim die 12 martii)."
    var_vesperas = ", Vesperas" if saint_gregoire_date.weekday() != 5 else ""
    saint_gregoire[
        "body"] = "\n\\item ad Vigilias: omnia in supplemento 160.\n\\item ad Laudes" + var_vesperas + " et Horas minores: antiphonæ propriæ.\n\\item \\textit{in ML: Missa \\emph{Si diligis me} (Commune Summorum Pontificum) cum orationibus e die 12 martii.}\n\\item in MC: lectiones propriæ: 2 Co \\textbf{4}, 1-2.5-7 / Lc \\textbf{22}, 24-30 ; præfatio de sanctis pastoribus."

    sainte_reine_date = datetime.date(current_year, 9, 7)
    sainte_reine = dict_sancto[sainte_reine_date] = {}
    sainte_reine["force"] = 100
    sainte_reine[
        "I_vesp"] = "\\item I Vesperæ sollemnitatis sequentis. Responsorium \\textit{Adiuvabit eam} et versiculum in AM 1178."
    # Si tombe un dimanche, on calcule quel dimanche (per annum, post Pentecosten).
    if sainte_reine_date.weekday() == 6:
        num_dim_ap_pentec = (sainte_reine_date - pentecote).days // 7
        num_dim_per_annum = f_roman_numbers(
            num_dim_ap_pentec + 35 - nb_dim_ap_pentec)
        num_summer = " - " + \
            f_num_summer(sainte_reine_date)[
                0] + f_num_summer(sainte_reine_date)[1]
        text_ap_pentec = f_roman_numbers(
            num_dim_ap_pentec) + " post Pentecosten" + num_summer
        text_dim = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + \
            " per annum}}" + " (" + text_ap_pentec + ")"
    else:
        text_dim = ""
    sainte_reine["header"] = text_dim + \
        " - þ \\textbf{\\MakeUppercase{S. Reginæ, virginis et martyris}} - \\textbf{sollemnitas minor} - \\textit{Rub.}"
    sainte_reine[
        "body"] = "\n\\item in Officio: omnia de Communi virginum ; oratio in supplemento 168.\n\\item ad Vigilias: hymnus proprius et lectiones II nocturni in folio supplemento ; lectio I nocturni de libro Ecclesiastici \\textbf{51}, 1-17 in breviario monastico 172*.\n\\item Ad Laudes: versiculum in AM 1178.\n\\item \\textit{in ML: \\emph{Gloria ; Credo} ; præfatio de sanctis martyribus.}\n\\item in MC: collecta propria ; Commune virginis martyris (MR 924) ; lectiones propriæ: Ct \\textbf{8}, 6-7 / Ep \\textbf{6}, 10-13. 18 / Mt \\textbf{25}, 1-13  ; præfatio de sanctis martyribus."
    sainte_reine["II_vesp"] = "\n\\item Vesperæ sollemnitatis. Responsorium \\textit{Adiuvabit eam} et versiculum in AM 1178." if sainte_reine_date.weekday(
    ) == 5 else "\\item ad Vesperas, responsorium \\textit{Adiuvabit eam} et versiculum in AM 1178."
    # Si 1er vendredi du mois, reporter le jeûne au lendemain:
    if sainte_reine_date.weekday() == 4:
        dict_tempo[sainte_reine_date]["symbols"] = dict_tempo[sainte_reine_date]["symbols"].replace(
            " µ", " ł")

    nativite_bmv_date = datetime.date(current_year, 9, 8)
    nativite_bmv = dict_sancto[nativite_bmv_date] = {}
    nativite_bmv["force"] = 70
    nativite_bmv["header"] = " - \\textbf{\\textsc{In Nativitate Beatæ Mariæ Virginis}} - \\textbf{festum} - \\textit{Alb.}"
    # Comme le 07/09 et le 08/09 appartiennent toujours à la même semaine, on inverse la semaine du psautier pour les Vigiles:
    hebdo_psalt_vigiles = hebdo_psalterii_inv[(
        (sainte_reine_date - datetime.date(2011, 11, 27)).days // 7) % 2]
    ant_bened = "" if even_year else "\\item ad Benedictus: ø \\textit{Gloriosæ} (AM 1031)."
    lectures_mc = "Rom \\textbf{8}, 28-30" if even_year else "Mic \\textbf{3}, 1-4"
    nativite_bmv["body"] = "\n\\item ad Vigilias: antiphonæ et psalmi hebdomadæ " + hebdo_psalt_vigiles + " (pro breviario veteri: in II nocturno vide in supplemento 169)." + \
        ant_bened + "\\item in MC: lectiones propriæ: " + lectures_mc + \
        " / Mt \\textbf{1}, 18-23 \\textit{(formula brevior)} ; præfatio I de Beata Maria Virgine."

    saint_nom_marie_date = datetime.date(current_year, 9, 12)
    saint_nom_marie = dict_sancto[saint_nom_marie_date] = {}
    saint_nom_marie["force"] = 40
    saint_nom_marie["header"] = " - \\textsc{Ss. Nominis Beatæ Virginis Mariæ} - \\textbf{\\textit{memoria maior}} - \\textit{Alb.}"
    saint_nom_marie[
        "body"] = "\n\\item ad Vigilias: lectio et oratio in supplemento 169*\n\\item ad Benedictus: ø \\textit{Sancta Maria} (AM 705).\n\\item in MC: præfatio I de Beata Maria Virgine."

    saint_jean_chrysostome_date = datetime.date(current_year, 9, 13)
    saint_jean_chrysostome = dict_sancto[saint_jean_chrysostome_date] = {}
    saint_jean_chrysostome["force"] = 40
    saint_jean_chrysostome[
        "header"] = " - \\textsc{S. Ioannis Chrysostomi}, episcopi et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.} (olim die 27 ianuarii)."
    saint_jean_chrysostome[
        "body"] = "\n\\item ad Vigilias: lectio, ¶ et oratio in supplemento 169.\n\\item ad Benedictus: ø \\textit{Semen est} (AM 324).\n\\item in MC: præfatio de sanctis pastoribus."

    sainte_croix_date = datetime.date(current_year, 9, 14)
    sainte_croix = dict_sancto[sainte_croix_date] = {}
    sainte_croix["force"] = 90
    # Si tombe un dimanche, on calcule quel dimanche (per annum, post Pentecosten) :
    if sainte_croix_date.weekday() == 6:
        num_dim_ap_pentec = (sainte_croix_date - pentecote).days // 7
        num_dim_per_annum = f_roman_numbers(
            num_dim_ap_pentec + 35 - nb_dim_ap_pentec)
        num_summer = " - " + \
            f_num_summer(sainte_croix_date)[
                0] + f_num_summer(sainte_croix_date)[1]
        text_ap_pentec = f_roman_numbers(
            num_dim_ap_pentec) + " post Pentecosten" + num_summer
        text_dim = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + \
            " per annum}}" + " (" + text_ap_pentec + ")"
    else:
        text_dim = ""
    sainte_croix["header"] = text_dim + \
        " - \\textbf{\\textsc{In Exaltatione Sanctæ Crucis}} - \\textbf{festum} - \\textit{Rub.}"
    lectures_mc = "Nb \\textbf{21}, 4b-9 / " if sainte_croix_date.weekday() == 6 else ""
    vepres = "\\item ad Vesperas: omnia ut in I Vesperis præter ad Magnificat: ø \\textit{O Crux benedicta} (AM 1046)." if even_year or sainte_croix_date.weekday(
    ) == 6 else "\\item ad Vesperas: omnia ut in I Vesperis."
    sainte_croix["body"] = "\n\\item in MC: lectiones propriæ: " + lectures_mc + \
        "Phil \\textbf{2}, 6-11 / Io \\textbf{3}, 13-17 ; præfatio propria." + vepres

    sept_douleurs_date = datetime.date(current_year, 9, 15)
    sept_douleurs = dict_sancto[sept_douleurs_date] = {}
    sept_douleurs["force"] = 40
    sept_douleurs["header"] = " - \\textsc{Beatæ Mariæ Virginis perdolentis} - \\textbf{memoria maior} - \\textit{Alb.}"
    ant_bened = "" if even_year else "\n\\item ad Benedictus: ø \\textit{Tuam ipsius} in tono VI f (AM 867)."
    evg_mc = "Lc \\textbf{2}, 33-35" if even_year else "Io \\textbf{19}, 25-27"
    ant_magnif = "" if even_year else "\\item ad Magnificat: ø \\textit{Nolite me} (AM 1046)."
    var_vesperas = ", Vesperas" if sept_douleurs_date.weekday() != 5 else ""
    sept_douleurs["body"] = "\n\\item ad Vigilias pro breviario veteri: in supplemento 170.\n\\item ad Laudes" + var_vesperas + " et Horas minores: antiphonæ propriæ." + \
        ant_bened + "\n\\item \\textit{in ML: sequentia ; non dicitur \\emph{Credo}.}\n\\item in MC: lectiones propriæ: Hebr \\textbf{5}, 7-9 / " + \
        evg_mc + " ; sequentia ; præfatio I de Beata Maria Virgine." + ant_magnif

    saints_corneille_cyprien_date = datetime.date(current_year, 9, 16)
    saints_corneille_cyprien = dict_sancto[saints_corneille_cyprien_date] = {}
    saints_corneille_cyprien["force"] = 40
    saints_corneille_cyprien["header"] = " - \\textsc{Ss. Cornelii}, papæ et \\textsc{Cypriani}, episcopi, martyrum - \\textbf{memoria maior} - \\textit{Rub.}"
    saints_corneille_cyprien[
        "body"] = "\n\\item in Officio: oratio in supplemento 172 vel in AM 1040.\n\\item ad Vigilias: lectio in supplemento 171.\n\\item ad Benedictus: ø \\textit{Adstiterunt iusti} in tono Ig (AM 929).\n\\item in MC: præfatio de sanctis martyribus."
    saints_corneille_cyprien[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Isti sunt sancti} in tono Id (AM 929)."

    if even_year:
        saint_robert_bellarmin_date = datetime.date(current_year, 9, 17)
        saint_robert_bellarmin = dict_sancto[saint_robert_bellarmin_date] = {}
        saint_robert_bellarmin["force"] = 20
        saint_robert_bellarmin[
            "header"] = " - S. Roberti Bellarmino, episcopi et Ecclesiæ doctoris - \\textit{memoria minor} - \\textit{Vir.} (olim die 13 maii)."
        saint_robert_bellarmin["body"] = "\n\\item ad Benedictus: ø \\textit{Euge} (AM 661) ; oratio in AM 907.\n\\item \\textit{in ML: Alb.}\n\\item in MC \\textit{(Alb.)}: Commune doctorum Ecclesiæ (MR 943)."
    else:
        sainte_hildegarde_date = datetime.date(current_year, 9, 17)
        sainte_hildegarde = dict_sancto[sainte_hildegarde_date] = {}
        sainte_hildegarde["force"] = 20
        sainte_hildegarde[
            "header"] = " - S. Hildegardis, virginis et Ecclesiæ doctoris - \\textit{memoria minor} - \\textit{Vir.}"
        sainte_hildegarde[
            "body"] = "\n\\item ad Benedictus: ø \\textit{Sponsa Christi} in tono IIIg in variationibus 24.\n\\item \\textit{in ML (Alb.): Missa in supplemento OSB.}\n\\item in MC \\textit{(Alb.)}: collecta in MP ; Commune virginum (MR 948)."

    saint_seine_date = datetime.date(current_year, 9, 19)
    saint_seine = dict_sancto[saint_seine_date] = {}
    saint_seine["force"] = 40
    saint_seine["header"] = " - S. Sequani, abbatis - memoria minor - \\textit{Vir.}"
    messe_lue = "\n\\item \\textit{in ML (Alb.): Missa pro abbate.}" if not(is_third_week_of_september(
        saint_seine_date) and saint_seine_date.weekday() in [2, 4, 5]) else "\n\\item \\textit{in ML (Viol.): Quatuor Temporum Septembris.}"
    saint_seine["body"] = "\n\\item ad Benedictus: ø \\textit{Serve bone} (AM 673) ; oratio in supplemento 172." + \
        messe_lue + \
        "\n\\item in MC \\textit{(Alb.)}: collecta propria ; Commune sanctorum et sanctarum (MR 958)."

    saint_just_breteniere_date = datetime.date(current_year, 9, 20)
    saint_just_breteniere = dict_sancto[saint_just_breteniere_date] = {}
    saint_just_breteniere["force"] = 40
    saint_just_breteniere[
        "header"] = " - S. Iusti de Bretenières, presbyteri et martyris - memoria minor - \\textit{Vir.}"
    messe_lue = "\n\\item \\textit{in ML (Rub.): Missa pro martyre non pontifice.}" if not(is_third_week_of_september(
        saint_just_breteniere_date) and saint_just_breteniere_date.weekday() in [2, 4, 5]) else "\n\\item \\textit{in ML (Viol.): Quatuor Temporum Septembris.}"
    saint_just_breteniere["body"] = "\n\\item ad Benedictus: ø \\textit{Alias oves} (AM 486) ; oratio in supplemento 172." + \
        messe_lue + \
        "\n\\item in MC \\textit{(Rub.)}: collecta propria ; Commune martyrum (MR 917)."

    saint_matthieu_date = datetime.date(current_year, 9, 21)
    saint_matthieu = dict_sancto[saint_matthieu_date] = {}
    saint_matthieu["force"] = 70
    saint_matthieu["header"] = " - \\textbf{\\textsc{S. Matthæi, apostoli et evangelistæ}} - \\textbf{festum} - \\textit{Rub.}"
    saint_matthieu["body"] = "\n\\item in MC: lectiones propriæ: Ep \\textbf{4}, 1-7.11-13 / Mt \\textbf{9}, 9-13 ; præfatio II de Apostolis."

    saint_maurice_date = datetime.date(current_year, 9, 22)
    saint_maurice = dict_sancto[saint_maurice_date] = {}
    saint_maurice["force"] = 10
    saint_maurice["body"] = "\n\\item \\textit{in ML (Rub.): Missa Ss. Mauritii et sociorum.}" if not(is_third_week_of_september(
        saint_maurice_date) and saint_maurice_date.weekday() in [2, 4, 5]) else "\n\\item \\textit{in ML (Viol.): Quatuor Temporum Septembris.}"

    saint_padre_pio_date = datetime.date(current_year, 9, 23)
    saint_padre_pio = dict_sancto[saint_padre_pio_date] = {}
    saint_padre_pio["force"] = 40
    saint_padre_pio[
        "header"] = " - S. Pii de Pietrelcina, presbyteri - memoria minor - \\textit{Vir.}"
    messe_lue = "\n\\item \\textit{in ML (Alb.): Missa pro confessore non pontifice.}" if not(is_third_week_of_september(
        saint_padre_pio_date) and saint_padre_pio_date.weekday() in [2, 4, 5]) else "\n\\item \\textit{in ML (Viol.): Quatuor Temporum Septembris.}"
    saint_padre_pio["body"] = "\n\\item ad Benedictus: ø \\textit{Vivo autem} (AM 1128) ; oratio in supplemento 172*." + \
        messe_lue + \
        "\n\\item in MC \\textit{(Alb.)}: Commune sanctorum et sanctarum (MR 961)."

    saints_come_damien_date = datetime.date(current_year, 9, 26)
    saints_come_damien = dict_sancto[saints_come_damien_date] = {}
    saints_come_damien["force"] = 20
    saints_come_damien[
        "header"] = " - Ss. Cosmæ et Damiani, martyrum - \\textit{memoria minor} - \\textit{Vir.} (olim die 27 huius)."
    messe_lue = "\n\\item \\textit{in ML: Rub.}" if not(is_third_week_of_september(saints_come_damien_date) and saints_come_damien_date.weekday() in [2, 4, 5]) else "\n\\item \\textit{in ML (Viol.): Quatuor Temporum Septembris.}"
    saints_come_damien[
        "body"] = "\n\\item ad Benedictus: ø \\textit{Sanctorum precibus} in tono VIII g (AM 829)." + messe_lue + "\n\\item in MC: \\textit{Rub.}"

    saint_vincent_de_paul_date = datetime.date(current_year, 9, 27)
    saint_vincent_de_paul = dict_sancto[saint_vincent_de_paul_date] = {}
    saint_vincent_de_paul["force"] = 40
    saint_vincent_de_paul[
        "header"] = " - \\textsc{S. Vincentii de Paul}, presbyteri - \\textbf{memoria maior} - \\textit{Alb.} (olim die 19 iulii)."
    messe_lue = "\n\\item \\textit{in ML: Missa in proprio sanctorum vel in PAL.}" if not(is_third_week_of_september(
        saint_vincent_de_paul_date) and saint_vincent_de_paul_date.weekday() in [2, 4, 5]) else "\n\\item \\textit{in ML (Viol.): Quatuor Temporum Septembris.}"
    saint_vincent_de_paul[
        "body"] = "\n\\item ad Vigilias: lectio in supplemento 172.\n\\item ad Benedictus: ø \\textit{Amen dico vobis} in tono I f (AM 829)." + messe_lue + "\n\\item in MC: præfatio II de sanctis."
    saint_vincent_de_paul[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{O viri} in tono I d (AM 973)."

    saints_archanges_date = datetime.date(current_year, 9, 29)
    saints_archanges = dict_sancto[saints_archanges_date] = {}
    saints_archanges["force"] = 70
    saints_archanges["header"] = " - \\textbf{\\textsc{Ss. Michaelis, Gabrielis et Raphaelis Archangelorum}} - \\textbf{festum} - \\textit{Alb.}"
    ant_bened = "" if even_year else "\\item ad Benedictus: ø \\textit{Dum sacrum mysterium} (AM 1057)."
    saints_archanges["body"] = "\n\\item omnia ut hucusque in festo S. Michaelis." + ant_bened + \
        "\\item \\textit{in ML: præfatio de Angelis.}\n\\item in MC: lectiones propriæ: Apoc \\textbf{12}, 7-12a / Io \\textbf{1}, 47-51 ; præfatio de Angelis."

    saint_jerome_date = datetime.date(current_year, 9, 30)
    saint_jerome = dict_sancto[saint_jerome_date] = {}
    saint_jerome["force"] = 40
    saint_jerome["header"] = " - \\textsc{S. Hieronymi}, presbyteri et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_jerome[
        "body"] = "\n\\item ad Vigilias pro breviario veteri: lectio XII cum ¶ suo.\n\\item ad Benedictus: ø \\textit{Qui verbum} (AM 325).\n\\item in MC: præfatio I de sanctis."

    # OCTOBRE:

    sainte_therese_ej_date = datetime.date(current_year, 10, 1)
    sainte_therese_ej = dict_sancto[sainte_therese_ej_date] = {}
    sainte_therese_ej["force"] = 40
    sainte_therese_ej[
        "header"] = " - \\textsc{S. Teresiæ a Iesu Infante, virginis et Ecclesiæ doctoris}, patronæ secundariæ Galliæ - \\textbf{memoria maior} - \\textit{Alb.} (olim die 3 huius)."
    lecture_mc = "Rom \\textbf{8}, 14-17" if even_year else "Is \\textbf{66} 10-14c"
    sainte_therese_ej[
        "body"] = "\n\\item in Officio: oratio in supplemento 175 vel in variationibus 24.\n\\item ad Vigilias: lectio in supplemento 174.\n\\item ad Benedictus: ø \\textit{Qui sperant} in variationibus 31.\n\\item \\textit{in ML: præfatio de Sanctis.}\n\\item in MC: lectiones propriæ: " + lecture_mc + " / Mt \\textbf{18}, 1-5 ; præfatio de sanctis virginibus et religiosis."
    sainte_therese_ej[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Virgo gloriosa} (AM 1143)."

    saints_anges_gardiens_date = datetime.date(current_year, 10, 2)
    saints_anges_gardiens = dict_sancto[saints_anges_gardiens_date] = {}
    saints_anges_gardiens["force"] = 40
    saints_anges_gardiens["header"] = " - \\textsc{Ss. Angelorum Custodum} - \\textbf{memoria maior} - \\textit{Alb.}"
    ant_bened = "" if even_year else "\\item ad Benedictus: ø \\textit{Omnes sunt} (AM 1066)."
    var_vesperas = ", Vesperas" if saints_anges_gardiens_date.weekday() != 5 else ""
    saints_anges_gardiens["body"] = "\n\\item ad Vigilias pro breviario veteri: in supplemento 175.\n\\item ad Laudes" + var_vesperas + " et Horas minores: antiphonæ propriæ." + \
        ant_bened + \
        "\\item \\textit{in ML: præfatio de Angelis.}\n\\item in MC: cantatur hymnus angelicus \\textit{Gloria} ; lectiones propriæ: Ex \\textbf{23}, 20-23a / Mt \\textbf{18}, 1-5.10 ; præfatio de Angelis."

    saint_francois_assise_date = datetime.date(current_year, 10, 4)
    saint_francois_assise = dict_sancto[saint_francois_assise_date] = {}
    saint_francois_assise["force"] = 40
    saint_francois_assise["header"] = " - \\textsc{S. Francisci Assisiensis} - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_francois_assise[
        "body"] = "\n\\item ad Vigilias pro breviario veteri: lectio XII cum ¶ suo.\n\\item ad Benedictus: ø \\textit{Vos qui reliquistis} (AM 624).\n\\item in MC: præfatio de sanctis virginibus et religiosis."
    saint_francois_assise[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Vivo autem} (AM 1128)."

    sainte_faustine_date = datetime.date(current_year, 10, 5)
    sainte_faustine = dict_sancto[sainte_faustine_date] = {}
    sainte_faustine["force"] = 20
    sainte_faustine["header"] = " - S. Faustinæ Kowalska, virginis - \\textit{memoria minor} - \\textit{Vir.}"
    sainte_faustine[
        "body"] = "\\item ad Benedictus: ø \\textit{Estote} in tono I f (AM 538) ; oratio in supplemento 176*.\n\\item \\textit{in ML (Alb.): Missa pro virgine tantum.}\n\\item in MC\\textit{(Alb.)}: collecta propria ; Commune virginum (MR 950)."

    saint_bruno_date = datetime.date(current_year, 10, 6)
    saint_bruno = dict_sancto[saint_bruno_date] = {}
    saint_bruno["force"] = 40
    saint_bruno["header"] = " - \\textsc{S. Brunonis}, eremitæ - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_bruno[
        "body"] = "\n\\item ad Vigilias: lectio in supplemento 176.\n\\item ad Benedictus: ø \\textit{Beati pacifici} (AM 623).\n\\item in MC: Commune pastorum (MR 934) ; præfatio de sanctis virginibus et religiosis."
    saint_bruno["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Vobis datum} (AM 323)."

    nd_rosaire_date = datetime.date(current_year, 10, 7)
    nd_rosaire = dict_sancto[nd_rosaire_date] = {}
    nd_rosaire["force"] = 40
    nd_rosaire["header"] = " - \\textsc{Beatæ Mariæ Virginis a Rosario} - \\textbf{memoria maior} - \\textit{Alb.}"
    var_vesperas = ", Vesperas" if nd_rosaire_date.weekday() != 5 else ""
    nd_rosaire[
        "body"] = "\n\\item ad Vigilias: invitatorium proprium ; in supplemento 177 pro breviario veteri.\n\\item ad Laudes" + var_vesperas + " et Horas minores: antiphonæ propriæ.\n\\item \\textit{in ML: non dicitur \\emph{Credo}.}\n\\item in MC: lectiones propriæ: Act \\textbf{1}, 12-14 / Lc \\textbf{1}, 26-38 ; præfatio I de Beata Maria Virgine."

    saint_denis_date = datetime.date(current_year, 10, 9)
    saint_denis = dict_sancto[saint_denis_date] = {}
    saint_denis["force"] = 20
    saint_denis[
        "header"] = " - Ss. Dionysii, episcopi, et sociorum, martyrum. - \\textit{memoria minor} - \\textit{Vir.}"
    saint_denis["body"] = "\n\\item ad Benedictus: ø \\textit{Sanctorum velut aquilæ} (AM 652) ; oratio in supplemento 179.\n\\item \\textit{in ML: Rub.}\n\\item in MC \\textit{(Rub.)}: Commune martyrum (MR 913)."

    sainte_therese_avila_date = datetime.date(current_year, 10, 15)
    sainte_therese_avila = dict_sancto[sainte_therese_avila_date] = {}
    sainte_therese_avila["force"] = 40
    sainte_therese_avila["header"] = " - \\textsc{S. Teresiæ a Iesu, virginis et Ecclesiæ doctoris} - \\textbf{memoria maior} - \\textit{Alb.}"
    sainte_therese_avila[
        "body"] = "\n\\item ad Laudes: hymnus proprius ; ad Benedictus: ø \\textit{O beata anima} (AM 1131).\n\\item \\textit{in ML: Missa in proprio sanctorum vel in PAL.}\n\\item in MC: præfatio de sanctis virginibus et religiosis."
    sainte_therese_avila[
        "II_vesp"] = "\n\\item ad Vesperas: hymnus proprius ; ad Magnificat: ø \\textit{Sanctissima Christi sponsa} (AM 1128)."

    sainte_marguerite_marie_date = datetime.date(current_year, 10, 16)
    sainte_marguerite_marie = dict_sancto[sainte_marguerite_marie_date] = {}
    sainte_marguerite_marie["force"] = 20
    sainte_marguerite_marie[
        "header"] = " - S. Margaritæ Mariæ Alacoque, virginis - \\textit{memoria minor} - \\textit{Vir.} (olim die 17 huius)."
    sainte_marguerite_marie["body"] = "\n\\item ad Benedictus: ø \\textit{Dum esset rex} (AM 686) ; oratio in supplemento 179.\n\\item \\textit{in ML: Alb.}\n\\item in MC \\textit{(Alb.)}: Commune virginum (MR 948)."

    saint_ignace_antioche_date = datetime.date(current_year, 10, 17)
    saint_ignace_antioche = dict_sancto[saint_ignace_antioche_date] = {}
    saint_ignace_antioche["force"] = 40
    saint_ignace_antioche[
        "header"] = " - \\textsc{S. Ignatii Antiocheni}, episcopi et martyris - \\textbf{memoria maior} - \\textit{Rub.} (olim die 1 februarii)."
    saint_ignace_antioche["body"] = "\n\\item ad Vigilias: lectio, ¶ et oratio in supplemento 180.\n\\item in MC: præfatio de sanctis martyribus."

    saint_luc_date = datetime.date(current_year, 10, 18)
    saint_luc = dict_sancto[saint_luc_date] = {}
    saint_luc["force"] = 70
    saint_luc["header"] = " - \\textbf{\\textsc{S. Lucæ, evangelistæ}} - \\textbf{festum} - \\textit{Rub.}"
    saint_luc["body"] = "\n\\item in MC: lectiones propriæ: 2 Tim \\textbf{4}, 9-17 / Lc \\textbf{10}, 1-9 ; præfatio II de Apostolis."

    saint_jean_brebeuf_date = datetime.date(current_year, 10, 19)
    saint_jean_brebeuf = dict_sancto[saint_jean_brebeuf_date] = {}
    saint_jean_brebeuf["force"] = 20
    saint_jean_brebeuf[
        "header"] = " - Ss. Ioannis de Brebeuf et Isaac Jogues, presbyterorum et sociorum, martyrum - \\textit{memoria minor} - \\textit{Vir.}"
    saint_jean_brebeuf["body"] = "\n\\item ad Benedictus: ø \\textit{Nos autem} (AM 1041) ; oratio in supplemento 181.\n\\item \\textit{in ML (Rub.): olim die 26 septembris in PAL.}\n\\item in MC \\textit{(Rub.)}: Commune martyrum (MR 910)."

    saint_jean_paul_II_date = datetime.date(current_year, 10, 22)
    saint_jean_paul_II = dict_sancto[saint_jean_paul_II_date] = {}
    saint_jean_paul_II["force"] = 20
    saint_jean_paul_II[
        "header"] = " - S. Ioannis Pauli II, papæ - \\textit{memoria minor} - \\textit{Vir.}"
    saint_jean_paul_II["body"] = "\n\\item ad Benedictus: ø \\textit{Dum esset} (AM 663) ; oratio in supplemento 181*.\n\\item \\textit{in ML: Missa \\emph{Si diligis me} de Communi Summorum Pontificum, præter orationem.}\n\\item in MC \\textit{(Alb.)}: collecta propria ; Commune pastorum (MR 927)."

    nd_sainte_esperance_date = datetime.date(current_year, 10, 23)
    nd_sainte_esperance = dict_sancto[nd_sainte_esperance_date] = {}
    nd_sainte_esperance["force"] = 40
    nd_sainte_esperance["header"] = " - \\textsc{Dominæ Nostræ Sanctæ Spei} - \\textbf{\\textit{memoria maior}} - \\textit{Alb.}"
    nd_sainte_esperance[
        "body"] = "\n\\item in Officio: oratio in supplemento 182.\n\\item ad Vigilias: lectio in supplemento 181.\n\\item \\textit{in ML: Missa Sanctissimi Nominis Mariæ (vide ad diem 12 septembris) præter orationem.}\n\\item in MC: CM 37 ; præfatio I de Beata Maria Virgine."

    saint_antoine_marie_claret_date = datetime.date(current_year, 10, 24)
    saint_antoine_marie_claret = dict_sancto[saint_antoine_marie_claret_date] = {
    }
    saint_antoine_marie_claret["force"] = 20
    saint_antoine_marie_claret[
        "header"] = " - S. Antonii Mariæ Claret, episcopi - \\textit{memoria minor} - \\textit{Vir.}"
    saint_antoine_marie_claret["body"] = "\n\\item ad Benedictus: ø \\textit{Sacerdos} (AM 656) ; oratio in supplemento 182.\n\\item \\textit{in ML (Alb.): olim die 23 huius.}\n\\item in MC \\textit{(Alb.)}: Commune pastorum (MR 938)."

    saints_simon_jude_date = datetime.date(current_year, 10, 28)
    saints_simon_jude = dict_sancto[saints_simon_jude_date] = {}
    saints_simon_jude["force"] = 70
    saints_simon_jude["header"] = " - \\textbf{\\textsc{Ss. Simonis et Iudæ, apostolorum}} - \\textbf{festum} - \\textit{Rub.}"
    saints_simon_jude["body"] = "\n\\item in MC: lectiones propriæ: Ep \\textbf{2}, 19-22 / Lc \\textbf{6}, 12-19 ; præfatio I de Apostolis."
    saints_simon_jude[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{In regeneratione} (AM 1125)."

    # NOVEMBRE:

    toussaint_date = datetime.date(current_year, 11, 1)
    toussaint = dict_sancto[toussaint_date] = {}
    toussaint["force"] = 110
    toussaint["I_vesp"] = "\\item I Vesperæ sollemnitatis sequentis."
    toussaint[
        "generalities"] = "\\medskip\n\\textit{Plenaria indulgentia, animabus in Purgatorio detentis tantummodo applicabilis, conceditur christifideli qui}\\par \\textit{1° singulis diebus, a primo usque ad octavum novembris, cœmeterium devote visitaverit et, vel mente tantum, pro defunctis exoraverit ;}\\par \\textit{2° die Commemorationis omnium fidelium defunctorum (vel, de consensu Ordinarii, die Dominico antecedenti aut subsequenti aut die sollemnitatis Omnium Sanctorum) ecclesiam aut oratorium pie visitaverit ibique recitaverit \\emph{Pater} et \\emph{Credo}.}\\begin{flushright}\\textit{(Enchiridion Indulgentiarum, concessio n. 29: Pro fidelibus defunctis).}\\end{flushright}"
    if toussaint_date.weekday() == 6:
        num_dim_ap_pentec = (toussaint_date - pentecote).days // 7
        num_dim_per_annum = f_roman_numbers(
            num_dim_ap_pentec + 35 - nb_dim_ap_pentec)
        num_summer = " - " + \
            f_num_summer(toussaint_date)[0] + f_num_summer(toussaint_date)[1]
        text_ap_pentec = f_roman_numbers(
            num_dim_ap_pentec) + " post Pentecosten" + num_summer
        text_dim = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + \
            " per annum}}" + " (" + text_ap_pentec + ")"
    else:
        text_dim = ""
    toussaint["header"] = text_dim + \
        " - ¬ \\textbf{\\MakeUppercase{Omnium Sanctorum}} - \\textbf{sollemnitas maior} - \\textit{Alb.}"
    toussaint["body"] = "\n\\item ad Laudes et Vesperas: hymnus in folio separato.\n\\item \\textit{in ML: præfatio de sanctis.}\n\\item in MC: lectiones propriæ: Apoc \\textbf{7}, 2-4.9-14 / 1 Io \\textbf{3}, 1-3 / Mt \\textbf{5}, 1-12a ; præfatio propria."
    toussaint["II_vesp"] = "\n\\item Vesperæ sollemnitatis ; benedictio Sanctissimi Sacramenti."
    # Si 1er vendredi du mois, reporter le jeûne au lendemain:
    if toussaint_date.weekday() == 4:
        dict_tempo[toussaint_date]["symbols"] = dict_tempo[toussaint_date]["symbols"].replace(
            " µ", " ł")
        dict_tempo[toussaint_date + datetime.timedelta(
            days=1)]["symbols"] = " µ" + dict_tempo[toussaint_date + datetime.timedelta(days=1)]["symbols"]

    comm_defunts_date = datetime.date(current_year, 11, 2)
    comm_defunts = dict_sancto[comm_defunts_date] = {}
    comm_defunts["force"] = 110
    # Si tombe un dimanche, on calcule quel dimanche (per annum, post Pentecosten).
    if comm_defunts_date.weekday() == 6:
        num_dim_ap_pentec = (comm_defunts_date - pentecote).days // 7
        num_dim_per_annum = f_roman_numbers(
            num_dim_ap_pentec + 35 - nb_dim_ap_pentec)
        num_summer = " - " + \
            f_num_summer(comm_defunts_date)[
                0] + f_num_summer(comm_defunts_date)[1]
        text_ap_pentec = f_roman_numbers(
            num_dim_ap_pentec) + " post Pentecosten" + num_summer
        text_dim = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + \
            " per annum}}" + " (" + text_ap_pentec + ")"
    else:
        text_dim = ""
    comm_defunts["header"] = text_dim + \
        " - \\textbf{\\textsc{In Commemoratione omnium fidelium defunctorum}} - \\textit{Nigr.}"
    if comm_defunts_date.weekday() == 6:
        # TODO: Séparer les cas.
        rajout_dimanche = "\n\\item Officium fit de dominica, officio defunctorum omisso. Missæ omnes sunt de Commemoratione omnium fidelium defunctorum."
        rajout_dim_ml = "\n\\item in ML: \\textit{Credo}."
        rajout_dim_mc = " non fit aspersio ; psalmodia Tertiæ in directum ; non dicitur hymnus angelicus \\textit{Gloria}; "
        credo_mc = " \\emph{Credo};"
    else:
        rajout_dimanche = ""
        rajout_dim_ml = ""
        rajout_dim_mc = ""
        credo_mc = ""
    nocturnes = "psalmi et lectiones sumuntur e Nocturnis I et II." if even_year else "psalmi sumuntur e Nocturnis I et III; lectiones sumuntur e Nocturnis I et II."
    comm_defunts["body"] = rajout_dimanche + "\n\\item ß \\textit{Gloria Patri} dicitur in fine omnium psalmorum et canticorum. In responsoriis omittitur ß \\textit{Requiem æternam}.\n\\item ad Vigilias: absolute incipitur ab invitatorio (psalmus 94); " + nocturnes + "\n\\item \\textit{hodie, licet omnibus sacerdotibus tres Missas celebrare, ea tamen lege, ut unam tantum libere applicare et pro ea stipem percipere queant: tenentur vero, nulla stipe percepta, alteram in suffragium omnium fidelium defunctorum, tertiam ad mentem Summi Pontificis applicare.}\n\\item \\textit{ritus in Missis servandus: In prima et secunda Missa, si immediate sacerdos aliam Missam sit celebraturus, sumpto divino Sanguine, purificat calicem cum aqua tantum.}" + \
        rajout_dim_ml + "\n\\item in MC \\textit{(1a Missa)}:" + rajout_dim_mc + \
        " lectiones propriæ: Is \\textbf{25}, 6a-9 / 1 Co \\textbf{15}, 51-54.57 ; sequentia \\textit{Dies iræ} (Besnier 53) / Io \\textbf{6}, 51-59 ;" + \
        credo_mc + " præfatio I de defunctis."
    comm_defunts["II_vesp"] = ("\\item I Vesperæ dominicæ sequentis." if comm_defunts_date.weekday(
    ) == 5 else "") + ("\\item Completorium pro defunctis: incipitur a \\textit{Confiteor}, post examen conscientiæ ; aspersio de more.") if comm_defunts_date.weekday() in [5, 6] else ""
    # Si 1er vendredi du mois, reporter le jeûne au lendemain:
    if comm_defunts_date.weekday() == 4:
        dict_tempo[comm_defunts_date]["symbols"] = dict_tempo[comm_defunts_date]["symbols"].replace(
            " µ", " ł")
        dict_tempo[comm_defunts_date + datetime.timedelta(
            days=1)]["symbols"] = " µ" + dict_tempo[comm_defunts_date + datetime.timedelta(days=1)]["symbols"]

    saint_martin_porres_date = datetime.date(current_year, 11, 3)
    saint_martin_porres = dict_sancto[saint_martin_porres_date] = {}
    saint_martin_porres["force"] = 20
    saint_martin_porres[
        "header"] = " - S. Martini de Porres, religiosi - \\textit{memoria minor} - \\textit{Vir.}"
    saint_martin_porres["body"] = "\n\\item ad Benedictus: ø \\textit{Similabo eum} (AM 669) ; oratio in supplemento 183.\n\\item \\textit{in ML (Alb.): Missa pro confessore non pontifice.}\n\\item in MC \\textit{(Alb.)}: Commune sanctorum et sanctarum (MR 961)."

    saint_charles_borromee_date = datetime.date(current_year, 11, 4)
    saint_charles_borromee = dict_sancto[saint_charles_borromee_date] = {}
    saint_charles_borromee["force"] = 40
    saint_charles_borromee["header"] = " - \\textsc{S. Caroli}, episcopi - \\textbf{memoria maior} - \\textit{Alb.}"
    saint_charles_borromee[
        "body"] = "\n\\item ad Vigilias: lectio de memoria in supplemento 183.\n\\item ad Benedictus: ø \\textit{Euge} (AM 661).\n\\item \\textit{in ML: Missa in proprio sanctorum vel in PAL.}\n\\item in MC: præfatio de sanctis pastoribus."
    saint_charles_borromee[
        "II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Sacerdos et pontifex} (AM 656)."

    sainte_elisabeth_trinite_date = datetime.date(current_year, 11, 8)
    sainte_elisabeth_trinite = dict_sancto[sainte_elisabeth_trinite_date] = {}
    sainte_elisabeth_trinite["force"] = 40
    sainte_elisabeth_trinite["header"] = " - \\textsc{Sanctæ Elisabeth a Trinitate}, virginis - memoria minor - \\textit{Vir.}"
    sainte_elisabeth_trinite["body"] = "\n\\item ad Benedictus: ø \\textit{O Beata} (AM 1131) ; oratio in supplemento 184.\n\\item \\textit{in ML (Alb.): Missa pro virgine tantum.}\n\\item in MC \\textit{(Alb.)}: collecta propria ; Commune virginum (MR 947)."

    dedicace_latran_date = datetime.date(current_year, 11, 9)
    dedicace_latran = dict_sancto[dedicace_latran_date] = {}
    dedicace_latran["force"] = 90
    # Si tombe un dimanche, on calcule quel dimanche (per annum, post Pentecosten).
    if dedicace_latran_date.weekday() == 6:
        num_dim_ap_pentec = (dedicace_latran_date - pentecote).days // 7
        num_dim_per_annum = f_roman_numbers(
            num_dim_ap_pentec + 35 - nb_dim_ap_pentec)
        num_summer = " - " + \
            f_num_summer(dedicace_latran_date)[
                0] + f_num_summer(dedicace_latran_date)[1]
        text_ap_pentec = f_roman_numbers(
            num_dim_ap_pentec) + " post Pentecosten" + num_summer
        text_dim = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + \
            " per annum}}" + " (" + text_ap_pentec + ")"
    else:
        text_dim = ""
    dedicace_latran["header"] = text_dim + \
        " - \\textbf{\\textsc{In Dedicatione Basilicæ Lateranensis}} - \\textbf{festum} - \\textit{Alb.}"
    # Lectures MC:
    if dedicace_latran_date.weekday() == 6:
        lectures_mc = "Ez \\textbf{47}, 1-2.8-9.12 / 1 Co \\textbf{3}, 9b-11.16-17"
    elif even_year:
        lectures_mc = "1 Co \\textbf{3}, 9b-11.16-17"
    else:
        lectures_mc = "Ez \\textbf{47}, 1-2.8-9.12"
    # Vêpres:
    text_vepres = "\n\\item Vesperæ festi." if dedicace_latran_date.weekday() == 5 else ""
    dedicace_latran["body"] = "\n\\item ad Vigilias: in nocturno II, lectiones de commune Dedicationis ecclesiæ in II nocturno.\n\\item \\textit{in ML: præfatio de dedicatione ecclesiæ.}\n\\item in MC: lectiones propriæ: " + \
        lectures_mc + \
        " / Io \\textbf{2}, 13-22 ; præfatio de dedicatione ecclesiæ II." + text_vepres

    saint_leon_date = datetime.date(current_year, 11, 10)
    saint_leon = dict_sancto[saint_leon_date] = {}
    saint_leon["force"] = 40
    saint_leon[
        "header"] = " - \\textsc{S. Leonis magni}, papæ et Ecclesiæ doctoris - \\textbf{memoria maior} - \\textit{Alb.} (olim die 11 aprilis)."
    saint_leon[
        "body"] = "\n\\item ad Vigilias: lectio de memoria in supplemento 184 ; oratio in supplemento 185.\n\\item ad Benedictus: ø \\textit{Dum esset} (AM 663).\n\\item in MC: præfatio de sanctis pastoribus."

    saint_martin_date = datetime.date(current_year, 11, 11)
    saint_martin = dict_sancto[saint_martin_date] = {}
    saint_martin["force"] = 70
    saint_martin["header"] = " - \\textbf{\\textsc{S. Martini, episcopi}} - \\textbf{festum} - \\textit{Alb.}"
    lectures_vigiles = "\\item ad Vigilias: in nocturno I: lectiones 3 et 4 cum ¶ lectionis 4." if even_year else "\\item ad Vigilias: in nocturno I: lectiones 1 et 2 cum ¶ lectionis 4."
    saint_martin["body"] = lectures_vigiles + \
        "\\item in MC: lectiones propriæ: Is \\textbf{61}, 1-3a / Mt \\textbf{25}, 31-40 ; præfatio de sanctis pastoribus."

    saint_theodore_studite_date = datetime.date(current_year, 11, 12)
    saint_theodore_studite = dict_sancto[saint_theodore_studite_date] = {}
    saint_theodore_studite["force"] = 20
    saint_theodore_studite[
        "header"] = " - S. Theodori Studitæ, abbatis - \\textit{memoria minor} - \\textit{Vir.}"
    saint_theodore_studite["body"] = "\n\\item ad Benedictus: ø \\textit{Serve bone} (AM 673) ; oratio in supplemento 185.\n\\item \\textit{in ML (Alb.): Missa pro abbate.}\n\\item in MC \\textit{(Alb.)}: collecta in MP ; Commune sanctorum et sanctarum (MR 958)."

    saint_benigne_date = datetime.date(current_year, 11, 13)
    saint_benigne = dict_sancto[saint_benigne_date] = {}
    saint_benigne["force"] = 70
    saint_benigne["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus RP Lini Mariæ \\textsc{Delbos}, sacerdotis, qui die 13 novembris 2011, in Abbatia Dominæ Nostræ Mayliliensis, obdormivit in Domino."
    saint_benigne["header"] = " - \\textbf{\\textsc{S. Benigni, martyris}} - \\textbf{festum} - \\textit{Rub.}"
    # Si 11/11 et 13/11 appartiennent à la même semaine, on inverse la semaine du psautier pour les Vigiles:
    inv_sem_vigiles = "; antiphonæ et psalmi hebdomadæ " + hebdo_psalterii_inv[(
        (saint_martin_date - datetime.date(2011, 11, 27)).days // 7) % 2] if saint_martin_date.weekday() < 5 else ""
    saint_benigne["body"] = "\n\\item in Officio: omnia de Communi unius martyris ; oratio in supplemento 188.\n\\item ad Vigilias: invitatorium proprium in supplemento 59 ; omnia de Communi unius martyris præter hymnum in supplemento 185, lectiones I et II nocturnorum in supplemento 185*" + \
        inv_sem_vigiles + \
        ".\n\\item \\textit{in ML: Missa et præfatio propriæ (olim die 20 novembris).}\n\\item in MC: oratio propria ; Commune martyrum (MR 915) ; lectiones propriæ: 1 Thes \\textbf{2}, 2-8 / Mc \\textbf{16}, 15-18 ; præfatio de sanctis martyribus."

    anniv_fr_joseph_date = datetime.date(current_year, 11, 14)
    anniv_fr_joseph = dict_sancto[anniv_fr_joseph_date] = {}
    anniv_fr_joseph["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus Reverendissimi Patris Ioannis \\textsc{Prou}, abbatis, qui die 14 novembris 1999, in Abbatia Sancti Petri Solesmensis, obdormivit in Domino."

    saint_albert_date = datetime.date(current_year, 11, 15)
    saint_albert = dict_sancto[saint_albert_date] = {}
    saint_albert["force"] = 20
    saint_albert[
        "header"] = " - S. Alberti Magni, episcopi et Ecclesiæ doctoris - \\textit{memoria minor} - \\textit{Vir.}"
    saint_albert["body"] = "\n\\item ad Benedictus: ø \\textit{Omnis sapientia} (AM 581).\n\\item \\textit{in ML: Alb.}\n\\item in MC \\textit{(Alb.)}: Commune doctorum Ecclesiæ (MR 943)."

    sainte_gertrude_date = datetime.date(current_year, 11, 16)
    sainte_gertrude = dict_sancto[sainte_gertrude_date] = {}
    sainte_gertrude["force"] = 40
    sainte_gertrude[
        "header"] = " - \\textsc{S. Gertrudis Magnæ}, virginis - \\textbf{memoria maior} - \\textit{Alb.} (olim die sequenti)."
    var_vesperas = ", Vesperas" if sainte_gertrude_date.weekday() != 5 else ""
    sainte_gertrude[
        "body"] = "\n\\item ad Vigilias pro breviario veteri: in supplemento 188.\n\\item ad Laudes" + var_vesperas + " et Horas minores: antiphonæ propriæ.\n\\item \\textit{in ML: Missa in supplemento OSB.}\n\\item in MC: Commune virginum (MR 948) ; lectiones propriæ: Ep \\textbf{3}, 14-19 / Io \\textbf{15}, 1-8 ; præfatio de sanctis virginibus et religiosis."
    sainte_gertrude["II_vesp"] = "" if even_year else "\\item ad Vesperas: omnia ut in I Vesperis."

    sainte_elisabeth_hongrie_date = datetime.date(current_year, 11, 17)
    sainte_elisabeth_hongrie = dict_sancto[sainte_elisabeth_hongrie_date] = {}
    sainte_elisabeth_hongrie["force"] = 20
    sainte_elisabeth_hongrie[
        "header"] = " - S. Elisabeth Hungariæ, religiosæ - \\textit{memoria minor} - \\textit{Vir.}"
    sainte_elisabeth_hongrie["body"] = "\n\\item ad Benedictus: ø \\textit{Simile est} (AM 680) ; oratio in supplemento 189.\n\\item \\textit{in ML (Alb.): olim die 19 huius.}\n\\item in MC \\textit{(Alb.)}: Commune sanctorum et sanctarum (MR 963)."

    dedicace_sts_pierre_paul_date = datetime.date(current_year, 11, 18)
    dedicace_sts_pierre_paul = dict_sancto[dedicace_sts_pierre_paul_date] = {}
    dedicace_sts_pierre_paul["force"] = 20
    dedicace_sts_pierre_paul[
        "anniv"] = "Cras recurrit anniversarium ingressus et installationis nostræ in Flaviniacum (1976)."
    dedicace_sts_pierre_paul[
        "header"] = " - Dedicatio Basilicarum Ss. Petri et Pauli, apostolorum - \\textit{memoria minor }- \\textit{Vir.}"
    ant_bened = "\\item ad Benedictus: ø \\textit{Corpora sanctorum} (AM 648)." if even_year else "\\item ad Benedictus: ø \\textit{Petrus apostolus} (AM 959)."
    dedicace_sts_pierre_paul["body"] = ant_bened + \
        "\\item \\textit{in ML (Alb.): præfatio de dedicatione ecclesiæ.}\n\\item in MC: lectiones propriæ: Act \\textbf{28}, 11-16.30-31 / Mt \\textbf{14}, 22-33 ; præfatio I de Apostolis."

    presentation_bmv_date = datetime.date(current_year, 11, 21)
    presentation_bmv = dict_sancto[presentation_bmv_date] = {}
    presentation_bmv["force"] = 40
    presentation_bmv["header"] = " - \\textsc{In Præsentatione Beatæ Mariæ Virginis} - \\textbf{memoria maior} - \\textit{Alb.}"
    presentation_bmv[
        "body"] = "\n\\item ad Vigilias pro breviario veteri: in supplemento 190.\n\\item in MC: lectiones propriæ: Zac \\textbf{2}, 14-17 / Mt \\textbf{12}, 46-50 ; præfatio I de Beata Maria Virgine."
    presentation_bmv["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Beata} (AM 1138)."

    sainte_cecile_date = datetime.date(current_year, 11, 22)
    sainte_cecile = dict_sancto[sainte_cecile_date] = {}
    sainte_cecile["force"] = 40
    sainte_cecile["header"] = " - \\textsc{S. Cæciliæ}, virginis et martyris - \\textbf{memoria maior} - \\textit{Rub.}"
    var_vesperas = ", Vesperas" if sainte_cecile_date.weekday() != 5 else ""
    sainte_cecile[
        "body"] = "\n\\item ad Vigilias pro breviario veteri: in supplemento 191.\n\\item ad Laudes" + var_vesperas + " et Horas minores: antiphonæ propriæ.\n\\item in MC: omnia in MP ; lectiones propriæ: Os \\textbf{2}, 16b.17b.21-22 / Mt \\textbf{25}, 1-13 ; præfatio de sanctis martyribus."
    sainte_cecile["II_vesp"] = "\n\\item ad Magnificat: ø \\textit{Est secretum} (AM 1139)."

    saint_clement_date = datetime.date(current_year, 11, 23)
    saint_clement = dict_sancto[saint_clement_date] = {}
    saint_clement["force"] = 40
    saint_clement["header"] = " - \\textsc{S. Clementis I}, papæ et martyris - \\textbf{memoria maior} - \\textit{Rub.}"
    var_vesperas = ", Vesperas" if saint_clement_date.weekday() != 5 else ""
    saint_clement[
        "body"] = "\n\\item ad Laudes" + var_vesperas + " et Horas minores: antiphonæ propriæ.\n\\item in MC: Commune martyrum (MR 917) ; lectiones propriæ: 1~P \\textbf{5}, 1-4 / Mt \\textbf{16}, 13-19; præfatio de sanctis martyribus."
    saint_clement[
        "II_vesp"] = "\n\\item ad Vesperas: a capitulo ut in II Vesperis de Communi unius martyris ; ad Magnificat: ø \\textit{Dedisti} (AM 1148)."

    saint_andre_dung_lac_date = datetime.date(current_year, 11, 24)
    saint_andre_dung_lac = dict_sancto[saint_andre_dung_lac_date] = {}
    saint_andre_dung_lac["force"] = 40
    saint_andre_dung_lac[
        "header"] = " - Ss. Andreæ Dung Lac, presbyteri, et sociorum, martyrum - memoria minor - \\textit{Vir.}"
    saint_andre_dung_lac["body"] = "\n\\item ad Benedictus: ø \\textit{Omnes sancti} (AM 647) ; oratio in supplemento 192*.\n\\item \\textit{in ML (Rub.): Missa pro pluribus martyribus.}\n\\item in MC: \\textit{Rub.}"

    sainte_catherine_laboure_date = datetime.date(current_year, 11, 25)
    sainte_catherine_laboure = dict_sancto[sainte_catherine_laboure_date] = {}
    sainte_catherine_laboure["force"] = 40
    sainte_catherine_laboure[
        "header"] = " - S. Catharinæ Labouré, virginis - memoria minor - \\textit{Vir.}"
    sainte_catherine_laboure["body"] = "\n\\item ad Benedictus: ø \\textit{Veni sponsa} (AM 678) ; oratio in supplemento 192.\n\\item \\textit{in ML (Alb.): Missa pro virgine tantum.}\n\\item in MC \\textit{(Alb.)}: Collecta propria ; Commune virginum (MR 950)."

    saint_andre_date = datetime.date(current_year, 11, 30)
    saint_andre = dict_sancto[saint_andre_date] = {}
    saint_andre["force"] = 70
    saint_andre["anniv"] = "Cras incipiunt preces novendiales ante sollemnitatem Immaculatæ Conceptionis Beatæ Mariæ Virginis."
    saint_andre["header"] = " - \\textbf{\\textsc{S. Andreæ, apostoli}} - \\textbf{festum} - \\textit{Rub.}"
    year = saint_andre_date.year
    even = year % 2 == 0
    var_benedictus = "\\item ad Benedictus: ø \\textit{Unus ex duobus} (AM 754)." if even else ""
    saint_andre["body"] = var_benedictus + \
        "\\item in MC: lectiones propriæ: Rom \\textbf{10}, 9-18 / Mt \\textbf{4}, 18-22 ; præfatio II de Apostolis."

    return(dict_sancto)
