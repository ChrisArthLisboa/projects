
print("="*10, "Lojas Guanabara", "="*10)
v = float(input("Preço das compras: R$"))
print("Formas de pagamento")
print("[ 1 ] à vista/cheque")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
o = int(input("Opção: "))
if o == 4:
    p = int(input("Quantas parcelas: "))
    print(f"Sua compra será parcelada em {p}x de {(v*20/100 +v)/p:.2f} com juros")
    print(f"Sua compra de R${v:.2f} vai custar {v*20/100 +v:.2f} no final.")
elif o == 1:
    d = 1/10
    print(f"Sua compra de R${v:.2f} vai custar {v - v*d:.2f} no final.")
elif o == 2:
    d = 5/100
    print(f"Sua compra de R${v:.2f} vai custar {v - v*d:.2f} no final.")
else:
    print(f"O valor a ser pago será integral de {v:.2f}")