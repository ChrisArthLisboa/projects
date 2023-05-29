
print("--"*16)
print("Sequência de Fibonacci".center(32))
print("--"*16)

cont = 0
q = int(input("Quantos termos: "))
n1 = 0
n2 = 1
n3 = 0

print(n1, "-", n2, end = " - ")
while cont <= q-3:
    n3 = n1 + n2
    print(n3, end=' - ')
    n1 = n2
    n2 = n3
    cont += 1
print("FIM")