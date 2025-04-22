#Leyendo el archivo CSV
import pandas as pd

df_Estudiantes = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Pandas/StudentsPerformance.csv')
print(df_Estudiantes)


                                            # AGREGAR COLUMNA NUEVA

# Agregar una nueva columna al DataFrame
df_Estudiantes['language score'] = 70 

#Impresion
print(df_Estudiantes)

#Importar numpy

import numpy as np

#Crear un array de 1000 elemntos
language_score = np.arange(0,1000)
print(language_score)

# Agregar una columna nueva al dataframe con array
df_Estudiantes['language score'] = language_score
print(df_Estudiantes)

# Crear números enteros aleatorios entre 1 y 100
int_language_score = np.random.randint(1,100,size=1000)

#El minimo valor es inclusivo y el maximo valor es exclusivo
print(min(int_language_score))
print(max(int_language_score))

#Agregaer una nueva columna al data frame con un array

df_Estudiantes['language_score'] = int_language_score
print(df_Estudiantes)

#Crear números decimales aleatorios entre 1 y 100

np.random.uniform(1,100, size=1000)

df_Estudiantes['language_score'].round