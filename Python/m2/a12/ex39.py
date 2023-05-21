from datetime import date
i = int(input("Ano de nascimento: "))
aa = date.today().year
print(f"Quem nasceu em {i} tem {aa-i} anos em {aa}")
if aa-i < 18:
    print(f"Ainda faltam {18-(aa-i)} anos para o alistamento")
    print(f"seu alistamento será em {i+18}")
elif aa-i == 18:
    print(f"Você deve se alistar Imediatamente!")
else:
    print(f"Você já deveria ter se alistado há {(aa-i)-18} anos.")
    print(f"Seu alistamento foi em {i+18}")
