"""
请求的二次封装
"""
import requests
from pn1.utils.operationExcal import OperationExcel
from pn1.utils.operationJson import OperationJson


class Method(object):
    def __init__(self):
        self.operationExcel = OperationExcel()
        self.operationJson = OperationJson()

    def post(self, row):
        """
        对post方法进行二次封装
        :return:
        """
        try:
            r = requests.post(
                url=self.operationExcel.get_url(row=row),
                data=self.operationJson.get_Request_Json(row=row),
                headers="",
                timeout=6
                              )
            return r
        except Exception as e:
            # 抛出一个异常
            raise RuntimeError('抛出未知的错误')

    def post(self, row, data):
        """
        对post方法进行二次封装
        :return:
        """
        try:
            r = requests.post(
                url=self.operationExcel.get_url(row=row),
                data=data,
                headers="",
                timeout=6
                              )
            return r
        except Exception as e:
            # 抛出一个异常
            raise RuntimeError('抛出未知的错误')

    def get(self):
        try:
            r = requests.get()
            return r
        except Exception as e:
            raise RuntimeError('抛出未知错误')

    def delete(self):
        try:
            r = requests.delete()
            return r
        except Exception as e:
            raise RuntimeError('抛出未知错误')


class IsAssert:
    def __init__(self):
        self.excel = OperationExcel()

    def isContent(self, row, str2):
        flag = None
        if self.excel.get_except(row=row) in str2:
            flag = True
        else:
            flag = False
        return flag
