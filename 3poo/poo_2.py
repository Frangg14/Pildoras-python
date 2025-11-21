from Herencia import Moto
from Herencia import Furgoneta
from Herencia import CocheElectrico

miMoto = Moto("Honda","CBR")
miMoto.arrancar()
miMoto.acelerar()
#miMoto.caballito()
miMoto.estado()
print("******************")
miFurgoneta = Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
print("******************")
miCoche = CocheElectrico("BYD","E6")
miCoche.estado()