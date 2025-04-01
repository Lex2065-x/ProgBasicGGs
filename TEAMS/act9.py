def ubicadorDeVocales(cadena):
    """
    Función que ubica las apariciones de vocales en una cadena y devuelve un diccionario
    con las vocales encontradas y sus posiciones en la cadena.
    """
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    ubicaciones = {}
    
    for i, caracter in enumerate(cadena):
        if caracter in vocales:
            if caracter not in ubicaciones:
                ubicaciones[caracter] = []
            ubicaciones[caracter].append(i)
    
    return ubicaciones

print(ubicadorDeVocales("murcielago"))
print(ubicadorDeVocales("eucalipto"))
print(ubicadorDeVocales("Albericoque"))