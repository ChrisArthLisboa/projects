from time import sleep
from random import randint

l = []
c2 = 0

print("--"*10)
print("Jogo na Mega Sena".center(20))
print("--"*10)

q = int(input("Quantos jogos você quer sortear: "))

print("-="*5, f"  Sorteando {q} Jogos  ", "-="*5)
for c in range(0,q):
    print(f"Jogo {c+1}: ",end="")
    while c2 < 6:
        rn = randint(1,60)
        if rn not in l:
            l.append(rn)
            c2 += 1
    print(l)
    l.clear()
    c2 = 0
    sleep(1)