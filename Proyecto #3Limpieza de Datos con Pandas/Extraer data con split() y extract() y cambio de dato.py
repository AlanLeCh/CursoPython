#Importando libreria
import pandas as pd

#Leer el archvio csv
Netflix = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Proyecto #3Limpieza de Datos con Pandas/netflix_titles.csv')

print(Netflix)

#Extrer data de columna "duration" con metdos split() y extract()
df_movie2 = Netflix[Netflix['type']=='Movie']

#Mostrar las primeras filas
print(df_movie2)

#Extraer  soo los números de la columna "duration"
df_duracion_movie = df_movie2['duration'].str.split(expand=True)[0]

#Mostrando resultado
print(df_duracion_movie)

#Mostrar el tipo de dato df_duracion_movie.dtypes
print(df_movie2.dtypes)

df_separacion = df_movie2['date_added'].str.split(',', expand=True)
#Mostrando resultado
print(df_separacion)

df_version_difernete = df_movie2['date_added'].str.split(pat='\d{4}', expand=True)
#Motrando resultado
print(df_version_difernete)

#Metodo extract() 
df_extract = df_movie2['date_added'].str.extract(r'(\d{4})')












