#importamos las librerias necesarias
import pandas as pd

#Leemos el archivo CSV
df_laptops = pd.read_csv('laptop_price.csv',encoding='latin1')

#Mostramos el CSV
print(df_laptops)

                                                        #Drp_duplicates() - Eliminar duplicados

#Eliminar duplicados en 2 o más columnas

df_laptops.drop_duplicates(['Company']).value_counts('Company')

df_laptops.drop_duplicates(['Company'])[['Company', 'Price_euros']]

#Ordenar dataframe ascendiente por compañia (Company) y precio (Price_euros)
#más barato primero y más caro al último

df_laptops = df_laptops.sort_values(by=['Company', 'Price_euros'])

#Más barato: keep = 'first'
df_laptops.drop_duplicates(['Company'], keep='first')[['Company', 'Price_euros']]

#Más caro_: keep = 'last'

df_laptops.drop_duplicates(['Company'], keep='last')[['Company', 'Price_euros']]

#Argumentos
df_laptops.drop_duplicates(['Company'], keep='last', inplace=True, ignore_index=True)

#Implace: eliminar duplicados en el dataframe o devuelve copia
#Ignore_index=True: el index resultado tendra etiqueta 0, 1,....

print(df_laptops[['Company', 'Price_euros']])

                                                                #EJERCICIO 1

#Leemos el archivo CSV
df_laptops = pd.read_csv('laptop_price.csv',encoding='latin1')

print(df_laptops)

#Ordenar dataframe escendiente por compañia (Company) y pulgadas (Inches)
#más pequeño primero y más grande al último

df_laptops = df_laptops.sort_values(by=['Company', 'Inches'])

#Más pequeño: keep = 'first'

df_laptops.drop_duplicates(['Company'], keep='first')[['Company', 'Inches']]

#Más grande: keep = 'last'

df_laptops.drop_duplicates(['Company'],keep='last')[['Company','Inches']]