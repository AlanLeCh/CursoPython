#Importando librería
import pandas as pd
#Merge ()

df1 = pd.DataFrame({'id':['A','B','C','D'], 
                    'age': [30,23,25,22]})

df2 =  pd.DataFrame({'id': ['C','D','E','F'],
                     'job':['Doctor', 'Statistician', 'Accountant','Developer']})

#Print
print(df1)

#Print
print(df2)

#Left Join
df_left_join = df1.merge(df2, on = 'id', how = 'left')

#Imprimir resultado
print(df_left_join)

#Indicator = True
df_indicator = df1.merge(df2, on = 'id', how = 'left', indicator = True)

#Imprimir resultado
print(df_indicator)

#Query
df_indicator_query = df1.merge(df2, on = 'id', how = 'left', indicator =  True).query("_merge == 'left_only' or _merge == 'right_only' ")

#Mostrar resultado
print(df_indicator_query)

#Ejercicio con DataFrame de películas e ratings
df_movies = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Juntar y Concatenar DataFrame/IMDb movies.csv',low_memory=False)
df_rating = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Juntar y Concatenar DataFrame/IMDb ratings.csv',low_memory=False)

#Extraer el 50% de muestras del df_movies
df_movies_samples = df_movies.sample(frac = 0.5)

#Merge df_movies_samples and df_ratings (left join)
df_movies_samples_merge = df_movies_samples.merge(df_rating, on = 'imdb_title_id', how = 'left')

#imperción de resultado
print(df_movies_samples_merge)

#shape
print(df_movies_samples_merge.shape)
 
 
 #Joins (Exclusive) Left Join
df_merge_join = df1.merge(df2, on = 'id', how = 'outer')

#Imprimir resultado
print(df_merge_join)

#indicator = True
df_indicator = df1.merge(df2, on = 'id', how = 'outer', indicator = True)

#imprimir resultado
print(df_indicator)

#query
df_query = df1.merge(df2, on = 'id', how = 'outer', indicator = True).query("_merge == 'left_only' ")

#imprimir resultado
print(df_query) 


#EJERCICIO con DataFrame de películas e ratings (Exclusive Left Join)

#Hacer copia de DataFrame df_movies


#Fijar primero 1000 valores e columna 'imdb_title_id' el valor 'tt1234567890'

#Merge df_movies_2 y df_rating (exclusive left join)

#shape
