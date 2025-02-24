def suma_serie_numerica(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

def suma_serie_aritmetica(a, d, n):
    suma = n / 2 * (2 * a + (n - 1) * d)
    return suma

def suma_serie_geometrica(a, r, n):
    if r == 1:
        suma = a * n
    else:
        suma = a * (1 - r**n) / (1 - r)
    return suma

def main():
    while True:
        print("\n--- Menú de opciones ---")
        print("1. Sumar los primeros n números naturales")
        print("2. Sumar una serie aritmética")
        print("3. Sumar una serie geométrica")
        print("4. Salir")
        
        opcion = int(input("Seleccione una opción (1-4): "))
        
        if opcion == 1:
            n = int(input("Ingrese el número de términos (n) de la serie: "))
            resultado = suma_serie_numerica(n)
            print(f"La suma de los primeros {n} números naturales es: {resultado}")
        
        elif opcion == 2:
            a = float(input("Ingrese el primer término (a) de la serie: "))
            d = float(input("Ingrese la diferencia común (d) de la serie: "))
            n = int(input("Ingrese el número de términos (n) de la serie: "))
            resultado = suma_serie_aritmetica(a, d, n)
            print(f"La suma de la serie aritmética es: {resultado}")
        
        elif opcion == 3:
            a = float(input("Ingrese el primer término (a) de la serie: "))
            r = float(input("Ingrese la razón común (r) de la serie: "))
            n = int(input("Ingrese el número de términos (n) de la serie: "))
            resultado = suma_serie_geometrica(a, r, n)
            print(f"La suma de la serie geométrica es: {resultado}")
        
        elif opcion == 4:
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 4.")

if __name__ == "__main__":
    main()
