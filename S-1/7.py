a = int(input("ingrese valor numerico: "))
b = int(input("ingrese valor numerico para ver si es multiplo: "))
if a % 2 == 0:
    print(f"{a} es un número par")
if a % 2 != 0:
    print(f"{a} es un número impar")
if a % b == 0:
    print(f"{a} es múltiplo de {b}")
if a % b != 0:
    print(f"{a} no es múltiplo de {b}")