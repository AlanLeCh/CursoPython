#Leyendo el archivo CSV
import pandas as pd

df_Estudiantes = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Pandas/StudentsPerformance.csv')
print(df_Estudiantes)

                                                    # SELECCIONAR DOS O MÁS COLUMNAS 

# Seleccionar 2 columnas usando [[]]
print(df_Estudiantes[['gender', 'math score']])

#revisar el tipo de data de la seleccion
print(type(df_Estudiantes[['gender','math score']]))

# Seleccionar 2 columnas usando [[]]
print(df_Estudiantes[['gender', 'math score','reading score','writing score']])