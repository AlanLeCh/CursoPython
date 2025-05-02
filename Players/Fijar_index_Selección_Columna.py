#Importar la librería pandas
import pandas as pd

#Leer el archivo csv
Player = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Players/players_20.csv')

#Leer archivo csv y guardar en un dataframe
print(Player)

#fijar index
Player = Player.set_index('short_name')

#Mostrar el dataframe
print(Player)

#Seleccionar una columnas
Player[['player_url', 'age', 'dob', 'height_cm', 'weight_kg', 'nationality', 'club']]