from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from keyboards.menu_kb import START_KB


async def start(msg: types.Message):
    await msg.answer('Выберите команду', reply_markup=START_KB)


def register_handlers_menu(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(start, filters.Text(contains='Меню', ignore_case=True))