import json
from httpx import AsyncClient
import asyncio 

# 异步HTTP请求的实现

async def getDate():
    async with AsyncClient() as client:
        tasks = []
        tasks.append(pic(client))
        data = await asyncio.gather(*tasks)
        return data


async def pic(client:AsyncClient):
    try:
        res = await client.post(
            "http://kaodigua.top:5000/",
        )
    except:
        return "hello"
    tag = json.loads(res.text)
    return tag

data = asyncio.run(getDate())

print(data)
