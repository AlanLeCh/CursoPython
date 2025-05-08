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

                                                                                    # .apply()
#Usar función de numpy y aplicar a la serie
import numpy as np

Player['age'].apply(np.sqrt)

#Crear tu propia función y aplicar a el dataframe kg/m2

def calcular_imc(row):
    return row['weight_kg'] / ((row['height_cm']/100) ** 2)

Player.apply(calcular_imc, axis=1)