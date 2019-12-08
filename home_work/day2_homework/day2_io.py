# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-08 19:41
@Author  : zhoujialin
@File    : day2_io.py
'''

# 读取data文件中的数据，将所有的数字去重并按照从小到大的顺序写入backup文件
# 1.简单
px_line = []
back_line = []
with open("/Users/zhoujialin/PycharmProjects/vip04/home_work/day2_homework/data_jd", "r")as f:
    lines=f.readlines()
    for line in lines:
        line = int(line.rstrip())
        if line not in px_line:
            px_line.append(line)
    px_line.sort()
    # 将排序后的int 类型改回 str 便于写入
    for line in px_line:
        line = str(line)
        back_line.append(line)
print(back_line)

with open("/Users/zhoujialin/PycharmProjects/vip04/home_work/day2_homework/backup.text_jd","w+") as b:
    # 增加换行写入
    b.writelines(line+'\n' for line in back_line)

# 2。复杂


