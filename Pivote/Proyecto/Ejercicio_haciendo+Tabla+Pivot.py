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

df_pivot = df_popularion_raw.pivot(index="country", columns="year", values="population")


#Mostrar el resultado
print(df_pivot)




# seleccione solo los países 'United States', 'India', 'China', 'Indonesia', 'Brazil'
df_pivote = df_pivot.loc[["United States", "India", "China", "Indonesia", "Brazil"]]

# Mostrar el resultado actualizado
print(df_pivote)