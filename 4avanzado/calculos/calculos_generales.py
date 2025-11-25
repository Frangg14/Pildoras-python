def sumar(op1,op2):
    print("La suma es: ", op1 + op2)

def restar(op1,op2):
    print("La resta es: ", op1 - op2)

def multiplicar(op1,op2):
    print("La multiplicación es: ", op1 * op2)

def dividir(dividendo,divisor):
    if divisor != 0:
        print("La división es: ", dividendo / divisor)
    else:
        print("Error: División por cero no permitida.")

def potencia(base,exponente):
    print("La potencia es: ", base ** exponente)

def redondear(numero):
    print("El número redondeado es: ", round(numero))
