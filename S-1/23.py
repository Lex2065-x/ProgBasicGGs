def crear_matriz(filas, columnas):
    matriz = []
    print(f"Ingrese los elementos para la matriz {filas}x{columnas}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Ingrese el elemento en la posición ({i+1},{j+1}): "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]
    return matriz_transpuesta

def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    suma = [[matriz1[i][j] + matriz2[i][j] for j in range(columnas)] for i in range(filas)]
    return suma

def restar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resta = [[matriz1[i][j] - matriz2[i][j] for j in range(columnas)] for i in range(filas)]
    return resta

def multiplicar_por_escalar(matriz, escalar):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = [[matriz[i][j] * escalar for j in range(columnas)] for i in range(filas)]
    return resultado

def multiplicar_matrices(matriz1, matriz2):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])

    if columnas1 != filas2:
        print("No se pueden multiplicar estas matrices. Las dimensiones no son compatibles.")
        return None

    resultado = [[sum(matriz1[i][k] * matriz2[k][j] for k in range(filas2)) for j in range(columnas2)] for i in range(filas1)]
    return resultado

def main():
    print("Operaciones con matrices:")
    matriz = []
    while True:
        print("\nOpciones:")
        print("1. Crear una matriz")
        print("2. Transponer una matriz")
        print("3. Sumar dos matrices")
        print("4. Restar dos matrices")
        print("5. Multiplicar una matriz por un escalar")
        print("6. Multiplicar dos matrices")
        print("7. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Opción no válida. Por favor ingrese un número.")
            continue

        if opcion == 1:
            filas = int(input("Ingrese el número de filas de la matriz: "))
            columnas = int(input("Ingrese el número de columnas de la matriz: "))
            matriz = crear_matriz(filas, columnas)
            print("\nMatriz creada:")
            mostrar_matriz(matriz)

        elif opcion == 2:
            if not matriz:
                print("Primero debe crear una matriz.")
                continue
            print("\nMatriz a transponer:")
            mostrar_matriz(matriz)
            matriz_transpuesta = transponer_matriz(matriz)
            print("\nMatriz transpuesta:")
            mostrar_matriz(matriz_transpuesta)

        elif opcion == 3:
            if not matriz:
                print("Primero debe crear una matriz.")
                continue
            filas = len(matriz)
            columnas = len(matriz[0])
            print("\nIngrese los elementos para la segunda matriz:")
            matriz2 = crear_matriz(filas, columnas)
            suma = sumar_matrices(matriz, matriz2)
            print("\nMatriz resultante de la suma:")
            mostrar_matriz(suma)

        elif opcion == 4:
            if not matriz:
                print("Primero debe crear una matriz.")
                continue
            filas = len(matriz)
            columnas = len(matriz[0])
            print("\nIngrese los elementos para la segunda matriz:")
            matriz2 = crear_matriz(filas, columnas)
            resta = restar_matrices(matriz, matriz2)
            print("\nMatriz resultante de la resta:")
            mostrar_matriz(resta)

        elif opcion == 5:
            if not matriz:
                print("Primero debe crear una matriz.")
                continue
            escalar = float(input("\nIngrese el número escalar para multiplicar la matriz: "))
            resultado = multiplicar_por_escalar(matriz, escalar)
            print("\nMatriz multiplicada por el escalar:")
            mostrar_matriz(resultado)

        elif opcion == 6:
            if not matriz:
                print("Primero debe crear una matriz.")
                continue
            filas = len(matriz)
            columnas = len(matriz[0])
            print("\nIngrese los elementos para la segunda matriz:")
            matriz2 = crear_matriz(columnas, int(input("Ingrese el número de columnas de la segunda matriz: ")))
            resultado = multiplicar_matrices(matriz, matriz2)
            if resultado:
                print("\nMatriz resultante de la multiplicación:")
                mostrar_matriz(resultado)

        elif opcion == 7:
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    main()
