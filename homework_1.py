# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-02 11:55
@Author  : zhoujialin
@File    : homework_1.py
'''

# list_old = [1,2,3,4,3,4,2,5,5,8,9,7]
# list_new = []
#
# for i in list_old:
#     if i not in list_new:
#         list_new.append(i)
#
# print(list_new)
#
# def feb(n):
#     while n >=0:
#         if n <= 1:
#             return n
#         return feb(n-1) + feb(n-2)
#
# for i in range(1,10):
#     print(feb(i))
#
# # 大于1除了1和他自身可以整除的数
#
# num = []
# for i in range(2,1001):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#         else:
#             if i not in num:
#                 num.append(i)
#
# print(num)
#
# a = 1.0
# b = 1.5
# print("%03d,%d"%(a,b))

a = [4,5,3,8,9,1]
# a.sort()
a.reverse()
print(a)
b = sorted(a)
print(a,b)

a = [1,2,3,4,5]
a.insert(3, "i")
print(a)
a = [1,2,3]
b = ['a','b','c']
a.extend(b)
print(a,b)

a = [1,2,3,4,5,2,3,2]
print(a.index(2))
print(a.count(2))
