#importar la libreria pandas
import pandas as pd

#Imporando el archivo de excel.
df_car = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/GroupBy y Función Agregada/Car_sales.csv")

#Leer archivo
print(df_car)

#Seleccionar las columnas que se van a utilizar
df_car = df_car[['Manufacturer','Sales_in_thousands','Vehicle_type','Price_in_thousands','Engine_size','Horsepower','Fuel_capacity']]

#Mostando el resultado del filtrado
print(df_car)

#Mostrar las cantidades de manufactureras de los autos
print(df_car.nunique())