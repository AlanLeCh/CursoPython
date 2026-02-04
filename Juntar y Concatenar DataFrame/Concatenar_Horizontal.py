#Importación de librería
import pandas as pd

#DataFrame edades
df1 = pd.DataFrame({'id':['A','B','C','D'],
                    'age': [30,23,25,22]})

#Dtaframe empleos
df2 = pd.DataFrame({'Job':['Doctor','Statistician','Accountant','Developer']})

#Mostrar los resultado
print(df1)

print(df2)

#Concatenar los dos DataFrame
Concatenar = pd.concat([df1,df2], axis=1)
print(Concatenar)

###########################################

df_movies = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Juntar y Concatenar DataFrame/IMDb movies.csv',low_memory=False)
df_rating = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Juntar y Concatenar DataFrame/IMDb ratings.csv',low_memory=False)


#Selección de columnas
df_movies = df_movies[['imdb_title_id','title','year','genre','country']]

df_rating = df_rating[['imdb_title_id','total_votes','mean_vote']]

#Metodo Shape

df_moviesshape = df_movies.shape
df_ratingsahpe = df_rating.shape

print(df_moviesshape)
print(df_ratingsahpe)

#Concatenar horizontalmente df_movies y df_ratings usando la columna 'imdb_title_id'

ConcateMovies = pd.concat([df_movies,df_rating], axis=1)

print(ConcateMovies)
#Shape,

ConcateMoviesShape = ConcateMovies.shape
print(ConcateMoviesShape)