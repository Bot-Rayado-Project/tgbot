from aiogram import types, Dispatcher
from initialize_bot import bot
import asyncio
from keyboards.menu_kb import TO_MENU_KB,START_KB


async def send_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать в Bot Rayado\n\nДля доступа к меню нажмите кнопку снизу' +\
        '\n\n Наши преимущества:\n\n - Есть шаблоны для быстрого получения расписания\n' +\
            ' - Всегда новое расписание, полученное с сайта\n - Большое количество потоков\n - Быстрая работа бота\n - Регулярные обновления',reply_markup=START_KB)


async def send_help(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=open('img/monkey.jpg', 'rb'), caption='В случае ошибок или вопросов пишите: \n@lamabot2000\n@crymother\n \
    \nИспользование шаблонов:\n\nСоздаете шаблон, который будет выводить нужное вам расписание по одному клику. Шаблоны хранятся в кнопке "Шаблоны расписания".\n \
    \nРасписание:\n\nДля вывода нужного вам расписания надо нажимать кнопки в нужной вам последовательности.\n \
    \nКлавиатура:\n\nЕсли у вас не отображается клавиатура, нажмите на кнопку слева от выбора эмодзи.', reply_markup=TO_MENU_KB)


def register_handler_commands_slash(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(send_start, commands = ['start'])
    bot_dispatcher.register_message_handler(send_help, commands = ['help'])