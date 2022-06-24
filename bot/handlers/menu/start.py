from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from bot.keyboards.menu_kb import START_KB
from bot.db.db import database_handler
from bot.logger.logger import get_logger
from bot.constants.schedule import START_PHRASES

'''
*
Файл хендлера для старта бота
*
'''

logger = get_logger(__name__)


@database_handler()
async def start(message_from_user: types.Message):

    message_for_user = 'Бот находится в разработке. В случае ошибок,' +\
        'просьба сообщить разработчикам, ' +\
        'чтобы мы исправили. \n@ALPHA_KENNYBODY\n@darttusin'

    await message_from_user.answer(message_for_user, reply_markup=START_KB)
    logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + 'Start printed')

def register_handlers_start(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(start, filters.Text(equals=START_PHRASES, ignore_case=True))
