import cv2
import pyautogui
import numpy
import pydirectinput
from mss import mss
import time

mon = {"top": 0, "left": 0, "width": 1920, "height": 1080}

def fishing_cast():
    for i in range(2):
        print(f'До каста рыбалки осталось {i}')
        time.sleep(1)

    pyautogui.mouseDown()
    time.sleep(0.4)
    pyautogui.mouseUp()

    time.sleep(1.5)

    paplowok_surveillance()

def paplowok_surveillance():
    while (True):
        src = mss()
        frame = numpy.array(src.grab(mon))

        frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        paplowok = cv2.imread('3dpaplowok.png', cv2.IMREAD_UNCHANGED)
        paplowok = cv2.cvtColor(paplowok, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(frame1, paplowok, cv2.TM_CCOEFF_NORMED)
        paplowok = cv2.cvtColor(paplowok, cv2.COLOR_GRAY2BGR)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        coincidence = 0.7

        if max_val >= coincidence:
            paplowok_weight = paplowok.shape[1]
            paplowok_height = paplowok.shape[0]

            top_left = max_loc
            bottom_right = (top_left[0] + paplowok_weight, top_left[1] + paplowok_height)

            cv2.rectangle(frame, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)
        else:
            pyautogui.leftClick()

            cv2.destroyAllWindows()

            time.sleep(0.15)
            fishing()

            break

        cv2.imshow('Result', frame)

        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break

def fishing():
    mouse_key_state = False
    cicle_number = 0
    print(cicle_number)

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
            if cicle_number == 0:
                cicle_number = 1

                if mouse_key_state == True:
                    pyautogui.mouseUp()

                    mouse_key_state = False
            else:
                if mouse_key_state == True:
                    pyautogui.mouseUp()

                    mouse_key_state = False

                print('Не нашёл мини игру')

                cv2.destroyAllWindows()

                break

    print('Цикл кончен!')

def main():
    while (True):
        fishing_cast()

main()
