from datetime import date


ano = int(input("(coloque 0 para analisar hoje)Que ano quer analisar: "))
if ano == 0:
    ano = date.today().year
if ano%4 != 0:
    e = "não é bissexto"
else:
    e = "é bissexto"
print(f"O ano {ano} {e}")