Countries = ['United States', 'Chana', 'India', 'Brazil']
print(Countries)

#Acceder a la lista.
print(Countries[1])

#Acceder a la lista, y que muestre el ultimo país,
print(Countries[-2])

#Trayendo de una posoción a una posisicón final
print(Countries[0:3])

#Trayndo todo
print(Countries[0:4])

#Operaciones y Metodos.

#Insercción con append
Countries.append('Canada')
print(Countries)

#Insección Insert
Countries.insert(0, 'México')
print(Countries)

Countries.insert(0, 'Israel')
print(Countries)


#Concatenar

Countries_2 = ['UK','Alemania', 'Australia', 'Siria']

print(Countries + Countries_2)

#Elimar registros de la lista
Countries.remove('Canada')
Countries.pop(0)

#Ordenar una lista 
numbers = [4,3,10,7,1,2]
print(numbers)

#SORT
numbers.sort()
print(numbers)

#REVERSE = TRUE
numbers.sort(reverse=True)
print(numbers)

#Actualización de un número
numbers[0] = 1000
print(numbers)