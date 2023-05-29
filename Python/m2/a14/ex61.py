
print("Gerador de PA.")
print("-="*6)

cont=0
n1 = int(input("1° valor: "))
r = int(input("Razão: "))

while cont != 10:
    print(n1, end='-> ')
    n1 += r
    cont += 1
print("FIM.")
