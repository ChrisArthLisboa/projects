import pyautogui

while True:
    try:
        pyautogui.press("Ctrl""c",presses=2)
    except (KeyboardInterrupt):
        break