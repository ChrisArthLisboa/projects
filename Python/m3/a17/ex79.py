
l = []

while True:
    n = int(input("Digite um valor: "))
    if n not in l:
        l.append(n)
        print(f"número adicionado com sucesso.")
    else:
        print(f"Número não colocado, já foi adicionado anteriormente.")
    r = str(input("Quer continuar [S/N]: ").upper())
    while r not in "SN":
        r = str(input("Tenta novamente: ").upper())
    if r == "N":
        break
print("-="*12)
print(f"Você digitou os valores: {l}.")
