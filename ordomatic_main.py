#!/usr/bin/env python3
# coding: utf-8

import sys
from functions.tempo import *
from functions.sancto import *
from functions.ordo_write import *

#ordo_year = int(input("Entrez l'année de l'ordo : "))
ordo_year = int(sys.argv[1])
even_year = True if ordo_year % 2 == 0 else False

letters = ["A", "B", "C"]
year_letter = letters[(ordo_year - 2011) % 3]

dict_tempo, ordo_start, nb_days, date_paques, nb_dim_ap_pentec, christ_roi = dict_tempo_create(ordo_year, even_year, year_letter)
dict_sancto = dict_sancto_create(ordo_year, even_year, year_letter, dict_tempo, date_paques, nb_dim_ap_pentec)
ordo_write(dict_tempo, dict_sancto, ordo_year, even_year, year_letter, ordo_start, nb_days, date_paques, christ_roi)

