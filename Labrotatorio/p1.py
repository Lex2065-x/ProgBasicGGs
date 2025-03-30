def analizar_texto(texto):
    palabras = texto.lower().split()
    num_palabras = len(palabras)
    palabras_unicas = set(palabras)
    freq_palabras = {}
    
    for palabra in palabras:
        if palabra in freq_palabras:
            freq_palabras[palabra] += 1
        else:
            freq_palabras[palabra] = 1
    
    palabra_mas_frecuente = max(freq_palabras, key=freq_palabras.get)
    resumen = {
        "Total de palabras": num_palabras,
        "Palabras unicas": len(palabras_unicas),
        "Frecuencia de palabras": freq_palabras,
        "Palabra mas frecuente": palabra_mas_frecuente,
        "Cantidad": freq_palabras[palabra_mas_frecuente]
    }
    
    return resumen

test_texto = input("Ingrese un texto para analizar: ")
resultado = analizar_texto(test_texto)
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")