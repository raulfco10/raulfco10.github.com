#Plantilla para preprocesado de datos
#Importar dataset
dataset = read.csv('Data.csv')

#Tratamiento de datos faltantes NaN por medio de sustituirlos por la media
dataset$Age = ifelse(is.na(dataset$Age), 
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary), 
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)