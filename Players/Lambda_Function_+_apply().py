#Importar la librería pandas
import pandas as pd

#Leer el archivo csv
Player = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Players/players_20.csv')

#Leer archivo csv y guardar en un dataframe
print(Player)

#fijar index
Player = Player.set_index('short_name')

#SELECCIONAR UNA COLUMNA
Player = Player[['long_name','age','dob','height_cm','weight_kg','club','nationality']]

#Mostrar resultado
print(Player)


# Función básica

def sum_numeros(a,b):
    x = a+b
    return x

#Función lambda (una línea)

sum_values_lambda = lambda a,b:a+b

#Mostrar resultaod
sum_values_lambda(2,3)

                                                                            #Apply + Función Lambda

#Usar función lambda para convertir serie "heigh_cm" a metros

Player['height_cm'].apply(lambda x:x/100)

#alternativa

Player['height_cm']/100

#Usar función lambda para convertir serie "long_name" a mayusculas

Player['long_name'].apply(lambda x:x.upper())

#Alternativa con atributo str
Player['long_name'].str.upper()

#Usar función lambda para obtener el año de la serie "dob"
Player['dob'] = Player['dob'].astype('datetime64[ns]')

Player['dob'].apply(lambda x:x.year)

#Alternativa con el atributo dt

Player['dob'].dt.year


#Aplicar función lambda al DataFrame para calculadora IMC

Player.apply(lambda X: X['weight_kg'] / ((X['height_cm']/100)**2), axis=1)


