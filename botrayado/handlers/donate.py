from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from botrayado.keyboards.menu_kb import START_KB
from botrayado.keyboards.admin_kb import ADMIN_KB
from botrayado.database.db import database_handler
from botrayado.utils.constants import USERSIDS
from botrayado.handlers.schedule import RESULTS
from botrayado.handlers.config import COMMANDS_2 as COMMANDS


@database_handler()
async def donate(msg: types.Message):
    if RESULTS == [] and COMMANDS == []:
        if str(msg.from_user.id) not in USERSIDS:
            await msg.answer('Сколько не жалко ❤️\nhttps://www.tinkoff.ru/cf/67hbUB2jUpf', reply_markup=START_KB)
            
        else:
            await msg.answer('Access granted', reply_markup=ADMIN_KB)

    else:
        RESULTS.clear()
        await msg.answer('Неправильная команда', reply_markup=START_KB)


def register_handlers_donate(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(
        donate, filters.Text(contains='Донат', ignore_case=True))
