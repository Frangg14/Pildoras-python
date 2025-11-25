import pickle

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

coche1 = Vehiculo("Mazda","MX5")
coche2 = Vehiculo("Seat","Ibiza")
coche3 = Vehiculo("Renault","Clio")
coches = [coche1, coche2, coche3]

fichero = open("losCoches", "wb")
pickle.dump(coches, fichero) # Serializar el objeto
fichero.close()
print("Se han serializado los objetos correctamente.")

#del (fichero) # Eliminar el objeto fichero