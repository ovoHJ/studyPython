from repeater import repeat, once

s = input("반복할 문자를 입력하세요 : ")
n = input("반복 회수를 입력하세요 : ")
repeat(s, int(n))
repeat(s)
once(s)