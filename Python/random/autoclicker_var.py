import pyautogui as pg
V = float(input("tempo entre clicks: "))
pg.sleep(3)
while True:
    try:
        pg.sleep(V)
        pg.click(776,724)
        continue
    except (KeyboardInterrupt):
        print("Finalizando")
        pg.sleep(1)
        break