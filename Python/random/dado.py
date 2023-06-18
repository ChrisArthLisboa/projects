from random import randint
from time import sleep


print()
print("\033[31m!!!Para parar aperte Ctrl+C!!!\033[37m")
Fudge = ["+","+",0,0,"-","-"]
try:
    while True:
        print("\033[33mSelecione o tipo de dado:")
        sleep(0.5)
        print("Tipos possíveis:")
        print("\033[34m(1)\033[33mComum - Dados normais de quantidade de lados definida pelo jogador.")
        print("\033[34m(2)\033[33mFudge - dados especificos do sistema 'Fate'.\033[37m")
        sleep(0.5)
        t = str(input("Tipo de dado: ").capitalize())
        print()
        s = 0
        while s == 0:
            s = 0
            if t == "Comum" or t == "1":
                ql = int(input("Quantos lados: "))
                qd = int(input("Quantos dados: "))
                for c in range(0,qd):
                    print(f"{c+1}. {randint(1,ql)}")
                s += 1
                print()
            elif t == "Fudge" or t == "2":
                print("\033[33mDados \033[36mFugde\033[33m são dados de 6 lados com marcações de ('-' '0' '+') onde 1 e 2 = '-' | 3 e 4 = '0' | 5 e 6 = '+'.\033[37m")
                sleep(0.2)
                for c in range(0,4):
                    print(f"{c+1}. {Fudge[randint(0,5)]}")
                s += 1
                print()
            else:
                t = str(input("Tente novamente: "))
except(KeyboardInterrupt): 
    print()
    print()
    print("-=-"*8)
    print("Finalizando programa")
    print("-=-"*8)
    sleep(1)