import math
def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("La edad no puede ser negativa")
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate..."
    else:
        return "Edad no válida"
#print(evaluaEdad(15))

def evaluar_raiz(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz de un número negativo")
    else:
        return math.sqrt(numero)

op1=(int(input("Introduce un número para calcular su raíz cuadrada: ")))
try:
    print(evaluar_raiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print("Programa terminado")
