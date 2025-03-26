import cv2
import numpy as np
import pyautogui
import keyboard
import time

# Give some time to switch to the game window
time.sleep(3)

def find_image(template_path, threshold=0.85):
    # Take screenshot
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Convert screenshot to grayscale
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    
    # Load template and convert to grayscale
    template = cv2.imread(template_path)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    
    # Get template dimensions
    h, w = template_gray.shape[:2]
    
    # Perform template matching with grayscale images
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Check if match is above threshold
    if max_val >= threshold:
        return True
    return False

while True:
    try:
        if find_image('looksLikeThis.png'):
            break
        elif find_image('investmentTag.png'):
            break
        else:
            # Using keyboard library for more reliable input
            keyboard.press('r')
            time.sleep(2)
            keyboard.release('r')
            time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)

print("Image found!") 