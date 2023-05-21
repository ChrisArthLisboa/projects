from math import inf

men = inf
mai = 0
cont = 0
r = ""
s = 0

while r != "N":
    n = int(input("Digite um número: "))
    s += n
    if men > n:
        men = n
    if mai < n:
        mai = n
    r = str(input("Quer continuar [S/N]: ").upper())
    cont += 1

print(f"Você digitou {cont} números e a média deles foi {s/cont:.2f} \nO maior valor foi {mai} e o menor foi {men}.")
