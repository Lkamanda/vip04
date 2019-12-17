import requests
# url = "http://im.jingcailvtu.org:6963/u/login"
url = "https://im.jingcailvtu.org:7453/"
# 1 web 2 app
body ={
    "phone":"18612463553",
    "password":"111111",
    "source": 1
}
path = "u/login"
r = requests.post(url=url+path, data=body)
print(r.status_code)
print(r.json())
print(r.headers["xAuthToken"])

# 验证token
print(r.headers)
data = {
    "xAuthToken": r.headers["xAuthToken"]
}
token_path = "u/isEnabled"
r_y = requests.post(url=url+token_path, data=data)
print(r_y.text)
