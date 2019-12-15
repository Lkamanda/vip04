# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-15 10:12
@Author  : zhoujialin
@File    : day4.py
'''

# 关键字参数

# dict1 = {"a":"1","b":"2" }
# def add(**kwargs):
#     print(kwargs)
# c = add(**dict1)
# print(type(c))
#
# try:
#     print(c)
# except Exception as e:
#     print(e)



class Human1(object):
    # dw = '公斤'
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def __str__(self):
        a= "当打印类实例的时候，打印这就话"
        return a

    def run(self):
        self.weight -= 0.5
        self.tz()

    def eat(self):
        self.weight += 1
        self.tz()

    dw = '公斤'
    def tz(self):
        print("{0}当前体重为：{1}{2}".format(self.name, self.weight, self.dw))

xm = Human1(weight=75,name="小明")
print(xm)
xm.run()
xm.eat()
mei = Human1(weight=45, name="小美")
mei.tz()


# 类对象
class human(object):

    color= 'red'

    def __sy(self):
        print('私有')

    @classmethod
    def lf(cls):
        return cls.color

    @staticmethod
    def jt():
        print('jt')
