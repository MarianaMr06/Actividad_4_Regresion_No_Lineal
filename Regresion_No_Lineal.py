#Cargamos librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as special
from scipy.optimize import curve_fit
import seaborn as sns
from sklearn.metrics import r2_score

#Carga de Archivos
credicel = pd.read_excel("Copia de df_limpio.xlsx")
credicel.info()

#Base sin edad negativa
credicel_edad = credicel[credicel["edad_cliente"] >= 0]
print(credicel_edad.info())

#Definimos variables
y_riesgo = credicel["riesgo"]
y_score_buro_ed = credicel_edad["score_buro"]
y_porc_eng = credicel["porc_eng"]
y_limite_credito = credicel["limite_credito"]

#riesgo
    #score_buro

#score_buro
    #edad_cliente

#porc_eng
    #costo_total

#limite_credito
    #precio

x_score_buro = credicel["score_buro"]
x_edad_cliente_edad = credicel_edad["edad_cliente"]
x_costo_total = credicel["costo_total"]
x_precio = credicel["precio"]


