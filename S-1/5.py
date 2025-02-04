n = int(input("Ingrese un número: "))
if n < 2:
    print("No es primo")
else:
    es_primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            es_primo = False 
            break

    if es_primo:
        print("Es primo")
    else:
        print("No es primo")