# 5 Normalización de Texto

#5.3 Remplazar cadena de texto con replace() o sub()

#Importando libreria
import pandas as pd
import matplotlib.pyplot as plt

#Leer el archvio csv
Netflix = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Proyecto #3Limpieza de Datos con Pandas/netflix_titles.csv')

#Eliminar signos de puntuación con el metodo str.replace() y regex
Eliminar_signos_de_puntuación = Netflix['title'].str.replace('[^\w\s]','',regex=True)

print(Eliminar_signos_de_puntuación)

#Eliminar puntuación con el metodo replace() y regex
Eliminar_signos_regex = Netflix.replace('[^\w\s]','',regex=True)

#Diferencia entre str.replace() y replace()
Eliminar_signos_replace = Netflix.replace(1, 2, regex=False)
print(Eliminar_signos_replace)

#Elimionar puntuación con la función re.sub() con el metodo apply
import re

Eliminacion_resub = Netflix['title'].apply(lambda x:re.sub('[^\w\s]','',x))
print(Eliminacion_resub)