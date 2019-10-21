#main.py
from order import Order
from file_manager import FileManager

file_manager = FileManager("history.bin")
history = []
try :
    history = file_manager.load()
    for h in history:
        print(h)
        sum += h.price
    print("여태껏 아마스빈에 퍼부은 내돈 : " + str(sum) + "원")
except FileNotFoundError:
    print("내역이 없습니다.")
print("-----------------------------------------")

o = Order()
o.order_drink()

file_manager.save(history + o.order_menu)