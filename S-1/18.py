import math

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return raiz1, raiz2
    
    elif discriminante == 0:
        raiz = -b / (2 * a)
        return raiz,
    
    else:
        return None

def main():
    print("Ecuación cuadrática: ax^2 + bx + c = 0")
    
    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))
    c = float(input("Introduce el valor de c: "))
    
    if a == 0:
        print("El valor de 'a' no puede ser cero. No es una ecuación cuadrática.")
        return
    
    resultado = resolver_ecuacion_cuadratica(a, b, c)
    
    if resultado is None:
        print("La ecuación no tiene soluciones reales.")
    elif len(resultado) == 1:
        print(f"La solución de la ecuación es: {resultado[0]}")
    else:
        print(f"Las soluciones de la ecuación son: {resultado[0]} y {resultado[1]}")

main()
