#importamos las librerias necesarias
import pandas as pd

#Crearmos un objeto de tipo DataFrame
df_laptops = pd.read_csv('laptop_price.csv',encoding='latin1')

#Mostrar el dataframe con el que vamos a trabajar
print(df_laptops)


                                                                        # isin(): FILTRO SIMPLE

#Select laptos Apple o HP

df_laptops['Company'].isin(['Apple','HP'])

#Filtrar DataFrame

df_laptops[df_laptops['Company'].isin(['Apple','HP'])]

#Filtrar por metodo Values

df_laptops[df_laptops['Company'].isin(['Apple','HP'])].value_counts('Company')

                                                                        #isin(): Filtrado Multiple

#Encontrar notebooks o ultabooks de Apple o HP

filtro1 = df_laptops['TypeName'].isin(['Notebook','Ultrabook'])
filtro2 = df_laptops['Company'].isin(['Apple','HP'])

#Filtrar DataFrame

df_laptops = [filtro1 & filtro2]

#Mostrar DataFrame filtrado
print(df_laptops)
