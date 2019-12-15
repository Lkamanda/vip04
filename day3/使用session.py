# -*- coding: utf-8 -*-
'''
@Time    : 2019-12-15 16:05
@Author  : zhoujialin
@File    : 使用session.py
'''
import requests, json

s = requests.session()

dl = {"username":"zhoujialin", "password": "5211314"}
dl_url = "https://www.wanandroid.com/user/login"
dl_r = s.post(url=dl_url, data=dl)

db_url = "https://www.wanandroid.com/lg/todo/list/0"

db_r = s.post(url=db_url)
print(db_r.text)