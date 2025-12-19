#Importamos la libreria
import pandas as pd

#Buscamos el archvio csv
df_car = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/GroupBy y Función Agregada/Car_sales.csv")

#Resultados de DataFrame
print(df_car)

#Modificar los miles de la columna Sales_in_thousands
Miles_Sales_Thousands = df_car.groupby('Manufacturer').sum().apply(lambda x:x*1000)[['Sales_in_thousands', 'Price_in_thousands']]

#Mostrando resultado
print(Miles_Sales_Thousands) 

#Restar valores de la media a cada grupo
media = df_car.groupby('Manufacturer')[['Engine_size','Fuel_capacity','Horsepower','Price_in_thousands','Sales_in_thousands']].apply(lambda x:x-x.mean())

#Mostrando resultado
print(media)
