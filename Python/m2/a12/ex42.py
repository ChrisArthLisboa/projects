
l = []

for c in range(0,3):
    s = float(input(f"{c+1}° segmento: "))
    l.append(s)
if l[0] + l[1] > l[2] and l[1] + l[2] > l[0] and l[0] + l[2] > l[1]:
    if l[0] == l[1] and l[1] == l[2]:
        ti = "equilatero"
    elif l[0] == l[1] or l[2] == l[1] or l[0] == l[2]:
        ti = "isósceles"
    else:
        ti = "escaleno"
    print(f"Os segmentos acima podem formar um triângulo {ti}.")
else:
    print("Os segmentos acima não podem formar um triângulo!")