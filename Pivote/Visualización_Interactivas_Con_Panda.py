#Importando librerias pandas 
import pandas as pd

#importando libreria plotly
import plotly.express as px
import plotly.graph_objects as go

#importando libreria cufflinks
import cufflinks as cf
from  IPython.display import display,HTML
cf.set_config_file (sharing='public',theme='white',offline=True)

#Mandaos llamar al archivo csv
df_population = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/Pivote/Proyecto/population_total.csv")
#mostrar el archivo
print(df_population)

#Limpiando datos nulos
df_population = df_population.dropna()

#colocar los años en el indice y los paises en las columnas
df_population = df_population.pivot(index='year', columns='country' ,values='population')

#Mostrar resultado
print(df_population)

#Mostando los paises seleccionados
df_population = df_population [['United States', 'India', 'China', 'Indonesia', 'Brazil']]

#mostrar resultado
print (df_population)

##########################################################################################################
                                                 #GRAFICO DE LINEPLOT
##########################################################################################################

fig_line = px.line(df_population.iplot(kind='line',xtile='Year',ytitle='Population',title= 'Year vs Population'))

#Mostrar el resultado
fig_line.show()

##########################################################################################################
                                                    #GRAFICO DE BARPLOT
##########################################################################################################

#Seleccionando el año 2020
df_population_2020 = df_population[df_population.index.isin([2020])]

#mostrar resultado
print(df_population_2020)