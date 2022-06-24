from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from bot.keyboards.menu_kb import START_KB
from bot.constants.schedule import PHRASES
from bot.db.db import database_handler
from bot.logger.logger import get_logger


'''
*
Файл хендлера для вызова помощи
*
'''


logger = get_logger(__name__)


@database_handler()
async def help_handler(message_from_user: types.Message):

    message_for_user = 'В случае ошибок или вопросов пишите: \n@ALPHA_KENNYBODY\n@darttusin\n \
    \nИспользование шаблонов:\n\nСоздаете шаблон, который будет выводить нужное вам расписание по одному клику. Шаблоны хранятся в кнопке "Шаблоны расписания".\n \
    \nРасписание:\n\nДля вывода нужного вам расписания надо нажимать кнопки в нужной вам последовательности.\n \
    \nКлавиатура:\n\nЕсли у вас не отображается клавиатура, нажмите на кнопку слева от отправки сообщения.'
    
    await message_from_user.answer(message_for_user, reply_markup=START_KB)
    logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + 'Help printed')


def register_handlers_help(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(help_handler, filters.Text(equals=PHRASES, ignore_case=True))
