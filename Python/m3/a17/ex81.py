c = 0
l = []

while True:
    n = int(input("Digite um valor: "))
    l.append(n)
    c += 1
    r = str(input("Qr continuar [S/N]: ").upper())
    while r not in "SN":
        r = str(input("Tente novamente [S/N]: ").upper())
    if r == "N":
        break

print(f"Você digitou {c} elementos.")
print(f"Os valores em ordem decrescente são {sorted(l)[::-1]}")
if 5 in l:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte lista.")
