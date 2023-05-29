
s = str(input("Informe seu sexo [M/F]: ").upper())
while s not in "MF" or s == "":
    s = str(input("Dado inválido. por favor digite M ou F: "))
print(f"Sexo {s} regstrado com sucesso!")
