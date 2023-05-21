matriz = [ [0,0,0], [0,0,0], [0,0,0] ]
sp = 0
s3 = 0
s2 = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Valor para [{l,c}]: "))

print("-="*14)

for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c]%2 == 0:
            sp += matriz[l][c]
        if c == 2:
            s3 += matriz[l][c]
        if l == 1:
            s2 += matriz[l][c]
        print(f"[{matriz[l][c]:^5}] ",end="")
    print()
print("-="*14)
print(f"A soma dos valores pares é {sp}.")
print(f"A soma dos valores da 3° coluna é {s3}.")
print(f"A soma dos valores da 2° linha é {s2}")