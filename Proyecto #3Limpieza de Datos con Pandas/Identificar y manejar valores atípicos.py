#Importando libreria
import pandas as pd
import matplotlib.pyplot as plt

#Leer el archvio csv
Netflix = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Proyecto #3Limpieza de Datos con Pandas/netflix_titles.csv')

#Mostrar el resultado
print(Netflix)

#4 Identificar Valores Atipicos
  #4.1 Usar histograma para identificar valores atipicos dentro de data numerica.
  
#Hacer histograma con pandas
Netflix['duration'] =(Netflix['duration'].str.extract(r'(\d+)').astype(float))
df_netflix = Netflix['duration'].plot(kind='hist', bins=10)
                                      
#Mostrar resultado
plt.show()

#manejo de valores atipicos
Netflix[(Netflix['duration']>31.2) & (Netflix['duration']<218)]

#Usar boxplot para identificar valores atipicos entro de data numerica.

#Hacer boxolot con pandas
Netflix['duration'].plot(kind='box', vert=False, color= 'blue', figsize=(10,5))

#mostar resultado
plt.show()  

#Revision a valores estadisticos
#IQR = Q3-Q1
min_boxplot = 87 - 1.5 * (114-87) #Q1 - 1.5*IQR
max_boxplot = 114 + 1.5 * (114-87) #Q3 + 1.5*IQR

#imprimendo resultado
print(min_boxplot)
print(max_boxplot)

#Usar grafico de barras para identificar valores atipicos dentro de data categorica.
#Hacwr barplot con pandas
Netflix['rating'].value_counts().plot(kind='bar')

#Mostrar resultado
plt.show()

#Hacer filtro que quite 6 categorias.
Netflix_filtrado = Netflix[~Netflix['rating'].isin(['TV-Y7-FV', 'NC-17', 'UR', '74 min', '84 min', '66 min'])]


#mostrar resultado
plt.show()
   