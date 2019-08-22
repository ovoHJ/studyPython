class Drink:
    _cups = ["레귤러","점보"]
    _ices = ["0%","50%","100%","150%"]
    _sugars = ["0%","50%","100%","150%"]
    _pearls = ["타피오카", "코코", "젤리", "알로에"]
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0    #0 : 레귤러, 1: 점보
        self.ice = 2    #0 : 0%, 1 : 50%, 2 : 100%, 3 : 150%
        self.sugar = 2  #0 : 0%, 1 : 50%, 2 : 100%, 3 : 150%

    def set_cup(self):
        self.cup = input("컵사이즈를 선택하세요.(0 : 레귤러, 1: 점보) : ")
        if self.cup == "":       #Enter치면 기본값 0 설정
            self.cup = 0
        else:
            self.cup = int(self.cup)

        if self.cup == 1:
            self.price+=500
        
    def set_ice(self):
        self.ice = input("얼음양을 선택하세요.(0 : 0%, 1 : 50%, 2 : 100%, 3 : 150%) : ")
        if self.ice == "":
            self.ice = 2
        else : 
            self.ice = int(self.ice)

    def set_sugar(self):
        self.sugar = input("당도를 선택하세요.(0 : 0%, 1 : 50%, 2 : 100%, 3 : 150%) : ")
        if self.sugar == "":
            self.sugar = 2
        else:
            self.sugar = int(self.sugar)

    def __str__(self):
        return "이름: "+self.name+"\t가격: "+str(self.price)+"\t컵사이즈: "+self._cups[self.cup]+"\t얼음양: "+self._ices[self.ice]+"\t당도: "+self._sugars[self.sugar]

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

class Coffee(Drink):
    pass

class BubbleTea(Drink):
    def __init__(self, name, price):
        super().__init__(name,price)
        self.pearl = 0  #0 : 타피오카, 1 : 코코, 2 : 젤리, 3 : 알로에

    def set_pearl(self):
        self.pearl = input("펄을 선택하세요.(0 : 타피오카, 1 : 코코, 2 : 젤리, 3 : 알로에): ")
        if self.pearl == "":
            self.pearl = 0
        else:
            self.pearl = int(self.pearl)

    def __str__(self):
        return super().__str__()+"\t펄: "+self._pearls[self.pearl]

    def order(self):
        super().order()
        self.set_pearl()

class Order:
    _drinks = [Coffee("아메리카노", 1800), BubbleTea("하동녹차오레오", 3900)]

    def __init__(self):
        self.order_menu = []

    def show_menu(self):
        print("0: 아메리카노 1800원, 1: 하동녹차오레오 3900원")
    
    def order_drink(self):
        #show menu
        while True:
            self.show_menu()

            #주문받기, 음료선택하기
            order = input("무엇을 고르시겠습니까? ")
            if order == "":
                break
            drink = Order._drinks[int(order)]
            drink.order()
            self.order_menu.append(drink)
        #반복!
        #주문한 음료 내용 보여주기
        for d in self.order_menu:
            print(d)
        #합계 금액 보여주기
        print("총금액 : " + str(self.sum_price()) + "원")

    def sum_price(self):
        sum = 0
        for d in self.order_menu:
            sum += d.price

        return sum

o = Order()
o.order_drink()

# print("< < Coffee 주문 > >")
아메리카노 = Coffee("아메리카노", 1800)
아메리카노.set_cup()
# 아메리카노.set_ice()
# 아메리카노.set_sugar()
# print(아메리카노)

# print("---------------------------------------------------")

# print("< < Bubble Tea 주문 > >")
# 하동녹차오레오 = BubbleTea("하동녹차오레오", 3900)
# 하동녹차오레오.set_cup()
# 하동녹차오레오.set_ice()
# 하동녹차오레오.set_sugar()
# 하동녹차오레오.set_pearl()
# print(하동녹차오레오)