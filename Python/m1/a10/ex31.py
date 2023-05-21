
d = float(input("Qual a distância da sua viagem: "))

print(f"Você está prestes a começar uma viagem de {d}Km.")
if d <= 200:
    v = d*0.50
else:
    v = d*0.45
print(f"E o preço da sua passagem será de {v:.2f}")