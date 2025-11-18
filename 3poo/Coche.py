class Coche():
    #Propiedades del coche
    #largoChasis = 250
    #anchoChasis = 120
    #ruedas = 4
    #enMarcha = False

    #Constructor, con sus propiedades
    def __init__(self):
        self.__largoChasis = 250 #Los dos guiones bajos indican que es una propiedad privada
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    #Métodos del coche, es decir, el comportamiento del coche
    #También se puedeb crear métodos privados. Ejemplo: def __privado(self):
    def __chequeoInterno(self):
        print("Realizando chequeo interno...")
        self.__gasolina = "Ok"
        self.__aceite = "Ok"
        self.__puertas = "Cerradas"
        if(self.__gasolina == "Ok" and self.__aceite == "Ok" and self.__puertas == "Cerradas"):
            return True
        else:
            return False
        
    def arrancar(self,arrancamos):
        self.__enMarcha = arrancamos
        if(self.__enMarcha):
            chequeo = self.__chequeoInterno()
        if(self.__enMarcha and chequeo):
            print("El coche está arrancando...")
        elif(self.__enMarcha and chequeo == False):
            print("Algo ha ido mal en el chequeo. No se puede arrancar.")
        else:
            print("El coche está parado.")
    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis, "y un largo de", self.__largoChasis)