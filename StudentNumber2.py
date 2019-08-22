#학번 입력 받아 학과 출력하기

majors = [
    ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"],
    ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"],
    ["인터랙티브미디어과", "뉴미디어디자인과", "뉴미디어솔루션과"]
]
#start
student_number = input("학번을 입력하세요 : ")

grade = student_number[0]
grade = int(grade)
classroom = student_number[1]
classroom = int(classroom)
print(majors[grade-1][(classroom-1)//2])
#end