from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from aiohttp import request
from botrayado.schedule.sheethandler import print_full_schedule
from botrayado.schedule.sheethandler import print_schedule
from botrayado.keyboards.menu_kb import START_KB
from botrayado.keyboards.schedule_kb import FACULTIES_KB
from botrayado.keyboards.schedule_kb import DAYS_OF_WEEK_CFG_KB
from botrayado.keyboards.schedule_kb import CURRENT_OR_NEXT_WEEK_KB
from botrayado.utils.constants import *
from botrayado.database.db import database_handler, fetch_commands, set_button_blueprint
from botrayado.utils.logger import get_logger
from datetime import datetime
import traceback


logger = get_logger(__name__)


@database_handler()
async def schedule(msg: types.Message):

    message = 'Выберите день'
    await msg.answer(message, reply_markup=DAYS_OF_WEEK_CFG_KB)
    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))


@database_handler()
async def faculties(msg: types.Message):

    try:
        all_commands = await fetch_commands(msg)
            
        if all_commands[0][0].lower() == 'вся неделя':

            message = 'Выберите неделю'
            await msg.answer(message, reply_markup=CURRENT_OR_NEXT_WEEK_KB)
            logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))


        elif (all_commands[0][0].lower() == 'завтра' or all_commands[0][0].lower() == 'сегодня'
            or all_commands[0][0].lower() == 'текущая неделя' or all_commands[0][0].lower() == 'следующая неделя'):

            message = 'Выберите факультет'
            await msg.answer(message, reply_markup=FACULTIES_KB)
            logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))


    except Exception as e:
        logger.error(
        f'Ошибка в обращении к users.db в faculties, schedule.py {e}, {traceback.format_exc()}')
        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)


@database_handler()
async def streams(msg: types.Message):

    try:
        all_commands = await fetch_commands(msg)
        
        if all_commands[1][0].lower() == 'сегодня' or all_commands[1][0].lower() == 'завтра':

            message = 'Выберите поток'
            await msg.answer(message, reply_markup=FACULTIES_KB_BUTTONS[msg.text.upper()])
            logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

        elif (all_commands[2][0].lower() == 'вся неделя' and (all_commands[1][0].lower() == 'текущая неделя' 
                    or all_commands[1][0].lower() == 'следующая неделя')):

            message = 'Выберите поток'
            await msg.answer(message, reply_markup=FACULTIES_KB_BUTTONS[msg.text.upper()])
            logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))


    except Exception as e:
        logger.error(
            f'Ошибка в обращении к users.db в streams, schedule.py {e}, {traceback.format_exc()}')
        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)


@database_handler()
async def streams_v2(msg: types.Message):

    try:
        all_commands = await fetch_commands(msg)

        if ((all_commands[2][0].lower() == 'текущая неделя' or all_commands[2][0].lower() == 'следующая неделя') and 
            all_commands[3][0].lower() == 'вся неделя'):

            message = 'Выберите группу'
            await msg.answer(message, reply_markup=STREAMS_KB[msg.text.lower()])
            logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

        elif all_commands[2][0].lower() == 'сегодня' or all_commands[2][0].lower() == 'завтра':
            
            message = 'Выберите группу'
            await msg.answer('Выберите группу', reply_markup=STREAMS_KB[msg.text.lower()])
            logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))


    except Exception as e:
        logger.error(
            f'Ошибка в обращении к users.db в streams_v2, schedule.py {e}, {traceback.format_exc()}')
        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)


@database_handler()
async def groups(msg: types.Message):
    start_time = datetime.now()

    try:
        all_commands = await fetch_commands(msg)
        
        if all_commands[4][0].lower() == 'расписание' or all_commands[4][0].lower() == 'вся неделя':
        
            if all_commands[3][0].lower() == 'сегодня' or all_commands[3][0].lower() == 'завтра':
                try:
                    schedule = await print_schedule(msg.from_user.id, all_commands[3][0].lower(), all_commands[0][0].lower())

                    if schedule == None:
                        logger.error(
                            f'Ошибка в выводе одного дня, groups, schedule.py, {traceback.format_exc()}')
                        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)

                    else:
                    
                        await msg.answer(schedule, reply_markup=START_KB)
                        logger.info('Time of table out: ' + str(datetime.now() - start_time))
                        logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(schedule))

                except Exception as e:
                    logger.error(
                        f'Ошибка в обращении к выводу одного дня, groups, schedule.py{e}, {traceback.format_exc()}')
                    await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)

            if all_commands[4][0].lower() == 'вся неделя' and (all_commands[3][0].lower() == 'текущая неделя' or all_commands[3][0].lower() == 'следующая неделя'):
                try:
                    schedule = await print_full_schedule(msg.from_user.id, all_commands[3][0].lower(), all_commands[0][0].lower())

                    if schedule == None:
                        logger.error(
                            f'Ошибка в выводе всей недели, groups, schedule.py, {traceback.format_exc()}')
                        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)

                    else:
                        
                        await msg.answer(schedule, reply_markup=START_KB, parse_mode='HTML')
                        logger.info('Time of table out: ' + str(datetime.now() - start_time))
                        logger.info('Answer: ' + str(msg.from_user.username) + ' - ' + str(schedule))

                except Exception as e:
                    logger.error(
                        f'Ошибка в обращении к выводу всей недели, groups, schedule.py{e}, {traceback.format_exc()}')
                    await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)
        
        elif all_commands[6][0].lower() == 'создать шаблон' or all_commands[5][0].lower() == 'создать шаблон':
            if all_commands[4][0].lower() == 'вся неделя':
                try:
        
                    set_button_blueprint(
                        str(all_commands[3][0][0].upper() + 'Н ' + all_commands[0][0].upper()), msg, all_commands[5][0])
                    
                    message = f'Шаблон записан: {all_commands[3][0][0].upper()}Н {all_commands[0][0].upper()}'
                    await msg.answer(message, reply_markup=START_KB)
                    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

                except Exception as e:
                    logger.error(
                        f'Ошибка в сохранении шаблона для всей недели, groups, schedule.py{e}, {traceback.format_exc()}')
                    await msg.answer('Непредвиденная ошибкa', reply_markup=START_KB)


            else:
                try:
                    set_button_blueprint(
                        str(all_commands[3][0].capitalize() + ' ' + all_commands[0][0].upper()), msg, all_commands[4][0])
                    
                    message = f'Шаблон записан: {all_commands[3][0].capitalize()} {all_commands[0][0].upper()}'
                    await msg.answer(message, reply_markup=START_KB)
                    logger.info('Answer: ' + str(msg.from_user.username) + ' - ' +  str(message))

                except Exception as e:
                    logger.error(
                        f'Ошибка в сохранении шаблона для одного дня, groups, schedule.py{e}, {traceback.format_exc()}')
                    await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)

    except Exception as e:
        logger.error(
            f'Ошибка в обращении к users.db в groups, schedule.py {e}, {traceback.format_exc()}')
        await msg.answer('Непредвиденная ошибка', reply_markup=START_KB)


def register_handlers_schedule(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(
        faculties, filters.Text(equals=DAYS_OF_WEEK, ignore_case=True))
    bot_dispatcher.register_message_handler(
        streams, filters.Text(equals=FACULTIES, ignore_case=True))
    bot_dispatcher.register_message_handler(
        streams_v2, filters.Text(equals=STREAMS, ignore_case=True))
    bot_dispatcher.register_message_handler(
        schedule, filters.Text(equals='Расписание', ignore_case=True))
    bot_dispatcher.register_message_handler(
        groups, filters.Text(equals=GROUPS, ignore_case=True))
