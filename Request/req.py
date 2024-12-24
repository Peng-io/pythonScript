import requests
import json

r = requests.get("https://www.baidu.com/")
# 响应内容（str类型）
print(type(r.text), r.text)
# 响应内容（bytes类型）
print(type(r.content), r.content)
# 状态码
print(type(r.status_code), r.status_code)
# 响应头
print(type(r.headers), r.headers)
# Cookies
print(type(r.cookies), r.cookies)
# URL
print(type(r.url), r.url)
# 请求历史
print(type(r.history), r.history)
