from aiogram import types, Dispatcher
from keyboards.menu_kb import START_KB
from utils.sqlite_requests import database_handler


@database_handler()
async def null(msg: types.Message):
    await msg.answer('Неправильная команда', reply_markup=START_KB)


def register_handlers_null(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(null)