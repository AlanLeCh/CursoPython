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


print(Player)

                                                                        #Fijar valor a una Celda
#Actualizar altura de L. Messi

Player.loc['L. Messi', 'height_cm'] = 175

#Mostrar resultado
print(Player)


                                                                        #2 Fijar valor a toda la columna
#Fijar tamaño de 190 a todos los jugadores

Player.loc[:, 'height_cm'] = 190

#Mostrar resultado
print(Player)

                                                                        #3 Fijar valores a toda la fila

#Obtener todas las columnas que corresponden al los jugadores rankeado ultimo en fifa
Player.iloc[-2,:]

#Sin Iloc
Player.loc['Pan Ximing',:]


#Fijar valor nulo a todas las columnas que corresponden al jugador

import numpy as np

Player.iloc[-2,:] = np.nan

print(Player)

#Sin ILOC
Player.loc['Pan Ximing', :] = np.nan
print(Player)

                                                                    #4 Fijar valor a Multiples celdas

#Fijar valor a todos los items que hacen match con la lista de nombres

Player.loc[['L. Messi','Cristiano Ronaldo'], ['height_cm']] = 175

#Mostrar dataframe

print(Player)

                                                                    #5 Fijar valor para filas que cumplan una condición

#Fijar valores para filas que cumplen una condición
Columnas = ['age','dob','height_cm','weight_kg']

Player['height_cm']>180

Player.loc[Player['height_cm']>180, Columnas] = 0

#Mostrar resultado
print(Player)

