

while True:
    print("---"*8)
    n = int(input("Número a ser tabuado: "))
    print("---"*8)
    if n < 0:
        break
    for c in range(1,11):
        print(f"{n} x {c} = {n*c}")
print("Programa de tabuada encerrado. Volte sempre!")