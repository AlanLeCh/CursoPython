#Importamos la libreria Pandas
import pandas as pd

#Buscamos el archvio csv
df_car = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/GroupBy y Función Agregada/Car_sales.csv")

#Mostramos el resultado
print (df_car)

#Agruparemos por Manufacturer
df_car_groupby = df_car.groupby('Manufacturer')

#Mostrando resultado
print(df_car_groupby)

#Mostrando un formato de tipo diccionario
df_tipo_diccionario = df_car_groupby.groups

#Mostrando resultado
print(df_tipo_diccionario)

#Obtener las llaves del diccionario
df_tipo_diccionario = df_car_groupby.groups.keys()

#Mostrando las llaves
print(df_tipo_diccionario)

#Muestra  todo lo relacionado a la manufacturera
Resultado_Manufacture = df_car_groupby.get_group('Ford')

#Mostrando resultado
print(Resultado_Manufacture)

#Agrupar por manufacturera y saber el promedio+
Promedio_Manufacturer = df_car_groupby.groups('Manufacturer').mean()

#Mostrando resultado
print(Promedio_Manufacturer)