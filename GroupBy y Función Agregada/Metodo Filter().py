#Importamos la libreria
import pandas as pd

#Buscamos el archvio csv
df_car = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/GroupBy y Función Agregada/Car_sales.csv")

#Resultados de DataFrame
print(df_car)

#Crear una función
def filter_fun(x):
    return x['Sales_in_thousands'].sum() >52 #Columna Sales_Thousands tiene que ser mayor a 52

#Filtrar por la función
df_filter = df_car.groupby(['Manufacturer']).filter(filter_fun)

#Mostrando resultado
print(df_filter)

#Calcular cuales fueron filtrados de menor a mayor
Datos_filtrados = df_car.groupby(['Manufacturer']).sum()['Sales_in_thousands'].sort_values()

#Mostrar los datos riltrados
print(Datos_filtrados)

#Calcular cuales fueron filtrados de menor a mayor y mostrar solo los 7 primeros
Datos_filtrados = df_car.groupby(['Manufacturer']).sum()['Sales_in_thousands'].sort_values().head(7)

#Mostrando los 7 priemros
print(Datos_filtrados) #Estos no deberian estar en los filtrados de la función: Porsche 12.128, Jaguar 15.467, Saab 21.306, Infiniti 23.713, Audi 40.557, BMW 46.505.

#Verificar si en verdad si fueron filtrados
filtrados_car = df_car['Manufacturer'].isin(['Porsche','Jaguar','Saab','Infiniti','Audi','BMW'])

#Mostrar si enverdad fueron filtrados
print(filtrados_car)

#Calcular el DataFrame 
print(filtrados_car.shape)



