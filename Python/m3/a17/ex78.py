from math import inf

l = []

me = inf
ma = -inf

for c in range(0,5):
    n = int(input(f"Digite um valor para a posição {c}: "))
    l.append(n)
    if ma <= n:
        ma = n

    if me >= n:
        me = n

print("-="*14)

print(f"Você digitou os valores: {l}")
print(f"O maior valor digitado foi {ma} nas posições ", end='')
for c in range(0,5):
    if l[c] == ma:
        print(f"{c}... ",end='')
print()
print(f"O menor valor digitado foi {me} nas posições ", end='')
for c in range(0,5):
    if l[c] == me:
        print(f"{c}... ",end='')
print()