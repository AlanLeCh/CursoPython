# Crear un bucle
Paises = ['Estados Unidos', 'México', 'Canada', 'Peru', 'Bolivia', 'Brazil', 'Colombia']

for país in Paises:
    print(país)

#For y If
Paises = ['Estados Unidos', 'México', 'Canada', 'Peru', 'Bolivia', 'Brazil', 'Colombia']

for país in Paises:
    if país == "Peru":
        print(país)

#Enunmerar las interacciones
Paises = ['Estados Unidos', 'México', 'Canada', 'Peru', 'Bolivia', 'Brazil', 'Colombia']

for numero, paiss in enumerate(Paises):
    print(numero,paiss)

# FOR AND DICTIONARY
my_data = {'nombre': 'Alan', 'edad': 28}
print (my_data)

#Interar en dictionario
for key, values in my_data.items():
    print(key,values)