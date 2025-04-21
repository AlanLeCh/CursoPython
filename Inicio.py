# Preguntando al usuario sus datos
nombre = input("Ingrese su nombre: ")
apellidoPa = input("Ingrese su apellido paterno: ")
apellidoMat = input("Ingrese su apellido materno: ")
edad = input("Ingrese su edad: ")

# Definimos una contraseña predefinida
intentos = 0
max_intentos = 3

# Pedimos al usuario que ingrese la contraseña
password = input("Ingrese su contraseña: ")
prepassword = input("Ingrese su contraseña: ")

# Mientras no sea correcta y queden intentos
while password != prepassword and intentos < max_intentos - 1:
    intentos += 1
    print("Contraseña incorrecta. Intente de nuevo.")
    password = input("Ingrese su contraseña: ")

if password == prepassword:
    print("¡Acceso correcto!")
    print(f"¡Hola {nombre} {apellidoPa} {apellidoMat}, seas bienvenido!")

