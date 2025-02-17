def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i 
    return -1  
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio  
        elif lista[medio] < objetivo:
            izquierda = medio + 1  
        else:
            derecha = medio - 1 
    return -1 
def ingresar_lista():
    print("Ingresa los números de la lista, separados por espacios:")
    entrada = input()  
    lista = list(map(int, entrada.split()))  
    return lista
def ingresar_objetivo():
    print("Ingresa el número objetivo a buscar:")
    objetivo = int(input())  
    return objetivo
def main():
    lista = ingresar_lista()  
    objetivo = ingresar_objetivo()  
    resultado_lineal = busqueda_lineal(lista, objetivo)
    if resultado_lineal != -1:
        print(f'Búsqueda Lineal: El elemento se encuentra en el índice {resultado_lineal}')
    else:
        print("Elemento no encontrado en la búsqueda lineal")

    lista.sort()  
    resultado_binaria = busqueda_binaria(lista, objetivo)
    if resultado_binaria != -1:
        print(f'Búsqueda Binaria: El elemento se encuentra en el índice {resultado_binaria}')
    else:
        print("Elemento no encontrado en la búsqueda binaria")

if __name__ == "__main__":
    main()
