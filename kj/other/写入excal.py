import xlwt

path= r"..\data\test.xlsx"
# 打开文件
book = xlwt.Workbook()
sheet = book.add_sheet('xiaolin')

book.save(r"..\data\test1.xls")