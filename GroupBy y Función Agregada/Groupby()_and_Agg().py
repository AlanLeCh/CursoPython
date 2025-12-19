#Importamos la libreria
import pandas as pd

#Buscamos el archvio csv
df_car = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/GroupBy y Función Agregada/Car_sales.csv")

#Resultados de DataFrame
print(df_car)

#Calcular a la vez el max y min
df_car.groupby('Vehicle_type').agg(['min','max'])

print(df_car)

#Agrupación
df_car.groupby('Vehicle_type').agg(min_engine_size = ('Engine_size','min'),max_horsepower = ('Horsepower','max'))

#impresion del resultado
print(df_car) 

#Agrupación del DataFrame por manufacturación, ventas y precios
Agrupacion = df_car.groupby('Manufacturer').agg (suma_sales = ('Sales_in_thousands', 'sum'), mean_price = ('Price_in_thousands','mean'))

#Se imprime el DataFrame
print(Agrupacion)
