# Code to check if left or right mouse buttons were pressed
import win32api
import time
 
state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
state_middle = win32api.GetKeyState(0x04)  # Right button down = 0 or 1. Button up = -127 or -128

while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
    c = win32api.GetKeyState(0x04)

    if a != state_left:  # Button state changed
        state_left= a
        if a < 0:
            print('Left Button Pressed')
            x, y = win32api.GetCursorPos()
            print(x,y)
    if b != state_right:  # Button state changed
        state_right= b
        if b < 0:
            print('Right Button Pressed')
            x, y = win32api.GetCursorPos()
            print(x,y)
    if c != state_middle:  # Button state changed
        state_middle= c
        if c < 0:
            print('Middle Button Pressed')
            x, y = win32api.GetCursorPos()
            print(x,y)