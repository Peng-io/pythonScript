import requests
from bs4 import BeautifulSoup
from urllib import request
import json

# url="https://www.dmoe.cc/random.php"
url = [
    "https://api.ixiaowai.cn/api/api.php",
    "https://iw233.cn/api/Random.php",
    "https://api.lolicon.app/setu/v2",
    "https://setu.yuban10703.xyz/setu"
]
name = "图片"
request.urlretrieve(url[0], f"imagess/{name}.jpg")
