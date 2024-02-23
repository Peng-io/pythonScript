import time
import requests

cookie = {
    "PHPSESSID": "3a769bfdc468f70058e60dd513fa19c5",
    "wordpress_sec_19441921a5f12a81ae1e9b8002b0279f	": "pengsonghao%7C1698810387%7ClEbcchledcnwBbggoRfNyOAXgW4HGj2t3gZnHH3xUAi%7C8f18d26f791de93c749d72c146e0e17782eaa5551c0d9b333e11d569bf521799",
    "wordpress_logged_in_19441921a5f12a81ae1e9b8002b0279f": "pengsonghao%7C1698810387%7ClEbcchledcnwBbggoRfNyOAXgW4HGj2t3gZnHH3xUAi%7C07224462b56f78be8793b901ccc3a80fd9620242b681a3704312e45017980a93",
    "wp-settings-110": "	libraryContent%3Dbrowse%26align%3Dcenter",
    "wp-settings-time-110	": str(int(time.time())),
}
beseUrl = "https://impactxchina.cn/wp-admin/admin-ajax.php"
data = {"action": "oembed-cache", "post": "9149"}
url = "https://impactxchina.cn/yjzpost/c2095430.html"

req = requests.get(url, cookies=cookie)
print(req.text)
with open("1.html", "w") as f:
    f.write(req.text)
