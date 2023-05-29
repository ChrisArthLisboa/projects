
cma = 0
ch = 0
cfmi = 0

while True:
    print("--"*10)
    print("CADASTRE UMA PESSOA".center(20))
    print("--"*10)
    i = int(input("Idade: "))
    s = str(input("Sexo [M/F]: ").upper())
    print("--"*10)
    if i > 18:
        cma+= 1
    if s == "M":
        ch +=1
    if s == "F" and i < 20:
        cfmi += 1
    r = str(input("Quer continuar [S/N]: ").upper())
    if r == "N":
        break

print(f"Total de pessoas com mais de 18 anos: {cma}.")
print(f"Ao todo temos {ch} homens cadastrados.")
print(f"E temos {cfmi} mulheres com menos de 20 anos.")