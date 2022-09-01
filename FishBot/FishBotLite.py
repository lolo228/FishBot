import cv2
import pyautogui
import numpy
import pydirectinput
from mss import mss
import time


mouse_key_state = False
mon = {"top": 0, "left": 0, "width": 1920, "height": 1080}

while (True):
    src = mss()
    frame = numpy.array(src.grab(mon))

    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    paplowok = cv2.imread('paplowok.png', cv2.IMREAD_UNCHANGED)
    paplowok = cv2.cvtColor(paplowok, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(frame1, paplowok, cv2.TM_CCOEFF_NORMED)
    paplowok = cv2.cvtColor(paplowok, cv2.COLOR_GRAY2BGR)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    coincidence = 0.65

    if max_val >= coincidence:
        paplowok_weight = paplowok.shape[1]
        paplowok_height = paplowok.shape[0]

        top_left = max_loc
        bottom_right = (top_left[0] + paplowok_weight, top_left[1] + paplowok_height)

        cv2.rectangle(frame, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)

        if max_loc[0] <= 965:
            pyautogui.mouseDown()

            mouse_key_state = True
        else:
            pyautogui.mouseUp()

            mouse_key_state = False
    else:
        if mouse_key_state == True:
            pyautogui.mouseUp()

            mouse_key_state = False
        else:
            if mouse_key_state == True:
                pyautogui.mouseUp()

                mouse_key_state = False
