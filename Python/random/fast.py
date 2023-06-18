
from pyautogui import *
def copy(q):
    for c in range(0,q):
        hotkey("ctrl","a")
        hotkey("ctrl", "c")
        hotkey("Alt","Tab")
        press("Down")
        hotkey("ctrl","v")
        hotkey("Alt","Tab")

copy(30)