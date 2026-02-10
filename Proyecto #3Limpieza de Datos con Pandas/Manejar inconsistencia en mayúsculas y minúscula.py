# 5 Normalización de Texto

#5.1 Manejar inconsistencia en mayúsculas / minusculas: lower(), upper() y title()

#Importando libreria
import pandas as pd
import matplotlib.pyplot as plt

#Leer el archvio csv
Netflix = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Proyecto #3Limpieza de Datos con Pandas/netflix_titles.csv')

#Cambiar mayusculas / minusculas con el atributo srt
Titulos_Minuscula = Netflix['title'].str.lower()
Titulo_Mayuscula = Netflix['title'].str.upper()
titulo_InicioMayuscula  =Netflix['title'].str.title()
#Mostrar resultado
print(Titulos_Minuscula)
print(Titulo_Mayuscula)
print(titulo_InicioMayuscula)

#Actualizar valores
Netflix ['title']= Netflix['title'].apply(lambda x:x.title())

print(Netflix)