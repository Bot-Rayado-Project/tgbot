from aiogram import types, Dispatcher
from bot.keyboards.menu_kb import START_KB
from bot.db.db import database_handler
from bot.logger.logger import get_logger


'''
*
Файл хендлера для обработки неправильных команд, то есть если
никакой хендлер не сработает придёт сюда
*
'''


logger = get_logger(__name__)


@database_handler()
async def null(message_from_user: types.Message):
    message_for_user = 'Неправильная команда'
    await message_from_user.answer(message_for_user, reply_markup=START_KB)
    logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + str(message_for_user))


def register_handlers_null(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(null)
