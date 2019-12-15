# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-15 13:36
@Author  : zhoujialin
@File    : day3request.py
'''

import requests
import json

urlstr = "http://www.baidu.com"
r = requests.get(url=urlstr)
# print(r.text)
# print(r.content)

payload = {"k":"Android"}

url_android = "https://www.wanandroid.com/article/query"

r_android = requests.get(url=url_android, params=payload)

# print(r.status_code)
#
# print(r.headers)
# print(r.json)
# print(r.text.encode('utf-8'))
# print(r.encoding('utf-8'))

# print(r.cookies)
# print(r_android.raw)

print(r.raise_for_status())

# dumps 将python类型转成 json
s = requests.session()

url = "https://www.wanandroid.com/user/login"
login = {"username":"zhoujialin", "password":"5211314"}
# login = json.dumps(login)
r = s.post(url=url, data=login)
# print(r.text)

print(r.json())
print(r.json()['data']['nickname'])
print(r.json()['errorCode'])

# 接口断言

if r.status_code == 200:
    if r.json()['errorCode'] == 0:
        print('error码正确')
        if r.json()['data']['nickname'] == login["username"]:
            print('登录成功')
    else:
        print('登录失败，errCode：%s' %r.json()['errorCode'])
else:
    print("请求状态不对，登录失败")


db_url = "https://www.wanandroid.com/lg/todo/list/0"

db_r = s.post(db_url)
print(db_r.text)




