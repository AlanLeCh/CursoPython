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


                                                            #1 Seleccionar con un valor LOC[NOMBRE_FILA, NOMBRE_COLUMNA]
#Obtener toda la data sobre L.Messi.

Player.loc['L. Messi']

#Obtener el tamaño de L.Messi.

Player.loc['L. Messi', 'height_cm']

#Obtener el peso de Cristiano Ronaldo.

Player.loc['Cristiano Ronaldo', 'weight_kg']

#Obtener todas las filas dentro de columna 'height_com'

Player.loc[:, 'height_cm']

#Obtener todas las columnas que correspondan al index 'L.Messi'

Player.loc['L. Messi', :]


                                                            # 2. Seleccionar con una lista de valores 

#Obtener data sobre L. Messi y Cristiano Ronaldo.

Player.loc[['L. Messi','Cristiano Ronaldo']]

#Obtener el tamaño de L. Messi y Cristiano Ronaldo.

Player.loc[['L. Messi', 'Cristiano Ronaldo'], 'height_cm']

#Obtener el tamaño y peso de L. Messi

Player.loc['L. Messi', ['height_cm', 'weight_kg']]

#Obtener el tamaño y peso de L. Messi y Cristiano Ronaldo.

Player.loc[['L. Messi', 'Cristiano Ronaldo'], ['height_cm', 'weight_kg']]


                                                        # 3. Seleccionar un rango de data coon un slice (rebanada)
                                            #START:STOP:STEP (NOTA: Contrariamente a las rebanadas tipicas en Python, "start" y "stop" en este caso son incluidos)

#Hacer slice a nombre de columnas
jugadores = ['L. Messi', 'Cristiano Ronaldo']
Player.loc[jugadores, 'age':'club']

#Hacer slice a los nombres de los index
columnas = ['age', 'dob', 'height_cm','weight_kg']

#Obtener los nombres de jugadores top1 y top10

Player.index[:10]

Player.loc['L. Messi':'M. Salah',columnas]

                                                        # 4 Seleccionar con Condiciones
#Una condición: seleccionar jugadores con tamaño arriba de 180cm
columna = ['age', 'dob', 'height_cm','weight_kg']

Player.loc[Player['height_cm'] >180, columna]


#Multiples condicones: Seleccionar jugadores con tamaño arriba de 180cm y que sean de Argentina

Player['height_cm'] >180
Player['nationality'] == 'Argentina'

Player.loc[(Player['height_cm'] > 180) & (Player['nationality'] == 'Argentina'), :]