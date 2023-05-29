
nma = ""
ma = 0
contf = 0
contg = 0
so = 0

for c in range(0,4):
    print("-"*5, f"{c+1}° PESSOA", "-"*5)
    n = str(input("Nome: ").capitalize().strip())
    i = int(input("Idade: "))
    s = str(input("Sexo [M/F]: ").strip())
    if ma < i and s in "Mm":
        ma = i
        nma = n
    if i < 20 and s in "Ff":
        contf += 1
    contg += 1
    so += i
med = so/contg

print(f"A média de idade do grupo é de {med:.1f} anos")
print(f"O homem mais velho se chama {nma} e tem {ma} anos.")
print(f"Ao todo são {contf} mulheres com menos de 20 anos.")
