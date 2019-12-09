# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-08 19:41
@Author  : zhoujialin
@File    : day2_io.py
'''

# 读取data文件中的数据，将所有的数字去重并按照从小到大的顺序写入backup文件
# 1.简单
px_line = []

with open(r"data_jd", "r")as f:
    lines=f.readlines()
    for line in lines:
        line = int(line.rstrip())
        if line not in px_line:
            px_line.append(line)
    px_line.sort()
    # 将排序后的int 类型改回 str 便于写入

with open("backup_jd","w+") as b:
    # 增加换行写入
    b.writelines(str(line)+'\n' for line in px_line)

# 2。复杂
# fa
r_fz = []
return_fz = []
with open("data_fz","r") as f:
    lines = f.readlines()
    print(lines)
    # 去掉空格
    for line in lines:
        str_line = line.rstrip()
        r_fz.append(str_line)

    for i in r_fz:
        #根据，进行str切割
        rs = i.split(",")
        print(rs)
        for r in rs:
            # 去重，去空，加入返回列表
            if r not in return_fz and r !='':
                r = int(r)
                return_fz.append(r)
    # 排序
    return_fz.sort()
    print(return_fz)
# 写入文件
with open("backup_fz","w+") as f:
    f.writelines(str(line)+'\n' for line in return_fz )

