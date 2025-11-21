from Persona import Persona
from Empleado import Empleado
Antonio = Persona("Antonio",55,"Barcelona")
Antonio.descripcion()
print("--------------")
Luis = Empleado(1500,10,"Luis",30,"Madrid")
Luis.descripcion()

# isinstance nos permite saber si un objeto es de una clase determinada
# Devuelve True o False
# Ejemplo:
print("--------------")
print("¿Luis es un empleado?")
print(isinstance(Luis,Empleado)) # True
print("¿Luis es una persona?")
print(isinstance(Luis,Persona))  # True
print("¿Antonio es un empleado?")
print(isinstance(Antonio,Empleado)) # False
print("¿Antonio es una persona?")
print(isinstance(Antonio,Persona))  # True
