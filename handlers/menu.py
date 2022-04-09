from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from handlers.config import COMMANDS, COMMANDS_2
from handlers.schedule import RESULTS
from keyboards.menu_kb import START_KB
from utils.sqlite_requests import database_handler


@database_handler()
async def start(msg: types.Message):
    COMMANDS_2.clear()
    RESULTS.clear()
    COMMANDS
    await msg.answer('Выберите команду', reply_markup=START_KB)


def register_handlers_menu(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(start, filters.Text(contains='Меню', ignore_case=True))