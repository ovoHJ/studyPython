from datetime import datetime

print("현재 날짜 시각 객체 얻기")
today = datetime.now()
print("today = datetime.now() :", today)
print("연, 월, 일 :", today.year, today.month, today.day);
print("시, 분, 초 :", today.hour, today.minute, today.second)
print("요일 : ", today.weekday())
print("특정 날짜 시각 객체 만들기")
day = datetime(2018, 1, 1, 0, 0, 0)
print("day = datetime(2018, 1, 1, 0, 0, 0) :", day)
print("2018년부터 지나온 시간 구하기")
print("today - day :", today - day)
print()
print("문제1. 내가 태어난 날은 무슨 요일??")
my = datetime(2002, 5, 4, 0, 0, 0)
print("내가 태어난 요일은", "월화수목금토일"[my.weekday()] , "요일입니다.")
print()
print("문제2. 나는 며칠 살았을까?")
life = today - my
print("나는", life, "일 살았습니다.")
print()
print("문제3. 올해 크리스마스 며칠 남았을까?")
xmas = datetime(2019, 12, 25, 0, 0, 0) - datetime.now()
print("올해 크리스마스까지", xmas, "일 남았습니다.")