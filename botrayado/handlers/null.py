from aiogram import types, Dispatcher
from botrayado.keyboards.menu_kb import START_KB
from botrayado.database.db import database_handler, fetch_commands
from botrayado.utils.logger import get_logger


logger = get_logger(__name__)


@database_handler()
async def null(msg: types.Message):

    message = 'Неправильная команда'
    await msg.answer(message, reply_markup=START_KB)
    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(message))


def register_handlers_null(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(null)
