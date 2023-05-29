from math import inf
l = []

ma = 0
me = inf

for c in range(0,3):
    n = int(input(f"{c+1}° valor: "))
    l.append(n)
    if ma < n:
        ma = n
    if me > n:
        me = n

print(f"O menor valor foi {me}")
print(f"O menor valor foi {ma}")