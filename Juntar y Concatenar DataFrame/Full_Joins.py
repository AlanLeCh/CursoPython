#Importando librería
import pandas as pd
#Merge ()

df1 = pd.DataFrame({'id':['A','B','C','D'], 
                    'age': [30,23,25,22]})

df2 =  pd.DataFrame({'id': ['C','D','E','F'],
                     'job':['Doctor', 'Statistician', 'Accountant','Developer']})

#Outer join (Full Join)

df__full_join = df1.merge(df2,on='id', how='outer')

#Mostrando resultado
print(df__full_join)


#Ejerccio con dataframe de películas e ratings
df_movies = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Juntar y Concatenar DataFrame/IMDb movies.csv',low_memory=False)
df_rating = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Juntar y Concatenar DataFrame/IMDb ratings.csv',low_memory=False)

#Haciendo un merge df_movies and df_ratings (Full Join)
df_full = df_movies.merge(df_rating, on = 'imdb_title_id', how='outer')

#impresión de resultado
print(df_full)


#Exclusive Outer Join (Exclusive Full Join)

df_exclusive = df1.merge(df2, on = 'id',  how ='outer')

print(df_exclusive)

#Complementando con lo exclusivo de indicator
df_exclusive_indicator = df1.merge(df2, on = 'id', how = 'outer', indicator = True)

#Impresion
print (df_exclusive_indicator)

#Query
df_exclusive_indicator_query = df1.merge(df2, on = 'id', how = 'outer', indicator = True). query("_merge == 'left_only' or _merge == 'right_only' ")

#mostrar resultado
print(df_exclusive_indicator_query)

#Ejercicio con DataFrame de películas e ratings (Exclusive Full Join), siguiendo el mismo procedimiento anterior

#Full join
df_full_join = df_movies.merge(df_rating, on = 'imdb_title_id', how = 'outer')

#Impreción de resultado
print(df_full_join)

# Parametro indicator
df_full_indicator = df_movies.merge(df_rating, on = 'imdb_title_id', how = 'outer', indicator= True)

#Mostrar resultado
print(df_full_indicator)

#Query
df_full_query = df_movies.merge(df_rating, on = 'imdb_title_id', how = 'outer', indicator=True).query("_merge == 'left_only' or _merge == 'right_only' ")

#Mostrar resultado
print(df_full_query)

