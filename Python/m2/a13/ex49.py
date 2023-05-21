n = int(input("Digite o número a ser tabuado: "))
print("-"*8)
for c in range(1,11):
    print(f"{n} x {c:2} = {n*c}")
print("-"*8)