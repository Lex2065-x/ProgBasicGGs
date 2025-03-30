agenda = []

def agregar_contacto(nombre, numero, correo):
    contacto = (nombre, numero, correo)
    agenda.append(contacto)
    print(f"Contacto {nombre} agregado.")

def buscar_contacto(nombre):
    for contacto in agenda:
        if contacto[0] == nombre:
            print(f"Contacto encontrado: {contacto}")
            return
    print("Contacto no encontrado.")

def listar_contactos():
    for contacto in sorted(agenda):
        print(contacto)

def eliminar_contacto(nombre):
    global agenda
    agenda = [contacto for contacto in agenda if contacto[0] != nombre]
    print(f"Contacto {nombre} eliminado.")

def menu():
    while True:
        print("\nMenu de Gestion de Contactos:")
        print("1. Agregar Contacto")
        print("2. Listar Contactos")
        print("3. Buscar Contacto")
        print("4. Eliminar Contacto")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            numero = input("Ingrese el numero del contacto: ")
            correo = input("Ingrese el correo del contacto: ")
            agregar_contacto(nombre, numero, correo)
        elif opcion == "2":
            print("\nLista de contactos:")
            listar_contactos()
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto(nombre)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intente nuevamente.")

menu()
