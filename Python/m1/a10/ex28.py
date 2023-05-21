from time import sleep
from random import randint
nb = randint(0,5)
print("-=-"*12)
print("Vou pensar em um número entre 0 e 5. tente adivinhar.")
print("-=-"*12)
nj = int(input("Em que número eu pensei: "))
sleep(1)
print("Processando...")
if nb == nj:
    print("Parabens, você venceu!")
else:
    print(f"Ganhei! Eu pensei no número {nb} e não em {nj}")