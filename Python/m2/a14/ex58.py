from random import randint

comp = randint(0,10)
p = -1
dica = ""
cont = 0

print("Sou seu computador... \nAcabei de pensar em um número de 0 a 10. \nSerá que você consegue adivinhar qual foi?")
while p != comp:
    p = int(input("Seu palpite: "))
    cont += 1
    if p == comp:
        break
    elif p < comp:
        dica = "Mais..."
    elif p > comp:
        dica = "Menos..."
    print(f"{dica} Tente mais uma vez.")

print(f"Acertou com {cont} tentativas. Parabéns")