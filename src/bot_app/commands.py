from aiogram import types
from . app import dp 
from . import messages, sqlite_db
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(messages.WELCOME_MESSAGE)
    sqlite_db.sql_start()

class FSMAdmin(StatesGroup):
    token = State()
    username = State()

@dp.message_handler(commands='Load', state=None)
async def cm_start(message: types.Message):
    await FSMAdmin.token.set()
    await message.reply('load token')

@dp.message_handler(state=FSMAdmin.token)
async def load_token(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['token'] = message.text
    await FSMAdmin.next()
    await message.reply('now your username')

@dp.message_handler(state=FSMAdmin.username)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await sqlite_db.sql_add_command(state)
    await state.finish()

def register_handlers_admin(dp):
    dp.register_message_handler(cm_start, commands=['Load_token'], state=None)