import asyncio
from httpx import AsyncClient
import os

proxies = {"http://": "http://127.0.0.1:7890", "https://": "http://127.0.0.1:7890"}


async def Fun():
    async with AsyncClient(proxies=proxies) as client:
        url = "https://pixiv.re/101013633.jpg"
        response = await client.get(url)
        if response.status_code == 200:
            return response


# result =  asyncio.run()
loop = asyncio.get_event_loop()
result = loop.run_until_complete(Fun())
url: str = result.headers.get("x-origin-url")
url = url.replace("net", "re")
print(url)
with open(f"{os.getcwd()}/imagess/1.jpg", "wb") as f:
    f.write(result.content)
    f.close()
