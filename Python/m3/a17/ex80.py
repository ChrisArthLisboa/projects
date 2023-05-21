
l = []

for c1 in range(0,5):
    n = int(input("Digite um valor: "))
    if c1 == 0:
        l.append(n)
    else:
        for c2 in range(len(l)-1,-1,-1):
            if n >= l[c2]:
                l.insert(c2+1,n)
                break
            else:
                l.insert(0,n)
                break

print(l)