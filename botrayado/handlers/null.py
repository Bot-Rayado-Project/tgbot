from aiogram import types, Dispatcher
from botrayado.keyboards.menu_kb import START_KB
from botrayado.database.db import database_handler
from botrayado.handlers.config import COMMANDS, COMMANDS_2
from botrayado.handlers.schedule import RESULTS


@database_handler()
async def null(msg: types.Message):
    COMMANDS_2.clear()
    RESULTS.clear()
    COMMANDS.clear()
    await msg.answer('Неправильная команда', reply_markup=START_KB)


def register_handlers_null(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(null)
