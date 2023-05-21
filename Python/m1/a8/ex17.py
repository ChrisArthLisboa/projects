import math

co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
h = co**2 + ca**2
print(f"A hipotenusa é igual {math.sqrt(h):.2f}")