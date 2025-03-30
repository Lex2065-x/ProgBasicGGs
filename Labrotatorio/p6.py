class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Anio: {self.anio}, Precio: ${self.precio}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, puertas):
        super().__init__(marca, modelo, anio, precio)
        self.puertas = puertas
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Numero de puertas: {self.puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, cilindrada):
        super().__init__(marca, modelo, anio, precio)
        self.cilindrada = cilindrada
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada} cc")

def menu():
    vehiculos = []
    while True:
        print("\nMenu de Gestion de Vehiculos:")
        print("1. Agregar Automovil")
        print("2. Agregar Motocicleta")
        print("3. Mostrar Vehiculos")
        print("4. Buscar Vehiculo por Marca")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            marca = input("Ingrese la marca: ")
            modelo = input("Ingrese el modelo: ")
            anio = int(input("Ingrese el anio: "))
            precio = float(input("Ingrese el precio: "))
            puertas = int(input("Ingrese el numero de puertas: "))
            auto = Automovil(marca, modelo, anio, precio, puertas)
            vehiculos.append(auto)
            print("Automovil agregado correctamente.")
        elif opcion == "2":
            marca = input("Ingrese la marca: ")
            modelo = input("Ingrese el modelo: ")
            anio = int(input("Ingrese el anio: "))
            precio = float(input("Ingrese el precio: "))
            cilindrada = int(input("Ingrese la cilindrada: "))
            moto = Motocicleta(marca, modelo, anio, precio, cilindrada)
            vehiculos.append(moto)
            print("Motocicleta agregada correctamente.")
        elif opcion == "3":
            if not vehiculos:
                print("No hay vehiculos registrados.")
            else:
                for vehiculo in vehiculos:
                    vehiculo.mostrar_info()
        elif opcion == "4":
            marca_buscar = input("Ingrese la marca del vehiculo a buscar: ")
            encontrados = [vehiculo for vehiculo in vehiculos if vehiculo.marca.lower() == marca_buscar.lower()]
            if encontrados:
                for vehiculo in encontrados:
                    vehiculo.mostrar_info()
            else:
                print("No se encontraron vehiculos de esa marca.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intente nuevamente.")

# Iniciar menu
menu()
