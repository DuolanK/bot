import sqlite3 as sq
from .app import bot
from .data_fetcher import get_random
from aiogram import types

def sql_start():
    global base, cur
    base = sq.connect('drf.db')
    cur = base.cursor()
    if base:
        print('DB connected!')
    base.execute('CREATE TABLE IF NOT EXISTS users(token TEXT, username TEXT PRIMARY KEY)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES (?,?)', tuple(data.values()))
        base.commit()

async def sql_find_command(message: types.Message):
    cur.execute('SELECT token FROM users')
    token = cur.fetchall()
    file = await get_random()
    for _ in file:
        if token == token:
            await message.reply(file)
        else:
            await bot.send_message('Token not found')