
l = []

for c1 in range(0,3):
    for c2 in range(0,3):
        v = int(input(f"Valor para {[c1,c2]}: "))
        l.append(v)

for c in range(0,9):
    if c == 2 or c == 5:
        print(f"[{l[c]:^5}]")
    else:
        print(f"[{l[c]:^5}]", end=" ")
    