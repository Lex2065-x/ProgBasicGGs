import math

def area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio ** 2

def volumen_esfera(radio):
    """Calcula el volumen de una esfera dado su radio."""
    return (4/3) * math.pi * radio ** 3

def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dada su base y altura."""
    return base * altura

def volumen_prisma(base, altura, profundidad):
    """Calcula el volumen de un prisma rectangular."""
    return base * altura * profundidad

def area_triangulo(base, altura):
    """Calcula el área de un triángulo."""
    return (base * altura) / 2

def volumen_piramide(base, altura):
    """Calcula el volumen de una pirámide de base cuadrada."""
    return (1/3) * base ** 2 * altura
def menu():
    while True:
        print("\nSeleccione la figura geométrica:")
        print("1. Círculo (Área)")
        print("2. Esfera (Volumen)")
        print("3. Rectángulo (Área)")
        print("4. Prisma rectangular (Volumen)")
        print("5. Triángulo (Área)")
        print("6. Pirámide cuadrada (Volumen)")
        print("7. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            radio = float(input("Ingrese el radio: "))
            print(f"Área del círculo: {area_circulo(radio)}")
        elif opcion == "2":
            radio = float(input("Ingrese el radio: "))
            print(f"Volumen de la esfera: {volumen_esfera(radio)}")
        elif opcion == "3":
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            print(f"Área del rectángulo: {area_rectangulo(base, altura)}")
        elif opcion == "4":
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            profundidad = float(input("Ingrese la profundidad: "))
            print(f"Volumen del prisma rectangular: {volumen_prisma(base, altura, profundidad)}")
        elif opcion == "5":
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            print(f"Área del triángulo: {area_triangulo(base, altura)}")
        elif opcion == "6":
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            print(f"Volumen de la pirámide cuadrada: {volumen_piramide(base, altura)}")
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
if __name__ == "__main__":
    menu()
