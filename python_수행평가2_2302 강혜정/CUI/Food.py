# 2302 강혜정
# 이 프로젝트는 우리 집 냉장고에 어떤 재료와 음식이 있는지 확인하고, 장 볼 때 이미 사놓은 재료를 사는 것을 방지해주는 프로그램을 구현하는 것입니다.
# 또한 구매한 재료들을 추가할 수 있습니다.
# 실행 방법은 refri_control.py에서 실행시키면 됩니다.

# 이 파일은 음식의 기본 정보를 담고 있으며, Refri_Control.py 파일에서 상속할 파일입니다.

class Food_info:
    name = ""           # 식품 이름
    make_date = ""      # 제조일자
    end_date = ""       # 유통기한
    left_date = 0       # 남은날짜
    memo = ""           # 메모

    