from Coche import Coche #Importar la clase Coche desde el archivo Coche.py
coche = Coche() #Crear un objeto de la clase Coche. Hemos instanciado la clase Coche
#Acceder a las propiedades del objeto coche
coche.arrancar(True)  #Llamar al método arrancar del objeto coche
coche.estado()

print("-----------------Coche 2-------------------------")
miCoche = Coche()
miCoche.arrancar(False)
#miCoche.__chequeoInterno() 
#Intentamos acceder al método privado __chequeoInterno desde 
#fuera de la clase, lo cual no es posible y dará error
miCoche.__ruedas=2 
#Accedemos a la propiedad ruedas y la modificamos, cosa que no debe hacerse. 
#Al ser privada (__) no debería dejarse modificar desde fuera de la clase
miCoche.estado()