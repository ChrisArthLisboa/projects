e = str(input("Expressão: "))
l = []
for s in e:
    if s == "(":
        l.append('(')
    elif s == ")":
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) == 0:
    print("Essa expressão é possível.")
else:
    print("Essa expressão não é possível.")