
l = ['Milhar','Centena','Dezena','Unidade']

n = int(input("Informe um número: "))
n = str(n)
print("Analisando o número.")
print("-="*8)
print(f"{l[3]}: {n[len(n)-1]}")
print(f"{l[2]}: {n[len(n)-2]}")
print(f"{l[1]}: {n[len(n)-3]}")
print(f"{l[0]}: {n[len(n)-4]}")