# 1、打印小猫爱吃鱼，小猫要喝水
class Cat(object):
    def eat(self):
        print('小猫爱吃鱼')
    def drink(self):
        print('小猫要喝水')

cat = Cat()
cat.eat()
cat.drink()

"""
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤
"""

class Human1(object):
    def __int__(self, weight, name):
        self.weight = weight
        self.name = name
    def run(self):
        self.weight -= 0.5
        print(self.name)

    def eat(self):
        self.weight += 1

xm = Human1(75,"XL")
xm.run()