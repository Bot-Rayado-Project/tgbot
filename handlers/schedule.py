from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from schedule.sheethandler import print_full_schedule, print_schedule
from keyboards.menu_kb import START_KB
from keyboards.schedule_kb import FACULTIES_BUTTONS_KB
from keyboards.schedule_kb import DAYS_OF_WEEK_KB
from keyboards.schedule_kb import CURRENT_OR_NEXT_WEEK_KB
from utils.constants_handlers import DAYS_OF_WEEK, FACULTIES, STREAMS, GROUPS, FACULTIES_KB, STREAMS_KB


RESULTS = []


async def schedule(msg: types.Message):
    await msg.answer('Выберите день', reply_markup=DAYS_OF_WEEK_KB)


async def faculties(msg: types.Message):
    if msg.text == 'Вся неделя':
        await msg.answer('Выберите неделю', reply_markup=CURRENT_OR_NEXT_WEEK_KB)
    else:
        RESULTS.clear()
        RESULTS.append(msg.text.lower())
        await msg.answer('Выберите факультет', reply_markup=FACULTIES_BUTTONS_KB)


async def streams(msg: types.Message):
    await msg.answer('Выберите поток', reply_markup=FACULTIES_KB[msg.text.upper()])
    

async def streams_v2(msg: types.Message):
    await msg.answer('Выберите группу', reply_markup=STREAMS_KB[msg.text.lower()])


async def groups(msg: types.Message):
    RESULTS.append(msg.text.lower())
    if RESULTS[0] == 'сегодня' or RESULTS[0] == 'завтра':
        await msg.answer(await print_schedule(RESULTS[0], RESULTS[1]), reply_markup=START_KB)
    else:
        await msg.answer(await print_full_schedule(RESULTS[0], RESULTS[1]), reply_markup=START_KB)
    RESULTS.clear()


def register_handlers_schedule(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(faculties, filters.Text(equals=DAYS_OF_WEEK, ignore_case=True))
    bot_dispatcher.register_message_handler(streams, filters.Text(equals=FACULTIES, ignore_case=True))
    bot_dispatcher.register_message_handler(streams_v2, filters.Text(equals=STREAMS, ignore_case=True))
    bot_dispatcher.register_message_handler(schedule, filters.Text(contains='Расписание', ignore_case=True))
    bot_dispatcher.register_message_handler(groups, filters.Text(equals=GROUPS, ignore_case=True))