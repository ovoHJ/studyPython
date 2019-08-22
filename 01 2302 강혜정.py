# 학번
# END

schoolNumber = input("학번 입력 : ")
grade = int(schoolNumber[0])
ban  = int(schoolNumber[1])
classNumber = int(schoolNumber[2:])

majors = [
    ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"],
    ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"],
    ["인터랙티브미디어과", "뉴미디어디자인과", "뉴미디어솔루션과"]
]

major = majors[grade-1][(ban-1)//2]

print(str(grade) + "학년", major, str(ban) + "반", str(classNumber) + "번입니다.")