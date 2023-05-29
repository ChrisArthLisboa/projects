
l = []
lp = []
li = []

for c in range(0,7):
    v = int(input(f"Digite o {c+1}° valor: "))
    l.append(v)
    if v%2 == 0:
        lp.append(v)
    else:
        li.append(v)

print("-="*14)
print(f"Os valores digitados foram {l}.")
print(f"Os valores pares digitados foram {lp}.")
print(f"Os valores ímpares digitados foram {li}.")