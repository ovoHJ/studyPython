# 각 자리수의 합 구하기
# END

number = input("숫자 입력 : ")
list = []
sum = 0

'''
for x in number:
    list += x

for i in range(0, len(number)):
    sum += int(list[i])
print(sum)
'''

for i in number :
    sum += int(i)
    
print(sum)