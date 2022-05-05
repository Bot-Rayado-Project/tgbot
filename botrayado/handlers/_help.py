from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from initialize_bot import bot
from botrayado.keyboards.menu_kb import START_KB
from botrayado.database.db import database_handler
from botrayado.utils.logger import get_logger


logger = get_logger(__name__)
PHRASES = ['помощь', '/help', 'help', '/помощь']


@database_handler()
async def _help(msg: types.Message):

    message = 'В случае ошибок или вопросов пишите: \n@ALPHA_KENNYBODY\n@darttusin\n \
    \nИспользование шаблонов:\n\nСоздаете шаблон, который будет выводить нужное вам расписание по одному клику. Шаблоны хранятся в кнопке "Шаблоны расписания".\n \
    \nРасписание:\n\nДля вывода нужного вам расписания надо нажимать кнопки в нужной вам последовательности.\n \
    \nКлавиатура:\n\nЕсли у вас не отображается клавиатура, нажмите на кнопку слева от отправки сообщения.'
    await bot.send_photo(chat_id=msg.chat.id, photo=open('botrayado/img/monkey.jpg', 'rb'), caption=message, reply_markup=START_KB)
    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + 'Help printed')


def register_handlers_help(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(
        _help, filters.Text(equals=PHRASES, ignore_case=True))
