def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
	#Función que puede tener una excepción
	try:		
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir entre cero")
		return "Operación errónea"

try:
	op1=(int(input("Introduce el primer número: ")))
except ValueError:
	print("Debes introducir un número correcto")
	op1=0
try:
	op2=(int(input("Introduce el segundo número: ")))		
except ValueError:
	print("Debes introducir un número correcto")
	op2=0
#Se podría hacer con un "while: True" para que no salga hasta que meta un valor correcto

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")
if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecución del programa ")