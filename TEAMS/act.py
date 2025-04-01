import cmath

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2 * a)
        x2 = (-b - discriminante**0.5) / (2 * a)
        return f"Dos soluciones reales distintas: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        x = -b / (2 * a)
        return f"Una solución real: x = {x}"
    else:
        x1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
        return f"Dos soluciones complejas: x1 = {x1}, x2 = {x2}"

if __name__ == "__main__":
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    c = float(input("Ingrese el coeficiente c: "))
    resultado = resolver_ecuacion_cuadratica(a, b, c)
    print(resultado)
