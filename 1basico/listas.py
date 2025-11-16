#Las listas son el equivalente/parecido a los arrays
#Sirven para almacenar varios valores
miLista=["Antonio","Pepe","María",7,True,75.8]

#Añadir elementos a la lista
#miLista.append("Manolo")
#miLista.insert(1,"Sandra")
#miLista.extend(["Sandra","Ana","Manolo"])
print(miLista[:])

#Para hacer comprobaciones
print(miLista.index("Pepe"))
print("Pepe" in miLista)

#Para eliminar
miLista.remove(7)
print(miLista[:])

#Eliminar último elemento
miLista.pop()
print(miLista[:])

#Para unir listas
miLista2=["José Luis","Rodolfo"]
miLista3=miLista+miLista2 #El '+' sirve para concatenar las listas
print(miLista3[:])

#"Repetir" la lista
miLista4 = ["Lolo","Laura","Davo"] * 3
print(miLista4[:])