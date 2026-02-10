#Importando libreria
import pandas as pd

#Leer el archvio csv
Netflix = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Proyecto #3Limpieza de Datos con Pandas/netflix_titles.csv')

#Leer el archvio
print(Netflix)

#Mostrar el tipo de dayo
Netflix.info()
#Mostrar los datos faltantes
print(Netflix.isnull())

#Sumar los datos faltantes
print(Netflix.isnull().sum())

# Mostrar el % de filas faltantes en cada columna
for column in Netflix.columns:
    percentage = Netflix[column].isnull().mean()
    print(column +':' + str(percentage))

    
    



