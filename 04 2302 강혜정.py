# 주차요금 계산
# RE

min = input("주차요금 계산(분) : ")
money = 0
money1 = int(min)/10
money2 = int(min)//10

if (int(min)<=30) :
    money = 2000
else :
    if money1 > money2 :
        money = money2*1000
    else :
        money = money2*1000-1000

if (25000 < money) :
    money = 25000

print(str(money) + "원")