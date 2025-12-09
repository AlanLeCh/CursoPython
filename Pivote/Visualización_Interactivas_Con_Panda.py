

#Importando librerias
import pandas as pd
import plotly.express as px
#Configurar pandas para usar plotly como backend de gráficos
pd.options.plotting.backend = "plotly"

#leerr archivo csv
df_population = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/Pivote/Proyecto/population_total.csv")

#mostrar resultados
print(df_population)

#Eliminar valores NULL
df_population = pd.read_csv("C:/Users/alanp/Desktop/CursoPython/Pivote/Proyecto/population_total.csv")
df_population.dropna()
df_population = df_population.pivot_table(index='year', columns='country', values='population')

#mostrar resultados
print(df_population)

#Seleccionar paises
df_population = df_population[['United States', 'India', 'China', 'Indonesia', 'Afghanistan']]   
#Mostrar resultados de los paises seleccionados
print(df_population)

##########################################################################################################
                                               #Grafico de Líneas (lineplot)
##########################################################################################################

fig = px.line(df_population) #Grafico de lineas
fig = df_population.plot(kind='line', title="Population vs Years") #Grafico de lineas, etiquetas.
fig.show() #Mostrar grafico

############################################################################################################
                                                  #Grafico de Barras (barplot)
############################################################################################################
fig_population_2020 = px.bar(df_population.loc[2020])
fig_population_2020 = df_population.loc[2020].plot(kind='bar', color={'United States': 'red',
    'India': 'green',
    'China': 'blue',
    'Indonesia': 'orange',
    'Afghanistan': 'purple'}, title="Population 2020") #Grafico de barras, etiquetas.
fig_population_2020.show() #Mostrar grafico

############################################################################################################
                                                #Grafico de Multiples (Barplot)
############################################################################################################
fig_population_multiple = px.bar(df_population.loc[[1980, 1990, 2000, 2010,2020]]) #Grafico de barras multiples
fig_population_multiple = df_population.loc[[1980, 1990, 2000, 2010,2020]].plot(kind='bar', title="Years vs Population") #Grafico de barras multiples, etiquetas.
fig_population_multiple.show() #Mostrar grafico

#############################################################################################################
                                                #Grafico de Caja (boxplot)
#############################################################################################################
fig_population_box = px.box(df_population) #Grafico de caja
fig_population_box.show() #Mostrar grafico

##############################################################################################################
                                                #Grafico de histogram (histogram)
##############################################################################################################
fig_population_histogram = px.histogram(df_population, x=['United States','Indonesia']) #Grafico de histograma
fig_population_histogram.show() #Mostrar grafico

################################################################################################
                                                #Grafico de Piechart (piechart)
################################################################################################

fig_population_pie_2020 = px.pie(df_population.loc[2020],
                                 values=df_population.loc[2020], 
                                 names=df_population.loc[2020].index, title="Population 2020") #Grafico de piechart.
fig_population_pie_2020.show() #Mostrar grafico
