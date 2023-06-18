
import speech_recognition as sr
from pyautogui import write, sleep, press

print("-="*20)
print("| select your language: PT-BR | EN-US |")
print("| selecione o seu idioma: PT-BR | EN-US |")
print("-="*20)
lang = str(input("idioma/language: ").lower())
while lang != "pt-br" and lang != "en-us":
    lang = str(input("Tente novamente/Try again: ").lower())
if lang == "pt-br":
    print("!.Aperte ctrl+c para parar.!")
if lang == "en-us":
    print("!.Press ctrl+c to stop.!")
sleep(5)
rec = sr.Recognizer()
with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    while True:
        try:
            print("Fala/say:")
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language=lang)
            write(f"{texto}.".capitalize())
            press("space")
            press("enter")
        except(sr.UnknownValueError):
            print("Voz não encontrada/Voice not found")
            sleep(2)
            print("Tente novamente/Try again")
            continue
        except(KeyboardInterrupt):
            print()
            print("pause")
            r = str(input("continuar?/start?[S/N]: ").capitalize())
            while r not in "SN":
                r = str(input("Tente novamente/Try again[S/N]: ").capitalize())
            if r == "S":
                continue
            else:
                break