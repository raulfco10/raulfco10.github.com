#Plantilla para preprocesado de datos
#Importar dataset
dataset = read.csv('Data.csv')

#Dividir los datos en conjunto de entrenamiento y test
#install.packages("caTools")#Instalar paquetes
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

#Escalado de valores
training_set[,2:3] = scale(training_set[,2:3])
testing_set[,2:3] = scale(testing_set[,2:3])