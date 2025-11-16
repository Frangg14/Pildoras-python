#Instrucción yield from
#Sirve para simplificar el código cuando un generador llama a otro generador.
#Es algo similar a los arrays bidimensionales.

def devuelve_ciudades(*ciudades): #El * indica que puede recibir múltiples argumentos, será una tupla
    for elemento in ciudades:
        #for sub_elemento in elemento:
            yield from elemento  #Con yield from, se itera directamente sobre cada carácter de la cadena, sin necesidad de un bucle for adicional.

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")
def ciudades(ciudades_devueltas):
    print(next(ciudades_devueltas))
    print(next(ciudades_devueltas)) 
    print(next(ciudades_devueltas)) 
    print(next(ciudades_devueltas)) 
ciudades(ciudades_devueltas) #Devuelve 'Madr'
