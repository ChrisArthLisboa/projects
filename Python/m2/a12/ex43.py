
p = float(input("Qual sua massa corporal: "))
h = float(input("Qual sua altura: "))

imc = p/h**2

print(f"O IMC dessa pessoa é de {imc:.2f}.")
if imc < 18.5:
    e = "abixo do peso"
elif imc < 25:
    e = "peso ideal"
elif imc < 30:
    e = "sobrepeso"
elif imc < 40:
    e = "obesidade"
else:
    e = "obesidade mórbida"
print(f"Você está na faixa de peso {e}.")