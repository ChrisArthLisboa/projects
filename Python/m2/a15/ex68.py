from random import randint

cont = 0

print("=-"*10)
print("VAMOS JOGARPAR OU ÍMPAR")
print("=-"*10)

while True:
    r = randint(0,10)
    j = int(input("Diga um valor: "))
    o = str(input("Par ou Ímpar [P/I]: "))
    if (r+j)%2 == 1:
        e = "ÍMPAR"
    else:
        e = "PAR"
    
    print("--"*10)
    print(f"Você jogou {j} e o computador {r}. Total de {j+r} que é {e}")
    print("--"*10)

    if o == "P" and e == "PAR" or o == "I" and e == "ÍMPAR":
        print("Vitória do jogador. Vamos de novo.")
        print("--"*10)
        cont += 1
        continue
    else:
        print("Vitória do computador.")
        print(f"Game Over! Você venceu {cont} vezes!")
        break