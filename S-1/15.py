def bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = int(input("Ingresa un año: "))

if bisiesto(year):
    print(f"El año {year} es bisiesto.")
else:
    print(f"El año {year} no es bisiesto.")