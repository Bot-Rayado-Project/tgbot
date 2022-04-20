from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from botrayado.keyboards.menu_kb import START_KB
from botrayado.database.db import database_handler
from botrayado.utils.logger import get_logger


START_PHRASES = ['начать', 'старт', '/начать', '/start', 'start']
logger = get_logger(__name__)


@database_handler()
async def start(msg: types.Message):

    message = 'Бот находится в разработке. В случае ошибок,' +\
        'просьба сообщить разработчикам, ' +\
        'чтобы мы исправили. \n@ALPHA_KENNYBODY\n@darttusin'
    await msg.answer(message, reply_markup=START_KB)
    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + 'Start printed')

def register_handlers_start(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(
        start, filters.Text(equals=START_PHRASES, ignore_case=True))
