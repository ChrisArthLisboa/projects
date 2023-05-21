from math import trunc

print("=="*16)
print("Banco CEV".center(32))
print("=="*16)

v = int(input("Qal o valor a ser sacado: "))

if v >= 50:
    ced50 = v/50
    print(f"Total de {trunc(ced50)} cedulas de R$50")
if v%50 >= 20:
    ced20 = (v%50)/20
    print(f"Total de {trunc(ced20)} cedulas de R$20")
if (v%50)%20 >= 10:
    ced10 = ((v%50)%20)/10
    print(f"Total de {trunc(ced10)} cedulas de R$10")
if ((v%50)%20)%10 > 0:
    ced1 = ((v%50)%20)%10
    print(f"Total de {trunc(ced1)} cedulas de R$1")

print("=="*16)
