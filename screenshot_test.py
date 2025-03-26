import pyautogui
from PIL import Image

# Take a screenshot
screenshot = pyautogui.screenshot()

# Save the screenshot
screenshot.save('screenshot.png')
print("Screenshot saved as 'screenshot.png'") 