def divide():
    try:
        op1=float(input("Ingrese el primer número (dividendo): "))
        op2=float(input("Ingrese el segundo número (divisor): "))
        print("El resultado de la división es: " +  str(op1/op2))
    except ValueError:
        print("El valor introducido no es válido.")
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    print("Operación finalizada.")
divide()

#Se podría hacer con un solo bloque except capturando la excepción base Exception,
#pero es una mala práctica ya que no se estaría manejando cada excepción 
# de forma específica.

#La instrucción finally se utiliza para definir un bloque de código 
# que se ejecutará siempre, independientemente de si se produjo una excepción o no.
# Se puede usar por ejemplo con las conexiones a bases de datos o archivos 
# para asegurarse de que se cierren correctamente.
#También puede usarse si no se quiere manejar la excepción pero se desea
# ejecutar un bloque de código al finalizar el try-except.