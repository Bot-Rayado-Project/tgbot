from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from keyboards.menu_kb import START_KB

START_PHRASES = ['начать', 'старт', '/начать', '/start', 'start']

async def start(msg: types.Message):
    await msg.answer('Добро пожаловать в Bot Rayado\n\nЕсли у вас не отобразилась клавиатура, нажми кнопку справа от отправки сообщения' +\
        '\n\n Наши преимущества:\n\n - Есть шаблоны для быстрого получения расписания\n' +\
            ' - Всегда новое расписание, полученное с сайта\n - Большое количество потоков\n - Быстрая работа бота\n - Регулярные обновления', reply_markup=START_KB)


def register_handlers_start(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(start, filters.Text(equals=START_PHRASES, ignore_case=True))