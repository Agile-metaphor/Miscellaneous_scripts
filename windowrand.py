import pyautogui
import time
import random

pyautogui.FAILSAFE = False

while True:
    x = random.randint(-999, 999)
    y = random.randint(-999, 999)
    
    pyautogui.moveTo(x,y)