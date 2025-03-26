import pyautogui
import keyboard
import time
from pyautogui import ImageNotFoundException

# Give some time to switch to the game window
time.sleep(3)

while True:
    try:
        pyautogui.locateOnScreen('looksLikeThis.png', confidence=0.85)
        break
    except ImageNotFoundException as e:
        try:
            pyautogui.locateOnScreen('investmentTag.png', confidence=0.85)
            break
        except ImageNotFoundException as e:
            # Using keyboard library for more reliable input
            keyboard.press('r')
            time.sleep(2)
            keyboard.release('r')
            time.sleep(2)

print("Image found!") 