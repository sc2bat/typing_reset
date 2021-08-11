import time
import pyautogui

w = pyautogui.getWindowsWithTitle("Typing")[0]
# print(w)
if w.isActive == False : 
    w.activate() 
# if w.isMaximized == False: 
#     w.maximize() 

time.sleep(3)

resetdir = r"C:\Users\Dero\Desktop\p\1234\reset_btn.png"
lesdir = r"C:\Users\Dero\Desktop\p\1234\lesson.png"

#####
img = pyautogui.locateOnScreen(r"C:\Users\Dero\Desktop\p\1234\JavaScript.png")
pyautogui.click(img, duration=1)
time.sleep(10)
reset = pyautogui.locateOnScreen(resetdir)
pyautogui.click(reset, duration=1)
time.sleep(10)
lesson = pyautogui.locateOnScreen(lesdir)
pyautogui.click(lesson, duration=1)
time.sleep(10)