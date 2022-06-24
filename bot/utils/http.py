import aiohttp


'''
*
В этом файле написана функция для парса страниц асинхронно
*
'''


async def aiohttp_fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()