print("Gerador de PA")
print("-="*8)

e = 0
q = 9
contg = 0
cont = 0
n1 = int(input("1° termo: "))
r = int(input("Razão: "))
while q != e:
    while cont <= q:
        print(n1+cont*r, end=' -> ')
        cont+=1
    print("Pausa")
    e = q
    q += int(input("Quantos mais termos quer ver: "))
print(f"Progressão finalizada. \nVocê mostrou {e+1} termos.")