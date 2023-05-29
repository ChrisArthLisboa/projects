
tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas',22.3, 'Livro', 34.9)

for c in range(0,len(tupla),2):
    print(f"{tupla[c]:-<30}",end=' ')
    print(f"R$ {tupla[c+1]:>7.2f}")

