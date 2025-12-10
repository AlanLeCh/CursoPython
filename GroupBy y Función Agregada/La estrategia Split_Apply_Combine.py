#Importamos la libreria
import pandas as pd

#Buscamos el archvio csv
df_car = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/GroupBy y Función Agregada/Car_sales.csv")

#Mostramos el resultado
print (df_car)

#Tipos de Vehiculos
print(df_car['Vehicle_type'].value_counts())

