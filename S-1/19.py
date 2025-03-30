import random

numero_real_uniforme = random.uniform(-1e10, 1e10)  
print(f"Distribución uniforme con números reales en [-1e10, 1e10]: {numero_real_uniforme}")

numero_real_normal = random.gauss(0, 1)  
print(f"Distribución normal (media 0, desviación estándar 1): {numero_real_normal}")

numero_real_grande = random.uniform(-float('inf'), float('inf'))  
print(f"Valor real en un gran rango: {numero_real_grande}")

lista_reales = [random.uniform(-1e10, 1e10) for _ in range(10)] 
print(f"Lista de 10 números reales aleatorios: {lista_reales}")

lista_reales_normales = [random.gauss(0, 1) for _ in range(10)]  
print(f"Lista de 10 números reales con distribución normal: {lista_reales_normales}")
