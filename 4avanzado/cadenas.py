nombreUsuario = input("Ingrese su nombre de usuario: ")

print("Hola, " + nombreUsuario.capitalize() + "! Bienvenido/a al sistema.")
print(nombreUsuario.upper())
print(nombreUsuario.lower())

edad = input("Ingrese su edad: ")
# print(edad.isdigit())  # Verifica si la edad es un número
while edad.isdigit() == False: 
    # Verifica si la edad es un número, si no lo es, el bucle se repite
    edad = input("Por favor, ingrese un número válido para su edad: ")
if(int(edad) < 18):
    print("No puede pasar.")
else:
    print("Puede pasar.")