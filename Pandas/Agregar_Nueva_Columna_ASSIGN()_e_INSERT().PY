#Leyendo el archivo CSV
import pandas as pd
import numpy as np
df_Estudiantes = pd.read_csv(' C:/Users/alanp/Desktop/CursoPython/Pandas/StudentsPerformance.csv')
print(df_Estudiantes)

                                                    #ASSIGN()

#Permite agregar multiples columnas en una sola línea de código
#cúando se necesita sobreescribir los valores existentes

#Crear números aleatorios
score1 = np.random.randint(1,100, size=1000)
score2 = np.random.randint(1,100, size=1000)

print(score1)
print(score2)

#crear una serie usando los numeros aleatorios

serie1 = pd.Series(score1, index=np.arange(0,1000))
serie2 = pd.Series(score2, index=np.arange(0,1000))
print(serie1)
print(serie2)

#Usando assign() para agregar multiples columnas
df_Estudiantes.assign(score1 = serie1, score2 = serie2)

# Guardar esos cambios definitivos
df_Estudiantes = df_Estudiantes.assign(score1=serie1, score2=serie2)

#Mostrando resultados
print(df_Estudiantes)

                                                        #INSERT()

# Nos permite insertar nueva columna en una posición especifica o en un index

#Usar insert() para adicionar una columna en una posición especifica
df_Estudiantes.insert(1, 'test', serie1)

#Mostrar el resultado

print(df_Estudiantes)