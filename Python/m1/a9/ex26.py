
fr = str(input("Frase: ").strip().upper())
print(f"A letra 'A' aparece {fr.count('A')} na frase")
print(f"A 1° letra A apareceu na posição {fr.find('A')+1}")
print(f"A ultima letra 'A' apareceu na posição {fr.rfind('A')+1}")