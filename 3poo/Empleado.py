from Persona import Persona
class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.__salario = salario
        self.__antiguedad = antiguedad
    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.__salario,"\nAntiguedad: ",self.__antiguedad)