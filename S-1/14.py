while True:
    try:
        numeros = list(map(int, input("\nIntroduce los números separados por espacios: ").split()))
        print("\nMétodos de ordenamiento disponibles:")
        print("1. Burbuja")
        print("2. Selección")
        print("3. Inserción")
        metodo = input("Elige un método (1/2/3): ").strip()
        if metodo == "1":
            for i in range(len(numeros) - 1):
                for j in range(len(numeros) - i - 1):
                    if numeros[j] > numeros[j + 1]:
                        numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

            print("\n✅ Lista ordenada con Burbuja:", numeros)
        elif metodo == "2":
            for i in range(len(numeros)):
                min_index = i
                for j in range(i + 1, len(numeros)):
                    if numeros[j] < numeros[min_index]:
                        min_index = j
                numeros[i], numeros[min_index] = numeros[min_index], numeros[i]
            print("\n✅ Lista ordenada con Selección:", numeros)
        elif metodo == "3":
            for i in range(1, len(numeros)):
                clave = numeros[i]
                j = i - 1
                while j >= 0 and numeros[j] > clave:
                    numeros[j + 1] = numeros[j]
                    j -= 1
                numeros[j + 1] = clave
            print("\nLista ordenada con Inserción:", numeros)
        else:
            print("Opción no válida. Intenta de nuevo.")
            continue 
    except ValueError:
        print("Error: Ingresa solo números separados por espacios.")
        continue
    opcion = input("\n¿Quieres ordenar otra lista? (s/n): ").strip().lower()
    if opcion != "s":
        print("\nSaliendo del programa. ¡Hasta luego!")
        break
