#Importamos las librerias necesarias
import pandas as pd

#Declaramos un objeto de tipo DataFrame
df_laptops = pd.read_csv('laptop_price.csv',encoding='latin1')

#ostramos el DataFrame original
print(df_laptops)

#Crear un array basado en multiple niveles de precio (+2 opciones)

import numpy as np



#Crear "Condicion" (Condicion) y "values" (Valores), para MUY CARO SEA >3000, CARO >2000,  BARATO >800 Y MUY BARATO <=800
condiciones = [
    df_laptops['Price_euros']>3000,
    (df_laptops['Price_euros']>2000) & (df_laptops['Price_euros']<=3000),
    (df_laptops['Price_euros']>800) & (df_laptops['Price_euros']<=2000),
    df_laptops['Price_euros']<=800
]
valores = ['MUY CARO', 'CARO', 'BARATO', 'MUY BARATO']

#Añadir una nueva columna.

df_laptops ['niveles_precio'] = np.select(condiciones, valores,default='Sin clasificar')

#Mostrar dataframe con la nueva columna

print(df_laptops)

#Contar los valores en columna price_tier

df_laptops['niveles_precio'].value_counts()

                                                                                                #EJERCICIO 

#Crear un array en multiples tamanos de pantalla ("Screen Size"), MUY GRANDE>16, GRANDE>14, PEQUEÑO>12, MUY PEQUEÑO<12
#Crear "Condition" (Condicion) y "values" (Valores)

import numpy as np

Array = [
    df_laptops['Inches'] > 16,
    (df_laptops['Inches'] >14) & (df_laptops['Inches']<=16),
    (df_laptops['Inches']>12) & (df_laptops['Inches']<=14),
    df_laptops['Inches']<=12
]

Valor = ['MUY GRANDE', 'GRANDE', 'PEQUEÑO', 'MUY PEQUEÑO']

#Añadir una nueva columna.

df_laptops ['Tipo_tamaño'] = np.select(Array,Valor,default='Sin clasificar')

#Mostrar dataframe con la nueva columna

print(df_laptops)

#Contar los valores en columna Screen Size
df_laptops['Tipo_tamaño'].value_counts()