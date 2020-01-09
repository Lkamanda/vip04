import xlrd
import os


def base_dir(filename=None):
    return os.path.join(os.path.dirname(__file__), filename)


# work = xlrd.open_workbook(r"C:/Users/zhoujialin/PycharmProjects/vip04/kj/data.xls", 'rb')
work = xlrd.open_workbook(base_dir('data_demo.xls'))
sheet = work.sheet_by_index(0)

print(sheet.nrows)

print(sheet.cell_value(1, 1))