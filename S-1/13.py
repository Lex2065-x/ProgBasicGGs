archivo_nombre = "conversion_temperaturas.txt"
while True:
    try:
        # Solicitar la temperatura y la escala
        valor = float(input("\nIntroduce el valor de la temperatura: "))
        escala = input("Introduce la escala (C, F, K): ").strip().lower()
        if escala == "c":  # De Celsius a otras escalas
            celsius = valor
            fahrenheit = (valor * 9/5) + 32
            kelvin = valor + 273.15
        elif escala == "f":  # De Fahrenheit a otras escalas
            celsius = (valor - 32) * 5/9
            fahrenheit = valor
            kelvin = celsius + 273.15
        elif escala == "k":  # De Kelvin a otras escalas
            celsius = valor - 273.15
            fahrenheit = (celsius * 9/5) + 32
            kelvin = valor
        else:
            print("❌ Escala no válida. Usa C, F o K.")
            continue 
        print(f"\n🌡 Resultados:")
        print(f"Celsius: {celsius:.2f}°C")
        print(f"Fahrenheit: {fahrenheit:.2f}°F")
        print(f"Kelvin: {kelvin:.2f}K")
        with open(archivo_nombre, "a") as archivo:
            archivo.write(f"\nEntrada: {valor}°{escala.upper()}\n")
            archivo.write(f"Celsius: {celsius:.2f}°C\n")
            archivo.write(f"Fahrenheit: {fahrenheit:.2f}°F\n")
            archivo.write(f"Kelvin: {kelvin:.2f}K\n")
            archivo.write("="*30 + "\n")
        print(f"\n✅ Conversión guardada en '{archivo_nombre}'.")
    except ValueError:
        print("Error: Ingresa un número válido.")
    opcion = input("\n¿Quieres convertir otra temperatura? (s/n): ").strip().lower()
    if opcion != "s":
        print(f"\n👋 Saliendo. Los resultados están guardados en '{archivo_nombre}'. ¡Hasta luego!")
        break
