from time import sleep
n = str(input("Digite seu nome: "))
print("-=-"*4)
sleep(1)
print("Analisando nome...")
sleep(1)
print("-=-"*4)

print(f"Seu nome em maiuscula é {n.upper()}")
print(f"Seu nome em minuscula é {n.lower()}")
print(f"Seu nome tem {len(n) - n.count(' ')} letras")
print(f"O seu primeiro nome é {n.split()[0]} tem {len(n.split()[0])}")