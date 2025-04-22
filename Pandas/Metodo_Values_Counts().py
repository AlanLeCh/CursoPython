#Leyendo el archivo CSV
import pandas as pd

df_Estudiantes = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Pandas/StudentsPerformance.csv')
print(df_Estudiantes)

#Contar los elementos en la columna "gender"

#función len

len(df_Estudiantes['gender'])

#metodo .count()

df_Estudiantes['gender'].count()

#Contar los elementos "gender" por categoria

df_Estudiantes['gender'].value_counts()

#Obtener la frecuncia relativa  (dividir todos los valores entre la suma)
df_Estudiantes['gender'].value_counts(normalize=True)

#Contar los elementos de la columna "parental level of education" por categoría

df_Estudiantes['parental level of education'].value_counts()

#Obtener la frecuncia relativa  (dividir todos los valores entre la suma)
df_Estudiantes['parental level of education'].value_counts(normalize=True)
