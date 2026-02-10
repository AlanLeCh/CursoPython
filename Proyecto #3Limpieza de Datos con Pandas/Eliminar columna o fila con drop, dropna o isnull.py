#Importando libreria
import pandas as pd

#Leer el archvio csv
Netflix = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Proyecto #3Limpieza de Datos con Pandas/netflix_titles.csv')

#######################Manejo de Data Faltante, hay 3 metodos distintos drop, dropna o isnull

#Hacer copia del DataFrame original
Netflix_cleaned2 = Netflix.copy()

#Eliminar columna o fila con drop, dropna o isnull
Netflixx = Netflix.drop('director', axis=1)

#Mostrar el DataFrame sin la columna director
print(Netflixx) 

#Eliminar filas con datos faltantes en la columna director
Netflixy = Netflix[Netflix['director'].isnull()].index
Netflix.drop(Netflixy, axis=0)


#Mostrar el DataFrame sin las filas con datos faltantes en la columna director
print(Netflix)

#hacer drop de las filas con datos faltantes en la columna director
Netflixz = [~(Netflix['director'].isnull())]

#Mostrar el data
print(Netflixz)

Netflixz.dropna(subset = ['director'])




