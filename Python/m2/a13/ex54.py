from datetime import date

mel = []
mal = []

for c in range(0,7):
    a = int(input(f"Em que ano a {c+1}° pessoa nasceu: "))
    i = date.today().year - a
    if i < 18:
        mel.append(i)
    else:
        mal.append(i)

print(f"Ao todo tivemos {len(mal)} pessoas de maior idade.")
print(f"E {len(mel)} pessoas de menor idade.")