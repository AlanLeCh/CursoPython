#Importando libreria
import pandas as pd

#Leer el archvio csv
Netflix = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Proyecto #3Limpieza de Datos con Pandas/netflix_titles.csv')

#Leer el archvio
print(Netflix)

#Mostrar el tipo de dayo
Netflix.info()




