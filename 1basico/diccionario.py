#El diccionario almacena clave:valor (muy parecido a un array asociativo en PHP)
#Orden indiferente
miDiccionario={"España":"Madrid","Francia":"París","Alemania":"Berlín","Reino Unido":"Londres"}
print(miDiccionario["España"])
print(miDiccionario)

#Agregar más elementos
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

#Modificar un valor
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#Eliminar
del miDiccionario["Reino Unido"]
print(miDiccionario)

#Ejemplo más elaborado de diccionario
diccionario={"Alemania":"Berlín",33:"Fernando Alonso","Mosqueteros":3}
print(diccionario)

miTupla = ["Francia","España","Reino Unido","Alemania"]
myDiccionario={miTupla[0]:"París",miTupla[1]:"Madrid",miTupla[2]:"Londres",miTupla[3]:"Berlín"}
print(myDiccionario)
print(myDiccionario["Francia"])

elDiccionario={14:"Alonso","Nombre":"Fernando","Equipo":"Aston Martin","campeonatos":{"temporadas":[2005,2006,2026]}}
print(elDiccionario["campeonatos"])

#Métodos importantes
print(elDiccionario.keys())
print(elDiccionario.values())
print(len(elDiccionario))