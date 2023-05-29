from math import inf

ma = 0
me = inf

for c in range(0,5):
    p = float(input(f"Peso da {c+1}° pessoa: "))
    if ma < p:
        ma = p
    if me > p:
        me = p

print(f"O maior peso lido foi de {ma:.1f}")
print(f"O menor peso lido foi de {me:.1f}")