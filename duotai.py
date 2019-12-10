class DuoTai_a(object):
    def eat(self):
        print('我是DuoTai_a')

class DuoTai_b(object):
    def eat(self):
        print("我是DuoTai_b")

def ceshi(temp):
    temp.eat()

a = DuoTai_a()
b = DuoTai_b()
ceshi(a)
ceshi(b)
