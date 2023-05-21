
lm = []
ln = []
v = []

while True:
    n = str(input("Nome: ").capitalize())
    v1 = float(input("Nota 1: "))
    v2 = float(input("Nota 2: "))
    vs = [v1,v2]
    v.append(vs)
    ln.append(n)
    lm.append((v1+v2)/2)
    r = str(input("Quer continuar [S/N]: ").upper())
    if r == "N":
        break
print("-="*20)
print("No. ", "  NOME          ", "MÉDIA")
print("--"*15)
for c in range(0,len(ln)):
    print(f"{c:^3} {ln[c]:^14} {lm[c]:.1f}")
print("--"*15)
while True:
    a = int(input("Notas de qual aluno [999 para]: "))
    if a == 999:
        break
    if a > len(ln)-1:
        a = int(input("Tente novamente [999 para]: "))
    print(f"Notas de {ln[a]} são {v[a]}.")
    