from math import inf


print("--"*12)
print("LOJA SUPER BARATÃO".center(24))
print("--"*12)

c = 0
r = ""
men = inf
menn = ""
s = 0

while r != "N":
    no = str(input("Nome do produto: ").capitalize())
    p = float(input("Preço: R$ "))
    r = str(input("Quer continuar [S/N]: ").upper())
    if p < men:
        men = p
        menn = no
    s+= p
    if p >= 1000:
        c += 1

print("--"*3, "Fim do Programa", "--"*3)

print(f"O total de compra foi R${s:.2f}")
print(f"Temos {c} produtos que custam mais de R$1000.00")
print(f"O produto mais barato foi {menn} que custou R${men:2f}")