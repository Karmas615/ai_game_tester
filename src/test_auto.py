import pyautogui
import time

time.sleep(3)
print(pyautogui.size())
print(pyautogui.position())

#Mouse Functions
pyautogui.moveTo(100, 500,3) #moves the mouse to that x,y position in that amount of time
pyautogui.moveRel(100,100,3) #moves the mouse relative to those x,y positions in that amount of time

#Click Function
pyautogui.click(100,100,3, button = "left") #clicks at that x,y location in that amount of time and what click

#Scroll Function
pyautogui.scroll(500)

#mouse Up & Down Functions
pyautogui.mouseDown(500,500, button = "left") #holds the mouse down until you have a mouse up
pyautogui.moveTo(1000,500,3)
pyautogui.mouseUp()

#Keyboard Function
pyautogui.write("Hello")
pyautogui.press("enter")
pyautogui.press("space")

