#Impportar librerias
import pandas as pd

#leear el archivo CSV
df_laptops = pd.read_csv('laptop_price.csv',encoding='latin1')

#mostrar el CSV
print(df_laptops)


                                                                #1- UNIQUE() - Obtener valores únicos de una columna.
                                                            #DEVUELVE VALORES UNICOS DE UNA SERIE (LOS VALORES UNICOS SON DEVUELTOS EN EL ORDEN QUE APARECEN)

#Obtener elementos unicos en la columna "Company"
df_laptops['Company'].unique()

#Obtener elementos unicos en la columna "Inches"
df_laptops['Inches'].unique()

#Obtener el tamaño de los elementos unicos.

len(df_laptops['Inches'].unique())
len(df_laptops['Company'].unique())

                                                                #2 NUNIQUE() - Obtener valores únicos de una columna.
                                                            #DEVOLVER NUMERO ÚNICO DE ELEMENTOS EN UN OBJETO(Excluye valores NA por defecto)

#Obtener número de valores unicos en la columna "Company"

df_laptops['Company'].nunique()

#Obtener número de valores unicos en la columna "Inches"

df_laptops['Inches'].nunique()