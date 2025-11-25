import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.__nombre = nombre
        self.__genero = genero
        self.__edad = edad
        print("Se ha creado una nueva persona, con el nombre de", self.__nombre)

    def __str__(self): # Representación en cadena del objeto Persona
        #return "{}, {}, {}".format(self.__nombre, self.__genero, self.__edad)
        # Hay otra forma más sencilla
        return f"{self.__nombre} {self.__genero} {self.__edad}"
        # Es mucho más cómodo usar f-strings
    
class ListaPersonas:
    personas = []

    def __init__(self):
        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
            #Con este print podemos ver las personas cargadas
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersona(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    def guardarPersonasEnFicheroExterno(self): # Con este método guardamos las personas en un fichero binario
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

miLista = ListaPersonas()
persona = Persona("María","Femenino",20)
miLista.agregarPersona(persona)
miLista.mostrarInfoFicheroExterno()