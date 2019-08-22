# 2302 강혜정
# 이 프로젝트는 우리 집 냉장고에 어떤 재료와 음식이 있는지 확인하고, 장 볼 때 이미 사놓은 재료를 사는 것을 방지해주는 프로그램을 구현하는 것입니다.
# 또한 구매한 재료들을 추가할 수 있습니다.
# 실행 방법은 refri_control.py에서 실행시키면 됩니다.

# 이 파일은 프로그램 보여주고 선택할 수 있는 파일입니다.

import Refri_Control

class Menu:
    freezer = Refri_Control.Freezer_Food()
    refri = Refri_Control.Refrigerator_Food()

    # 어떤 기능을 수행할지 고르는 함수
    def choice(self):
        # 제대로 입력할 때까지 무한 반복
        while True:
            print("우리집 냉장고에는?")
            print("  1. 냉장고 확인")
            print("  2. 식품 추가")
            print("  3. 프로그램 종료")
            e = input("  [입력]  ")
            print("")
            if e == '1':
                # 제대로 입력할 때까지 무한 반복
                while True:
                    print("어느 곳을 확인하시겠습니까?")
                    print("  1. 냉동실")
                    print("  2. 냉장실")
                    print("  3. 뒤로가기")
                    ee = input("  [입력]  ")
                    print("")

                    if ee == '1':
                        self.freezer.show()
                        break
                    elif ee == '2':
                        self.refri.show()
                        break
                    elif ee == '3':
                        break
                    else:
                        print("  [WARNING] 다시 입력하십시오.\n")
            elif e == '2':
                while True:
                    print("어느 곳에 추가하시겠습니까?")
                    print("  1. 냉동실")
                    print("  2. 냉장실")
                    print("  3. 뒤로가기")
                    ee = input("  [입력]  ")
                    print("")
                    
                    if ee == '1':
                        self.freezer.add()
                        break
                    elif ee == '2':
                        self.refri.add()
                        break
                    elif ee == '3':
                        break
                    else:
                        print("  [WARNING] 다시 입력하십시오.\n")
            elif e == '3':
                break
            # 그 외 버튼을 누르면 경고문장이 뜨며 다시 입력
            else:
                print("[WARNING] 다시 입력하십시오.\n")
        print("[SYSTEM] 프로그램을 종료했습니다")