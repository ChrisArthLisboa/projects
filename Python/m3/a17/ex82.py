
l = []
li = []
lp = []

while True:
    n = int(input("Digite um valor: "))
    l.append(n)
    if n%2 == 1:
        li.append(n)
    else:
        lp.append(n)
    r = str(input("Qr continuar [S/N]: ").upper())
    while r not in "SN":
        r = str(input("Tente novamente [S/N]: ").upper())
    if r == "N":
        break

print(f"Você digitou os números {l}.")
print(f"A lista de números pares {li}.")
print(f"A lista de números ímpares {lp}.")