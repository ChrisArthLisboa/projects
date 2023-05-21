
fr = str(input("Digite uma frase: ").replace(" ","").upper())
rfr = fr[len(fr)-1:0:-1] + fr[0]
print(f"O inverso de {fr} é {rfr}")
if fr == rfr:
    e = "é palíndromo"
else:
    e = "não é palíndromo"

print(f"A frase digitada {e}.")