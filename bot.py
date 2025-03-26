import pyautogui
import pydirectinput
import time
from pyautogui import ImageNotFoundException

time.sleep(2)

while True:
    try:
        pyautogui.locateOnScreen('looksLikeThis.png', confidence=0.85)
        break
    except ImageNotFoundException as e:
        try:
            pyautogui.locateOnScreen('investmentTag.png', confidence=0.85)
            break
        except ImageNotFoundException as e:
            pydirectinput.keyDown('r')
            pyautogui.keyDown('r')
            time.sleep(2)
            pydirectinput.keyUp('r')
            pyautogui.keyUp('r')
            time.sleep(2)

print("investment tag found!")