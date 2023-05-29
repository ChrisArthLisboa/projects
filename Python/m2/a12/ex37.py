ti = ['binário','octal','hexadecimal']
n = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão: \n[ 1 ] converter para Binário \n[ 2 ] converter para Octal \n[ 3 ] converter para Hexadecimal")
o = int(input("Sua opção: "))
if o == 1:
    ot = bin(n)
elif o == 2:
    ot = oct(n)
else:
    ot = hex(n)
print(f"{n} convertido para {ti[o-1]} é igual a {ot[2:]}")