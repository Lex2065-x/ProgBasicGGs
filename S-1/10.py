def escribir_archivo(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        texto = input("Introduce el texto para escribir en el archivo: ")
        archivo.write(texto)
    print("Archivo escrito correctamente.")
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print("\nContenido del archivo:")
            print(contenido if contenido else "El archivo está vacío.")
    except FileNotFoundError:
        print("El archivo no existe. Primero escribe en él.")
def editar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "a") as archivo:
            texto = input("Introduce el texto para agregar al archivo: ")
            archivo.write("\n" + texto)
        print("Texto agregado correctamente.")
    except FileNotFoundError:
        print("El archivo no existe. Primero escribe en él.")
def limpiar_archivo(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        pass  
    print("El archivo ha sido limpiado.")
nombre_archivo = "archivo.txt"
while True:
    print("\nOpciones:")
    print("1. Escribir en el archivo")
    print("2. Leer el archivo")
    print("3. Editar el archivo")
    print("4. Limpiar el archivo")
    print("5. Salir")
    opcion = input("Elige una opción (1-5): ")
    if opcion == "1":
        escribir_archivo(nombre_archivo)
    elif opcion == "2":
        leer_archivo(nombre_archivo)
    elif opcion == "3":
        editar_archivo(nombre_archivo)
    elif opcion == "4":
        limpiar_archivo(nombre_archivo)
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
