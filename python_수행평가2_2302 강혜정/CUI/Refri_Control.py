# 2302 강혜정
# 이 프로젝트는 우리 집 냉장고에 어떤 재료와 음식이 있는지 확인하고, 장 볼 때 이미 사놓은 재료를 사는 것을 방지해주는 프로그램을 구현하는 것입니다.
# 또한 구매한 재료들을 추가할 수 있습니다.
# 실행 방법은 refri_control.py에서 실행시키면 됩니다.

# 이 파일은 재료추가, 냉장고 확인 등 프로그램의 주요기능이 모여있는 파일입니다.

import Food
from datetime import date

class Refrigerator_Food():
    refri_info = Food.Food_info()
    refri_food = []

    def show(self):
        #refri_food가 null이라면 파일에 문자열 읽기
        if not self.refri_food:
            with open('CUI/txt/Refri.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    #'\t'으로 구분해서 넣기
                    a = lines[i].split('\t')
                    self.refri_food.append(a)
    
        # 만약 refri_food가 null이라면?
        if not self.refri_food:
            print("[SYSTEM] 냉장실 안이 텅텅 비었습니다\n")
        else:
            print("──────────────────────────────────────────\n")
            print("[FOOD] 냉장실 확인 ")
            for i in self.refri_food:
                print("식품명  :  " + i[0])
                print("유통기한  :  " + i[1])
                print("제조일자  :  " + i[2])
                print("유통기한까지 남은 날짜  :  " + str(i[3]) + "일")
                print("메모  :  " + i[4])
                print("")
            print("──────────────────────────────────────────")

    def add(self):
        # 음식정보 입력
        while True:
            print("냉장실에 넣을 음식 정보를 입력해주십시오")
            self.refri_info.name = input("  이름 : ")
            self.refri_info.make_date = input("  제조일자(YYYY.MM.DD) : ")        # 내가 원하는 것 : 지정된 포맷대로 하지 않으면 다시 입력할 수 있게
            self.refri_info.end_date = input("  유통기한(YYYY.MM.DD) : ")
            self.refri_info.memo = input("  메모 : ")
            print("")

            # 유통기한 남은 날짜 계산
            # 제조일자와 유통기한 쪼개기
            m1, m2, m3 = self.refri_info.make_date.split('.')
            e1, e2, e3 = self.refri_info.end_date.split('.')
            # 제조일자와 유통기한을 date() 함수로 바꾸기
            make = date(int(m1), int(m2), int(m3))
            end = date(int(e1), int(e2), int(e3))
            # 며칠 남았는지 day를 이용해 저장
            self.refri_info.left_date = str((end-make).days)

            # 리스트 안에 넣기
            self.refri_food.append([self.refri_info.name, self.refri_info.end_date, self.refri_info.make_date, self.refri_info.left_date, self.refri_info.memo])

            #파일에 문자열 쓰기
            with open('CUI/txt/Refri.txt', 'a', encoding='utf-8') as file:
                file.writelines('\t'.join([self.refri_info.name, self.refri_info.end_date, self.refri_info.make_date, self.refri_info.left_date, self.refri_info.memo]))
                file.write('\n')
                file.close()

            # 추가로 입력할 것인지 질문->선택
            while True:
                print("추가로 입력하시겠습니까?")
                print("  1. 추가 작성")
                print("  2. 그만 작성")
                i = input("  [입력]  ")
                print("") 
                if i == '1':
                    break  
                elif i == '2':
                    break
                else:
                    print("  [WARNING] 다시 입력하십시오.\n")
            if i == '2':
                break

class Freezer_Food:
    freezer_info = Food.Food_info()
    freezer_food = []

    def show(self):
        #refri_food가 null이라면 파일에 문자열 읽기
        if not self.freezer_food:
            with open('CUI/txt/Freezer.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    a = lines[i].split('\t')
                    self.freezer_food.append(a)

        # 만약 refri_food가 null이라면?
        if not self.freezer_food:
            print("[SYSTEM] 냉장실 안이 텅텅 비었습니다\n") 
        else:
            print("──────────────────────────────────────────\n")
            print("[FOOD] 냉동실 확인 ")
            for i in self.freezer_food:
                print("식품명  :  " + i[0])
                print("유통기한  :  " + i[1])
                print("제조일자  :  " + i[2])
                print("유통기한까지 남은 날짜  :  " + str(i[3]) + "일")
                print("메모  :  " + i[4])
                print("")
            print("──────────────────────────────────────────")

    def add(self):
        # 음식정보 입력
        while True:
            print("냉동실에 넣을 음식 정보를 입력해주십시오")
            self.freezer_info.name = input("  이름 : ")
            self.freezer_info.make_date = input("  제조일자(YYYY.MM.DD) : ")        # 내가 원하는 것 : 지정된 포맷대로 하지 않으면 다시 입력할 수 있게
            self.freezer_info.end_date = input("  유통기한(YYYY.MM.DD) : ")
            self.freezer_info.memo = input("  메모 : ")
            print("")

            # 유통기한 남은 날짜 계산
            # 제조일자와 유통기한 쪼개기
            m1, m2, m3 = self.freezer_info.make_date.split('.')
            e1, e2, e3 = self.freezer_info.end_date.split('.')
            # 제조일자와 유통기한을 date() 함수로 바꾸기
            make = date(int(m1), int(m2), int(m3))
            end = date(int(e1), int(e2), int(e3))
            # 며칠 남았는지 day를 이용해 저장
            self.freezer_info.left_date = str((end-make).days)

            # 리스트 안에 넣기
            self.freezer_food.append([self.freezer_info.name, self.freezer_info.end_date, self.freezer_info.make_date, self.freezer_info.left_date, self.freezer_info.memo])

            #파일에 문자열 쓰기
            with open('CUI/txt/Freezer.txt', 'a', encoding='utf-8') as file:
                file.writelines('\t'.join([self.freezer_info.name, self.freezer_info.end_date, self.freezer_info.make_date, self.freezer_info.left_date, self.freezer_info.memo]))
                file.write('\n')
                file.close()

            # 추가로 입력할 것인지 질문->선택
            while True:
                print("추가로 입력하시겠습니까?")
                print("  1. 추가 작성")
                print("  2. 그만 작성")
                i = input("  [입력]  ")
                print("") 
                if i == '1':
                    break  
                elif i == '2':
                    break
                else:
                    print("  [WARNING] 다시 입력하십시오.\n")
            if i == '2':
                break