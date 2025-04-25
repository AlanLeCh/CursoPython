
#Importamos la libreria pandas
import pandas as pd

#Acceder al archivo csv
df_laptops = pd.read_csv('laptop_price.csv', encoding='latin1')

#Leer el DataFrame
print(df_laptops)

                                                            #Filtrar DataFrame Basado en una Condició

#Encontrar laptops Apples.
df_laptops['Company'] == 'Apple'

#Encontrar laptops que cuesten más de 2000 euros.
df_laptops['Price_euros'] > 2000


                                                            #Filtrar DataFrame basado en multiples condiciones.

#Encontrar laptops Apple que cuesten más de 2000 euros.
(df_laptops['Company'] == 'Apple') & (df_laptops['Price_euros'] > 2000)

# & = AND
df_laptops[(df_laptops['Company'] == 'Apple') & (df_laptops['Price_euros'] > 2000)]

# | = OR
#Encontrar laptops Apple o Dell
df_laptops[(df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')]

#Encontrar laptops Apple o Dell que cuesten más de 2000 euros.
df_laptops['Company'] == 'Apple'
df_laptops['Company'] == 'Dell'
df_laptops['Price_euros'] > 2000

#Uniendo los filtros.

((df_laptops['Company'] == 'Apple') | (df_laptops['Company']) == 'Dell') & (df_laptops['Price_euros'] > 2000)

#Filtrar dataframe basado en multiples condiciones.
df_laptops[((df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')) & (df_laptops['Price_euros'] > 2000)]


