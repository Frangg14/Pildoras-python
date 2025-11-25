import pickle

fichero=open("lista_nombres", "rb")
lista=pickle.load(fichero)
fichero.close()
print("Lista deserializada correctamente.")
print(lista)