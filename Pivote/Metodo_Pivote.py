#Importamos la liobreia de Pandas
import pandas as pd

#Leer archivo

try:
    Pivote = pd.read_csv('C:/Users/alanp/Desktop/CursoPython/Pivote/gdp.csv', encoding='latin1')
    print(Pivote.head())
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")

#Leer archivo csv y guardar en un dataframe
print(Pivote)

#Usando metodo pivot
def_Pivotes = Pivote.pivot(index="year", columns="country", values="gdppc")

#Mostrar resultado
print(def_Pivotes)
    