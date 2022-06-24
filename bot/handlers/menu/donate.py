from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from bot.keyboards.menu_kb import START_KB
from bot.db.db import database_handler
from bot.logger.logger import get_logger


'''
*
Файл хендлера для обращению к донату 
*
'''


logger = get_logger(__name__)


@database_handler()
async def donate(message_from_user: types.Message):

    message_for_user = 'Сколько не жалко ❤️\nhttps://www.tinkoff.ru/cf/67hbUB2jUpf'
    
    await message_from_user.answer(message_for_user, reply_markup=START_KB)
    logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + 'Donat printed')


def register_handlers_donate(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(donate, filters.Text(equals='Донат', ignore_case=True))
