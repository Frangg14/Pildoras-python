class Vehiculo:
    def __init__(self,marca,modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__enmarcha = False
        self.__acelera = False
        self.__frena = False

    def arrancar(self):
        self.__enmarcha = True
    def acelerar(self):
        self.__acelera = True
    def frenar(self):
        self.__frena = True
    def estado(self):
        print("Marca:",self.__marca,"\nModelo:",self.__modelo,"\nEn Marcha:",self.__enmarcha,"\nAcelerando:",self.__acelera,"\nFrenando:",self.__frena)
        #Disclaimer: "\n" se usa para salto de linea

class Furgoneta(Vehiculo):
    def carga(self,cargar):
        self.__cargado = cargar
        if self.__cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"
        
class VElectrico(Vehiculo):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.__autonomia = 100
    def cargarEnergia(self):
        self.__cargando = True
    def estado(self):
        super().estado()
        print("Autonomia:",self.__autonomia,"%")

class Moto(Vehiculo):
    __hcaballito = ""
    def caballito(self):
        self.__hcaballito = "Voy haciendo el caballito"
    def estado(self):
        super().estado() #El super() llama al metodo estado de la clase padre
        if self.__hcaballito != "":
            print(self.__hcaballito)
        else:
            print("No estoy haciendo el caballito")

class CocheElectrico(VElectrico,Vehiculo):
    pass