
print("=="*16)
print("10 TERMOS DE UMA PA".center(32))
print("=="*16)


t1 = int(input("Primeiro termo: "))
ra = int(input("Razão: "))

print(t1, end=' -> ')
for c in range(1,10):
    print(t1+c*ra, end=' -> ')
    
print("Acabou")