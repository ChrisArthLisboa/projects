from math import inf

ma = -inf
me = inf
l = []
nma = []
nme = []

while True:
    n = str(input("Nome: ").capitalize())
    p = float(input("Peso: "))
    l.append(n)
    l.append(p)
    r = str(input("Quer continuar: ").upper())
    if r == "N":
        break

for c in range(0,len(l),2):
    if l[c+1] > ma:
        ma = l[c+1]
        if len(nma) > 0:
            nma.clear()
        nma.append(l[c])
    elif l[c+1] == ma:
        nma.append(l[c])
    if l[c+1] < me:
        me = l[c+1]
        if len(nme) > 0:
            nme.clear()
        nme.append(l[c])
    elif l[c+1] == me:
        nme.append(l[c])

print(f"Você cadastrou {len(l)/2} pessoas.")
print(f"O maior peso foi de {ma:.1f} Kg. Peso de {nma}.")
print(f"O menor peso foi de {me:.1f} Kg. Peso de {nme}.")

