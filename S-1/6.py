cap = float(input("Ingrese valor capital inicial: "))
tas = int(input("Ingrese valor tasa de interes: "))/100
tiem = float(input("Ingrese valor en años: "))
ic = cap*((1+tas)**tiem)
print(f"El interés compuesto al cabo de {tiem} años, con un interés de {tas*100}% es: {ic}")
print ("el beneficio es:", ic - cap)