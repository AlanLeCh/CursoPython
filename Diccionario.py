# Crear un diccionario
My_Data = {'nombre': 'Alan', 'edad': 28}
print(My_Data)

#mostrar el vaslor que solo guarda
My_Data['nombre']
print(My_Data)

#mostrar el nombre de las llaves
My_Data.keys()

#mostrar los valores que guarda las Keys
My_Data.values()

#Muestra el nombre campo y su valor
My_Data.items()

#Actualizar o eliminar

My_Data['Estatura'] = 1.75
print(My_Data)

#Actualizar con Update
My_Data.update({'Estatura': 1.80, 'Lenguages':['Español','Inglés', 'Arameo']})
print(My_Data)

#Copia de un diccionario
New_My_Data = My_Data.copy()
print(New_My_Data)

#Eliminar elementos
My_Data.pop('Estatura')
print(My_Data)

del My_Data['Lenguages']
print(My_Data)

#Elimina todo lo que hay en un diccionario
My_Data.clear()