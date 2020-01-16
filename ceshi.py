# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-29 16:49
@Author  : zhoujialin
@File    : configHttp.py
'''
import requests
import json

class configHttp(object):

    def __init__(self):
        print('开始请求接口')
        # self.myData = myData

    def get(self, url, params=None, **kw):
        try:
            res = requests.get(url, params, **kw)
        except TimeoutError:
            print('超时')
        else:
            print(res.text)
            print(res.status_code)
            return res
    #
    # def post(self, url, data=None, json=None, **kw ):
    #     try:
    #         res = requests.post(url, data=data, json=json, **kw)
    #         print(res.json())
    #     except TimeoutError:
    #         print('超时')
    #     else:
    #         return res


    def put(self):
        print('put 请求')
        return 0

    def post(self, url, params, **kw):
        result = requests.post(url=url, data=param)
        print(result.status_code)
        dict1 = json.loads(result.text)
        print(dict1)
        print(dict1['code'])
        return dict1['code']


if __name__ == '__main__':
    test = configHttp()
    baseurl = "https://mall.jingcailvtu.org:9443"
    path = "/couponNew/getCouponList"
    url = baseurl + path
    param = {
        # "mytype":""
    }
    test.get(url=url, params=param)
