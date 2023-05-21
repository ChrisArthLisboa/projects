
s = -999
n = 0
cont = -1

while n != 999:
    n = int(input("Digite um número [999 parada]: "))
    s += n
    cont += 1
print(f"Você digitou {cont} números e o seu somatório foi de {s}.")