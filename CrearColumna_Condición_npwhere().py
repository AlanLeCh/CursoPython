
#Importar la libreria pandas
import pandas as pd

#Crear un dataframe 
df_laptops = pd.read_csv('laptop_price.csv', encoding='latin1')

#Leear el dataframe
print(df_laptops)

#Crear una columna basada en 1na condición np.where()

import numpy as np

#Crear un array basado en nivel de precio (price_tier)
df_laptops['Price_euros'] > 2000

Precio = np.where(df_laptops['Price_euros'] > 2000, 'Caro', 'Barato')

#Mostrar el resultado
print(Precio)

#Añadir a una nueva columna al dataframe
df_laptops['Price_Categoria'] = Precio

#Mostrar el resultado de las primero 5 filas

df_laptops.head(5)

#Contar los valores en columna price_tier
df_laptops.value_counts('Price_Categoria')

                                                                        #EJERCICOS.

#Crear un array basado en el tamaño de pantalla (screen_size), NOTA: SI sceen_size es >15, es pantalla grande, sino es pantalla pequeña.

df_laptops['Inches']> 15

Screen_Size = np.where(df_laptops['Inches']>15, 'Big Screen', 'Small Screen')

#Mostrar resultado del DataFrame
print(Screen_Size)

#Añadir a nueva columna al dataframe
df_laptops['Screen_Size'] = Screen_Size

#Mostrar los primeros 5 filas
df_laptops.head()

#Contar valores en columna screen_size
df_laptops.value_counts('Screen_Size')



