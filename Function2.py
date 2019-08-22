# #107-109-112
# import random
# # def rolling_dice():
# #     n = random.randint(1, 6) #1<=n<=6 랜덤수
# #     print("6면 주사위 굴린 결과 :", n)

# # def rolling_dice(pip):
# #     n = random.randint(1, pip) #1<=n<=6 랜덤수
# #     print("6면 주사위 굴린 결과 :", n)

# def rolling_dice(pip, repeat):
#     for r in range(1, repeat+1):
#         n = random.randint(1, pip) #1<=n<=6 랜덤수
#         print(pip, "면 주사위 굴린 결과", r, ":", n)

# rolling_dice(6, 1)
# rolling_dice(6, 2)
# rolling_dice(12, 0)
# rolling_dice(20, -3)

# def star():
#     print("*****")

# star()
# star()
# star()


# #p113
# print("♡")
# print("♡", "♪")
# print("♡", "♪", "♣")
# print("♡", "♪", "♣", "♠")
# print("♡", "♪", "♣", "♠", "☆")

# # def p(*args):
# #     string=""
# #     for a in args:
# #         string += a
# #     print(string)

# # p("안녕")


# #p114
# def p(space, space_num, *args):
#     string = args[0]
#     for i in range(1, len(args)):
#         string += (space * space_num) + args[i]
#     print(string)

# p(",", 3, "핱", "읖")


#115
def star2(space, *nums):
    for i in range(0, len(nums)):
        print(space * nums[i])

star2("읖", 3) #읖읖읖
star2("핱", 1, 2, 3)
#핱
#핱핱
#핱핱핱


#p116
def fn(a, b, c, d, e):
    print(a, b, c, d, e)

#p118
# ***__***
# ***__***
# ***__***

def star(mark, repeat, space, space_repeat, line):
        for i in range(line):
                string = (mark*repeat)+(space*space_repeat)+(mark*repeat)
                print(string)

#p119
def hello(msg="안녕하세요"):
        print(msg + "!")

hello("하이")
hello("hi")
hello()

#p120
def hello2(name, msg="안녕하세요"):
        print(name + "님, " + msg + "!")

hello2("김가영", "오랜만이에요")
hello2("김선옥")

def fn2(a, b=[]):
        b.append(a)
        print(b)

fn2(3)
fn2(5)
fn2(10)

#p123
def gugudan(dan=2):
        for i in range(1, 9+1):
                print(dan, "× ", i, "= ", dan*i)
        print()

gugudan(3)
gugudan(2)
gugudan()

def sum(*numbers):
        sum_value = 0
        for number in numbers:
                sum_value += number

        return sum_value

print("1 + 3 =", sum(1, 3))
print("1 + 3 + 5 + 7 =", sum(1, 3, 5, 7))  

def max(*numbers):
        max_number = numbers[0]
        for number in numbers:
                if max_number < number:
                        max_number = number
        return max_number

print("max(8, 1, -1, 12) =", max(8, 1, -1, 12))

def nulti_num(multi, start, end):
        result = []
        for n in range(start, end):
                if n % multi:
                        result.append(n)
        return result

print("nulti_num(17, 1, 200) =", nulti_num(17, 1, 200))
print("nulti_num(3, 1, 100) =", nulti_num(3, 1, 100))

def min_max(*args):
        min_value = args[0]
        max_value = args[0]
        for a in args:
                if min_value > a:
                        min_value = a
                if max_value < a:
                        max_value = a
        return min_value, max_value

min, max = min_max(52, -3, 23, 89, -21)
print("최소값 :", min, "최댓값 :", max)