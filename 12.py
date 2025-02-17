while True:
    try:
        num1 = float(input("\nIntroduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        num3 = float(input("Introduce el tercer número: "))
        if num1 >= num2 and num1 >= num3:
            mayor = num1
        elif num2 >= num1 and num2 >= num3:
            mayor = num2
        else:
            mayor = num3
        print(f"\nEl número mayor es: {mayor}")
    except ValueError:
        print("Error: Ingresa solo números válidos.")
    opcion = input("\n¿Quieres intentar otra vez? (s/n): ").strip().lower()
    if opcion != "s":
        print("Saliendo del programa. ¡Hasta luego!")
        break