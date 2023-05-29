
no = str(input("Digite seu nome completo: "))
nol = no.split()
print(f"Muito prazer em te conhecer {nol[0].title()}.")
nol.reverse()
print(f"Seu último nome é {nol[0].title()}")
