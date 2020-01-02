# import itchat
# import requests
# import re
#
# def getHtmlText(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "获取失败"
#
# # 调用itchat封装好的装饰器
# @itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing','Picture'])
#
# # 定义自动回复函数
# def text_reply(msg):
#     # 判断一下发件人是不是自己
#     if not msg ['FromUserName'] == '小林':
#         url = "http://www.tuling123.com/openapi/api?key=287d4ce32b2b4a5e9ea0947c77e3e790&info="
#         url = url + msg['Text']
#         html = getHtmlText(url)
#         message = re.findall()
#         message = re.findall(r'\"text\"\:\".*?\"', html)
#
#         reply = eval(message[0].split(':')[1])
#         return reply
#
#
#
#
#
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     itchat.auto_login()
#
#     # 获取所有微信好友的信息
#     friends = itchat.get_friends(update=True)[0:]
#     # 使用字典存放好友的昵称与用户名
#     Name = {}
#
#     Nic = []
#
#     User = []
#     for i in range(len(friends)):
#         Nic.append(friends[i]["NickName"])
#         User.append(friends[i]["UserName"])
#     for i in range(len(friends)):
#         Name[Nic[i]] = User[i]
#         itchat.run()



# from time import sleep
# import requests
# s = input("请主人输入话题：")
# while True:
#     resp = requests.post("http://www.tuling123.com/openapi/api",data={"key": "4fede3c4384846b9a7d0456a5e1e2943", "info": s, })
#     resp = resp.json()
#     sleep(1)
#     print('小鱼：', resp['text'])
#     s = resp['text']
#     resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid': 0, 'msg': s})
#     resp.encoding = 'utf8'
#     resp = resp.json()
#     sleep(1)
#     print('菲菲：', resp['content'])

import itchat
import requests

url = "http://www.tuling123.com/openapi/api"
key = "720b8495c39f40ac92284c5d6b3d1dd7"


@itchat.msg_register("Text")
def text_reply(msg):
    return get_reply(msg["Text"])


def get_reply(msg):
    print(msg)
    repson = requests.post(url + "?key=" + key + "&info=" + msg).json()
    print(repson)
    return repson.get("text")


itchat.auto_login(hotReload=True)
itchat.run()

