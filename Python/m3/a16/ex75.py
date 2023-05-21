
qp = 0
tp = ()



n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))

t = (n1, n2, n3, n4)
q9 = t.count(9)
p3 = t.index(3)

print(f"Você digitou os valores {t}")
print(f"O valor 9 apareceu {q9} vezes")
print(f"O valor 3 apareceu na {p3+1}° posição")
print(f"Os valores pares digitados foram ", end='')
for c in t:
    if c%2 == 0:
        print(c, end=" ")