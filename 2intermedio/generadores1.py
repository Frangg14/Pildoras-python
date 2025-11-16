#Instrucción yield, se crea un objeto generador iterable. 
#Cada vez que se llama a la función, esta reanuda su ejecución 
#desde el punto donde se quedó la última vez. Devuelve un valor.

#Función clásica
def genera_pares(limite):
    num=1
    lista_pares=[]
    while num<limite:
        lista_pares.append(num*2)
        num+=1
    return lista_pares
#print(genera_pares(10))

#Con generador
def lista_pares(limite):
    num=1
    while num<limite:
        yield num*2
        num+=1
devuelve_pares=lista_pares(10) #Guarda un objeto iterable de 9 pares

def pares(devuelve_pares):
    print(next(devuelve_pares)) # Devuelve 2
    print("Más código entre yields") #Entra en suspensión hasta la siguiente llamada
    print(next(devuelve_pares)) # Devuelve 4
    print("Más código entre yields") #Entra en suspensión hasta la siguiente llamada
    print(next(devuelve_pares)) # Devuelve 6
    print("Más código entre yields") #Entra en suspensión hasta la siguiente llamada
    print(next(devuelve_pares)) # Devuelve 8
pares(devuelve_pares)

#El generador sirve para no cargar en memoria grandes cantidades de datos.
#Por ejemplo, si queremos generar una lista de números pares hasta 1 millón,
#con el generador no cargamos todos los números en memoria, 
# sino que los vamos generando uno a uno.