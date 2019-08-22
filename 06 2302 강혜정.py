# 369 게임
# END

for i in range(1, 100):
    i = str(i)
    n = 0

    if (len(i) == 1) :
        if int(i[0]) % 3 == 0 :
            n += 1

    if (len(i) == 2) :
        if int(i[0]) % 3 == 0 :
            n += 1
        if int(i[1]) % 3 == 0 and int(i[1]) != 0:
            n += 1

    if(n == 0) :
            print(i)
    else :
            print("짝"*n)

