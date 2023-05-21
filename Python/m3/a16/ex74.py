from random import randint
from math import inf

ma = -inf
me = inf

ns = (randint(-15,15), randint(-15,15), randint(-15,15), randint(-15,15), randint(-15,15))

for c in ns:
    if c > ma:
        ma = c
    if c < me:
        me = c

print("Os números sorteados foram: ",end='')
for c in ns:
    print(f"{c}", end=' ')
print()
print(f"O maior valor sorteado foi {ma}")
print(f"O menor valor sorteado foi {me}")