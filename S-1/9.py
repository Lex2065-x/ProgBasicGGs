n = int(input("Ingrese valor a cual lleagremos: "))
par = []
impar = []
for i in range (n+1):
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(par)
print(impar)