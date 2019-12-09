import pyautogui as pag
import time

if __name__ == '__main__':
    # 메모장


    pag.moveTo(150, 1065, 1);
    pag.click()
    pag.press("hangul")
    pag.typewrite("apahwkd")
    pag.press("hangul")
    pag.press("\n")
    pag.sleep(1)
    # hello world 치자
    pag.typewrite("Hello World!!")
    #  두번 내리자
    pag.press("enter")
    pag.press("enter")
    # 반갑구나 세상아 치자
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk!!")
    pag.press("hangul")
    # 저장하자
    pag.hotkey("ctrl", "s")
    # 파이썬월드
    pag.typewrite("C:\\Users\\s2018\\Downloads\\")
    pag.press("hangul")
    pag.typewrite("vkdlTjsdnjfem")
    pag.press("hangul")
    pag.sleep(1)
    pag.press("\n")