from botrayado.keyboards.admin_kb import ADMIN_KB
from botrayado.keyboards.special_blueprints_kb import SPECIAL_BLUEPRINTS_KB
from botrayado.keyboards.menu_kb import START_KB
from datetime import datetime
from aiogram import Dispatcher, types
from aiogram.dispatcher import filters
from botrayado.database.db import database_handler
from botrayado.utils.constants import USERSIDS
from initialize_bot import bot


@database_handler()
async def special_blueprints_handler(msg: types.Message) -> str:
    if str(msg.from_user.id) in USERSIDS:
        await msg.answer('Выберите шаблон', reply_markup=SPECIAL_BLUEPRINTS_KB)

    else:
        await msg.answer('Неправильная команда', reply_markup=START_KB)


@database_handler()
async def logs_handler(msg: types.Message) -> str:
    if str(msg.from_user.id) in USERSIDS:
        await msg.answer(f'Файл логов на {datetime.now()}', reply_markup=ADMIN_KB)
        await bot.send_document(msg.chat.id, open('logs.log', 'rb'))

    else:
        await msg.answer('ACCESS DENIED.', reply_markup=START_KB)


def register_handlers_admin(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(special_blueprints_handler, filters.Text(
        contains='SP Шаблоны', ignore_case=True))
    bot_dispatcher.register_message_handler(logs_handler, filters.Text(
        contains='Логи', ignore_case=True))
