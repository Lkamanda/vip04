import xlrd
from xlutils.copy import copy
from pn1.utils.public import *


class ExcalVariable(object):
    caseID = 0
    url = 2
    request_data = 3
    expect = 4
    result = 5


def getCaseID():
    #
    return ExcalVariable.caseID


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

opera = OperationExcel()
print(opera.get_rows())
print(opera.get_row_cel(1, 1))