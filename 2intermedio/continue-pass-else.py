def contador_nombre():
    nombre = "Pildoras informaticas"
    contador = 0
    for i in nombre:
        if i == " ": #Ignora los espacios en blanco
            continue
        contador+=1
    print(contador)
#contador_nombre()

def email_validator():
    email = input("Introduce tu email: ")
    for i in email:
        if i == "@":
            arroba = True
            break
    else: #Si no se encuentra el @, se ejecuta este bloque
        arroba = False
    print(arroba)
email_validator()
