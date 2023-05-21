import random

l = []

for c in range(1,5):
    a = str(input(f"{c}° Aluno: ").title())
    l.append(a)

print(f"O aluno escolhido foi {random.choice(l)}")