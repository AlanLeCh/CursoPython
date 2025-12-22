#Importación de la librería
import pandas as pd

df_movies = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Juntar y Concatenar DataFrame/IMDb movies.csv',low_memory=False)
print(df_movies)
#Extraer el 50% de muestra del DataFrame orignal
df_samples = df_movies.sample(frac=0.5)
print(df_samples)

#Shape
df_sampleshape = df_samples.shape
df_moviesshape = df_movies.shape

print(df_sampleshape)
print(df_moviesshape)

#Concatenar verticalmente df_movies y df_samples

Concatenación = pd.concat([df_movies, df_samples], axis=0)
print(Concatenación)

concatenaciónshape = Concatenación.shape
print(concatenaciónshape)