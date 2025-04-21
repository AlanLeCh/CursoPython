Paises = ['Estados Unidos', 'México', 'Canada', 'Peru', 'Bolivia', 'Brazil', 'Colombia']

#Calculando el tamaño de la lista
len(Paises)

#Crear una lista, para calcular el maximo

max([4,15,16,83,32,1,10])
print(max)

#Calcula el minimo
min([4,15,16,83,32,1,10])
print(min)

#Tipo de dato del objeto
type(Paises)

#round, redondea un número

round(2.333,1)

#Función range
range(1,10,2)

#Mostrando interacción
for i in range(1,10,2):
    print(i)

# Creando la propia funcion de uno

def suma_numeros(a,b):
    suma_final = a + b
    return suma_final

suma_numeros (19,20)
print(suma_numeros)
