import math


def while_func():
    i=1
    while i<=10:
        print("Ejecución " + str(i))
        i+=1 #Esto hace que el bucle no sea infinito
    print("Fin del bucle")
#while_func()

#Función práctica
def introducir_edad():
    edad=int(input("Introduce tu edad: "))
    while edad<5 or edad>100: #Se ejecutará dependiendo del número introducido por el usuario
        print("Has introducido una edad inválida o demasiado alta. Inténtalo de nuevo.")
        edad=int(input("Introduce tu edad: "))
    print("Gracias. Has introducido una edad válida: " + str(edad))
#introducir_edad()

def raiz_cuadrada():
    print("Cálculo de la raíz cuadrada")
    numero=int(input("Introduce un número por favor: "))
    intentos=0
    while numero<0:
        print("No se puede calcular la raíz cuadrada de un número negativo.")
        if intentos==2:
            print("Has agotado el número de intentos. El programa ha finalizado.")
            break
        numero=int(input("Introduce un número por favor: "))
        if numero<0:
            intentos+=1 #O intentos=intentos+1
    if(intentos<2):
        resultado=math.sqrt(numero)
        print("La raíz cuadrada de " + str(numero) + " es " + str(resultado))
raiz_cuadrada()