# 야구게임
# 세자리 중복없는 임의의수 만들자
# 무한반복   while
# 사용자 입력을 받자   input()
# strlike, ball 판정하자
# 사용자 입력한 것, strike, ball 출력하자   print()
# 임의의수랑 사용자 입력한게 같으면 HIT, break     if
import random

l = random.sample(range(1, 9+1), 3)
computer = ''.join(str(i) for i in l)

while True:
    player = input("숫자 세자리 맞춰봐 : ")
    strike = 0
    ball = 0
    #strike, ball 판정하자
    for i in range(len(computer)):
        for j in range(len(player)):
            if computer[i] == player[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1

    print(player, "strike :", strike, "ball :", ball)
    if computer == player:
        print("HIT")
        break