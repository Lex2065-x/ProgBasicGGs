def km_a_millas(km):
    return km * 0.621371

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def litros_a_galones(litros):
    return litros * 0.264172

if __name__ == "__main__":
    print("Opciones de conversion:")
    print("1. Kilometros a millas")
    print("2. Celsius a Fahrenheit")
    print("3. Litros a galones")
    
    opcion = int(input("Seleccione una opcion: "))
    valor = float(input("Ingrese el valor a convertir: "))
    
    if opcion == 1:
        print(f"{valor} km son {km_a_millas(valor)} millas.")
    elif opcion == 2:
        print(f"{valor} C son {celsius_a_fahrenheit(valor)} F.")
    elif opcion == 3:
        print(f"{valor} litros son {litros_a_galones(valor)} galones.")
    else:
        print("Opcion invalida.")
