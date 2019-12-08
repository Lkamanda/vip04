# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-07 15:58
@Author  : zhoujialin
@File    : ioread.py
'''

# f = open(r"/Users/zhoujialin/PycharmProjects/vip04/test.text","w+")
#
# try:
#     print(f.readlines())
#     f.writelines()
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# 读取这个文件重小到大排列写入新文件，去重

# import Mymodule
#
# Mymodule.fun1()

# from Mymodule import *
# fun1()


from practice import  Mymodule
Mymodule.fun1()

append_list = []
with open("/Users/zhoujialin/PycharmProjects/vip04/test.text", "r") as f:
    lines = f.readlines()
    # print(f.read())
    for i in lines:
        i= i.strip('\n')
        append_list.append(i)
    print(append_list)
new_list = []
for i in append_list:
    if i not in new_list:
        new_list.append(i)




