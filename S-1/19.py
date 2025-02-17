import random

# Generar un número aleatorio con distribución uniforme entre los números reales (a, b)
# Este intervalo puede ser ajustado a valores más grandes si se necesita simular todos los números reales posibles.
numero_real_uniforme = random.uniform(-1e10, 1e10)  # Usamos un rango grande para cubrir más números reales
print(f"Distribución uniforme con números reales en [-1e10, 1e10]: {numero_real_uniforme}")

# Generar un número aleatorio de tipo flotante (reales) usando una distribución normal
# Parámetros: media = 0, desviación estándar = 1
numero_real_normal = random.gauss(0, 1)  # Normal con media 0 y desviación estándar 1
print(f"Distribución normal (media 0, desviación estándar 1): {numero_real_normal}")

# Generar un número aleatorio real en todo el rango de números flotantes de Python
# Esto se logra generando un número entre -1e10 y 1e10, lo cual cubre muchos valores reales
numero_real_grande = random.uniform(-float('inf'), float('inf'))  # Este enfoque no es práctico, pero da la idea de "todos los reales"
print(f"Valor real en un gran rango: {numero_real_grande}")

# Generar una lista de números reales aleatorios en un rango amplio
lista_reales = [random.uniform(-1e10, 1e10) for _ in range(10)]  # 10 números reales aleatorios
print(f"Lista de 10 números reales aleatorios: {lista_reales}")

# Generar una lista de números reales usando la distribución normal
lista_reales_normales = [random.gauss(0, 1) for _ in range(10)]  # 10 números con distribución normal
print(f"Lista de 10 números reales con distribución normal: {lista_reales_normales}")
