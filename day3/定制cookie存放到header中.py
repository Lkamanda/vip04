# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-15 17:24
@Author  : zhoujialin
@File    : 定制cookie存放到header中.py
'''

import requests, json
dl = {"username":"zhoujialin", "password": "5211314"}
dl_url = "https://www.wanandroid.com/user/login"

r = requests.post(dl_url,dl)
r_cookies = r.cookies
print(type(r_cookies))
print(r_cookies["JSESSIONID"])

# 使用部分cookie ，制作新的cookie
# new_cookies = {
#     "JSESSIONID": r_cookies["JSESSIONID"]
# }

new_header = {
    "cookie": "JSESSIONID="+r_cookies["JSESSIONID"]
}

db_url = "https://www.wanandroid.com/lg/todo/list/0"
db = requests.post(db_url, headers= new_header)
# print(db.status_code)
print(db.text)