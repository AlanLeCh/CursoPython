#Importar la librería pandas
import pandas as pd

#Leer el archivo csv
Player = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Players/players_20.csv')

#Leer archivo csv y guardar en un dataframe
print(Player)

#fijar index
Player = Player.set_index('short_name')

#SELECCIONAR UNA COLUMNA
Player = Player[['long_name','age','dob','height_cm','weight_kg','club','nationality']]

#Mostrar resultado
print(Player)

                                                                            #1 Query()

#Seleccionar jugadores mayores a 34 años

Player.query('age>34')

#Ejercicio: Escribir el equivalente SLICING BOOLEANO

Player[Player['age']>34]

#Seleccionar jugadores mayores a 34 años de Italia

Player.query('age>34 and nationality== "Italy" ') 

#Ejercicio: Escribir el equivalente SLICING BOOLEANO

Player[(Player['age']>34) & (Player['nationality'] == 'Italy')]


#Agregar un operador de negación al primer ejemplo

Player.query("not (age>34)")

#Ejercicio: Escribir el equivalente SLICING BOOLEANO


#Convertir la altura a metros y seleccionar aquellos que midan mas de 1.80

Player.query('height_cm/100 >1.8')

#Ejercicio: Escribir el equivalente SLICING BOOLEANO

Player['height_cm']/100 >1.8

#Seleccionar jugadores que nacieron antes de 1990
#Revisar el tipo de data
Player.dtypes

#Convertir el tipo de data e la columna "dob" a datetime

Player['dob'] = Player['dob'].astype('datetime64[ns]')

#Query

Player['dob'].dt.year

#Ejercicio: escribir el equivalente SLICING BOOLEANO