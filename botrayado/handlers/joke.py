from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from botrayado.keyboards.menu_kb import START_KB
from botrayado.utils.aiohttp_requests import aiohttp_fetch
from botrayado.database.db import database_handler
from botrayado.handlers.schedule import RESULTS
from botrayado.handlers.config import COMMANDS_2 as COMMANDS
from botrayado.utils.logger import get_logger


logger = get_logger(__name__)


@database_handler()
async def joke(msg: types.Message):
    if RESULTS == [] and COMMANDS == []:
        mesg = (await aiohttp_fetch(url='http://rzhunemogu.ru/RandJSON.aspx?CType=11'))[12:-2]
        await msg.answer(str(mesg), reply_markup=START_KB)
        logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(mesg))

    else:
        RESULTS.clear()
        COMMANDS.clear()
        message = 'Неправильная команда'
        await msg.answer(message, reply_markup=START_KB)
        logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(message))


def register_handlers_joke(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(
        joke, filters.Text(contains=['Анекдот'], ignore_case=True))
