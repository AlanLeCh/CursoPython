#Estartegia Split-Apply-Combine (Separación, Aplicación, Combinación)

#Importamos la libreria
import pandas as pd

#Buscamos el archvio csv
df_car = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/GroupBy y Función Agregada/Car_sales.csv")

#Mostramos el resultado
print (df_car)

#Tipos de Vehiculos
print(df_car['Vehicle_type'].value_counts())

#Condicion del tipo Split
Car_Filter = df_car['Vehicle_type'] == 'Car'
Passenger_filter = df_car['Vehicle_type']== 'Passenger'

#Mostrando los datos filtrados
print(Car_Filter)
print(Passenger_filter)
 
#Aplicación con Apply
Car_average = df_car[Car_Filter]['Sales_in_thousands'].mean()
Passenger_average = df_car[Passenger_filter]['Sales_in_thousands'].mean()

#Mostando el resultado
print(Car_average)
print(Passenger_average)

#combine
Resultado = pd.DataFrame({'Vehicle_Type':['Car','Passenger'],
                          'Sales_in_thousands':[Car_average,Passenger_average]})
#Mostandro resultado de ambas
print(Resultado)
