def mostrar_menu():
    print("\n--- Menú de la Agenda de Contactos ---")
    print("1. Agregar un nuevo contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar un contacto")
    print("4. Eliminar un contacto")
    print("5. Salir")

def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    email = input("Ingrese el correo electrónico: ")
    agenda[nombre] = {'telefono': telefono, 'email': email}
    print(f"Contacto de {nombre} agregado exitosamente.")

def ver_contactos(agenda):
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("\n--- Contactos en la agenda ---")
        for nombre, datos in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"  Teléfono: {datos['telefono']}")
            print(f"  Email: {datos['email']}\n")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"\n--- Información del contacto ---")
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"No se encontró el contacto con el nombre {nombre}.")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto de {nombre} eliminado exitosamente.")
    else:
        print(f"No se encontró el contacto con el nombre {nombre}.")

def main():
   
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            agregar_contacto(agenda)
        elif opcion == '2':
            ver_contactos(agenda)
        elif opcion == '3':
            buscar_contacto(agenda)
        elif opcion == '4':
            eliminar_contacto(agenda)
        elif opcion == '5':
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 5.")

if __name__ == "__main__":
    main()