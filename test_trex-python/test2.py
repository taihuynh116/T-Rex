# file nay xu ly cac file theo kieu hard code cac vi tri
import win32api
import pyautogui
import time
import numpy as np
import cv2

from mss import mss

#####
# SOME CONSTANTS
BLANK_BOX = 280000
BIRD_BOX = 50000
GAMEOVER_RANGE = [620000, 660000]
TIME_BETWEEN_FRAMES = 0.01
TIME_BETWEEN_GAMES = 1




class Cordinates(object):
    # vi tri cua cac object
    replay_pos = (960,387) # vi tri cua button replay
    # replay_pos = (520, 390)

def restart_game():
    pyautogui.click(Cordinates.replay_pos)

def press_up(v):
    pyautogui.keyDown("up") # press a key down
    time.sleep(0.02)
    v.i += 1
    print("jump",v.i)
    pyautogui.keyUp("up") # release a key

def press_down(v):
    pyautogui.keyDown("down") # press a key down
    time.sleep(1)
    v.i += 1
    print("down",v.i)
    pyautogui.keyUp("down") # release a key

def get_cactus_box_value():
    cactus_box = {'left': 800, 'top': 379, 
                  'width': 23, 'height': 54}
                  # x: 724 - 748, y: 388 - 434
    # cactus_box = {'left': 370, 'top': 400, 
    #               'width': 50, 'height': 20}
    sct = mss()
    img = np.array(sct.grab(cactus_box))[:,:,:3]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #print(gray.sum())
    return gray.sum()

def get_bird_box_value():
    cactus_box = {'left': 800, 'top': 388, 
                  'width': 24, 'height': 11}
                  # x: 724 - 748, y: 388 - 434
    # cactus_box = {'left': 370, 'top': 400, 
    #               'width': 50, 'height': 20}
    sct = mss()
    img = np.array(sct.grab(cactus_box))[:,:,:3]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(gray.sum())
    return gray.sum()

def check_gameover(gameover_range = GAMEOVER_RANGE):
    result = False
    gameover_box = {'left': 943, 'top': 372, 
                  'width': 34, 'height': 30}
                  # x: 943 - 977, y: 372 - 402
    # gameover_box = {'left': 430, 'top': 345, 
    #               'width': 200, 'height': 15}
    sct = mss()
    img = np.array(sct.grab(gameover_box))[:,:,:3]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    curr_state = gray.sum()
    #print(curr_state)
    #if curr_state < GAMEOVER_RANGE[1] and curr_state > GAMEOVER_RANGE[0]:
    if curr_state < 200000:
        result = True
    return result

state_mouseclick = win32api.GetKeyState(0x04)
v = type('', (), {})()
v.i = 0
u = type('', (), {})()
u.i = 0
while True:
    a = win32api.GetKeyState(0x04)
    if a != state_mouseclick:  # Button state changed
        state_mouseclick = a
        if a < 0:
            break
    gameover_state = check_gameover()
    if gameover_state:
        time.sleep(TIME_BETWEEN_GAMES)
        print("Game over. Restart game")
        break
        restart_game()
    
    cactus_state = get_cactus_box_value()
    if cactus_state < BLANK_BOX:
        press_up(v)
    else:
        bird_state = get_bird_box_value()
        if bird_state < BIRD_BOX:
            press_down(u)
    #time.sleep(TIME_BETWEEN_FRAMES)

print("Finish")