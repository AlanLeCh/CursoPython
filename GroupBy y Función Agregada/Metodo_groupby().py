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
#Promedio_Manufacturer = df_car_groupby('Manufacturer')
#Mostrando resultado
#print(Promedio_Manufacturer)

#Agrupar por manufacturera y saber la suma
#Suma_Manufacturer = df_car_groupby.groups('Manufacturer').sum()

#Contar por vehiculo como Car y Passenger
#Suma_Vehiculo = df_car_groupby('Vehicle_type').count()

#print(Suma_Vehiculo)

#Checando los null
nulos  = df_car.isnull().sum()

#Print resultado
print(nulos)

#agrupando por tamaño
Agrupación_de_tamañoMotor = df_car.groupby('Engine_size',dropna=False).count()

print(Agrupación_de_tamañoMotor)
