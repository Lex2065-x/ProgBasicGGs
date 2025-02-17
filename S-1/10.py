# Escribir en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de texto.")

# Leer el archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:", contenido)

# Modificar el archivo (agregar texto)
with open("archivo.txt", "a") as archivo:
    archivo.write("\nNueva línea agregada.")
