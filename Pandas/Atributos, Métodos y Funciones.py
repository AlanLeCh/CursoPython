#Leyendo el archivo CSV
import pandas as pd

df_Estudiantes = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Pandas/StudentsPerformance.csv')
print(df_Estudiantes)

# Obtener acceso al atributo shape
print(df_Estudiantes.shape)

# Obtener acceso al atrtibuto Index
print(df_Estudiantes.index)

#Obtener acceso al atributo columns
print(df_Estudiantes.columns)

# tipo de datos de la columna
print(df_Estudiantes.dtypes)

# METODOS

#Mostrando las 5 primeras filas
print(df_Estudiantes.head())

#mostrar información del DataFrame
print(df_Estudiantes.info())

#Obteniendo valores estadisticos del dataframe
print(df_Estudiantes.describe())

# FUNCIONES

#Muestra y obtiene las filas del DataFrame
print(len(df_Estudiantes))

#Muestra y Obtiene el maximo
print(max(df_Estudiantes.index))

#Muestra y Obtiene el maximo
print(min(df_Estudiantes.index))

#Obtener el tipo de dato
print(type(df_Estudiantes))

#Redondear valores del DataFrame
print(round(df_Estudiantes,2))