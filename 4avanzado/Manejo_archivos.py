from io import open

# Crear y escribir en un archivo de texto, con open
archivo_texto = open("archivo.txt", "w", encoding="utf-8") # El modo "w" es para escribir en el archivo
frase = "Estupendo día para estudiar Python\nEl lenguaje de programación del futuro"
archivo_texto.write(frase) # Con este método escribimos en el archivo
archivo_texto.close() # Siempre cerrar el archivo después de usarlo

# Abrir archivo en modo lectura
archivo_lectura = open("archivo.txt", "r", encoding="utf-8") 
# El modo "r" es para leer el archivo
contenido = archivo_lectura.read() # Leer todo el contenido del archivo
print(contenido) # Mostrar el contenido en pantalla
archivo_lectura.close() # Cerrar el archivo después de leerlo

texto_lineas = open("archivo.txt", "r", encoding="utf-8")
lineas_texto = texto_lineas.readlines() 
# Leer todas las líneas y guardarlas en una lista manipulable
texto_lineas.close()
print(lineas_texto) # Mostrar la lista de líneas
print(lineas_texto[0]) # Mostrar la primera línea del archivo
#También se puede usar un bucle for para recorrer las líneas

linea3 = open("archivo.txt", "a", encoding="utf-8")
linea3.write("\nSiempre es buena ocasión para aprender algo nuevo")
# El modo "a" es para añadir contenido al final del archivo
linea3.close()

# Podemos usar el puntero y manipular su posición con seek() y tell()
lectura = open("archivo.txt", "r", encoding="utf-8")
#lectura.seek(0) # Coloca el puntero al inicio del archivo
#lectura.seek(len(lectura.read())/2) # Coloca el puntero a la mitad del archivo
lectura.seek(len(lectura.readline())) # Coloca el puntero al final de la primera línea
print(lectura.read())
lectura.close()

lectura_escritura = open("archivo.txt", "r+", encoding="utf-8")
# El modo "r+" es para leer y escribir en el archivo
lista_texto = lectura_escritura.readlines()
lista_texto[1] = "Esta línea ha sido incluida desde el exterior\n"

lectura_escritura.seek(0) # Volver al inicio del archivo
lectura_escritura.writelines(lista_texto) # Escribir la lista modificada en el archivo
lectura_escritura.close()