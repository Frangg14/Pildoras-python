#Listas inmutables, no se puede cambiar absolutamente nada
nombreTupla=("Antonio","Pedro","Fernando Alonso",33)
print(nombreTupla[2])
#Convertir tupla a lista
miLista=list(nombreTupla)
miLista.append("Toni")
miLista.append(33)
print(miLista)
#Convertir lista a tupla
miTupla=tuple(miLista)
print(miTupla)
print("Toni" in miTupla)
#Averigüar cuantos elementos hay en una tupla
print(miTupla.count(33))

#Comprobar la cantidad de elementos que hay
print(len(miTupla))

#Tupla unitaria
unitaria=("Juan",)

#Ejemplo de uso de las tuplas (desempaquetado de tuplas)
datos=("Juan",13,1,1995)
nombre, dia, mes, anio = datos
print(nombre)
print(anio)
print(dia)
print(mes)