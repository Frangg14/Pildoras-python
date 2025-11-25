import pickle

lista_nombres = ["Ana", "Luis", "María", "Carlos"]

# Serialización: Guardar la lista en un archivo binario
fichero_binario = open("lista_nombres", "wb")
#Volcado de la lista al fichero
pickle.dump(lista_nombres, fichero_binario)
print("Lista serializada correctamente.")
fichero_binario.close()

#del fichero_binario  # Eliminamos la referencia al fichero