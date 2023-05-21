
l = []
s = 0

print("-="*18)
print("Analisador de triângulos")
print("-="*18)

for c in range(0,3):
    s = float(input(f"{c+1}° segmento: "))
    l.append(s)
if l[0] + l[1] > l[2] and l[1] + l[2] > l[0] and l[0] + l[2] > l[1]:
    r = "podem formar"
else:
    r = "não podem formar"
print(f"Os segmentos acima {r} um triângulo!")