from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from botrayado.keyboards.menu_kb import START_KB
from botrayado.keyboards.admin_kb import ADMIN_KB
from botrayado.database.db import database_handler
from botrayado.utils.constants import USERSIDS
from botrayado.handlers.schedule import RESULTS
from botrayado.handlers.config import COMMANDS_2 as COMMANDS
from botrayado.utils.logger import get_logger


logger = get_logger(__name__)

@database_handler()
async def donate(msg: types.Message):
    if RESULTS == [] and COMMANDS == []:
        if str(msg.from_user.id) not in USERSIDS:
            message = 'Сколько не жалко ❤️\nhttps://www.tinkoff.ru/cf/67hbUB2jUpf'
            await msg.answer(message, reply_markup=START_KB)
            logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(message))
            
        else:
            message = 'Access granted'
            await msg.answer(message, reply_markup=ADMIN_KB)
            logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(message))

    else:
        RESULTS.clear()
        message = 'Неправильная команда'
        await msg.answer(message, reply_markup=START_KB)
        logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(message))


def register_handlers_donate(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(
        donate, filters.Text(contains='Донат', ignore_case=True))
