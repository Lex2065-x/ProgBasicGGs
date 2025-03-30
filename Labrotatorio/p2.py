inventario = []

def agregar_producto(nombre, categoria, precio, cantidad):
    producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print(f"Producto {nombre} agregado.")

def eliminar_producto(nombre):
    global inventario
    inventario = [producto for producto in inventario if producto["nombre"] != nombre]
    print(f"Producto {nombre} eliminado.")

def buscar_producto(nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            print(f"Producto encontrado: {producto}")
            return
    print("Producto no encontrado.")

def mostrar_productos():
    productos_ordenados = sorted(inventario, key=lambda x: x["precio"])
    for producto in productos_ordenados:
        print(producto)

# Entrada de productos por el usuario
n = int(input("Cuantos productos desea agregar? "))
for _ in range(n):
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoria: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))
    agregar_producto(nombre, categoria, precio, cantidad)

# Mostrar productos agregados
print("\nInventario actual:")
mostrar_productos()

# Buscar y eliminar productos de ejemplo
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
buscar_producto(nombre_buscar)

nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")
eliminar_producto(nombre_eliminar)

print("\nInventario actualizado:")
mostrar_productos()