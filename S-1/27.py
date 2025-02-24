def convertir_longitud(valor, unidad_origen, unidad_destino):
    
    conversiones = {
        'metros': 1,
        'kilometros': 1000,
        'centimetros': 0.01,
        'milimetros': 0.001,
        'pulgadas': 0.0254,
        'pies': 0.3048,
        'yardas': 0.9144
    }
    
    valor_en_metros = valor * conversiones[unidad_origen]
    valor_convertido = valor_en_metros / conversiones[unidad_destino]
    
    return valor_convertido

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Celsius" and unidad_destino == "Fahrenheit":
        return (valor * 9/5) + 32
    elif unidad_origen == "Fahrenheit" and unidad_destino == "Celsius":
        return (valor - 32) * 5/9
    elif unidad_origen == "Celsius" and unidad_destino == "Kelvin":
        return valor + 273.15
    elif unidad_origen == "Kelvin" and unidad_destino == "Celsius":
        return valor - 273.15
    elif unidad_origen == "Fahrenheit" and unidad_destino == "Kelvin":
        return (valor - 32) * 5/9 + 273.15
    elif unidad_origen == "Kelvin" and unidad_destino == "Fahrenheit":
        return (valor - 273.15) * 9/5 + 32
    else:
        return valor 
def mostrar_menu():
    print("\n--- Conversor de Unidades ---")
    print("1. Convertir Longitud")
    print("2. Convertir Temperatura")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            print("\n--- Convertir Longitud ---")
            valor = float(input("Ingrese el valor a convertir: "))
            unidad_origen = input("Ingrese la unidad de origen (metros, kilometros, centimetros, milimetros, pulgadas, pies, yardas): ").lower()
            unidad_destino = input("Ingrese la unidad de destino (metros, kilometros, centimetros, milimetros, pulgadas, pies, yardas): ").lower()
            
            if unidad_origen in ['metros', 'kilometros', 'centimetros', 'milimetros', 'pulgadas', 'pies', 'yardas'] and unidad_destino in ['metros', 'kilometros', 'centimetros', 'milimetros', 'pulgadas', 'pies', 'yardas']:
                resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
                print(f"{valor} {unidad_origen} son {resultado} {unidad_destino}")
            else:
                print("Unidad no válida. Por favor, intente de nuevo.")

        elif opcion == '2':
            print("\n--- Convertir Temperatura ---")
            valor = float(input("Ingrese el valor a convertir: "))
            unidad_origen = input("Ingrese la unidad de origen (Celsius, Fahrenheit, Kelvin): ").capitalize()
            unidad_destino = input("Ingrese la unidad de destino (Celsius, Fahrenheit, Kelvin): ").capitalize()
            
            if unidad_origen in ['Celsius', 'Fahrenheit', 'Kelvin'] and unidad_destino in ['Celsius', 'Fahrenheit', 'Kelvin']:
                resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
                print(f"{valor} {unidad_origen} son {resultado} {unidad_destino}")
            else:
                print("Unidad no válida. Por favor, intente de nuevo.")

        elif opcion == '3':
            print("Saliendo del conversor...")
            break
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 3.")

if __name__ == "__main__":
    main()
