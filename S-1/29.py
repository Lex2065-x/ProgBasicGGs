def calcular_media(datos):
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    if n % 2 == 1:
        return datos_ordenados[n // 2]
    else:
        mid1 = datos_ordenados[n // 2 - 1]
        mid2 = datos_ordenados[n // 2]
        return (mid1 + mid2) / 2

def calcular_desviacion_estandar(datos, media):
    varianza = sum((x - media) ** 2 for x in datos) / len(datos)
    return varianza ** 0.5

def calcular_varianza(datos, media):
    return sum((x - media) ** 2 for x in datos) / len(datos)

def calcular_rango(datos):
    return max(datos) - min(datos)

def mostrar_estadisticas(datos):
    media = calcular_media(datos)
    mediana = calcular_mediana(datos)
    desviacion_estandar = calcular_desviacion_estandar(datos, media)
    varianza = calcular_varianza(datos, media)
    rango = calcular_rango(datos)

    print(f"Datos: {datos}")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Desviación Estándar: {desviacion_estandar}")
    print(f"Varianza: {varianza}")
    print(f"Rango: {rango}")

def main():
    print("Bienvenido al Analizador de Datos Estadísticos.")
    datos_input = input("Ingrese los datos separados por comas (por ejemplo: 1,2,3,4,5): ")
   
    datos = [float(x) for x in datos_input.split(",")]

    mostrar_estadisticas(datos)

if __name__ == "__main__":
    main()
