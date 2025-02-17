class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def agregar(self, item):
        self.items.append(item)
    
    def sacar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
    
    def ver_cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None
    
    def mostrar(self):
        return self.items

class Cola:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def agregar(self, item):
        self.items.append(item)
    
    def sacar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None
    
    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]
        return None
    
    def mostrar(self):
        return self.items

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.esta_vacia():
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
        else:
            self.cabeza = nuevo_nodo
    
    def eliminar(self, valor):
        if self.esta_vacia():
            return False
        nodo_actual = self.cabeza
        if nodo_actual.valor == valor:
            self.cabeza = nodo_actual.siguiente
            return True
        while nodo_actual.siguiente:
            if nodo_actual.siguiente.valor == valor:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return True
            nodo_actual = nodo_actual.siguiente
        return False
    
    def mostrar(self):
        elementos = []
        nodo_actual = self.cabeza
        while nodo_actual:
            elementos.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return elementos

def menu():
    pila = Pila()
    cola = Cola()
    lista = ListaEnlazada()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar a la Pila")
        print("2. Agregar a la Cola")
        print("3. Agregar a la Lista Enlazada")
        print("4. Ver Pila")
        print("5. Ver Cola")
        print("6. Ver Lista Enlazada")
        print("7. Eliminar de la Lista Enlazada")
        print("8. Salir")
        opcion = input("Elige una opción (1-8): ")

        if opcion == "1":
            valor = input("Introduce un valor para agregar a la Pila: ")
            pila.agregar(valor)
            print(f"Elemento '{valor}' agregado a la Pila.")
        
        elif opcion == "2":
            valor = input("Introduce un valor para agregar a la Cola: ")
            cola.agregar(valor)
            print(f"Elemento '{valor}' agregado a la Cola.")
        
        elif opcion == "3":
            valor = input("Introduce un valor para agregar a la Lista Enlazada: ")
            lista.agregar(valor)
            print(f"Elemento '{valor}' agregado a la Lista Enlazada.")
        
        elif opcion == "4":
            print("Elementos en la Pila:", pila.mostrar())
        
        elif opcion == "5":
            print("Elementos en la Cola:", cola.mostrar())
        
        elif opcion == "6":
            print("Elementos en la Lista Enlazada:", lista.mostrar())
        
        elif opcion == "7":
            valor = input("Introduce un valor para eliminar de la Lista Enlazada: ")
            if lista.eliminar(valor):
                print(f"Elemento '{valor}' eliminado de la Lista Enlazada.")
            else:
                print(f"Elemento '{valor}' no encontrado en la Lista Enlazada.")
        
        elif opcion == "8":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida, por favor elige una opción del 1 al 8.")
menu()
