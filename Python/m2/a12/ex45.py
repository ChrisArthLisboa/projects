from random import randint
from time import sleep

l = ['Pedra', 'Papel', 'Tesoura']
r = randint(0,2)

print("Suas opções:")
print(f"[ 1 ] {l[0]}")
print(f"[ 2 ] {l[1]}")
print(f"[ 3 ] {l[2]}")
j = int(input("Sua jogada: "))

j = j-1

if j == r:
    e = "Houve empate"
if j == 0 and r == 2 or j == 1 and r == 0 or j == 2 and r == 1:
    e = "O jogador venceu."
else:
    e = "O computador venceu!"

print("")
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO")
sleep(0.5)

print("")
print("-="*10)
print(f"O computador jogou {l[r]}.")
print(f"O jogador jogou {l[j]}.")
print("-="*10)

print("")
print(f"{e}")
print("")