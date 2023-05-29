
o = 0
ma = 0

while o != 5:
    n1 = int(input("1° valor: "))
    n2 = int(input("2° valor: "))
    while True:
        print(" [ 1 ] Somar")
        print(" [ 2 ] Multiplicar")
        print(" [ 3 ] Maior")
        print(" [ 4 ] Novos números")
        print(" [ 5 ] Sair do programa")
        o = int(input("Sua opção: "))
        while o != 1 and o != 2 and o != 3 and o != 4 and o != 5:
            o = int(input("Valor invalido: "))
        print("-="*10)
        
        if o == 1:
            print(f"A soma entre {n1} e {n2} é igual a {n1+n2}")
        elif o == 2:
            print(f"A multiplicação de {n1} e {n2} é {n1*n2}")
        elif o == 3:
            if n1 > n2:
                ma = n1
            elif n2 > n1:
                ma = n2
            print(f"O maior número entre {n1} e {n2} é {ma}")
        elif o == 4:
            break
        elif o == 5:
            break