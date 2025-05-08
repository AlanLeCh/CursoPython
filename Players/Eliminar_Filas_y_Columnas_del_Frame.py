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

                                                            #1 Eliminar filas
#Eliminar una fila, con parametro "AXIS"

Player.drop('L. Messi', axis=0)

#Parametro index

Player.drop(index=['L. Messi'])

#Eliminar dos o más filas y actualizar data (inplace_True)

Player.drop(index=['L. Messi','Cristiano Ronaldo'], inplace=True)

#Con AXIS
Player.drop(['L. Messi','Cristiano Ronaldo'], axis=0, inplace=True)

#Mostrar resultado

print(Player)

                                                            #2 Eliminar Columna

#Eliminar una columna, con parametro "AXIS"

Player.drop('long_name', axis=1)

#Parametro columns

Player.drop(columns=['long_name'])


#Eliminar columna por posición/index (eliminar ultima columna)

Player.columns[[-2]]

Player.drop(Player.columns[[-2]], axis=1)

#Eliminar dos o más columnas y actualizar data (inplace=true)
Player.drop(['long_name','dob'], axis=1, inplace=True)

#Mostramos el resultaod
print(Player)