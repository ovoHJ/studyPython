# 자리배치
# END
import random

x = 0
exceptNumber = 0
listA = []
listB = []

lastNumber = int(input("끝번호를 입력하세요 : "))

for i in range(1, lastNumber+1) :
    listA.append(i)

while x < 1 :
    exceptNumber = int(input("제외할 번호를 입력하세요 (없다면 0 입력) : "))
    if exceptNumber == 0 :
        x += 1
    else :
        listA.remove(exceptNumber)

for i in range(1, len(listA)+1) :
    listB.append(i)

random.shuffle(listB)

for i in range(0, len(listA)):
    print("{:5d}".format(listA[i]), "{:5d}".format(listB[i]))