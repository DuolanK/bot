from aiogram import types
from . app import dp 
from .data_fetcher import get_random


@dp.message_handler(commands='echoserver')
async def echoserver(message: types.Message):
    await message.reply('echoserver')
    res = await get_random() 
    await message.reply(res) 