from datetime import date

cat = ""

a = int(input("Ano de nascimento: "))
i = date.today().year - a

if i <= 9:
    cat = "Mirim"
elif i <= 14:
    cat = "Infantil"
elif i <= 19:
    cat = "Junior"
elif i <= 25:
    cat = "Sênior"
elif i > 25:
    cat = "Master"

print(f"O Atleta tem {i} anos \nClassificação: {cat}")