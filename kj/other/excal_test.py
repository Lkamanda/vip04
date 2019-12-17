import xlrd, os
# C:\Users\zhoujialin\PycharmProjects\vip04\kj\data\test.xlsx
print(os.path.dirname(__file__))
path= r"..\data\test.xlsx"
# 打开文件
data = xlrd.open_workbook(filename=path)
table = data.sheets()[0]
# table1 = data.sheet_by_name('sheet_1')

# 返回excal中所有工作表的名字
names = data.sheet_names("Sheet1")
print(names)

# 检查某个sheet是否导入完毕
data.sheet_loaded(1)
