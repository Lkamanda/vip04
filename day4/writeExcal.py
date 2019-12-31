from  xlutils.copy import copy
import xlrd
import time

# xlutils 追加写入
# str_path = ''
# path = r'C:\Users\zhoujialin\PycharmProjects\interface\testData\data_demo{0}.xls'.format(str_path)
path = r'C:\Users\zhoujialin\PycharmProjects\interface\testData\data_demo.xls'

rb = xlrd.open_workbook(path)

# 复制读取源的excal对象
wb = copy(rb)
# 通过get_sheet()获取复制对象的sheet 页
ws = wb.get_sheet(2)

ws.write(1,3, 'ok2')

# time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# print(time.strftime('%Y-%m-%d %H:%M:%S'))
#
str_path = str(time.strftime('%Y-%m-%d %H-%M-%S')) + 'result'

path = r'C:\Users\zhoujialin\PycharmProjects\interface\testData\{0}.xls'.format(str_path)

wb.save(path)
