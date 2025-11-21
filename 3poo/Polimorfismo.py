class Coche:
    def desplazamiento(self):
        print("El coche se desplaza sobre 4 ruedas.")

class Moto:
    def desplazamiento(self):
        print("La moto se desplaza sobre 2 ruedas.")

class Camion:
    def desplazamiento(self):
        print("El camión se desplaza sobre 6 ruedas.")

miVehiculo = Moto()
#miVehiculo.desplazamiento()

miVehiculo2 = Coche()
#miVehiculo2.desplazamiento()

miVehiculo3 = Camion()
#miVehiculo3.desplazamiento()

#Uso del polimorfismo
# Por ejemplo a través de una función
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento() 
    # Llamada al método desplazamiento del objeto pasado como argumento
desplazamientoVehiculo(miVehiculo)
desplazamientoVehiculo(miVehiculo2)
desplazamientoVehiculo(miVehiculo3)
