#Bucles determinados y bucles indeterminados

def bucle_basico():
    for i in ["primavera","verano","otoño","invierno"]:
        print("Hola " + i, end=". ")
#bucle_basico()

def tabla_multiplicar(numero):
    num = [1,2,3,4,5,6,7,8,9,10]
    for i in num:
        print(i*numero)
#tabla_multiplicar(4)

def comprobador_email():
    email = input("Introduce tu dirección de email: ")
    contador = 0
    for i in email:
        if(i=="@" or i=="."):
            contador=contador+1
    if contador==2:
        print("Email correcto")
    else:
        print("El email no es correcto")
#comprobador_email()

#Tipo range
def range_func():
    for i in range(5,10): #Desde el 5 hasta el 10, si le quitamos el 10 de 0 a 4. 
        #Si le añadimos un número más el tercer número hace que se vayan saltando
        print(f"Valor de la variable {i+1}") #La notación f hace más sencillo concatenar
range_func()

def range_email():
    valido=False
    email = input("Introduce tu email: ")
    for i in range(len(email)):
        if email[i]=="@":
            valido=True
    if valido:
        print("Es correcto")
    else:
        print("Email incorrecto")
range_email()