
n1 = float(input("1° nota: "))
n2 = float(input("2° nota: "))
m = (n1+n2)/2
print(f"Tirando {n1} e {n2}, a média é {m}")
if m >= 7:
    r = "foi aprovado."
elif m < 5:
    r = "foi reprovado."
else:
    r = "pegou recuperação."
print(f"O aluno {r}")