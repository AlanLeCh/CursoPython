#Importando librería
import pandas as pd
#Merge ()

df1 = pd.DataFrame({'id':['A','B','C','D'], 
                    'age': [30,23,25,22]})

df2 =  pd.DataFrame({'id': ['C','D','E','F'],
                     'job':['Doctor', 'Statistician', 'Accountant','Developer']})

#Mostrar el resultado df1
print(df1)

#Mostrando el resultado df2
print(df2)

#Inner join
resultado_del_dfr1 = df1.merge(df2, on = 'id', how = 'inner')

#Muestra el resultado final
print (resultado_del_dfr1)

#Ejercicio con DataFrame de películas e ratings
df_movies = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Juntar y Concatenar DataFrame/IMDb movies.csv',low_memory=False)
df_rating = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Juntar y Concatenar DataFrame/IMDb ratings.csv',low_memory=False)

#Hacer un merge df_movies and df_ratings (Inner Join)

df_movie_and_rating  = df_movies.merge(df_rating, on= 'imdb_title_id', how='inner')

#Imprimir el resultado
print(df_movie_and_rating)

