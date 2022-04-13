from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from botrayado.schedule.sheethandler import print_full_schedule
from botrayado.schedule.sheethandler import print_schedule
from botrayado.keyboards.menu_kb import START_KB
from botrayado.keyboards.schedule_kb import FACULTIES_KB
from botrayado.keyboards.schedule_kb import DAYS_OF_WEEK_KB
from botrayado.keyboards.schedule_kb import CURRENT_OR_NEXT_WEEK_KB
from botrayado.utils.constants import *
from botrayado.database.db import database_handler, set_button_blueprint
from botrayado.handlers.config import COMMANDS_2 as COMMANDS
from botrayado.utils.logger import get_logger
from datetime import datetime
import traceback


RESULTS = []
logger = get_logger(__name__)


@database_handler()
async def schedule(msg: types.Message):

    RESULTS.append(msg.text.lower())
    message = 'Выберите день'
    await msg.answer(message, reply_markup=DAYS_OF_WEEK_KB)
    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))


@database_handler()
async def faculties(msg: types.Message):
    RESULTS.append(msg.text.lower())

    try:
        if RESULTS[0] == 'расписание' or COMMANDS != []:

            if RESULTS[-1] == 'вся неделя':

                message = 'Выберите неделю'
                await msg.answer(message, reply_markup=CURRENT_OR_NEXT_WEEK_KB)
                logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

            elif (RESULTS[-1] == 'завтра' or RESULTS[-1] == 'сегодня' or RESULTS[-1] == 'текущая неделя'
                        or RESULTS[-1] == 'следующая неделя'):

                message = 'Выберите факультет'
                await msg.answer(message, reply_markup=FACULTIES_KB)
                logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

            else:

                RESULTS.clear()
                message = 'Неправильная команда'
                await msg.answer(message, reply_markup=START_KB)

        else:

            RESULTS.clear()
            message = 'Неправильная команда'
            await msg.answer('Неправильная команда', reply_markup=START_KB)
            logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

    except Exception as e:
        logger.error(
        f'Ошибка в обращении к RESULTS в faculties, schedule.py {e}, {traceback.format_exc()}')
        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)


@database_handler()
async def streams(msg: types.Message):
    RESULTS.append(msg.text.lower())

    try:
        if RESULTS[0] == 'расписание' or COMMANDS != []:
            if RESULTS[-1] in [i.lower() for i in FACULTIES]:
                if RESULTS[-2] == 'сегодня' or RESULTS[-2] == 'завтра':

                    message = 'Выберите поток'
                    await msg.answer(message, reply_markup=FACULTIES_KB_BUTTONS[msg.text.upper()])
                    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

                elif (RESULTS[-3] == 'вся неделя' and (RESULTS[-2] == 'текущая неделя' 
                            or RESULTS[-2] == 'следующая неделя')):

                    message = 'Выберите поток'
                    await msg.answer(message, reply_markup=FACULTIES_KB_BUTTONS[msg.text.upper()])
                    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

                else:

                    RESULTS.clear()
                    message = 'Неправильная команда'
                    await msg.answer(message, reply_markup=START_KB)
                    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

            else:

                RESULTS.clear()
                message = 'Неправильная команда'
                await msg.answer(message, reply_markup=START_KB)
                logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

        else:

            RESULTS.clear()
            message = 'Неправильная команда'
            await msg.answer(message, reply_markup=START_KB)
            logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

    except Exception as e:
        logger.error(
            f'Ошибка в обращении к RESULTS в streams, schedule.py {e}, {traceback.format_exc()}')
        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)


@database_handler()
async def streams_v2(msg: types.Message):
    RESULTS.append(msg.text.lower())

    try:
        if RESULTS[0] == 'расписание' or COMMANDS != []:

            if RESULTS[-2] in [i.lower() for i in FACULTIES]:

                if RESULTS[-1] in [i.lower() for i in STREAMS]:

                    if (RESULTS[-3] == 'текущая неделя' or RESULTS[-3] == 'следующая неделя'):

                        message = 'Выберите группу'
                        await msg.answer(message, reply_markup=STREAMS_KB[msg.text.lower()])
                        logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

                    elif RESULTS[-3] == 'сегодня' or RESULTS[-3] == 'завтра':
                        
                        message = 'Выберите группу',
                        await msg.answer('Выберите группу', reply_markup=STREAMS_KB[msg.text.lower()])
                        logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

                    else:

                        RESULTS.clear()
                        message = 'Неправильная команда'
                        await msg.answer(message, reply_markup=START_KB)
                        logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

                else:

                    RESULTS.clear()
                    message = 'Неправильная команда'
                    await msg.answer(message, reply_markup=START_KB)
                    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

            else:

                RESULTS.clear()
                message = 'Неправильная команда'
                await msg.answer(message, reply_markup=START_KB)
                logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

        else:

            RESULTS.clear()
            message = 'Неправильная команда'
            await msg.answer(message, reply_markup=START_KB)
            logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

    except Exception as e:
        logger.error(
            f'Ошибка в обращении к RESULTS в streams_v2, schedule.py {e}, {traceback.format_exc()}')
        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)


@database_handler()
async def groups(msg: types.Message):
    start_time = datetime.datetime.now()
    RESULTS.append(msg.text.lower())

    try:
        if RESULTS[0] != 'расписание':
            if COMMANDS != []:

                if RESULTS[0] == 'вся неделя':
                    try:
                        set_button_blueprint(
                            str(RESULTS[1][0].upper() + 'Н ' + RESULTS[-1].upper()), msg, COMMANDS[-1])

                    except Exception as e:
                        logger.error(
                            f'Ошибка в сохранении шаблона для всей недели, groups, schedule.py{e}, {traceback.format_exc()}')
                        await msg.answer('Непредвиденная ошибкa', reply_markup=START_KB)

                    message = f'Шаблон записан: {RESULTS[1][0].upper()}Н {RESULTS[-1].upper()}'
                    await msg.answer(message, reply_markup=START_KB)
                    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

                else:
                    try:
                        set_button_blueprint(
                            str(RESULTS[0].capitalize() + ' ' + RESULTS[-1].upper()), msg, COMMANDS[-1])

                    except Exception as e:
                        logger.error(
                            f'Ошибка в сохранении шаблона для одного дня, groups, schedule.py{e}, {traceback.format_exc()}')
                        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)

                    message = f'Шаблон записан: {RESULTS[0].capitalize()} {RESULTS[-1].upper()}'
                    await msg.answer(message, reply_markup=START_KB)
                    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

            else:
                RESULTS.clear()
                message = 'Неправильная команда'
                await msg.answer(message, reply_markup=START_KB)
                logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

        else:
            if RESULTS[1] == 'сегодня' or RESULTS[1] == 'завтра':
                try:
                    schedule = await print_schedule(RESULTS[1], RESULTS[-1])

                    if schedule == None:
                        logger.error(
                            f'Ошибка в выводе одного дня, groups, schedule.py, {traceback.format_exc()}')
                        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)

                    else:

                        await msg.answer(schedule, reply_markup=START_KB)
                        logger.info('Time of table out: ' + str(datetime.datetime.now() - start_time))
                        logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(schedule))

                except Exception as e:
                    logger.error(
                        f'Ошибка в обращении к выводу одного дня, groups, schedule.py{e}, {traceback.format_exc()}')
                    await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)

            if RESULTS[1] == 'вся неделя':
                try:
                    schedule = await print_full_schedule(RESULTS[2], RESULTS[-1])

                    if schedule == None:
                        logger.error(
                            f'Ошибка в выводе всей недели, groups, schedule.py, {traceback.format_exc()}')
                        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)

                    else:
                        
                        await msg.answer(schedule, reply_markup=START_KB, parse_mode='HTML')
                        logger.info('Time of table out: ' + str(datetime.datetime.now() - start_time))
                        logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(schedule))

                except Exception as e:
                    logger.error(
                        f'Ошибка в обращении к выводу всей недели, groups, schedule.py{e}, {traceback.format_exc()}')
                    await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)
        COMMANDS.clear()
        RESULTS.clear()

    except Exception as e:
        logger.error(
            f'Ошибка в обращении к RESULTS в groups, schedule.py {e}, {traceback.format_exc()}')
        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)


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
