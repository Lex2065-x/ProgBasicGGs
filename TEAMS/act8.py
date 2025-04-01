def contadorDeVocales(cadena):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    conteo = {v: 0 for v in vocales}
    
    for caracter in cadena:
        if caracter in conteo:
            conteo[caracter] += 1
    
    return {k: v for k, v in conteo.items() if v > 0}

if __name__ == "__main__":
    palabra = input("Ingrese la palabra a analizar: ")
    print(contadorDeVocales(palabra))