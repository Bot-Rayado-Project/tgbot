import sched
from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from keyboards.schedule_kb import FACULTIES_BUTTONS_KB
from keyboards.schedule_kb import STREAM_IT_BUTTONS_KB
from keyboards.schedule_kb import STREAM_TSEIMK_BUTTONS_KB
from keyboards.schedule_kb import STREAM_RIT_BUTTONS_KB
from keyboards.schedule_kb import STREAM_KIIB_BUTTONS_KB
from keyboards.schedule_kb import STREAM_SISS_BUTTONS_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BFI_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BVT_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BST_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BEI_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BIB_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BAP_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BMP_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BUT_KB
from keyboards.schedule_kb import GROUP_BUTTONS_ZRC_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BRT_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BIK_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BEE_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BER_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BBI_KB
from keyboards.schedule_kb import GROUP_BUTTONS_BIN_KB
from keyboards.schedule_kb import DAYS_OF_WEEK_KB
from keyboards.schedule_kb import CURRENT_OR_NEXT_WEEK_KB

DAYS_OF_WEEK = ['Сегодня', 'Завтра', 'Вся неделя', 'Текущая неделя', 'Следующая неделя']
FACULTIES = ['ИТ', 'КиИБ', 'РиТ', 'ЦЭиМК', 'СиСС']
STREAMS = ['БВТ', 'БФИ', 'БСТ', 'БЭИ', 'БИБ', 'БМП', 
'ЗРС', 'БАП', 'БУТ', 'БРТ', 'БИК', 'ББИ', 'БЭЭ', 'БЭР', 'БИН']
FACULTIES_KB = {
    'ИТ': STREAM_IT_BUTTONS_KB,
    'КИИБ': STREAM_KIIB_BUTTONS_KB,
    'РИТ': STREAM_RIT_BUTTONS_KB,
    'СИСС': STREAM_SISS_BUTTONS_KB,
    'ЦЭИМК': STREAM_TSEIMK_BUTTONS_KB}
STREAMS_KB = {
    'бвт': GROUP_BUTTONS_BVT_KB,
    'бфи': GROUP_BUTTONS_BFI_KB,
    'бст': GROUP_BUTTONS_BST_KB,
    'бэи': GROUP_BUTTONS_BEI_KB,
    'биб': GROUP_BUTTONS_BIB_KB,
    'бмп': GROUP_BUTTONS_BMP_KB,
    'зрс': GROUP_BUTTONS_ZRC_KB,
    'бап': GROUP_BUTTONS_BAP_KB,
    'бут': GROUP_BUTTONS_BUT_KB,
    'брт': GROUP_BUTTONS_BRT_KB,
    'бик': GROUP_BUTTONS_BIK_KB,
    'бби': GROUP_BUTTONS_BBI_KB,
    'бээ': GROUP_BUTTONS_BEE_KB,
    'бэр': GROUP_BUTTONS_BER_KB,
    'бин': GROUP_BUTTONS_BIN_KB
}


async def schedule(msg: types.Message):
    await msg.answer('Выберите день', reply_markup=DAYS_OF_WEEK_KB)


async def faculties(msg: types.Message):
    if msg.text == 'Вся неделя':
        await msg.answer('Выберите неделю', reply_markup=CURRENT_OR_NEXT_WEEK_KB)
    else:
        await msg.answer('Выберите факультет', reply_markup=FACULTIES_BUTTONS_KB)


async def streams(msg: types.Message):
    await msg.answer('Выберите поток', reply_markup=FACULTIES_KB[msg.text.upper()])
    

async def streams_v2(msg: types.Message):
    await msg.answer('Выберите группу', reply_markup=STREAMS_KB[msg.text.lower()])


""" async def groups(msg: types.Message): """



def register_handlers_schedule(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(faculties, filters.Text(equals=DAYS_OF_WEEK, ignore_case=True))
    bot_dispatcher.register_message_handler(streams, filters.Text(equals=FACULTIES, ignore_case=True))
    bot_dispatcher.register_message_handler(streams_v2, filters.Text(equals=STREAMS, ignore_case=True))
    bot_dispatcher.register_message_handler(schedule, filters.Text(contains='Расписание', ignore_case=True))