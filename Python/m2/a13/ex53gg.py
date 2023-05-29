inverso = ""

fr = str(input("Digite uma frase: ").strip().upper())
fr = fr.split()
junto = "".join(fr)

for c in range(len(junto)-1,-1,-1):
    inverso += junto[c]
if inverso == junto:
    e = "É UM PALINDROMO"
else:
    e = "NÃO É UM PALINDROMO"
print(f"A palavra {junto} {e}.")