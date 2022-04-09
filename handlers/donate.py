from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from keyboards.menu_kb import START_KB
from utils.sqlite_requests import database_handler


@database_handler()
async def donate(msg: types.Message):
    await msg.answer('Сколько не жалко ❤️\nhttps://www.tinkoff.ru/cf/67hbUB2jUpf', reply_markup=START_KB)


def register_handlers_donate(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(donate, filters.Text(contains='Донат', ignore_case=True))