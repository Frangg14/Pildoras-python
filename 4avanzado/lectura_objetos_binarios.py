import pickle
from serializar_objetos import Vehiculo

ficheroApertura = open("losCoches", "rb")
misCoches = pickle.load(ficheroApertura) # Carga (deserializa) la lista de objetos
ficheroApertura.close()

for coche in misCoches:
    print(coche.estado())

# Si lo hacemos separado de el .py principal nos dará error de que no encuentra la clase Coche
# solución: from serializar_objetos import Vehiculo