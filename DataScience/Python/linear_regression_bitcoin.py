#Regresion lineal Simple

#Plantilla de preprocesado

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importar el dataset
dataset = pd.read_csv('BTC_historical.csv')
"""data_type = {'Open':'float',
             'High':'float',
             'Low':'float',
             'Close':'float',
             'Volume':'int64',
             'Market Cap':'int64'}

dataset['Date'] = dataset['Date'].apply(lambda x:x.replace(',',''))
dataset['Open'] = dataset['Open'].apply(lambda x:x.replace(',',''))
dataset['High'] = dataset['High'].apply(lambda x:x.replace(',',''))
dataset['Low'] = dataset['Low'].apply(lambda x:x.replace(',',''))
dataset['Close'] = dataset['Close'].apply(lambda x:x.replace(',',''))
dataset['Volume'] = dataset['Volume'].apply(lambda x:x.replace(',',''))
dataset['Volume'] = dataset['Volume'].apply(lambda x:x.replace('-','0'))
dataset['Market Cap'] = dataset['Market Cap'].apply(lambda x:x.replace(',',''))

dataset.astype(data_type)"""
X=dataset.iloc[:,5:6].values #Todas las columnas excepto la ultima
y=dataset.iloc[:,1].values



#Dividir el dataset en entrenamiento y testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0) #Por la cantidad tan pequena de la muestra se usara un 33% de texting

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
#y_pred = regression.predict(X_test)
y_pred = regression.predict([[20000000000]])

#Visualizar los resultados de entrenamiento
plt.scatter(X_train, y_train, color = "red")
plt.plot(X_train, regression.predict(X_train), color = "blue")
plt.title("Precio vs Volumen (Conjunto de entrenamiento)")
plt.xlabel("Volumen")
plt.ylabel("Precio (USD)")
plt.show()

#Visualizar los resultados de test
plt.scatter(X_test, y_test, color = "red")
plt.plot(X_train, regression.predict(X_train), color = "blue")
plt.title("Precio vs Volumen (Conjunto de testing)")
plt.xlabel("Volumen")
plt.ylabel("Precio (USD)")
plt.show()