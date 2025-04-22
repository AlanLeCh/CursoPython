#Leyendo el archivo CSV
import pandas as pd

df_Estudiantes = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Pandas/StudentsPerformance.csv')
print(df_Estudiantes)

                                                        #Seleccionando 1 columna SINTAXIS 1

#Seleccionar una columna con [] (forma periferica de seleccionar una columna)
print(df_Estudiantes['gender'])

#Revisar el tippo de data de una columna
print(type(df_Estudiantes['gender']))

                                                                    #SYNTAX 2

#Seleccionar una columna con (.)
print(df_Estudiantes.gender)

#Seleccionar una columna con [] 
print(df_Estudiantes['math score'])