def contar_vocales_consonantes(texto):
    texto = texto.lower() 
    vocales = "aeiou"
    consonantes = "bcdfghjklmnpqrstvwxyz"
    
    contador_vocales = sum(1 for letra in texto if letra in vocales)
    contador_consonantes = sum(1 for letra in texto if letra in consonantes)
    
    return contador_vocales, contador_consonantes

cadena = input("Ingrese una cadena de texto: ")
vocales, consonantes = contar_vocales_consonantes(cadena)
print(f"Vocales: {vocales}, Consonantes: {consonantes}")