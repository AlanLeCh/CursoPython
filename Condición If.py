import pandas as pd
import numpy as np
#Declaración de variable
edad = 30

#calculando SI ES MAYOR O NO
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


#Declarando un arreglo en DataFrame

Edades = np.array([[12],[20],[30],[50]])

for Edad in Edades:

    if Edad >= 30:
     print(f"{Edad} Eres maoyor de edad")
    else:
        print(f"{Edad} No eres mayor de edad")

#Declaramos array

Agencia = ['Mecedes Benz','Chebrolet', 'Peugeot']

for carro in Agencia:
   if carro == 'Mercedez Benz':
      print (f"{carro} existe en la lista.")
else:
      print(f"{carro} no se encuentra.")