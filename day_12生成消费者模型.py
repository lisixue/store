"""
@author:86152
@file:生成消费者模型.py
@time:2021/11/04
"""
import threading
from threading import Thread
import time
lock = threading.Lock()
tart = 0
checkstand = 0
T=0  # 程序执行30秒
class Cooker(Thread):
    username = ""
    count = 0
    money = 0

    def run(self) -> None:
        global tart
        global T
        while T < 30:
            if tart < 500:
                self.count +=1
                tart +=1
                money = self.count * 1.5
                lock.acquire()
                print(self.username,"做了",self.count,"个蛋挞,现在一共有",tart,"个蛋挞")
                lock.release()

            else:
                time.sleep(3)
            lock.acquire()
            print(self.username,"一共挣了",money,"块钱")
            lock.release()



class Customer(Thread):
    name = ""
    money = 3000
    buycount = 0

    def run(self) -> None:
        global checkstand
        global T
        while T < 30:
            if tart > 0:
                if self.money > 3:
                    self.buycount +=1
                    self.money -=3
                    lock.acquire()
                    print(self.name,"买了",self.buycount,"个蛋挞,还有",self.money,"块钱")
                    lock.release()
                    checkstand = self.buycount * 3
            else:
                time.sleep(2)



class clock(Thread):

    def run(self)->None:
        global T
        while T < 30:
            time.sleep(1)
            T += 1


c1 = Cooker()
c2 = Cooker()
c3 = Cooker()
customer1 = Customer()
customer2 = Customer()
customer3 = Customer()
customer4 = Customer()
customer5 = Customer()
customer6 = Customer()
time1=clock()

c1.username = "厨师一号"
c2.username = "厨师二号"
c3.username = "厨师三号"
customer1.name = "顾客一号"
customer2.name = "顾客二号"
customer3.name = "顾客三号"
customer4.name = "顾客四号"
customer5.name = "顾客五号"
customer6.name = "顾客六号"

time1.start()
c1.start()
c2.start()
c3.start()
customer1.start()
customer2.start()
customer3.start()
customer4.start()
customer5.start()
customer6.start()








