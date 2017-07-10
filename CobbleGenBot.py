import pyautogui #imports the module 'pyautogui'
import time #imports the module 'time'

pyautogui.FAILSAFE = True #enables a failsafe that pyautogui comes with.
#move the mouse to the top left corner of the screen. doesnt always work

time.sleep(10) #sleeps (waits) for ten seconds

pyautogui.mouseDown() #sets the left click of the mouse to the down state

waitpickswitch = 0 #sets the variable for time between pickaxe switches

while True: #makes an infinite loop
    waitpickswitch = 0 #sets waitpickswitch back to 0 so picks
#can switch more than once
    while waitpickswitch < 2: #switches pick about once per second
        time.sleep(1) #pauses code for a second
        waitpickswitch += 1 #adds one to the waitpickswitch variable
    pyautogui.scroll(-1) #scrolls the mouse wheel, switching the pickaxe
    
