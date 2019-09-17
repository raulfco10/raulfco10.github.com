# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:27:21 2019

@author: rbuenfil
"""

#Regresion lineal Simple

#Plantilla de preprocesado

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
import json
import time

#Leer la informacion desde bittrex
res = requests.get("https://api.bittrex.com/api/v1.1/public/getmarkethistory?market=USD-BTC")
j = res.json()

#print(j)
#Mandar resultado a un dataframe de pandas
#filename = "temp.csv"
df = pd.DataFrame(j["result"])
print(df.head())
df["TimeStamp"] = df["TimeStamp"].apply(lambda x: time.mktime(time.strptime(x[0:19], "%Y-%m-%dT%H:%M:%S")))

#Convertir a matriz tipo numpy
X=df.iloc[:,5:6].values #Columna de fecha
y=df.iloc[:,3].values

#Dividir el dataset en entrenamiento y testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_numeric, y, test_size = 0.3, random_state = 0) #Por la cantidad tan pequena de la muestra se usara un 33% de texting

#Escalado de Variables #Con regresion lineal simple no es necesario el escalado
#from sklearn.preprocessing import StandardScaler
#sc_X = StandardScaler()
#X_train = sc_X.fit_transform(X_train)
#X_test = sc_X.transform(X_test)

#Crear modelo de regresion lineal simple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

#Predecir el conjunto de test
y_pred = regression.predict(X_test)

#Visualizar los resultados de entrenamiento
plt.scatter(X_train, y_train, color = "red")
plt.plot(X_train, regression.predict(X_train), color = "blue")
plt.title("Precio a lo largo del tiempo (Conjunto de entrenamiento)")
plt.xlabel("Fecha")
plt.ylabel("Precio (USD)")
plt.show()

#Visualizar los resultados de test
plt.scatter(X_test, y_test, color = "red")
plt.plot(X_train, regression.predict(X_train), color = "blue")
plt.title("Precio a lo largo del tiempo (Conjunto de testing)")
plt.xlabel("Fecha")
plt.ylabel("Precio (USD)")
plt.show()