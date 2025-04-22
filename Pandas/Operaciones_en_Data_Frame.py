#Leyendo el archivo CSV
import pandas as pd

df_Estudiantes = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Pandas/StudentsPerformance.csv')
print(df_Estudiantes)


                                                    #Operaciones

#Operaciones en Columna

#Selecionar una columna y calcular la suma total.

df_Estudiantes['math score'].sum()

#Contar, promedio, desv, estandar, maximo, minimo

df_Estudiantes['math score'].count()
df_Estudiantes['math score'].mean()
df_Estudiantes['math score'].std()
df_Estudiantes['math score'].max()
df_Estudiantes['math score'].min()

#calcula más rapido con .describe()
df_Estudiantes.describe()


                                                                #Operaciones en filas

#Calcula la suma en una fila

df_Estudiantes ['math score'] + df_Estudiantes ['reading score'] + df_Estudiantes ['writing score']

#Calcula el score promedio y asignar los resultados a una nueva columna
df_Estudiantes['average'] = (df_Estudiantes ['math score'] + df_Estudiantes ['reading score'] + df_Estudiantes ['writing score'])/3

#Mostrar el DataFrame

print(df_Estudiantes. round(2))
