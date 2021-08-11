import time
import pyautogui
# pyautogui.mouseInfo()

pyautogui.hotkey("win", "1") 
time.sleep(2)

pyautogui.write("https://www.speedcoder.net/lessons/")
time.sleep(1)
pyautogui.press("ENTER")

time.sleep(2)
w = pyautogui.getWindowsWithTitle("Typing")[0]
if w.isActive == False : 
    w.activate() 
# if w.isMaximized == False: 
#     w.maximize() 

# cx = 326
# cy = 479
# time.sleep(2)
# pyautogui.click(cx, cy, duration=0.5)
# time.sleep(5)
# pyautogui.click(414, 241, duration=1)
# pyautogui.click(576, 130, duration=0.5)

color = (81,142,194)
s = pyautogui.screenshot()
for x in range(s.width):
    for y in range(s.height):
        if s.getpixel((x, y)) == color:
            pyautogui.click(x, y)

# lessons point 576,130 143,191,222 #8FBFDE
# C 326,479 244,245,232 #F4F5E8
# reset 414,241 38,90,136 #265A88

# w.restore()

