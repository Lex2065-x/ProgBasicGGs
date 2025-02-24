def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def invertir_cadena(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

def main():
    print("Bienvenido al programa de funciones recursivas.")
    
    numero = int(input("Ingrese un número para calcular su factorial: "))
    print(f"El factorial de {numero} es {factorial(numero)}")

    numeros = [int(x) for x in input("Ingrese una lista de números separados por coma: ").split(",")]
    print(f"La suma de los números en la lista es: {suma_lista(numeros)}")

    fibonacci_num = int(input("Ingrese el índice para calcular el número de Fibonacci: "))
    print(f"El número de Fibonacci en la posición {fibonacci_num} es {fibonacci(fibonacci_num)}")

    texto = input("Ingrese una cadena de texto: ")
    print(f"La cadena invertida es: {invertir_cadena(texto)}")

if __name__ == "__main__":
    main()
