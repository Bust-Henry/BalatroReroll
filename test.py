import pyautogui
from pyautogui import ImageNotFoundException
while True:
    try:
        pyautogui.locateOnScreen('looksLikeThis.png', confidence=0.99)
        break
    except ImageNotFoundException as e:
        try:
            pyautogui.locateOnScreen('investmentTag.png', confidence=0.99)
            break
        except ImageNotFoundException as e:
            pass

print("image found")