# 5 Normalización de Texto

#5.2 Eliminar espacios en blanco con strip(), Istrip() y rstrip()

#Importando libreria
import pandas as pd
import matplotlib.pyplot as plt

#Leer el archvio csv
Netflix = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Proyecto #3Limpieza de Datos con Pandas/netflix_titles.csv')

#Como el metodo strip() funciona
movie_title = ' Titanic                  '
print(movie_title)

#Eliminar espacios delanteros con lstrip ()
Sin_espacio = movie_title.lstrip()
print(Sin_espacio)

#Eliminar espacios finales con rstrip()
eliminar_espacios = movie_title.rstrip()
print(eliminar_espacios)

#Eliminar espacios delanteros y finales con strip()
Eliminar_delantero_y_final = movie_title.strip()
print(Eliminar_delantero_y_final)

#Eliminar espacios delanteros y finales con el metodo strip ()
Netflix['title'].str.strip()
print(Netflix)

#Eliminar espacios delanteros y finales cojn el metodo apply()
Netflix['title'].apply(lambda x:x.strip())
print(Netflix)
