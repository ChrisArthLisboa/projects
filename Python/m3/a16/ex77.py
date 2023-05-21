
tp = ('aprender', 'programar', 'linguagem', 'python',
             'curso', 'gratis', 'estudar', 'praticar',
             'trabalhar', 'mercado', 'programador', "futuro")

tv = ('a','e','i','o','u')

for c1 in tp:
    print(f"Na palavra {c1.upper()} temos ",end='')
    for c2 in tv:
        if c2 in c1:
            print(f"{c2} "*c1.count(c2), end='')
    print()