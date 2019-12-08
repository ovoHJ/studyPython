import pyautogui as pag
import time

if __name__ == '__main__':
    pag.moveTo(400, 400, 2)
    pag.click()
    pag.typewrite("HAPPY BIRTHDAY TO SEUNGYEON", interval=0.5)
    pag.press("hangul")
    pag.typewrite("skaruddk toddlf cnrgkgo")