from pyautogui import press,sleep,write


print("| 1.Instalar pacote  | \n|2.Desinstalar pacote| \n| 3.Atualizar pip3 |")
faz = int(input("O que fazer: ").lower())
if faz == 1:
    lib = str(input("Biblioteca: ").lower())

    press('Win')
    sleep(0.5)
    write("cmd")
    sleep(0.5)
    press('Enter')
    sleep(2)
    write(f"python3 -m pip install {lib}")
    press('Enter')
elif faz == 2:
    lib = str(input("Biblioteca: ").lower())

    press('Win')
    sleep(0.5)
    write("cmd")
    sleep(0.5)
    press('Enter')
    sleep(3)
    write(f"pip3 uninstall {lib}")
    press('Enter')
else:
    press('Win')
    sleep(0.5)
    write("cmd")
    sleep(0.5)
    press('Enter')
    sleep(3)
    write("python.exe -m pip3 install --upgrade pip3")
    press('Enter')