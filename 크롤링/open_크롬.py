import pyautogui as pag
import time

if __name__ == '__main__' :
    # 크롬 이미지 인식하자
    data1 = pag.locateOnScreen("크롬아이콘.png");
    print(data1)
    center1 = (data1.left + (data1.width/2), data1.top + (data1.height/2))
    print(center1)
    data2 = pag.locateCenterOnScreen("크롬아이콘.png");
    print(data2)
    center2 = pag.center(data1)
    print(center2)

    '''
    datas = pag.locateAllOnScreen("크롬아이콘.png")
    for data in datas:
        print(data)
        center = pag.center(data)
        pag.moveTo(center, duration=1)
    '''