
s = float(input("Qual é o sálario do funcionário? R$"))
if s >= 1250:
    p = 1/10
else:
    p = 15/100
print(f"Quem ganhava R${s:.2f} passa a ganhar {s + (s*p):.2f}")
