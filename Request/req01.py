import requests
from bs4 import BeautifulSoup
from urllib import request

url = "http://www.netbian.com/erciyuan/"
res = requests.get(url)
res.encoding = "gbk"
html = BeautifulSoup(res.text, "html.parser")
pra = html.find("div", class_="list")
images = pra.find_all("img")
for i in images:
    name = i.attrs["alt"]
    request.urlretrieve(i.attrs["src"], f"imagess/{name}.jpg")
