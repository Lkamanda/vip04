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
       v                                                                                                                                                                                                                                                        cv                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                v vbnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnbn
        """
        # return self.getReadJson()[self.excal.get_requestData(row)]
        return json.dumps(self.getReadJson()[self.excal.get_requestData(row=row)],
                          ensure_ascii=False)


if __name__ == '__main__':
    Oa = OperationJson()
    print(type(Oa.getReadJson()))
    print(Oa.get_Request_Json(1))
    print(type(Oa.get_Request_Json(1)))