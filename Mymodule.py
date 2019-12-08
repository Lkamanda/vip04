# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-07 16:59
@Author  : zhoujialin
@File    : Mymodule.py
'''

def fun1():
    print('fun1')

def fun2():
    print('fun2')

class Person(object):
    def __init__(self, name, age):
        # 定义实例属性
        self.name = name
        self.age = age
        print(self.name,self.age)

    def eat(self,food):
        print('i eat %s'%food)
    def sleep(self):
        print('sleep')


xl = Person('xl',15)
xl.sleep()
xl.eat('lingshi')


class Student(object):

    # 类属性
    color ='red'
    #实例属性
    def __init__(self,name,course, id):
        self.name = name
        self.course = course
        self.id = id

    def study(self):
        print('{0}学习{1}课程'.format(self.name,self.course))

a = Student('xl', "数学","003")
a.study()