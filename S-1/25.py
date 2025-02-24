def calcular_histograma(datos, num_bins):
  
    minimo = min(datos)
    maximo = max(datos)

    bin_width = (maximo - minimo) / num_bins

    bins = [0] * num_bins  

    for dato in datos:
        
        index = int((dato - minimo) / bin_width)
        if index == num_bins:  
            index -= 1
        bins[index] += 1

    return bins, minimo, bin_width, maximo

def visualizar_histograma(bins, minimo, bin_width, maximo):
    print("\n--- Histograma ---")
    for i, bin_count in enumerate(bins):
        bin_start = minimo + i * bin_width
        bin_end = bin_start + bin_width
        print(f"{bin_start:.2f} - {bin_end:.2f}: {'*' * bin_count}")

def analizar_datos(datos):
    media = sum(datos) / len(datos)
    varianza = sum((x - media) ** 2 for x in datos) / len(datos)
    desviacion_estandar = varianza ** 0.5
    minimo = min(datos)
    maximo = max(datos)

    print("\n--- Análisis de los Datos ---")
    print(f"Media: {media:.2f}")
    print(f"Desviación Estándar: {desviacion_estandar:.2f}")
    print(f"Varianza: {varianza:.2f}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")

def main():
    
    datos = [1.5, 2.3, 2.8, 3.1, 3.5, 4.2, 5.5, 6.2, 6.8, 7.4, 8.1, 8.9, 9.2]
    
    num_bins = int(input("Ingrese el número de bins para el histograma: "))
    
    bins, minimo, bin_width, maximo = calcular_histograma(datos, num_bins)

    visualizar_histograma(bins, minimo, bin_width, maximo)

    analizar_datos(datos)

if __name__ == "__main__":
    main()
