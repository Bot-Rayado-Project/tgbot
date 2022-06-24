from aiogram import types, Dispatcher
from aiogram.dispatcher import filters
from bot.schedule.schedule import print_full_schedule
from bot.schedule.schedule import print_schedule
from bot.keyboards.menu_kb import START_KB
from bot.keyboards.schedule_kb import FACULTIES_KB
from bot.keyboards.schedule_kb import DAYS_OF_WEEK_KB
from bot.keyboards.schedule_kb import CURRENT_OR_NEXT_WEEK_KB
from bot.constants.schedule import *
from bot.db.db import database_handler, database_fetch_all_commands, database_set_button_blueprint
from bot.logger.logger import get_logger
from datetime import datetime
import traceback


'''
*
Этот файл отвечает за работу хендлеров для приема информации о выводимом расписании
*
'''


logger = get_logger(__name__)


@database_handler()
async def start(message_from_user: types.Message):
    ''' Стартовый хендлер, реагирует на команду расписание '''

    message_for_user = 'Выберите день'
    await message_from_user.answer(message_for_user, reply_markup=DAYS_OF_WEEK_KB)
    logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' +  str(message_for_user))


@database_handler()
async def week_or_faculty(message_from_user: types.Message):
    ''' Хендлер, отвечающий за выбор либо факультета, елси выбран один день одного дня, либо четности недели '''

    try:
        all_commands = await database_fetch_all_commands(message_from_user)
            
        if all_commands[0][0].lower() == 'вся неделя':

            message_for_user = 'Выберите неделю'
            await message_from_user.answer(message_for_user, reply_markup=CURRENT_OR_NEXT_WEEK_KB)
            logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' +  str(message_for_user))


        elif (all_commands[0][0].lower() == 'завтра' or all_commands[0][0].lower() == 'сегодня'
            or all_commands[0][0].lower() == 'текущая неделя' or all_commands[0][0].lower() == 'следующая неделя'):

            message_for_user = 'Выберите факультет'
            await message_from_user.answer(message_for_user, reply_markup=FACULTIES_KB)
            logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' +  str(message_for_user))
        
        else:
            message_for_user = 'Неправильная команда'
            await message_from_user.answer(message_for_user, reply_markup=START_KB)
        
        # Делается проверка на вводимые команды пользователем, чтобы была правильная последовательность
        # защита от рандомного набирания слов пользователем

    except Exception as e:
        logger.error(
        f'Ошибка в обращении к db в week_or_faculty, schedule.py {e}, {traceback.format_exc()}')
        await message_from_user.answer('Непредвиденная ошибка', reply_markup=START_KB)


@database_handler()
async def streams(message_from_user: types.Message):
    ''' Хендлер, отвечающий за выбор потока, также как и в прошлом хендлере делается проверка 
    комманд введённых пользователем, чтобы была правильная последовательность '''

    try:
        all_commands = await database_fetch_all_commands(message_from_user)
        
        if all_commands[1][0].lower() == 'сегодня' or all_commands[1][0].lower() == 'завтра':

            message_for_user = 'Выберите поток'
            await message_from_user.answer(message_for_user, reply_markup=FACULTIES_KB_BUTTONS[message_from_user.text.upper()])
            logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' +  str(message_for_user))

        elif (all_commands[2][0].lower() == 'вся неделя' and (all_commands[1][0].lower() == 'текущая неделя' 
                    or all_commands[1][0].lower() == 'следующая неделя')):

            message_for_user = 'Выберите поток'
            await message_from_user.answer(message_for_user, reply_markup=FACULTIES_KB_BUTTONS[message_from_user.text.upper()])
            logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' +  str(message_for_user))
        
        else:
            message_for_user = 'Неправильная команда'
            await message_from_user.answer(message_for_user, reply_markup=START_KB)

    except Exception as e:
        logger.error(
            f'Ошибка в обращении к db в streams, schedule.py {e}, {traceback.format_exc()}')
        await message_from_user.answer('Непредвиденная ошибка', reply_markup=START_KB)


@database_handler()
async def groups(message_from_user: types.Message):
    ''' Хендлер, отвечающий за выбор группы, также как и в прошлых хендлерах делается проверка 
    комманд введённых пользователем, чтобы была правильная последовательность '''

    try:
        all_commands = await database_fetch_all_commands(message_from_user)

        if ((all_commands[2][0].lower() == 'текущая неделя' or all_commands[2][0].lower() == 'следующая неделя') and 
            all_commands[3][0].lower() == 'вся неделя'):

            message_for_user = 'Выберите группу'
            await message_from_user.answer(message_for_user, reply_markup=STREAMS_KB[message_from_user.text.lower()])
            logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' +  str(message_for_user))

        elif all_commands[2][0].lower() == 'сегодня' or all_commands[2][0].lower() == 'завтра':
            
            message_for_user = 'Выберите группу'
            await message_from_user.answer('Выберите группу', reply_markup=STREAMS_KB[message_from_user.text.lower()])
            logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' +  str(message_for_user))
            
        else:
            message_for_user = 'Неправильная команда'
            await message_from_user.answer(message_for_user, reply_markup=START_KB)

    except Exception as e:
        logger.error(
            f'Ошибка в обращении к db в groups, schedule.py {e}, {traceback.format_exc()}')
        await message_from_user.answer('Непредвиденная ошибка', reply_markup=START_KB)


@database_handler()
async def schedule(message_from_user: types.Message):
    start_time = datetime.now() # Засекает начало старта алгоритма, чтобы в логи записать время выполнения

    ''' Хендлер, отвечающий за вывод расписания, также делается проверка последовательности, но также из-за отсутствия пейлоадов как в 
    вконтакте взаимодействие с шаблонами, то есть их запись происходит тут, именно поэтому две части кода тут '''

    try:
        all_commands = await database_fetch_all_commands(message_from_user)

        if all_commands[4][0].lower() == 'расписание' or all_commands[5][0].lower() == 'расписание':
            if all_commands[3][0].lower() == 'сегодня' or all_commands[3][0].lower() == 'завтра':
                try:
                    schedule = await print_schedule(message_from_user.from_user.id, all_commands[3][0].lower(), all_commands[0][0].lower())

                    if schedule == None:
                        logger.error(
                            f'Ошибка в выводе одного дня, schedule, schedule.py, {traceback.format_exc()}')
                        await message_from_user.answer('Непредвиденная ошибка', reply_markup=START_KB)

                    else:
                        await message_from_user.answer(schedule, reply_markup=START_KB)
                        logger.info('Time of table out: ' + str(datetime.now() - start_time))
                        logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + str(schedule))

                except Exception as e:
                    logger.error(
                        f'Ошибка в обращении к выводу одного дня, schedule, schedule.py{e}, {traceback.format_exc()}')
                    await message_from_user.answer('Непредвиденная ошибка', reply_markup=START_KB)

            if all_commands[4][0].lower() == 'вся неделя' and (all_commands[3][0].lower() == 'текущая неделя' or all_commands[3][0].lower() == 'следующая неделя'):
                try:
                    schedule = await print_full_schedule(message_from_user.from_user.id, all_commands[3][0].lower(), all_commands[0][0].lower())

                    if schedule == None:
                        logger.error(
                            f'Ошибка в выводе всей недели, schedule, schedule.py, {traceback.format_exc()}')
                        await message_from_user.answer('Непредвиденная ошибка', reply_markup=START_KB)

                    else:
                        await message_from_user.answer(schedule, reply_markup=START_KB, parse_mode='HTML')
                        logger.info('Time of table out: ' + str(datetime.now() - start_time))
                        logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' + str(schedule))

                except Exception as e:
                    logger.error(
                        f'Ошибка в обращении к выводу всей недели, schedule, schedule.py{e}, {traceback.format_exc()}')
                    await message_from_user.answer('Непредвиденная ошибка', reply_markup=START_KB)
        
        # Эта часть кода сверху отвечает за вывод расписания, также в с проверкой на последовательность комманд и обработкой ошибки вывода расписания

        elif len(all_commands) > 5: # Это условие сделано, чтобы алгоритм не проверял даже шаблоны если юзер впервые зашёл и смотрит расписание, так как индекс выйдет за границы
            if all_commands[6][0].lower() == 'создать шаблон' or all_commands[5][0].lower() == 'создать шаблон':
                if all_commands[4][0].lower() == 'вся неделя':
                    try:
                    
                        await database_set_button_blueprint(
                            str(all_commands[3][0][0].upper() + 'Н ' + all_commands[0][0].upper()), message_from_user, all_commands[5][0])

                        message_for_user = f'Шаблон записан: {all_commands[3][0][0].upper()}Н {all_commands[0][0].upper()}'
                        await message_from_user.answer(message_for_user, reply_markup=START_KB)
                        logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' +  str(message_for_user))

                    except Exception as e:
                        logger.error(
                            f'Ошибка в сохранении шаблона для всей недели, schedule, schedule.py{e}, {traceback.format_exc()}')
                        await message_from_user.answer('Непредвиденная ошибкa', reply_markup=START_KB)

                else:
                    try:
                        await database_set_button_blueprint(
                            str(all_commands[3][0].capitalize() + ' ' + all_commands[0][0].upper()), message_from_user, all_commands[4][0])

                        message_for_user = f'Шаблон записан: {all_commands[3][0].capitalize()} {all_commands[0][0].upper()}'
                        await message_from_user.answer(message_for_user, reply_markup=START_KB)
                        logger.info('Answer: ' + str(message_from_user.from_user.username) + ' - ' +  str(message_for_user))

                    except Exception as e:
                        logger.error(
                            f'Ошибка в сохранении шаблона для одного дня, schedule, schedule.py{e}, {traceback.format_exc()}')
                        await message_from_user.answer('Непредвиденная ошибка', reply_markup=START_KB)
            
        # Эта часть кода сверху отвечает за сохранение шаблона в базу данных, также в с проверкой на последовательность комманд и обработкой ошибки не подключения к бд

    except Exception as e:
        logger.error(
            f'Ошибка в обращении к db в schedule, schedule.py {e}, {traceback.format_exc()}')
        await message_from_user.answer('Непредвиденная ошибка', reply_markup=START_KB)


def register_handlers_schedule(bot_dispatcher: Dispatcher):
    bot_dispatcher.register_message_handler(week_or_faculty, filters.Text(equals=DAYS_OF_WEEK, ignore_case=True))
    bot_dispatcher.register_message_handler(streams, filters.Text(equals=FACULTIES))
    bot_dispatcher.register_message_handler(groups, filters.Text(equals=STREAMS))
    bot_dispatcher.register_message_handler(start, filters.Text(equals='Расписание'))
    bot_dispatcher.register_message_handler(schedule, filters.Text(equals=GROUPS, ignore_case=True))
