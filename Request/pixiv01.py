import requests
import httpx
import sqlite3

proxies = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
}
conn = sqlite3.connect("pixiv.db")
cursor = conn.cursor()
sql = "SELECT pid FROM omega_pixiv_artwork  WHERE pid>95147811  ORDER BY pid asc LIMIT 20000"
img_url = cursor.execute(sql).fetchall()
for i in img_url:
    url = f"https://pixiv.re/{i[0]}.jpg"
    res = requests.get(url, headers=headers)
    img_url = res.headers.get("x-origin-url")
    print(img_url)
    try:
        url = img_url.replace("pximg", "pixiv").replace("net", "re")
    except:
        cursor.execute(f"DELETE FROM omega_pixiv_artwork  WHERE pid={i[0]}")
        conn.commit()
        continue
    cursor.execute(f"update omega_pixiv_artwork set url='{url}' where pid={i[0]}")
    conn.commit()
cursor.close()
conn.close()
