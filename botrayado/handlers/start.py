from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from botrayado.handlers.config import COMMANDS_2 as COMMANDS
from botrayado.keyboards.menu_kb import START_KB
from botrayado.database.db import database_handler
from botrayado.handlers.schedule import RESULTS

START_PHRASES = ['начать', 'старт', '/начать', '/start', 'start']


@database_handler()
async def start(msg: types.Message):
    if RESULTS == [] and COMMANDS == []:
        await msg.answer('Бот находится в разработке. В случае ошибок, просьба сообщить разработчикам, ' +
                     'чтобы мы исправили. \n@ALPHA_KENNYBODY\n@darttusin',
                     reply_markup=START_KB)
    else:
        RESULTS.clear()
        await msg.answer('Неправильная команда', reply_markup=START_KB)


def register_handlers_start(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(
        start, filters.Text(equals=START_PHRASES, ignore_case=True))
