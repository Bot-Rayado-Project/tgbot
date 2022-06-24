from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from bot.keyboards.menu_kb import START_KB
from bot.db.db import database_handler
from bot.utils.http import aiohttp_fetch
from bot.logger.logger import get_logger


'''
*
Файл хендлера для вывода шутки
*
'''


logger = get_logger(__name__)


@database_handler()
async def joke(message_from_user: types.Message):

    message_for_user = (await aiohttp_fetch(url='http://rzhunemogu.ru/RandJSON.aspx?CType=11'))[12:-2]

    await message_from_user.answer(str(message_for_user), reply_markup=START_KB)
    logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + 'Joke printed')


def register_handlers_joke(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(joke, filters.Text(contains=['Анекдот'], ignore_case=True))
