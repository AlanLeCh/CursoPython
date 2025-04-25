
#Importar la libreria pandas
import pandas as pd

#Crear un dataframe 
df_laptops = pd.read_csv('laptop_price.csv', encoding='latin1')

#Leear el dataframe
print(df_laptops)

#Filtrar dataframe basado en una columnna

#Encontrar filas que tengan "Apple" en la columna "Company"
df_laptops['Company'] == 'Apple'

#Hacer un filtro en el dataframe basado en la condición
df_laptops[df_laptops['Company'] == 'Apple']

#Verificar que compañias estan en la colulmna "Company" con el metdodo Value_counts()
df_laptops[df_laptops['Company'] == 'Apple'].value_counts('Company')

                                                                                        #Ejercicios

#Ejercicio 1: Encontrar que filas no tienen "HP" en la columna "Company"

df_laptops['Company'] != 'HP'

#Filtrar datafarame basado en la condicón

df_laptops[df_laptops['Company'] == 'HP']

#Ejercicio 2: Encontrar laptop con precio arriba de 2000 Euros.

df_laptops['Price_euros'] > 2000
