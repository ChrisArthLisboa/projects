
import datetime
from pyautogui import alert, sleep

m = int(input("Quantos minutos de trabalho/estudo: "))
et = m*60

d = int(input("Quantos minutos de descanso: "))
dt = d*60
try:
    while (True):
        alert("Trabalho/estudo")
        print("Trabalho/estudo")
        print(datetime.datetime.now().strftime("%H:%M:%S"))


        c=0
        for c in range(0,et):
            sleep(1)
            c += 1
            tr = (et-c)/60
            if tr == 5:
                print(f"Faltam {tr} minutos")
            if tr == 10:
                print(f"Faltam {tr} minutos")
        alert("Descanso")
        print("Descanso")
        print(datetime.datetime.now().strftime("%H:%M:%S"))
        c=0
        for c in range(0,dt):
            sleep(1)
            c += 1
            dr = (dt-c)/60
            if tr == 5:
                print(f"Faltam {dr} minutos")
            if tr == 10:
                print(f"Faltam {dr} minutos")
except(KeyboardInterrupt): 
    print("Parando programa")
    sleep(1)
