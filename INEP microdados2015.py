# -*- coding: utf-8 -*-
"""
Microdados Censa Ed Superior 2015
@author: Ester Pereira Martins
"""
import pandas as pd
import numpy as np
import os

os.listdir()

edsup2015 = pd.read_csv("DM_CURSO.CSV", sep = "|", encoding = "latin1")
edsup2015.shape
edsup2015.columns

nova = edsup2015.loc[:,["NO_CURSO"]]

nova.NO_CURSO.describe

nova = edsup2015.loc[:,["NO_IES","DS_CATEGORIA_ADMINISTRATIVA",
                        "DS_ORGANIZAÇÃO_ACADÊMICA","NO_MUNICIPIO_CURSO",
                        "SGL_UF_CURSO","NO_CURSO", "QT_MATRICULA_CURSO",
                        "QT_CONCLUINTE_CURSO", "QT_INGRESSO_CURSO"]]

nova.NO_IES.value_counts()
nova.DS_CATEGORIA_ADMINISTRATIVA.value_counts()
nova.QT_MATRICULA_CURSO.describe()
nova.QT_CONCLUINTE_CURSO.describe
nova.QT_INGRESSO_CURSO.describe

