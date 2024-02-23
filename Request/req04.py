import requests
from lxml import etree
import time

proxies = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}
# 进行UA伪装
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36x-requested-with: XMLHttpRequest"
}
for num in range(1, 100):

    url = "https://www.pixiv.net/ranking.php"
    param = {"p": num}
    # 获取排行榜页面
    response = requests.get(url=url, headers=header, params=param, proxies=proxies).text
    # 建立xpath正则 获取ID
    tree = etree.HTML(response)
    img_id_list = tree.xpath("//*/div/a/@href")[3:]
    for each in img_id_list:
        if "series" in each:
            continue
        url = "https://embed.pixiv.net/decorate.php"
        # each 是/artworks/87898731
        # 由此我们进行切片获取具体ID
        date_id = each[10:]
        param = {"illust_id": date_id}
        img_data = requests.get(
            url=url, params=param, headers=header, proxies=proxies
        ).content
        # 设置图片名字
        img_file_name = "imagess/" + date_id + ".jpg"
        # 写入图片
        with open(img_file_name, "wb") as fp:
            fp.write(img_data)
            print(img_file_name + "下载成功")

        # 防止被封 加个延迟
        time.sleep(0.5)
