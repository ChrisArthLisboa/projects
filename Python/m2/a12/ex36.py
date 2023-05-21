
v = float(input("Valor da casa: R$"))
s = float(input("Salário do comprador: R$"))
t = int(input("Quantos anos de financiamento: "))
if s*30/100 >= v/(t*12):
    r = "pode ser aprovado!"
else:
    r = "reprovado."

print(f"para pagar a casa de R${v} em {t} anos a prestação será de {v/(t*12):.2f}")
print(f"Empréstimo {r}")