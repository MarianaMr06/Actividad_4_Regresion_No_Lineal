#Cargamos librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as special
from scipy.optimize import curve_fit
import seaborn as sns
from sklearn.metrics import r2_score
import math

#Carga de Archivos
credicel = pd.read_excel("Copia de df_limpio.xlsx")
credicel.info()

#Relaciones
    #riesgo
        #score_buro modelo 1
        #precio modelo 2 
        #costo_total modelo 3
        #monto_financiado modelo 4
        #puntos modelo 5

    #score_buro
        #edad_cliente todos los modelos

#Base riesgo y score
credicel_riesgo_score = credicel[(credicel["riesgo"] > 0) & (credicel["score_buro"] > 0)]
print("CREDICEL RIESGO SCORE", credicel_riesgo_score.head())

#Base riesgo y precio
credicel_riesgo_precio = credicel[(credicel["riesgo"] > 0) & (credicel["precio"] > 0)]
print("CREDICEL RIESGO PRECIO", credicel_riesgo_precio.head())

#Base riesgo y costo_total
credicel_riesgo_costo_total = credicel[(credicel["riesgo"] > 0) & (credicel["costo_total"] > 0)]
print("CREDICEL RIESGO COSTO TOTAL", credicel_riesgo_costo_total.head())

#Base riesgo y monto_financiado
credicel_riesgo_monto_financiado = credicel[(credicel["riesgo"] > 0) & (credicel["monto_financiado"] > 0)]
print("CREDICEL RIESGO MONTO FINANCIADO", credicel_riesgo_monto_financiado.head())

#Base riesgo y puntos
credicel_riesgo_puntos = credicel[(credicel["riesgo"] > 0) & (credicel["puntos"] > 0)]
print("CREDICEL RIESGO PUNTOS", credicel_riesgo_puntos.head())

#Base sin edad negativa o 0s y score 
credicel_edad = credicel[(credicel["edad_cliente"] >= 0) & (credicel["score_buro"] > 0)]
print("CREDICEL EDAD SCORE", credicel_edad.head())

#Definimos variables
y_riesgo_score = credicel_riesgo_score["riesgo"]
x_riesgo_score = credicel_riesgo_score["score_buro"]

y_riesgo_precio = credicel_riesgo_precio["precio"].values
x_riesgo_precio = credicel_riesgo_precio["riesgo"].values

y_riesgo_costo_total = credicel_riesgo_costo_total["riesgo"]
x_riesgo_costo_total = credicel_riesgo_costo_total["costo_total"]

y_riesgo_monto_financiado = credicel_riesgo_monto_financiado["riesgo"]
x_riesgo_monto_financiado = credicel_riesgo_monto_financiado["monto_financiado"]

y_riesgo_puntos = credicel_riesgo_puntos["riesgo"]
x_riesgo_puntos = credicel_riesgo_puntos["puntos"]

y_edad_score = credicel_edad["score_buro"]
x_edad_score = credicel_edad["edad_cliente"]

#Modelos
    #cuadratica: y = ax^2 + bx + c
    #exponencial: y = a*exp(bx) + c
    #inversa: y = 1/a*x          
    #logaritmica: y = a*np.log(x) + b
    #polinomial_inversa: y = a/b*x**2 + c*x 

#Definimos funciones
    #Cuadrática
def funcion_cuadratica (x, a, b, c):
    return a*x**2 + b*x + c

#Exponencial
def funcion_exponencial (x, a, b, c):
    return a * np.exp(b * x) + c

#Inversa
def funcion_inversa (x, a):
    return 1/a*x

#Logaritmica
def funcion_logaritmica (x, a, b):
    return a * np.log(x)+b

#Polinomial Inversa
def funcion_polinomial_inversa (x, a, b, c):
    return a/b*x**2 + c*x

#MODELOS de RIESGO
#Riesgo y Score Buró funcion cuadratica
print("CORRELACION RIESGO Y SCORE BURO")
parametros, covs = curve_fit(funcion_cuadratica, x_riesgo_score, y_riesgo_score)
print("Parametros: ", parametros)
    #modelo
parametros, _ = curve_fit(funcion_cuadratica, x_riesgo_score, y_riesgo_score)
a, b, c = parametros[0], parametros[1], parametros[2]
modelo_riesgo_buro = a * x_riesgo_score ** 2 + b * x_riesgo_score + c
R2_modelo_riesgo_score = r2_score(y_riesgo_score, modelo_riesgo_buro)
print("R2: ", R2_modelo_riesgo_score)

# Riesgo y precio
#Arreglos a Numpy
x_riesgo_precio = np.array(x_riesgo_precio)
y_riesgo_precio = np.array(y_riesgo_precio)
print("CORRELACION RIESGO Y PRECIO")
parametros, covs = curve_fit(funcion_exponencial, x_riesgo_precio, y_riesgo_precio)
print("Parámetros: ", parametros)
# Modelo
parametros, _ = curve_fit(funcion_exponencial, x_riesgo_precio, y_riesgo_precio)
a, b, c = parametros[0], parametros[1], parametros[2]
modelo_riesgo_precio = a * np.exp(b * x_riesgo_precio) + c
R2_modelo_riesgo_precio = r2_score(y_riesgo_precio, modelo_riesgo_precio)
print("R2 del modelo Riesgo Precio:", R2_modelo_riesgo_precio)

#riesgo y puntos Inversa
print("CORRELACION RIESGO Y PUNTOS")
parametros, covs = curve_fit(funcion_inversa, x_riesgo_puntos, y_riesgo_puntos)
print("Parámetros: ", parametros)
# Modelo
a = parametros
modelo_riesgo_puntos = 1/a*x_riesgo_puntos
R2_modelo_riesgo_puntos = r2_score(y_riesgo_puntos, modelo_riesgo_puntos)
print("R2 para el modelo Riesgo Puntos:", R2_modelo_riesgo_puntos)

#Riesgo y monto_financiado Logaritmica
print("CORRELACION RIESGO Y MONTO FINANCIADO")
parametros, covs = curve_fit(funcion_logaritmica, x_riesgo_monto_financiado, y_riesgo_monto_financiado)
print("Parámetros: ", parametros)
# Modelo
a, b = parametros[0], parametros[1]
modelo_riesgo_monto_financiado = a * np.log(x_riesgo_monto_financiado)+b
R2_modelo_riesgo_monto_financiado = r2_score(y_riesgo_monto_financiado, modelo_riesgo_monto_financiado)
print("R2 para el modelo Riesgo Monto financiado:", R2_modelo_riesgo_monto_financiado)

#Riesgo y costo_total polinomial inversa
print("CORRELACION RIESGO Y COSTO TOTAL")
parametros, covs = curve_fit(funcion_polinomial_inversa, x_riesgo_costo_total, y_riesgo_costo_total)
print("Parámetros: ", parametros)
# Modelo
a, b, c = parametros[0], parametros[1], parametros[2]
modelo_riesgo_costo_total = a/b*x_riesgo_costo_total**2 + c*x_riesgo_costo_total
R2_modelo_riesgo_costo_total = r2_score(y_riesgo_costo_total, modelo_riesgo_costo_total)
print("R2 para el modelo Riesgo Monto financiado:", R2_modelo_riesgo_costo_total)