import random

l = []

for c in range(1,5):
    a = str(input(f"{c}° Aluno: ").capitalize())
    l.append(a)

random.shuffle(l)

print(f"A ordem de apresentação será: \n {l}")