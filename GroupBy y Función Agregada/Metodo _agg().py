#Importamos la libreria
import pandas as pd

#Buscamos el archvio csv
df_car = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/GroupBy y Función Agregada/Car_sales.csv")

#Mostramos el resultado
print (df_car)

#Sumar y Mostrar el resultado
print(df_car.agg('sum'))

#Promedio y mostrar el resultado
promedio = df_car.select_dtypes(include='number').agg('mean')
print(promedio)

#Juntar Suma y Promedio
Ambas = df_car.select_dtypes(include='number').agg(['sum','mean'])

#Mostramos el resultado
print(Ambas)

#Diccionarios con agg
diccionario_agg = df_car.select_dtypes(include='number').agg({'Sales_in_thousands':['sum','mean'],
            'Price_in_thousands':['sum','max']})
#Mostrar resultado
print(diccionario_agg)

#Suma la venta y el precio por columna.
suma_porPrecio = df_car[['Sales_in_thousands','Price_in_thousands']].agg('sum', axis=1)
#Mostando resultado
print(suma_porPrecio)

#cambiar el nombre de la columna
cambio_nombre = df_car.select_dtypes(include='number').agg (x=('Sales_in_thousands','sum'),
                                                      y=('Price_in_thousands','mean'))
#Mostando resultado
print(cambio_nombre)
