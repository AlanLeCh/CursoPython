#Importando libreria
import pandas as pd

#Leer el archvio csv
Netflix = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Proyecto #3Limpieza de Datos con Pandas/netflix_titles.csv')


#Remplazar por la mediana (data numerica) y moda (data categorica)
df_repetdios = Netflix ['rating'].mode()

#Mostrar los repetidos
print(df_repetdios)

#Convirtiendo la serie en cadena de texto con join
df_repetdios = Netflix ['rating'].mode() [0]
print(df_repetdios)

#Mostrando y remplazando los NaN de la columna RATING
moda = Netflix ['rating'].mode() [0] 
Netflix ['rating'].fillna(moda,inplace=True)

print(Netflix.loc[5989])

#Reemplazar por número arbitrario con .fillna()
Netflix['duration'].fillna(0,inplace=True)

#Otros metodos de los cuales ayudan a rellenar los campos NaN. el primero bfill llena de abajo hacía arriba y el segundo ffill llena de arriba hacía abajo
Netflix.fillna(method = 'bfill') #backward fill

#Muestra el DataFrame con los campos NaN rellenados con el método bfill
print(Netflix)

#Rellenar los campos NaN con el método ffill
Netflix.fillna(method = 'fill') #forward fill

#Muestra el DataFrame con los campos NaN rellenados con el método ffill
print(Netflix)

