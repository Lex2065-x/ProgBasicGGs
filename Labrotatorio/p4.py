import math

# Funciones
promedio = lambda numeros: sum(numeros) / len(numeros)

def mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    medio = n // 2
    if n % 2 == 0:
        return (numeros_ordenados[medio - 1] + numeros_ordenados[medio]) / 2
    else:
        return numeros_ordenados[medio]

def desviacion_estandar(numeros):
    prom = promedio(numeros)
    varianza = sum((x - prom) ** 2 for x in numeros) / len(numeros)
    return math.sqrt(varianza)

def calcular_estadisticas(*args):
    numeros = list(args)
    return {
        "Promedio": promedio(numeros),
        "Mediana": mediana(numeros),
        "Desviacion Estandar": desviacion_estandar(numeros)
    }

# Prueba
numeros = [float(x) for x in input("Ingrese una lista de numeros separados por espacio: ").split()]
resultado = calcular_estadisticas(*numeros)
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")