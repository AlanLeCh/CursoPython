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


                                                                                #1 Sample()

#Extraer 10 elementos aleatorios de la columna "Nationality"

Player['nationality'].sample(10)

#Extraer 20% de muestra aleatoria del DataFrame

Player.sample(frac=0.2)

#Incrementar la muestra -> frac>1 (Obs: el parametro replace tiene que ser TRUE cuando el parametro frac>1)

Player.sample(frac=2,replace=True)