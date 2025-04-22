#Leyendo el archivo CSV
import pandas as pd

df_Estudiantes = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Pandas/StudentsPerformance.csv')
print(df_Estudiantes)

#ordenar por columna asendente
df_Estudiantes.sort_values(by = 'math score')

#ordenar por columna descendiente
df_Estudiantes.sort_values('math score',ascending=False)

#Ordenar por descendientes multiples tablas
df_Estudiantes.sort_values(['math score', 'reading score', 'writing score'],ascending=False,
                           inplace=True)

#Mostrar resultado
print(df_Estudiantes)
