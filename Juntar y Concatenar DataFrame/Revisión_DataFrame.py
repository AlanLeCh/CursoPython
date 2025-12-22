#Importación de la libreria

import pandas as pd

df_movies = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Juntar y Concatenar DataFrame/IMDb movies.csv',low_memory=False)
df_rating = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Juntar y Concatenar DataFrame/IMDb ratings.csv',low_memory=False)

#Impresión del resultado
print (df_movies)
print (df_rating)

#Muestra de columnas 
columnas = df_movies.columns
columnass = df_rating.columns

#Muestra el nombre de las columnas
print(columnas)
print(columnass)

#Selección de columnas
df_movies = df_movies[['imdb_title_id','title','year','genre','country']]

df_rating = df_rating[['imdb_title_id','total_votes','mean_vote']]

#Impresión de ambos DataFrame
print(df_movies)
print(df_rating)
	

