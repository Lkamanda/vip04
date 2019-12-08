# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-07 11:16
@Author  : zhoujialin
@File    : day2.py
'''
example = [[1,2,3], [5,6,4], [7,8,9], [10]]
x = []
for i in example:
    if len(i) > 1:
        for j in i:
            if j%2 == 0:
                j*=j
                x.append(j)
print(x)

#列出100以内的偶数能被3整除

a = [j for i in range(0,101)  if i%3==0 and i%2==0]
print(a)

#
# a,b,c = input('请输入三个参数：').split(',')

def js(a,b,c):
    if a.isnumber and c.isnumber:
        a,c  = int(a),int(c)
        if b == "+":
            return a+c
        elif b == "/":
            return a//c
        elif b == "-":
            return a - c
        elif b == "*":
            return a*c
        else:
            print('你输入的符号有误')

# print(js(a,b,c))

def add_end(l=None):
    if l == None:
        l =[]
    l.append('end')
    return l

print(add_end())
print(add_end())


def add(name, age, *args, **kwargs):
    print(name, age, *args, **kwargs)

add('xiao', 12, 13,14,{'xiao':'hah','ce':"shi"})

def calc(a1,b1):
    try:
        print(a1/b1+c)
    # except (ZeroDivisionError,NameError) as e:
    #     print(e)
    #     print('不能为o')

    # except BaseException as e:
    #     print(e)

    except Exception as e:
        print(e)


a1 = int(input("请输入a1"))
b2 = int(input("请输入b1"))
calc(a1,b2)