from math import factorial

n = int(input("Digite um número para \ncalcular o fatorial: "))

print(f"O fatorial de {n}! = ", end=' ')

for c in range(n, 1, -1):
    print(c, end=' x ')

print(f"1 = {factorial(n)}")