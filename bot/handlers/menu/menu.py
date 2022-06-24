from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from bot.keyboards.menu_kb import START_KB
from bot.db.db import database_handler
from bot.logger.logger import get_logger


'''
*
Файл хендлера для выхода в меню
*
'''


logger = get_logger(__name__)


@database_handler()
async def menu(message_from_user: types.Message):

    message_for_user = 'Выберите команду'
    await message_from_user.answer('Выберите команду', reply_markup=START_KB)
    logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + str(message_for_user))


def register_handlers_menu(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(menu, filters.Text(contains='Меню', ignore_case=True))
