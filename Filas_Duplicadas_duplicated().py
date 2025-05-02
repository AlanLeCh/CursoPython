# importamos las librerias necesarias
import pandas as pd

#Creamos un objeto de tipo DataFrame
df_laptops = pd.read_csv('laptop_price.csv',encoding='latin1')

#Mostrar el dataframe con el que vamos a trabajar
print(df_laptops)

                                                                        #Duplicated()

#Encontrar duplicados en 1 columna/serie

df_laptops.duplicated('laptop_ID')

#Mostrar elementos en DataFrame con duplicados en columna 'laptop_ID'
df_laptops[df_laptops.duplicated('laptop_ID')]

#Duplicados en 2 o más columnas

duplicado = df_laptops.duplicated(['Product', 'TypeName', 'Inches'])

#Muestra todos los valores duplicados (Excepto por el primer - keep=False)
df_laptops[duplicado].sort_values(by=['Product', 'TypeName'])

                                                                            #EJEMPLO 2 

#Ordenar dataframe asccendente por "company" y "Price_euros"
#más barato primero y más caro al ultimo

df_laptops = df_laptops.sort_values(by = ['Company','Price_euros'])

#Mostrar dataframe ordenado por "Company" y "Price_euros"
print(df_laptops)

#Revisar todas la scotegorias en la columna "Company"

df_laptops.value_counts('Company')

#Valores duplicados en la columna "Company" (por defecto keep = 'first')

duplicated_first = df_laptops.duplicated('Company', keep='first')

#Mostrar dataframe con valores duplicados en la columna "Company"

df_laptops[duplicated_first]

#keep = 'first' (laptop más baratas por compañia)
#Mostrar dataframe con valores no duplicados en la columna "Company"

df_laptops[~duplicated_first][['Company', 'Price_euros']]

#Revisar todas las categorias
df_laptops[~duplicated_first].value_counts('Company')

#keerp = 'last' (laptop más caras por compañia)

duplicated_last = df_laptops.duplicated('Company', keep='last')

#mostrar dataframe con valores duplicados en la columna "Company"
print(df_laptops[~duplicated_last])

#Mostrar DataFrame con valores no duplicados en la columna "Company"
print(df_laptops[~duplicated_last][['Company', 'Price_euros']])

#Valores duplicados en la columna "Company" (por defecto keep = False)
duplicated_false = df_laptops.duplicated('Company', keep=False)

#keep = False (laptop más baratas y más caras por compañia)
#Mostrar dataframe con valores duplicados en la columna "Company"
df_laptops[~duplicated_false]