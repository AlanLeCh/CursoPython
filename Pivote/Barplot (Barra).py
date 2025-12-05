#Importamos Libreri Pandas
import pandas as pd

#Leemos el arcchivo de excel
df_popularion_raw = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/Pivote/Proyecto/population_total.csv")

#Mostramos los resultados
print(df_popularion_raw)

#Eliminar valores NULL
df_popularion_raw.dropna(inplace=True)

print(df_popularion_raw.isnull().sum())  # ver si aún quedan nulos


# hacer una tabla pivote con el método .pivot () (países en los nombres de las columnas y años en el índice)

df_pivot = df_popularion_raw.pivot(index="year", columns="country", values="population")


#Mostrar el resultado
print(df_pivot)


# seleccione solo los países 'United States', 'India', 'China', 'Indonesia', 'Brazil'
df_pivote = df_pivot[["United States", "India", "China", "Indonesia", "Brazil"]]

# Mostrar el resultado actualizado
print(df_pivote)

######################################################################################################################################################################
                                                                     #Lineplot (Grafico de linea)
#####################################################################################################################################################################

#Importar la libreria
#import matplotlib.pyplot as plt

##df_pivot.plot(kind='line', xlabel= 'Año', ylabel='Población', title='Population (1955-2020)', figsize=(8,4)) #Kind es el tipo de grafíca, 
                                                                                                             #xlabel es la etiqueta del eje x, 
                                                                                                             #ylabel es la etiqueta del eje y, 
                                                                                                             #title es el título del gráfico,
                                                                                                             #figsize es el tamaño del gráfico
##plt.show()  #Mostrar el grafico

#####################################################################################################################################
                                                                        #Barplot (Grafico de Barra)
#####################################################################################################################################

#Importar la libreria
import matplotlib.pyplot as plt

df_pivote_2020 = df_pivote.loc[2020]  # Seleccionar datos del año 2020

print(df_pivote_2020) # Mostrar datos del año 2020

#trasponer un dataframe (cambiando filas con columnas y viceversa)
df_pivote_2020.T

#Hacer el barplot (Grafico de Barra)
df_pivote_2020.T.plot(kind='bar', color='orange', xlabel='Years', ylabel='Population', title='Population in 2020')
plt.show()  #Mostrar el grafico

#Barplot agrupado por "N" varibales
df_pivote_sample= df_pivote.loc[[1980, 1990, 2000, 2010, 2020]]  # Seleccionar más de un año

#mostrando resultado normal
print(df_pivote_sample)

#Mostando el resultado con la grafica
df_pivote_sample.plot(kind='bar',xlabel='Years', ylabel='Population', title='Population of countrys (1980-2020)')
plt.show()