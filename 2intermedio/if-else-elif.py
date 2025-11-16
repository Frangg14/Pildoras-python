#Condicionales
def evaluacion(nota):
    #valoracion="aprobado"
    if nota<5:
        valoracion="suspendido"
    else:
        valoracion="aprobado"
    return valoracion

#(Introducir por teclado)
print("Programa de evaluación de notas de alumnos")
nota_alumno = int(input("Introduce la nota del alumno: ")) #Transforma el string (texto) del input a formato int (numérico)
print(evaluacion(nota_alumno))


print("Verifiación de acceso")
notaAlumno=int(input("Introduce tu nota, por favor: "))
#Uso de else
def ponerNota(nota):
    if nota < 5:
        print("Insuficiente")
    #Instrucción elif
    elif nota < 6:
        print("Suficiente")
    elif nota < 7:
        print("Bien")
    elif nota < 9:
        print("Notable")
    else:
        print("Sobresaliente")
ponerNota(notaAlumno)