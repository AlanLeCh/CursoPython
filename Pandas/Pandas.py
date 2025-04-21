# importamos dos librerias PANDAS y NUMPY
import pandas as pd
import numpy as np

#Crear un Arrays
data = np.array([[1,4],[2,5],[3,4]])

#Acomodando y dandole nombres
df = pd.DataFrame(data, index=['row1', 'row2', 'row3'],
                columns=['col1', 'col2'])
print(df)

import pandas as pd
#Creando el mismo pero en forma de lista
data = [[1,4],[2,5],[3,4]]

#Acomodando y dandole nombres
dfi = pd.DataFrame(data, index=['row1', 'row2', 'row3'],
                columns=['col1', 'col2'])
print(dfi)

import pandas as pd
#Listas
states = ['CALIFORNIA', 'TEXAS', 'FLORIDA', 'NEW YORK']
populatipon = [396134963,29730311,219444577,19299981]

#Almacenando lista en diccionario
dict_states = {'\nStates': states, 'population':populatipon}

#Creando el DataFramne
df_population = pd.DataFrame(dict_states)
print(df_population)

#Creando DataFrame con archivo CSV

#Leyendo el archivo CSV
import pandas as pd

df_Estudiantes = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Pandas/StudentsPerformance.csv')
print(df_Estudiantes)

#Mostrar primero las 5 filas del dataframe
print(df_Estudiantes.head())

# Mostrar los ultimos 5 filas del dataframe
print(df_Estudiantes.tail())

# Mostrar las ultimas N filas del dataframe
print(df_Estudiantes.head(10))

#Accediendo al atributo shape
pd.set_option('display.max_rows',1000)

