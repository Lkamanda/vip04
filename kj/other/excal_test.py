import xlrd, xlwt, xlutils
# xlwt 写 excal
# xlrd 读 excal
# xlutils 修改

path= r"..\data\test.xlsx"
# 打开文件
data = xlrd.open_workbook(filename=path)
table = data.sheets()[0]
# table1 = data.sheet_by_name('sheet_1')

sheet = data.sheet_by_name("Sheet1")

# 返回excal中所有工作表的名字
names = data.sheet_names()
print(names)

# 检查某个sheet是否导入完毕, name or index
data.sheet_loaded(1)

# 获取总行数，
rows = sheet.nrows
print(rows)

columns = sheet.ncols
print(columns)
# 获取总列数

# 第一行第一列
print(sheet.cell(1,1).value)

print(sheet.row_values(1))