#importando 
import pandas as pd

#Leemos el archivo de excel
df_market = pd.read_excel("C:/Users/alanp/Desktop/CursoPython/Pivote/supermarket_sales.xlsx")


#Mostramos el contenido del archivo
print(df_market)


#Hacer una tabla pívot para saber cuanto gastan las mujes y los hombres 

pivot = df_market.pivot_table(index= "Gender", 
                       values= ["Quantity","Total"],
                       aggfunc= "sum")

#imprimir el resultado
print(pivot)

#Hacer una tabla pívot para saber cuanto gastan las mujes y los hombres por Product line
pivote = df_market.pivot_table(index= "Gender", 
                      columns= "Product line",
                       values= "Total",
                       aggfunc= "sum")

#Verificamos los resultados
print(pivote)