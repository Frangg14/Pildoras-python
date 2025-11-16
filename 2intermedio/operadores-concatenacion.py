def salarios():
    salario_presidente=int(input("Introduce salario del presidente: "))
    print("Salario presidente: " + str(salario_presidente))
    salario_director=int(input("Introduce salario del director: "))
    print("Salario director: " + str(salario_director))
    salario_jefe_area=int(input("Introduce salario del jefe de área: "))
    print("Salario jefe de área: " + str(salario_jefe_area))
    salario_administrativo=int(input("Introduce salario del administrativo: "))
    print("Salario jefe de área: " + str(salario_administrativo))

    #Concatenacion de comparación
    if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
        print("Todo correcto")
    else:
        print("Algo falla en esta empresa")
        
#salarios()

#Operadores lógicos
def beca():
    print("Programa de becas")
    distancia = int(input("Introduce la distancia a la escuela en km: "))
    num_hermanos = int(input("Introduce el número de hermanos que van a la misma escuela: "))
    salario_familia = int(input("Introduce el salario anual de la familia (€): "))
    if(distancia > 40 and num_hermanos > 2 or salario_familia <= 20000):
        print("Tienes beca de 5000€")
    else:
        print("No tienes derecho a beca")
#beca()

def asignaturaOptativa():
    print("Asignaturas optativas 2025")
    print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
    opcion = input("Escribe la asignatura escogida: ")
    asignatura = opcion.lower()
    if asignatura in ("informática gráfica","pruebas de software","usabilidad y accesibilidad"):
        print("Has elegido la optativa -> " + asignatura)
    else:
        print("La asignatura escogida no está contemplada")
asignaturaOptativa()