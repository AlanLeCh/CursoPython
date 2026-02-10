#Importar libreria de expresiones regulares
import re

texto = '''Hola Mundo.
Me gusta Python!!!
Mi primer número de la suerte es 987-654-321
Mi segundo número de la suerte es 876-543-210
Mi tercer número de la suerte es 765-432-100
Mi cuarto número de la suerte es 123-456-123-123-456
'''
#Buscar el primer emparejamiento
print(re.search(r'\d',texto))

#Buscrar todas las coincidencias
print(re.findall(r'\d',texto))

#Encontrar puntuación (Encontrar caracteres que no estan dentro del corchete, y espacios en blanco)
print(re.findall(r'[^\w\s]', texto))

#Validar una Fecha
Texto2 = '''13-04-2021
            2021-13-04
            2021-04-13
'''
print(re.findall(r'\d{2}-\d{2}-\d{4}',Texto2))

#Validar un Usuario, de 4 a 14 y solo números o letras

texto3 = '''
usuario10
abc
10
'''
print(re.findall(r'[a-z0-9]{4,14}',texto3))