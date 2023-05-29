
l = []
s = 0

for c in range(0,6):
    n = int(input(f"Digite o {c+1}° número: "))
    if n%2 == 0:
        s += n
        l.append(n)

print(f"Os {len(l)} números paraes digitados foram: {str(l)[1:-1]} e a soma desses valores é {s}.")
