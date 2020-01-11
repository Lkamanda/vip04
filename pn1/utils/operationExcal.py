""""
对excal的数据处理
"""
import xlrd
from xlutils.copy import copy
from pn1.utils.public import *
from pn1.utils.excalData import *


class OperationExcel:

    def getExcel(self):
        """获取sheet"""
        db = xlrd.open_workbook(data_dir('data', 'data_demo.xls'))
        sheet = db.sheet_by_index(0)
        return sheet

    def get_rows(self):
        """获取excel的行数"""
        return self.getExcel().nrows

    def get_row_cel(self, row, col):
        """
        获取单元格内容
        :param row: 行
        :param col: 列
        :return: 对应单元格内容
        """
        return self.getExcel().cell_value(row, col)

    def get_url(self, row):
        """获取"""
        return self.get_row_cel(row, getBaseUrl()) + self.get_row_cel(row, getInterface())

    def get_requestData(self, row):
        """获取请求参数"""
        return self.get_row_cel(row, getRequest_data())

    def get_result(self):
        """获取断言"""



if __name__ == '__main__':
    opera = OperationExcel()
    # print(opera.get_rows())
    # print(opera.get_row_cel(1, 1))
    print(opera.get_requestData(1))
