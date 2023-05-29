
cont = 0

n = int(input("Digite um número: "))
for c in range(1,n+1):
    if n%c == 0:
        print(f"\033[0;33m{c}\033[0;37m", end=' ')
        cont += 1
    else:
        print(f"\033[0;31m{c}\033[0;37m", end=' ')

if cont == 2:
    t = "\033[32mÉ PRIMO\033[37m"
else:
    t = "\033[31mNÃO É PRIMO\033[37m"

print("")
print(f"O número {n} foi divisivel {cont} vezes")
print(f"E por isso ele {t}.")
