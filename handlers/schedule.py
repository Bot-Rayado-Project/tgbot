from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from schedule.sheethandler import print_full_schedule, print_schedule
from keyboards.menu_kb import START_KB
from keyboards.schedule_kb import FACULTIES_BUTTONS_KB
from keyboards.schedule_kb import DAYS_OF_WEEK_KB
from keyboards.schedule_kb import CURRENT_OR_NEXT_WEEK_KB
from utils.constants_handlers import DAYS_OF_WEEK, FACULTIES, STREAMS, GROUPS, FACULTIES_KB, STREAMS_KB
from utils.constants import *
from utils.sqlite_requests import database_handler, set_button_blueprint
from handlers.config import COMMANDS_2 as COMMANDS

RESULTS = []

@database_handler()
async def schedule(msg: types.Message):
    RESULTS.append(msg.text.lower())
    await msg.answer('Выберите день', reply_markup=DAYS_OF_WEEK_KB)

@database_handler()
async def faculties(msg: types.Message):
    RESULTS.append(msg.text.lower())
    if msg.text == 'Вся неделя':
        await msg.answer('Выберите неделю', reply_markup=CURRENT_OR_NEXT_WEEK_KB)
    else:
        await msg.answer('Выберите факультет', reply_markup=FACULTIES_BUTTONS_KB)

@database_handler()
async def streams(msg: types.Message):
    await msg.answer('Выберите поток', reply_markup=FACULTIES_KB[msg.text.upper()])

@database_handler()
async def streams_v2(msg: types.Message):
    await msg.answer('Выберите группу', reply_markup=STREAMS_KB[msg.text.lower()])

@database_handler()
async def groups(msg: types.Message):
    RESULTS.append(msg.text.lower())
    if RESULTS[0] != 'расписание':
        if RESULTS[0] == 'вся неделя':
            set_button_blueprint(str(RESULTS[1][0].upper() + 'н ' + RESULTS[-1]), msg, COMMANDS[-1])
            await msg.answer('Шаблон записан: {0}н {1}'.format(RESULTS[-2][0].upper(), RESULTS[-1]), 
                            reply_markup=START_KB)
        else:
            set_button_blueprint(str(RESULTS[0].capitalize() + ' ' + RESULTS[-1]), msg, COMMANDS[-1])
            await msg.answer('Шаблон записан: {0} {1}'.format(RESULTS[0].capitalize(), RESULTS[-1]), 
                            reply_markup=START_KB)
    else:
        if RESULTS[1] == 'сегодня' or RESULTS[1] == 'завтра':
            await msg.answer(await print_schedule(RESULTS[1], RESULTS[-1]),
            reply_markup=START_KB)
        else:
            await msg.answer(await print_full_schedule(RESULTS[1], RESULTS[-1]),
            reply_markup=START_KB)
    COMMANDS.clear()
    RESULTS.clear()


def register_handlers_schedule(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(
        faculties, filters.Text(equals=DAYS_OF_WEEK, ignore_case=True))
    bot_dispatcher.register_message_handler(
        streams, filters.Text(equals=FACULTIES, ignore_case=True))
    bot_dispatcher.register_message_handler(
        streams_v2, filters.Text(equals=STREAMS, ignore_case=True))
    bot_dispatcher.register_message_handler(
        schedule, filters.Text(contains='Расписание', ignore_case=True))
    bot_dispatcher.register_message_handler(
        groups, filters.Text(equals=GROUPS, ignore_case=True))
    
