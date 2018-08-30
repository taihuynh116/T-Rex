import numpy as np
import cv2
from mss import mss

def get_cactus_box_value():
    cactus_box = {'left': 761, 'top': 379, 
                  'width': 23, 'height': 69}
                  # x: 724 - 748, y: 388 - 434
    # cactus_box = {'left': 370, 'top': 400, 
    #               'width': 50, 'height': 20}
    sct = mss()
    img = np.array(sct.grab(cactus_box))[:,:,:3]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(gray.sum())
    return gray.sum()

get_cactus_box_value()