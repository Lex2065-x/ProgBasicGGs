a = 0
b = 1 
n = int(input("ingrese valor a fibbonaciar "))
for i in range (n):
    print(a)
    aux = a
    a = b 
    b = aux + b