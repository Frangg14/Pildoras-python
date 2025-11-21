class Persona:
    def __init__(self, nombre, edad,residencia):
        self.__nombre = nombre
        self.__edad = edad
        self.__residencia = residencia
    def descripcion(self):
        print("Nombre: ",self.__nombre,"\nEdad: ",self.__edad,"\nResidencia: ",self.__residencia)
        