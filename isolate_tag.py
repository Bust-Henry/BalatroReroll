import pyautogui
from PIL import Image
import time

# Load the screenshot
screenshot = Image.open('screenshot.png')

try:
    # Find the investment tag location
    location = pyautogui.locateOnScreen('investmentTag.png', confidence=0.85)
    
    if location:
        # Crop the screenshot to just the investment tag region
        # Add some padding around the found location
        left = location.left - 10
        top = location.top - 10
        right = location.left + location.width + 10
        bottom = location.top + location.height + 10
        
        # Ensure we don't go outside the image boundaries
        left = max(0, left)
        top = max(0, top)
        right = min(screenshot.width, right)
        bottom = min(screenshot.height, bottom)
        
        # Crop and save the isolated region
        cropped = screenshot.crop((left, top, right, bottom))
        cropped.save('isolated_tag.png')
        print("Investment tag isolated and saved as 'isolated_tag.png'")
    else:
        print("Investment tag not found in the screenshot")
except Exception as e:
    print(f"Error: {e}") 