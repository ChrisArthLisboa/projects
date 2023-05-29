
s = 0
cont = 0

for c in range(0,501,3):
    if c%2 == 1:
        s += c
        cont += 1

print(f"A soma dos {cont} números foi de {s}.")