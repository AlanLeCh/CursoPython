#Importamos Libreri Pandas
import pandas as pd

#Leemos el arcchivo de excel
df_popularion_raw = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/Pivote/Proyecto/population_total.csv")

#Mostramos los resultados
print(df_popularion_raw)

                                                                #HACER UNA TABLA PIVOTE
                                                                
#Eliminar valores NULL
df_popularion_raw.dropna(inplace=True)

print(df_popularion_raw.isnull().sum())  # ver si aún quedan nulos


# hacer una tabla pivote con el método .pivot () (países en los nombres de las columnas y años en el índice)

df_pivot = df_popularion_raw.pivot(index="year", columns="country", values="population")


#Mostrar el resultado
print(df_pivot)


# seleccione solo los países 'United States', 'India', 'China', 'Indonesia', 'Brazil'
df_pivote = df_pivot.loc[["United States", "India", "China", "Indonesia", "Brazil"]]

# Mostrar el resultado actualizado
print(df_pivote)

######################################################################################################################################################################

#####################################################################################################################################################################

import matplotlib.pyplot as plt

# Lineplot (Grafico de linea)

df_pivote = plt.plot(kind='line', figsize=(8, 5))
plt.title("Población Total por Países")
plt.xlabel("Años")  
plt.ylabel("Población Total")
plt.grid(True) 
plt.tight_layout()
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor visibilidad
plt.show()



#mostramos el grafico
print(df_pivote)