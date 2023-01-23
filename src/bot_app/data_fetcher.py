import aiohttp
from .local_settings import WORDS_API_URL 

async def get_random():
    async with aiohttp.ClientSession() as session:
        headers = {'Authorization': 'Token b8fba941857808c42e0477450a8098dd1445c5ca'}
        async with session.get(WORDS_API_URL, headers=headers) as response:
            return await response.json() 