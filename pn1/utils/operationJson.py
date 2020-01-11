"""
通过去取json文件获取请求数据
"""
from pn1.utils.public import *
from pn1.utils.operationExcal import OperationExcel
import json


class OperationJson(object):
    def __init__(self):
        self.excal = OperationExcel()

    def getReadJson(self):
        """读取json文件"""
        with open(data_dir(fileName='requestData.json'), encoding='utf-8') as f:
            return json.load(f)

    def get_Request_Json(self, row):
        """
        通过读取json文件返回的是个字典格式的数据，通过对应的k，取出需要的请求参数v
        :param row: 行数    self.excal.get_requestData(row） 字典的k
        :return: 字典的v
        """
        # return self.getReadJson()[self.excal.get_requestData(row)]
        return json.dumps(self.getReadJson()[self.excal.get_requestData(row=row)],
                          ensure_ascii=False)


if __name__ == '__main__':
    Oa = OperationJson()
    print(Oa.get_Request_Json(1))