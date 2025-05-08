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

                                                                                        # 1 COPY()
                                                                                    #1.1 DEEP = TRUE

#DEEP=TRUE por defecto (Las modificaciones a la data o indices de la )

Player_copy = Player.copy()

#Actualizar valor en el DataFrame Original

Player.loc['L. Messi', 'height_cm'] = 180
print(Player)

#Copia vs DataFrame Original

print(Player_copy)

                                                                                        #1.2 DEEP = FALSE

#DEEP=FALSE por defecto (Las modificaciones a la data o indices de la )

Player_shallow_copy = Player.copy(deep=False)

#Actualizar valor en el DataFrame Original

Player.loc['Cristiano Ronaldo', 'height_cm'] = 200

print(Player)

#Copia vs DataFrame Original

print(Player_shallow_copy)

                                                                                        # 1.3 Asignación Simple
                                                                                        
#Hcaer copia 

Player_nueva_copy = Player

#Actualizar valores en el DataFrame Original

Player.loc['Neymar Jr','height_cm'] = 190

#Copia vs DataFrame Original

print(Player)

print(Player_nueva_copy)

