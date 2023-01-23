from aiogram import types
from . app import dp 
from .data_fetcher import get_random
from . import sqlite_db
import json

@dp.message_handler(commands='echoserver')
async def echoserver(message: types.Message):
    await message.reply('echoserver')
    await sqlite_db.sql_find_command(message)







