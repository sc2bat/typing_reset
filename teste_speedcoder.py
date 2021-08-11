# https://www.speedcoder.net/lessons/
# 타자 연습 사이트 모든 항목 완료 후 reset 자동화

import time
import pyautogui

pyautogui.hotkey("win", "1") 

w = pyautogui.getWindowsWithTitle("Typing Practice")[0]
# print(w)
if w.isActive == False : 
    w.activate() 
if w.isMaximized == False: 
    w.maximize() 
    
# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)



pyautogui.sleep(1)

# C = pyautogui.locateOnScreen("C.png")
# pyautogui.click(C)
# ###############################
# # 리셋
# reset = pyautogui.locateOnScreen("reset_btn.png")
# pyautogui.click(reset)
# # 홈화면
# rtp = pyautogui.locateOnScreen("returnToP.png")
# pyautogui.click(rtp)
# ################################
# time.sleep(2)

C2 = pyautogui.locateOnScreen("C2.png")
pyautogui.click(C2)
###############################
# 리셋
reset = pyautogui.locateOnScreen("reset_btn.png")
pyautogui.click(reset)
# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)
################################
time.sleep(2)

C3 = pyautogui.locateOnScreen("C3.png")
pyautogui.click(C3)
###############################
# 리셋
reset = pyautogui.locateOnScreen("reset_btn.png")
pyautogui.click(reset)
# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)
################################
time.sleep(2)

CSS = pyautogui.locateOnScreen("CSS.png")
pyautogui.click(CSS)
###############################
# 리셋
reset = pyautogui.locateOnScreen("reset_btn.png")
pyautogui.click(reset)
# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)
################################
time.sleep(2)

Haskell = pyautogui.locateOnScreen("Haskell.png")
pyautogui.click(Haskell)
###############################
# 리셋
reset = pyautogui.locateOnScreen("reset_btn.png")
pyautogui.click(reset)
# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)
################################
time.sleep(2)
HTML = pyautogui.locateOnScreen("HTML.png")
pyautogui.click(HTML)
###############################
# 리셋
reset = pyautogui.locateOnScreen("reset_btn.png")
pyautogui.click(reset)
# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)
################################
time.sleep(2)

Java = pyautogui.locateOnScreen("Java.png")
pyautogui.click(Java)
###############################
# 리셋
reset = pyautogui.locateOnScreen("reset_btn.png")
pyautogui.click(reset)
# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)
################################
time.sleep(2)

JavaScript = pyautogui.locateOnScreen("JavaScript.png")
pyautogui.click(JavaScript)
###############################
# 리셋
reset = pyautogui.locateOnScreen("reset_btn.png")
pyautogui.click(reset)
# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)
################################
time.sleep(2)

Perl = pyautogui.locateOnScreen("Perl.png")
pyautogui.click(Perl)
###############################
# 리셋
reset = pyautogui.locateOnScreen("reset_btn.png")
pyautogui.click(reset)
# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)
################################
time.sleep(2)

PHP = pyautogui.locateOnScreen("PHP.png")
pyautogui.click(PHP)
###############################
# 리셋
reset = pyautogui.locateOnScreen("reset_btn.png")
pyautogui.click(reset)
# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)
################################
time.sleep(2)

Ruby = pyautogui.locateOnScreen("Ruby.png")
pyautogui.click(Ruby)
###############################
# 리셋
reset = pyautogui.locateOnScreen("reset_btn.png")
pyautogui.click(reset)
# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)
################################
time.sleep(2)

Python = pyautogui.locateOnScreen("Python.png")
pyautogui.click(Python)
###############################
# 리셋
reset = pyautogui.locateOnScreen("reset_btn.png")
pyautogui.click(reset)
# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)
################################
time.sleep(2)

# 홈화면
rtp = pyautogui.locateOnScreen("returnToP.png")
pyautogui.click(rtp)

time.sleep(3)

w.restore()
