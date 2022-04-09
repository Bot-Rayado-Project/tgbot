from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from keyboards.menu_kb import START_KB
from utils.sqlite_requests import database_handler


START_PHRASES = ['начать', 'старт', '/начать', '/start', 'start']


@database_handler()
async def start(msg: types.Message):
    await msg.answer('Бот находится в разработке. В случае ошибок, просьба сообщить разработчикам, ' +\
         'чтобы мы исправили. \n@ALPHA_KENNYBODY\n@darttusin',
         reply_markup=START_KB)


def register_handlers_start(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(
        start, filters.Text(equals=START_PHRASES, ignore_case=True))
