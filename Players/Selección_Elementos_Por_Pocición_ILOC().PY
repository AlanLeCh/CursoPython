#Importar la librería pandas
import pandas as pd

#Leer el archivo csv
Player = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Players/players_20.csv')

#Leer archivo csv y guardar en un dataframe
print(Player)

#SELECCIONAR UNA COLUMNA
Player = Player[['long_name','age','dob','height_cm','weight_kg','club','nationality']]

#fijar index
Player = Player.set_index('short_name')

print(Player)

                                                                            #1 Seleccionar con un valor
                                                                        #LOC[NOMBRE_FILA, NOMBRE_COLUMNA]
            
#Obtener el tamaño de L. Messi.

Player.iloc[0,3]

#Obtener el peso de Cristiano Ronaldo.
Player.iloc[1,4]

#Obtener todas lasa filas dentro de columna 'height_com'
Player.iloc[:,3]

#Obtener todas las columnas que correspondan al index 'L.Messi'

Player.iloc[0,:]


                                                                        #2 SELECCIONAR CON UNA LISTA DE VALORES

#Obtener data sobre L. Messi y Cristiano Ronaldo.
Player.iloc[[0,1], :]

#Obtener el tamaño de L. Messi y Cristiano Ronaldo.
Player.iloc[[0,1],3]

#Obtener el tamaño y peso de L. Messi
Player.iloc[[0],[3,4]]

#Obtener el tamaño y peso de L. Messi y Cristiano Ronaldo.
Player.iloc[[0,1],[3,4]]

                                                                        # 3. Seleccionar un rango de data coon un slice (rebanada)
                                            #START:STOP:STEP (NOTA: Contrariamente a las rebanadas tipicas en Python, "start" y "stop" en este caso son incluidos)

#Hacer slice a nombre de columnas
Jugadores = [0,1]
Player.iloc[Jugadores,0:6]

#Hacer slice a los nombres de los index
columnas = [1, 2, 3,4]

#Obtener los nombres de jugadores top1 y top10
Player.index[0:10]
Player.iloc[0 : 18274, columnas]

                                                                            # 4 Seleccionar con Condiciones

#Una condición: seleccionar jugadores con tamaño arriba de 180cm

columna = [0, 1, 2, 3]
Player.iloc[list(Player['height_cm'] >180), columna]


#Multiples condicones: Seleccionar jugadores con tamaño arriba de 180cm y que sean de Argentina

Player['height_cm']> 180
Player['nationality'] == 'Argentina'

Player.iloc[list(Player['height_cm']> 180 & (Player['nationality'] == 'Argentina')), :]

