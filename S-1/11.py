def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]
texto = input("Introduce una cadena: ")
if es_palindromo(texto):
    print("La cadena es un palíndromo.")
else:
    print("La cadena NO es un palíndromo.")
