class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Se han depositado ${cantidad}.")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro exitoso. Se han retirado ${cantidad}.")
            else:
                print("No hay suficiente saldo para realizar el retiro.")
        else:
            print("El monto a retirar debe ser positivo.")

    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo}")

def mostrar_menu():
    print("\n--- Menú de Cuenta Bancaria ---")
    print("1. Realizar Depósito")
    print("2. Realizar Retiro")
    print("3. Consultar Saldo")
    print("4. Salir")

def main():
    nombre = input("Ingrese el nombre del titular de la cuenta: ")
    cuenta = CuentaBancaria(nombre)  

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == '2':
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == '3':
            cuenta.consultar_saldo()
        elif opcion == '4':
            print("Gracias por usar el sistema de cuentas bancarias. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 4.")

if __name__ == "__main__":
    main()
